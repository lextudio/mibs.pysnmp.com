# SNMP MIB module (RUCKUS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:42 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruckusProducts,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusProducts")

(RuckusCountryCode,) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusCountryCode")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusWirelessRouterProducts_ObjectIdentity = ObjectIdentity
ruckusWirelessRouterProducts = _RuckusWirelessRouterProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1)
)
_RuckusVF2825_ObjectIdentity = ObjectIdentity
ruckusVF2825 = _RuckusVF2825_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1)
)
_RuckusVF2811_ObjectIdentity = ObjectIdentity
ruckusVF2811 = _RuckusVF2811_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 2)
)
_RuckusVF2821_ObjectIdentity = ObjectIdentity
ruckusVF2821 = _RuckusVF2821_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 3)
)
_RuckusVF2835_ObjectIdentity = ObjectIdentity
ruckusVF2835 = _RuckusVF2835_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 4)
)
_RuckusVF7811_ObjectIdentity = ObjectIdentity
ruckusVF7811 = _RuckusVF7811_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 5)
)
_RuckusWirelessAdapterProducts_ObjectIdentity = ObjectIdentity
ruckusWirelessAdapterProducts = _RuckusWirelessAdapterProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 2)
)
_RuckusVF2111_ObjectIdentity = ObjectIdentity
ruckusVF2111 = _RuckusVF2111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 1)
)
_RuckusVF2121_ObjectIdentity = ObjectIdentity
ruckusVF2121 = _RuckusVF2121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 2)
)
_RuckusVF7111_ObjectIdentity = ObjectIdentity
ruckusVF7111 = _RuckusVF7111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 3)
)
_RuckusWirelessMetroProducts_ObjectIdentity = ObjectIdentity
ruckusWirelessMetroProducts = _RuckusWirelessMetroProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 3)
)
_RuckusMM2225_ObjectIdentity = ObjectIdentity
ruckusMM2225 = _RuckusMM2225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 1)
)
_RuckusMM2211_ObjectIdentity = ObjectIdentity
ruckusMM2211 = _RuckusMM2211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 2)
)
_RuckusMM2221_ObjectIdentity = ObjectIdentity
ruckusMM2221 = _RuckusMM2221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 3)
)
_RuckusWirelessHotzoneProducts_ObjectIdentity = ObjectIdentity
ruckusWirelessHotzoneProducts = _RuckusWirelessHotzoneProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4)
)
_RuckusZF2925_ObjectIdentity = ObjectIdentity
ruckusZF2925 = _RuckusZF2925_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 1)
)
_RuckusZF2942_ObjectIdentity = ObjectIdentity
ruckusZF2942 = _RuckusZF2942_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 2)
)
_RuckusZF7942_ObjectIdentity = ObjectIdentity
ruckusZF7942 = _RuckusZF7942_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 3)
)
_RuckusZF7962_ObjectIdentity = ObjectIdentity
ruckusZF7962 = _RuckusZF7962_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 4)
)
_RuckusZF2741_ObjectIdentity = ObjectIdentity
ruckusZF2741 = _RuckusZF2741_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 5)
)
_RuckusZF7762_ObjectIdentity = ObjectIdentity
ruckusZF7762 = _RuckusZF7762_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 6)
)
_RuckusZF7761CM_ObjectIdentity = ObjectIdentity
ruckusZF7761CM = _RuckusZF7761CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7)
)


