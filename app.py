import streamlit as st
import folium
from streamlit_folium import st_folium
st.set_page_config(page_title="Khutay", layout="wide")
language = st.selectbox(
"اختر اللغة | Choose language",
["العربية", "English"]
)
st.title("خُطاي | KHUTAY")
if language == "العربية":
     st.write("اكتشف مسارات المشي في المدينة المنورة")
else:
     st.write("Discover walking routes in Madinah")
if language == "العربية":
     st.info("تنبيه: المسارات وأعداد الجلسات المعروضة بيانات تجريبية وليست مباشرة.")
else:
     st.info("Note: Routes and session counts are demo data, not live information.")

if language == "العربية":
     selected_route = st.selectbox(
"اختاري المسار",
["المسار الأول", "المسار الثاني", "المسار الثالث"]
)
else:
     selected_route = st.selectbox(
"Choose a route",
["Route 1", "Route 2", "Route 3"]
)

if language == "العربية":
     st.success(f"المسار المختار: {selected_route}")
else:
     st.success(f"Selected route: {selected_route}")

activity_levels = {
"المسار الأول": "🟠 مستوى النشاط: متوسط",
"المسار الثاني": "🟢 مستوى النشاط: منخفض",
"المسار الثالث": "🔴 مستوى النشاط: مرتفع",
"Route 1": "🟠 Activity level: Medium",
"Route 2": "🟢 Activity level: Low",
"Route 3": "🔴 Activity level: High"
}

route_distances = {

"المسار الأول": 1.2,
"المسار الثاني": 0.9,
"المسار الثالث": 1.5,
"Route 1": 1.2,
"Route 2": 0.9,
"Route 3": 1.5
}

if language == "العربية":
    st.metric("📏 طول المسار التقديري", f"{route_distances[selected_route]} كم")
else:
     st.metric("📏 Estimated route distance", f"{route_distances[selected_route]} km")

route_difficulty = {
"المسار الأول": "سهل",
"المسار الثاني": "سهل",
"المسار الثالث": "متوسط",
"Route 1": "Easy",
"Route 2": "Easy",
"Route 3": "Moderate"
}

if language == "العربية":
     st.write(f"👟 صعوبة المسار التجريبية: {route_difficulty[selected_route]}")
else:
     st.write(f"👟 Demo route difficulty: {route_difficulty[selected_route]}")

walking_minutes = round(route_distances[selected_route] / 5 * 60)


if language == "العربية":
     st.write(f"⏱️ مدة المشي التقديرية: {walking_minutes} دقيقة")
     st.caption("حُسبت المدة على أساس سرعة مشي افتراضية تبلغ 5 كم/ساعة.")
else:
     st.write(f"⏱️ Estimated walking time: {walking_minutes} minutes")
     st.caption("Calculated using an assumed walking speed of 5 km/h.")

session_counts = {
"المسار الأول": 12,
"المسار الثاني": 5,
"المسار الثالث": 25,
"Route 1": 12,
"Route 2": 5,
"Route 3": 25
}

if language == "العربية":
     st.write(f"👟 نشاط المشي التجريبي: {session_counts[selected_route]} جلسة")
     st.caption(f"يعرض النموذج بيانات تجريبية تعادل نشاط {session_counts[selected_route]} شخصًا يمارسون رياضة المشي.")
else:
     st.write(f"👟 Demo walking sessions: {session_counts[selected_route]}")
     st.caption(f"Demo data representing {session_counts[selected_route]} people walking.")

with st.container(border=True): st.subheader("📊 معلومات المسار" if language == "العربية" else "📊 Route Details")

if language == "العربية":
    st.metric("📏 طول المسار التقديري", f"{route_distances[selected_route]} كم")
else:
    st.metric("📏 Estimated route distance", f"{route_distances[selected_route]} km")

if language == "العربية":
    st.metric("⏱️ مدة المشي التقديرية", f"{walking_minutes} دقيقة")
else:
    st.metric("⏱️ Estimated walking time", f"{walking_minutes} min")

if language == "العربية":
    st.write(f"👟 صعوبة المسار التجريبية: {route_difficulty[selected_route]}")
else:
    st.write(f"👟 Demo route difficulty: {route_difficulty[selected_route]}")

    st.write(activity_levels[selected_route])

if language == "العربية":
    st.write(f"👟 نشاط المشي التجريبي: {session_counts[selected_route]} جلسة")
    st.caption(f"بيانات تجريبية تعادل نشاط {session_counts[selected_route]} شخصًا يمارسون المشي.")
else:
    st.write(f"👟 Demo walking sessions: {session_counts[selected_route]}")
    st.caption(f"Demo data representing {session_counts[selected_route]} people walking.")

