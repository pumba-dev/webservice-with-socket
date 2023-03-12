import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";

import { createVuetify } from "vuetify";

export default createVuetify({
  theme: {
    defaultTheme: "lightTheme",
    themes: {
      lightTheme: {
        dark: false,
        colors: {
          background: "#FAFAFA",
          surface: "#FFFFFF",
          primary: "#114B5F",
          secondary: "#242424",
          error: "#FF513D",
          "light-primary": "#1A936F",
          "light-secondary": "#88D498",
          "primary-text": "#242424",
          "secondary-text": "#5E5E5E",
          "modal-background": "#00000040",
          border: "#D9E0E6",
        },
      },
    },
  },
});