class _RuckusZF7761CMControlLED_Type(Integer32):
    """Custom type ruckusZF7761CMControlLED based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("blueActive", 5),
          ("blueActiveCMOnlineLed", 6),
          ("factoryResetAP", 12),
          ("factoryResetCM", 15),
          ("heartbeatOffAP", 9),
          ("heartbeatOffCM", 8),
          ("ledAllOff", 7),
          ("ledAlternateMode1Mode2Mode6", 4),
          ("ledAlternateMode1Mode2OneHour", 3),
          ("ledPerAP", 2),
          ("ledPerCM", 1),
          ("powerCycleAP", 11),
          ("powerCycleCM", 14),
          ("softResetAP", 10),
          ("softResetCM", 13))
    )


_RuckusZF7761CMControlLED_Type.__name__ = "Integer32"
_RuckusZF7761CMControlLED_Object = MibScalar
ruckusZF7761CMControlLED = _RuckusZF7761CMControlLED_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 3),
    _RuckusZF7761CMControlLED_Type()
)
ruckusZF7761CMControlLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMControlLED.setStatus("current")
_RuckusZF7761CMWanIPAddr_Type = IpAddress
_RuckusZF7761CMWanIPAddr_Object = MibScalar
ruckusZF7761CMWanIPAddr = _RuckusZF7761CMWanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 4),
    _RuckusZF7761CMWanIPAddr_Type()
)
ruckusZF7761CMWanIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZF7761CMWanIPAddr.setStatus("current")
_RuckusZF7761CMCustomization_ObjectIdentity = ObjectIdentity
ruckusZF7761CMCustomization = _RuckusZF7761CMCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5)
)


class _RuckusZF7761CMHTTPService_Type(TruthValue):
    """Custom type ruckusZF7761CMHTTPService based on TruthValue"""


_RuckusZF7761CMHTTPService_Object = MibScalar
ruckusZF7761CMHTTPService = _RuckusZF7761CMHTTPService_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 1),
    _RuckusZF7761CMHTTPService_Type()
)
ruckusZF7761CMHTTPService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMHTTPService.setStatus("current")


class _RuckusZF7761CMTelnetService_Type(TruthValue):
    """Custom type ruckusZF7761CMTelnetService based on TruthValue"""


_RuckusZF7761CMTelnetService_Object = MibScalar
ruckusZF7761CMTelnetService = _RuckusZF7761CMTelnetService_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 2),
    _RuckusZF7761CMTelnetService_Type()
)
ruckusZF7761CMTelnetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMTelnetService.setStatus("current")


class _RuckusZF7761CMSSHService_Type(TruthValue):
    """Custom type ruckusZF7761CMSSHService based on TruthValue"""


_RuckusZF7761CMSSHService_Object = MibScalar
ruckusZF7761CMSSHService = _RuckusZF7761CMSSHService_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 3),
    _RuckusZF7761CMSSHService_Type()
)
ruckusZF7761CMSSHService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMSSHService.setStatus("current")


class _RuckusZF7761CMUsername_Type(DisplayString):
    """Custom type ruckusZF7761CMUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZF7761CMUsername_Type.__name__ = "DisplayString"
_RuckusZF7761CMUsername_Object = MibScalar
ruckusZF7761CMUsername = _RuckusZF7761CMUsername_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 4),
    _RuckusZF7761CMUsername_Type()
)
ruckusZF7761CMUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMUsername.setStatus("current")


class _RuckusZF7761CMPassword_Type(DisplayString):
    """Custom type ruckusZF7761CMPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZF7761CMPassword_Type.__name__ = "DisplayString"
_RuckusZF7761CMPassword_Object = MibScalar
ruckusZF7761CMPassword = _RuckusZF7761CMPassword_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 5),
    _RuckusZF7761CMPassword_Type()
)
ruckusZF7761CMPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMPassword.setStatus("current")


class _RuckusZF7761CMLEDMode_Type(Integer32):
    """Custom type ruckusZF7761CMLEDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blueActive", 1),
          ("blueActiveCMOnlineLed", 2),
          ("ledAllOff", 0))
    )