route_number = {
"المسار الأول": 1,
"المسار الثاني": 2,
"المسار الثالث": 3,
"Route 1": 1,
"Route 2": 2,
"Route 3": 3
}[selected_route]

#Create a map centered on Madinah
map_center = [24.4672, 39.6111]

if  selected_route in ["المسار الثاني", "Route 2"]:
     map_center = [24.4800, 39.6200]
elif selected_route in ["المسار الثالث", "Route 3"]:
     map_center = [24.4750, 39.6350]
madinah_map = folium.Map(
location=map_center,
zoom_start=14,
tiles="OpenTopoMap"
)

route_number = {
"المسار الأول": 1,
"المسار الثاني": 2,
"المسار الثالث": 3,
"Route 1": 1,
"Route 2": 2,
"Route 3": 3
}[selected_route]

if route_number == 1:
     folium.Marker(
     location=[24.4672, 39.6111],
     popup=folium.Popup(
       (
        "موقع تجريبي<br>الجلسات النشطة: 12<br>مستوى النشاط: متوسط (بيانات تجريبية)"
        if language == "العربية"
        else "Demo Location<br>Active sessions: 12<br>Activity: Medium (Demo)"
    ),
       max_width=300,
       min_width=220
    ),
    tooltip="موقع تجريبي" if language == "العربية" else "Demo Location",
    icon=folium.Icon(color="orange")
     ).add_to(madinah_map)

if route_number == 2:
    folium.Marker(
        location=[24.4800, 39.6200],
        popup=folium.Popup(
        (
            "المسار التجريبي الثاني<br>الجلسات النشطة: 5<br>مستوى النشاط: منخفض (بيانات تجريبية)"
            if language == "العربية"
            else "Demo Route 2<br>Active sessions: 5<br>Activity: Low (Demo)"
        ),
            max_width=300,
            min_width=220
        ),
        tooltip="المسار التجريبي الثاني" if language == "العربية" else "Demo Route 2",
        icon=folium.Icon(color="green")
    ).add_to(madinah_map)

if route_number == 1:

    folium.PolyLine(
        locations=[
            [24.4672, 39.6111],
            [24.4720, 39.6150],
            [24.4800, 39.6200]
        ],
        color="#E879A0",
        weight=5,
        tooltip="مسار مشي تجريبي" if language == "العربية" else "Demo Walking Route",
    ).add_to(madinah_map)

if route_number == 3:

    folium.Marker(
        location=[24.4750, 39.6350],
        popup=folium.Popup(
            (
            "المسار التجريبي الثالث<br>الجلسات النشطة: 25<br>مستوى النشاط: مرتفع (بيانات تجريبية)"
            if language == "العربية"
            else "Demo Route 3<br>Active sessions: 25<br>Activity: High (Demo)"
        ),
            max_width=300,
            min_width=220
        ),
        tooltip="المسار التجريبي الثالث" if language == "العربية" else "Demo Route 3",
        icon=folium.Icon(color="red")
    ).add_to(madinah_map)
 
if route_number == 2:
    folium.PolyLine(
    locations=[
    [24.4800, 39.6200],
    [24.4830, 39.6250],
    [24.4870, 39.6290]
    ],
    color="#22C55E",
    weight=5,
    tooltip="المسار الثاني (تجريبي)" if language == "العربية" else "Demo Route 2"
    ).add_to(madinah_map)

if route_number == 3:
    folium.PolyLine(
    locations=[
    [24.4750, 39.6350],
    [24.4780, 39.6400],
    [24.4820, 39.6440]
    ],
    color="#EF4444",
    weight=5,
    tooltip="المسار الثالث (تجريبي)" if language == "العربية" else "Demo Route 3"
    ).add_to(madinah_map)

if language == "العربية":
    with st.expander("دليل مستويات النشاط"):
     st.caption("🟢 نشاط منخفض")
     st.caption("🟠 نشاط متوسط")
     st.caption("🔴 نشاط مرتفع")
else:
    with st.expander("Activity Level Guide"):
     st.caption("🟢 Low activity")
     st.caption("🟠 Medium activity")
     st.caption("🔴 High activity")

if language == "العربية":
     st.subheader(f"🗺️ خريطة {selected_route}")
else:
     st.subheader(f"🗺️ Map of {selected_route}")

st_folium(madinah_map, width=900, height=500)

if language == "العربية":
     st.caption("📍 الخط المرسوم توضيحي فقط، وليس مسار مشي معتمدًا.")
else:
     st.caption("📍 The displayed line is illustrative, not a verified walking route.")