_RuckusZF7761CMLEDMode_Type.__name__ = "Integer32"
_RuckusZF7761CMLEDMode_Object = MibScalar
ruckusZF7761CMLEDMode = _RuckusZF7761CMLEDMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 6),
    _RuckusZF7761CMLEDMode_Type()
)
ruckusZF7761CMLEDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMLEDMode.setStatus("current")
_RuckusZF7761CMHeartbeatMonitorCM_Type = TruthValue
_RuckusZF7761CMHeartbeatMonitorCM_Object = MibScalar
ruckusZF7761CMHeartbeatMonitorCM = _RuckusZF7761CMHeartbeatMonitorCM_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 7),
    _RuckusZF7761CMHeartbeatMonitorCM_Type()
)
ruckusZF7761CMHeartbeatMonitorCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMHeartbeatMonitorCM.setStatus("current")
_RuckusZF7761CMHeartbeatMonitorAP_Type = TruthValue
_RuckusZF7761CMHeartbeatMonitorAP_Object = MibScalar
ruckusZF7761CMHeartbeatMonitorAP = _RuckusZF7761CMHeartbeatMonitorAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 8),
    _RuckusZF7761CMHeartbeatMonitorAP_Type()
)
ruckusZF7761CMHeartbeatMonitorAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZF7761CMHeartbeatMonitorAP.setStatus("current")
_RuckusZF7762S_ObjectIdentity = ObjectIdentity
ruckusZF7762S = _RuckusZF7762S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 8)
)
_RuckusZF7762T_ObjectIdentity = ObjectIdentity
ruckusZF7762T = _RuckusZF7762T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 9)
)
_RuckusZF7762N_ObjectIdentity = ObjectIdentity
ruckusZF7762N = _RuckusZF7762N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 10)
)
_RuckusZF7343_ObjectIdentity = ObjectIdentity
ruckusZF7343 = _RuckusZF7343_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 12)
)
_RuckusZF7363_ObjectIdentity = ObjectIdentity
ruckusZF7363 = _RuckusZF7363_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 13)
)
_RuckusZF7341_ObjectIdentity = ObjectIdentity
ruckusZF7341 = _RuckusZF7341_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 14)
)
_RuckusZF7731_ObjectIdentity = ObjectIdentity
ruckusZF7731 = _RuckusZF7731_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 16)
)
_RuckusZF7025_ObjectIdentity = ObjectIdentity
ruckusZF7025 = _RuckusZF7025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 20)
)
_RuckusZF7321_ObjectIdentity = ObjectIdentity
ruckusZF7321 = _RuckusZF7321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 22)
)
_RuckusZF7321U_ObjectIdentity = ObjectIdentity
ruckusZF7321U = _RuckusZF7321U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 23)
)
_RuckusZF2741EXT_ObjectIdentity = ObjectIdentity
ruckusZF2741EXT = _RuckusZF2741EXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 24)
)
_RuckusZF7982_ObjectIdentity = ObjectIdentity
ruckusZF7982 = _RuckusZF7982_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 25)
)
_RuckusZF7782_ObjectIdentity = ObjectIdentity
ruckusZF7782 = _RuckusZF7782_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 28)
)
_RuckusZF7782S_ObjectIdentity = ObjectIdentity
ruckusZF7782S = _RuckusZF7782S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 29)
)
_RuckusZF7782N_ObjectIdentity = ObjectIdentity
ruckusZF7782N = _RuckusZF7782N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 30)
)
_RuckusZF7782E_ObjectIdentity = ObjectIdentity
ruckusZF7782E = _RuckusZF7782E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 31)
)
_RuckusZF8800SAC_ObjectIdentity = ObjectIdentity
ruckusZF8800SAC = _RuckusZF8800SAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 32)
)
_RuckusZF7762AC_ObjectIdentity = ObjectIdentity
ruckusZF7762AC = _RuckusZF7762AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 35)
)
_RuckusZF7762SAC_ObjectIdentity = ObjectIdentity
ruckusZF7762SAC = _RuckusZF7762SAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 36)
)
_RuckusZF7762TAC_ObjectIdentity = ObjectIdentity
ruckusZF7762TAC = _RuckusZF7762TAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 37)
)
_RuckusZF7372_ObjectIdentity = ObjectIdentity
ruckusZF7372 = _RuckusZF7372_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 40)
)
_RuckusZF7372E_ObjectIdentity = ObjectIdentity
ruckusZF7372E = _RuckusZF7372E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 41)
)
_RuckusZF7352_ObjectIdentity = ObjectIdentity
ruckusZF7352 = _RuckusZF7352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 45)
)
_RuckusZF7351_ObjectIdentity = ObjectIdentity
ruckusZF7351 = _RuckusZF7351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 48)
)
_RuckusZF7742_ObjectIdentity = ObjectIdentity
ruckusZF7742 = _RuckusZF7742_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 50)
)
_RuckusZF7055_ObjectIdentity = ObjectIdentity
ruckusZF7055 = _RuckusZF7055_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 52)
)
_RuckusZF7781M_ObjectIdentity = ObjectIdentity
ruckusZF7781M = _RuckusZF7781M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 55)
)
_RuckusZF7781CM_ObjectIdentity = ObjectIdentity
ruckusZF7781CM = _RuckusZF7781CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 56)
)
_RuckusZF7781CME_ObjectIdentity = ObjectIdentity
ruckusZF7781CME = _RuckusZF7781CME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 57)
)
_RuckusZF7781CMS_ObjectIdentity = ObjectIdentity
ruckusZF7781CMS = _RuckusZF7781CMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 58)
)
_RuckusZF7781FN_ObjectIdentity = ObjectIdentity
ruckusZF7781FN = _RuckusZF7781FN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 60)
)
_RuckusZF7781FNE_ObjectIdentity = ObjectIdentity
ruckusZF7781FNE = _RuckusZF7781FNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 61)
)
_RuckusZF7781FNS_ObjectIdentity = ObjectIdentity
ruckusZF7781FNS = _RuckusZF7781FNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 62)
)
_RuckusSC8800SAC_ObjectIdentity = ObjectIdentity
ruckusSC8800SAC = _RuckusSC8800SAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 65)
)
_RuckusSC8800S_ObjectIdentity = ObjectIdentity
ruckusSC8800S = _RuckusSC8800S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 66)
)
_RuckusWirelessControllerProducts_ObjectIdentity = ObjectIdentity
ruckusWirelessControllerProducts = _RuckusWirelessControllerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5)
)
_RuckusZD1000_ObjectIdentity = ObjectIdentity
ruckusZD1000 = _RuckusZD1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1)
)
_RuckusZD1000SystemName_Type = DisplayString
_RuckusZD1000SystemName_Object = MibScalar
ruckusZD1000SystemName = _RuckusZD1000SystemName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 1),
    _RuckusZD1000SystemName_Type()
)
ruckusZD1000SystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemName.setStatus("current")
_RuckusZD1000SystemIPAddr_Type = IpAddress
_RuckusZD1000SystemIPAddr_Object = MibScalar
ruckusZD1000SystemIPAddr = _RuckusZD1000SystemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 2),
    _RuckusZD1000SystemIPAddr_Type()
)
ruckusZD1000SystemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemIPAddr.setStatus("current")
_RuckusZD1000SystemMacAddr_Type = MacAddress
_RuckusZD1000SystemMacAddr_Object = MibScalar
ruckusZD1000SystemMacAddr = _RuckusZD1000SystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 3),
    _RuckusZD1000SystemMacAddr_Type()
)
ruckusZD1000SystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemMacAddr.setStatus("current")
_RuckusZD1000SystemUptime_Type = TimeTicks
_RuckusZD1000SystemUptime_Object = MibScalar
ruckusZD1000SystemUptime = _RuckusZD1000SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 4),
    _RuckusZD1000SystemUptime_Type()
)
ruckusZD1000SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemUptime.setStatus("current")
_RuckusZD1000SystemModel_Type = DisplayString
_RuckusZD1000SystemModel_Object = MibScalar
ruckusZD1000SystemModel = _RuckusZD1000SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 5),
    _RuckusZD1000SystemModel_Type()
)
ruckusZD1000SystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemModel.setStatus("current")
_RuckusZD1000SystemLicensedAPs_Type = Unsigned32
_RuckusZD1000SystemLicensedAPs_Object = MibScalar
ruckusZD1000SystemLicensedAPs = _RuckusZD1000SystemLicensedAPs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 6),
    _RuckusZD1000SystemLicensedAPs_Type()
)
ruckusZD1000SystemLicensedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemLicensedAPs.setStatus("current")
_RuckusZD1000SystemSerialNumber_Type = DisplayString
_RuckusZD1000SystemSerialNumber_Object = MibScalar
ruckusZD1000SystemSerialNumber = _RuckusZD1000SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 7),
    _RuckusZD1000SystemSerialNumber_Type()
)
ruckusZD1000SystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemSerialNumber.setStatus("current")
_RuckusZD1000SystemVersion_Type = DisplayString
_RuckusZD1000SystemVersion_Object = MibScalar
ruckusZD1000SystemVersion = _RuckusZD1000SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 8),
    _RuckusZD1000SystemVersion_Type()
)
ruckusZD1000SystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000SystemVersion.setStatus("current")
_RuckusZD1000CountryCode_Type = RuckusCountryCode
_RuckusZD1000CountryCode_Object = MibScalar
ruckusZD1000CountryCode = _RuckusZD1000CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 9),
    _RuckusZD1000CountryCode_Type()
)
ruckusZD1000CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1000CountryCode.setStatus("current")
_RuckusZD1100_ObjectIdentity = ObjectIdentity
ruckusZD1100 = _RuckusZD1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2)
)
_RuckusZD1100SystemName_Type = DisplayString
_RuckusZD1100SystemName_Object = MibScalar
ruckusZD1100SystemName = _RuckusZD1100SystemName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 1),
    _RuckusZD1100SystemName_Type()
)
ruckusZD1100SystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemName.setStatus("current")
_RuckusZD1100SystemIPAddr_Type = IpAddress
_RuckusZD1100SystemIPAddr_Object = MibScalar
ruckusZD1100SystemIPAddr = _RuckusZD1100SystemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 2),
    _RuckusZD1100SystemIPAddr_Type()
)
ruckusZD1100SystemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemIPAddr.setStatus("current")
_RuckusZD1100SystemMacAddr_Type = MacAddress
_RuckusZD1100SystemMacAddr_Object = MibScalar
ruckusZD1100SystemMacAddr = _RuckusZD1100SystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 3),
    _RuckusZD1100SystemMacAddr_Type()
)
ruckusZD1100SystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemMacAddr.setStatus("current")
_RuckusZD1100SystemUptime_Type = TimeTicks
_RuckusZD1100SystemUptime_Object = MibScalar
ruckusZD1100SystemUptime = _RuckusZD1100SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 4),
    _RuckusZD1100SystemUptime_Type()
)
ruckusZD1100SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemUptime.setStatus("current")
_RuckusZD1100SystemModel_Type = DisplayString
_RuckusZD1100SystemModel_Object = MibScalar
ruckusZD1100SystemModel = _RuckusZD1100SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 5),
    _RuckusZD1100SystemModel_Type()
)
ruckusZD1100SystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemModel.setStatus("current")
_RuckusZD1100SystemLicensedAPs_Type = Unsigned32
_RuckusZD1100SystemLicensedAPs_Object = MibScalar
ruckusZD1100SystemLicensedAPs = _RuckusZD1100SystemLicensedAPs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 6),
    _RuckusZD1100SystemLicensedAPs_Type()
)
ruckusZD1100SystemLicensedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemLicensedAPs.setStatus("current")
_RuckusZD1100SystemSerialNumber_Type = DisplayString
_RuckusZD1100SystemSerialNumber_Object = MibScalar
ruckusZD1100SystemSerialNumber = _RuckusZD1100SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 7),
    _RuckusZD1100SystemSerialNumber_Type()
)
ruckusZD1100SystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemSerialNumber.setStatus("current")
_RuckusZD1100SystemVersion_Type = DisplayString
_RuckusZD1100SystemVersion_Object = MibScalar
ruckusZD1100SystemVersion = _RuckusZD1100SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 8),
    _RuckusZD1100SystemVersion_Type()
)
ruckusZD1100SystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100SystemVersion.setStatus("current")
_RuckusZD1100CountryCode_Type = RuckusCountryCode
_RuckusZD1100CountryCode_Object = MibScalar
ruckusZD1100CountryCode = _RuckusZD1100CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 9),
    _RuckusZD1100CountryCode_Type()
)
ruckusZD1100CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD1100CountryCode.setStatus("current")
_RuckusZD3000_ObjectIdentity = ObjectIdentity
ruckusZD3000 = _RuckusZD3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3)
)
_RuckusZD3000SystemName_Type = DisplayString
_RuckusZD3000SystemName_Object = MibScalar
ruckusZD3000SystemName = _RuckusZD3000SystemName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 1),
    _RuckusZD3000SystemName_Type()
)
ruckusZD3000SystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemName.setStatus("current")
_RuckusZD3000SystemIPAddr_Type = IpAddress
_RuckusZD3000SystemIPAddr_Object = MibScalar
ruckusZD3000SystemIPAddr = _RuckusZD3000SystemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 2),
    _RuckusZD3000SystemIPAddr_Type()
)
ruckusZD3000SystemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemIPAddr.setStatus("current")
_RuckusZD3000SystemMacAddr_Type = MacAddress
_RuckusZD3000SystemMacAddr_Object = MibScalar
ruckusZD3000SystemMacAddr = _RuckusZD3000SystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 3),
    _RuckusZD3000SystemMacAddr_Type()
)
ruckusZD3000SystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemMacAddr.setStatus("current")
_RuckusZD3000SystemUptime_Type = TimeTicks
_RuckusZD3000SystemUptime_Object = MibScalar
ruckusZD3000SystemUptime = _RuckusZD3000SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 4),
    _RuckusZD3000SystemUptime_Type()
)
ruckusZD3000SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemUptime.setStatus("current")
_RuckusZD3000SystemModel_Type = DisplayString
_RuckusZD3000SystemModel_Object = MibScalar
ruckusZD3000SystemModel = _RuckusZD3000SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 5),
    _RuckusZD3000SystemModel_Type()
)
ruckusZD3000SystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemModel.setStatus("current")
_RuckusZD3000SystemLicensedAPs_Type = Unsigned32
_RuckusZD3000SystemLicensedAPs_Object = MibScalar
ruckusZD3000SystemLicensedAPs = _RuckusZD3000SystemLicensedAPs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 6),
    _RuckusZD3000SystemLicensedAPs_Type()
)
ruckusZD3000SystemLicensedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemLicensedAPs.setStatus("current")
_RuckusZD3000SystemSerialNumber_Type = DisplayString
_RuckusZD3000SystemSerialNumber_Object = MibScalar
ruckusZD3000SystemSerialNumber = _RuckusZD3000SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 7),
    _RuckusZD3000SystemSerialNumber_Type()
)
ruckusZD3000SystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemSerialNumber.setStatus("current")
_RuckusZD3000SystemVersion_Type = DisplayString
_RuckusZD3000SystemVersion_Object = MibScalar
ruckusZD3000SystemVersion = _RuckusZD3000SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 8),
    _RuckusZD3000SystemVersion_Type()
)
ruckusZD3000SystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000SystemVersion.setStatus("current")
_RuckusZD3000CountryCode_Type = RuckusCountryCode
_RuckusZD3000CountryCode_Object = MibScalar
ruckusZD3000CountryCode = _RuckusZD3000CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 9),
    _RuckusZD3000CountryCode_Type()
)
ruckusZD3000CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD3000CountryCode.setStatus("current")
_RuckusZD5000_ObjectIdentity = ObjectIdentity
ruckusZD5000 = _RuckusZD5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8)
)
_RuckusZD5000SystemName_Type = DisplayString
_RuckusZD5000SystemName_Object = MibScalar
ruckusZD5000SystemName = _RuckusZD5000SystemName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 1),
    _RuckusZD5000SystemName_Type()
)
ruckusZD5000SystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemName.setStatus("current")
_RuckusZD5000SystemIPAddr_Type = IpAddress
_RuckusZD5000SystemIPAddr_Object = MibScalar
ruckusZD5000SystemIPAddr = _RuckusZD5000SystemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 2),
    _RuckusZD5000SystemIPAddr_Type()
)
ruckusZD5000SystemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemIPAddr.setStatus("current")
_RuckusZD5000SystemMacAddr_Type = MacAddress
_RuckusZD5000SystemMacAddr_Object = MibScalar
ruckusZD5000SystemMacAddr = _RuckusZD5000SystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 3),
    _RuckusZD5000SystemMacAddr_Type()
)
ruckusZD5000SystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemMacAddr.setStatus("current")
_RuckusZD5000SystemUptime_Type = TimeTicks
_RuckusZD5000SystemUptime_Object = MibScalar
ruckusZD5000SystemUptime = _RuckusZD5000SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 4),
    _RuckusZD5000SystemUptime_Type()
)
ruckusZD5000SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemUptime.setStatus("current")
_RuckusZD5000SystemModel_Type = DisplayString
_RuckusZD5000SystemModel_Object = MibScalar
ruckusZD5000SystemModel = _RuckusZD5000SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 5),
    _RuckusZD5000SystemModel_Type()
)
ruckusZD5000SystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemModel.setStatus("current")
_RuckusZD5000SystemLicensedAPs_Type = Unsigned32
_RuckusZD5000SystemLicensedAPs_Object = MibScalar
ruckusZD5000SystemLicensedAPs = _RuckusZD5000SystemLicensedAPs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 6),
    _RuckusZD5000SystemLicensedAPs_Type()
)
ruckusZD5000SystemLicensedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemLicensedAPs.setStatus("current")
_RuckusZD5000SystemSerialNumber_Type = DisplayString
_RuckusZD5000SystemSerialNumber_Object = MibScalar
ruckusZD5000SystemSerialNumber = _RuckusZD5000SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 7),
    _RuckusZD5000SystemSerialNumber_Type()
)
ruckusZD5000SystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemSerialNumber.setStatus("current")
_RuckusZD5000SystemVersion_Type = DisplayString
_RuckusZD5000SystemVersion_Object = MibScalar
ruckusZD5000SystemVersion = _RuckusZD5000SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 8),
    _RuckusZD5000SystemVersion_Type()
)
ruckusZD5000SystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000SystemVersion.setStatus("current")
_RuckusZD5000CountryCode_Type = RuckusCountryCode
_RuckusZD5000CountryCode_Object = MibScalar
ruckusZD5000CountryCode = _RuckusZD5000CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 9),
    _RuckusZD5000CountryCode_Type()
)
ruckusZD5000CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZD5000CountryCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-PRODUCTS-MIB",
    **{"ruckusProductsMIB": ruckusProductsMIB,
       "ruckusWirelessRouterProducts": ruckusWirelessRouterProducts,
       "ruckusVF2825": ruckusVF2825,
       "ruckusVF2811": ruckusVF2811,
       "ruckusVF2821": ruckusVF2821,
       "ruckusVF2835": ruckusVF2835,
       "ruckusVF7811": ruckusVF7811,
       "ruckusWirelessAdapterProducts": ruckusWirelessAdapterProducts,
       "ruckusVF2111": ruckusVF2111,
       "ruckusVF2121": ruckusVF2121,
       "ruckusVF7111": ruckusVF7111,
       "ruckusWirelessMetroProducts": ruckusWirelessMetroProducts,
       "ruckusMM2225": ruckusMM2225,
       "ruckusMM2211": ruckusMM2211,
       "ruckusMM2221": ruckusMM2221,
       "ruckusWirelessHotzoneProducts": ruckusWirelessHotzoneProducts,
       "ruckusZF2925": ruckusZF2925,
       "ruckusZF2942": ruckusZF2942,
       "ruckusZF7942": ruckusZF7942,
       "ruckusZF7962": ruckusZF7962,
       "ruckusZF2741": ruckusZF2741,
       "ruckusZF7762": ruckusZF7762,
       "ruckusZF7761CM": ruckusZF7761CM,
       "ruckusZF7761CMControlLED": ruckusZF7761CMControlLED,
       "ruckusZF7761CMWanIPAddr": ruckusZF7761CMWanIPAddr,
       "ruckusZF7761CMCustomization": ruckusZF7761CMCustomization,
       "ruckusZF7761CMHTTPService": ruckusZF7761CMHTTPService,
       "ruckusZF7761CMTelnetService": ruckusZF7761CMTelnetService,
       "ruckusZF7761CMSSHService": ruckusZF7761CMSSHService,
       "ruckusZF7761CMUsername": ruckusZF7761CMUsername,
       "ruckusZF7761CMPassword": ruckusZF7761CMPassword,
       "ruckusZF7761CMLEDMode": ruckusZF7761CMLEDMode,
       "ruckusZF7761CMHeartbeatMonitorCM": ruckusZF7761CMHeartbeatMonitorCM,
       "ruckusZF7761CMHeartbeatMonitorAP": ruckusZF7761CMHeartbeatMonitorAP,
       "ruckusZF7762S": ruckusZF7762S,
       "ruckusZF7762T": ruckusZF7762T,
       "ruckusZF7762N": ruckusZF7762N,
       "ruckusZF7343": ruckusZF7343,
       "ruckusZF7363": ruckusZF7363,
       "ruckusZF7341": ruckusZF7341,
       "ruckusZF7731": ruckusZF7731,
       "ruckusZF7025": ruckusZF7025,
       "ruckusZF7321": ruckusZF7321,
       "ruckusZF7321U": ruckusZF7321U,
       "ruckusZF2741EXT": ruckusZF2741EXT,
       "ruckusZF7982": ruckusZF7982,
       "ruckusZF7782": ruckusZF7782,
       "ruckusZF7782S": ruckusZF7782S,
       "ruckusZF7782N": ruckusZF7782N,
       "ruckusZF7782E": ruckusZF7782E,
       "ruckusZF8800SAC": ruckusZF8800SAC,
       "ruckusZF7762AC": ruckusZF7762AC,
       "ruckusZF7762SAC": ruckusZF7762SAC,
       "ruckusZF7762TAC": ruckusZF7762TAC,
       "ruckusZF7372": ruckusZF7372,
       "ruckusZF7372E": ruckusZF7372E,
       "ruckusZF7352": ruckusZF7352,
       "ruckusZF7351": ruckusZF7351,
       "ruckusZF7742": ruckusZF7742,
       "ruckusZF7055": ruckusZF7055,
       "ruckusZF7781M": ruckusZF7781M,
       "ruckusZF7781CM": ruckusZF7781CM,
       "ruckusZF7781CME": ruckusZF7781CME,
       "ruckusZF7781CMS": ruckusZF7781CMS,
       "ruckusZF7781FN": ruckusZF7781FN,
       "ruckusZF7781FNE": ruckusZF7781FNE,
       "ruckusZF7781FNS": ruckusZF7781FNS,
       "ruckusSC8800SAC": ruckusSC8800SAC,
       "ruckusSC8800S": ruckusSC8800S,
       "ruckusWirelessControllerProducts": ruckusWirelessControllerProducts,
       "ruckusZD1000": ruckusZD1000,
       "ruckusZD1000SystemName": ruckusZD1000SystemName,
       "ruckusZD1000SystemIPAddr": ruckusZD1000SystemIPAddr,
       "ruckusZD1000SystemMacAddr": ruckusZD1000SystemMacAddr,
       "ruckusZD1000SystemUptime": ruckusZD1000SystemUptime,
       "ruckusZD1000SystemModel": ruckusZD1000SystemModel,
       "ruckusZD1000SystemLicensedAPs": ruckusZD1000SystemLicensedAPs,
       "ruckusZD1000SystemSerialNumber": ruckusZD1000SystemSerialNumber,
       "ruckusZD1000SystemVersion": ruckusZD1000SystemVersion,
       "ruckusZD1000CountryCode": ruckusZD1000CountryCode,
       "ruckusZD1100": ruckusZD1100,
       "ruckusZD1100SystemName": ruckusZD1100SystemName,
       "ruckusZD1100SystemIPAddr": ruckusZD1100SystemIPAddr,
       "ruckusZD1100SystemMacAddr": ruckusZD1100SystemMacAddr,
       "ruckusZD1100SystemUptime": ruckusZD1100SystemUptime,
       "ruckusZD1100SystemModel": ruckusZD1100SystemModel,
       "ruckusZD1100SystemLicensedAPs": ruckusZD1100SystemLicensedAPs,
       "ruckusZD1100SystemSerialNumber": ruckusZD1100SystemSerialNumber,
       "ruckusZD1100SystemVersion": ruckusZD1100SystemVersion,
       "ruckusZD1100CountryCode": ruckusZD1100CountryCode,
       "ruckusZD3000": ruckusZD3000,
       "ruckusZD3000SystemName": ruckusZD3000SystemName,
       "ruckusZD3000SystemIPAddr": ruckusZD3000SystemIPAddr,
       "ruckusZD3000SystemMacAddr": ruckusZD3000SystemMacAddr,
       "ruckusZD3000SystemUptime": ruckusZD3000SystemUptime,
       "ruckusZD3000SystemModel": ruckusZD3000SystemModel,
       "ruckusZD3000SystemLicensedAPs": ruckusZD3000SystemLicensedAPs,
       "ruckusZD3000SystemSerialNumber": ruckusZD3000SystemSerialNumber,
       "ruckusZD3000SystemVersion": ruckusZD3000SystemVersion,
       "ruckusZD3000CountryCode": ruckusZD3000CountryCode,
       "ruckusZD5000": ruckusZD5000,
       "ruckusZD5000SystemName": ruckusZD5000SystemName,
       "ruckusZD5000SystemIPAddr": ruckusZD5000SystemIPAddr,
       "ruckusZD5000SystemMacAddr": ruckusZD5000SystemMacAddr,
       "ruckusZD5000SystemUptime": ruckusZD5000SystemUptime,
       "ruckusZD5000SystemModel": ruckusZD5000SystemModel,
       "ruckusZD5000SystemLicensedAPs": ruckusZD5000SystemLicensedAPs,
       "ruckusZD5000SystemSerialNumber": ruckusZD5000SystemSerialNumber,
       "ruckusZD5000SystemVersion": ruckusZD5000SystemVersion,
       "ruckusZD5000CountryCode": ruckusZD5000CountryCode}
)
