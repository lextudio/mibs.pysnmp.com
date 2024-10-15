# SNMP MIB module (SUN-ILOM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-ILOM-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:33 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ilomCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102)
)
ilomCtrlMIB.setRevisions(
        ("2010-06-11 00:00",
         "2010-06-08 00:00",
         "2009-03-30 00:00",
         "2009-03-03 00:00",
         "2008-05-15 00:00",
         "2008-04-11 00:00",
         "2007-02-20 00:00",
         "2006-12-15 00:00",
         "2005-12-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ILOMCtrlTargetIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 110),
    )



class ILOMCtrlModTargetIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class ILOMCtrlInstanceTargetIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



class ILOMCtrlSessionsConnectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("shell", 1),
          ("snmp", 4),
          ("web", 2))
    )



class ILOMCtrlLocalUserUsername(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )



class ILOMCtrlLocalUserPassword(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 16),
    )



class ILOMCtrlUserRole(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 1),
          ("none", 3),
          ("operator", 2),
          ("other", 4))
    )



class ILOMCtrlUserRoles(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )



class ILOMCtrlLocalUserAuthCLIMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alom", 2),
          ("default", 1))
    )



class ILOMCtrlPowerAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("powerCycle", 3),
          ("powerOff", 2),
          ("powerOn", 1),
          ("powerSoft", 4))
    )



class ILOMCtrlResetAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("force", 3),
          ("reset", 1),
          ("resetNonMaskableInterrupt", 2))
    )



class ILOMCtrlNetworkIpDiscovery(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("other", 3),
          ("static", 1))
    )



class ILOMCtrlEventLogType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("action", 2),
          ("fault", 3),
          ("log", 1),
          ("other", 6),
          ("repair", 5),
          ("state", 4))
    )



class ILOMCtrlEventLogClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("audit", 1),
          ("chassis", 3),
          ("fma", 4),
          ("ipmi", 2),
          ("other", 7),
          ("pcm", 6),
          ("system", 5))
    )



class ILOMCtrlEventSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("disable", 1),
          ("down", 5),
          ("major", 3),
          ("minor", 4),
          ("other", 6))
    )



class ILOMCtrlAlertType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("email", 1),
          ("ipmipet", 3),
          ("snmptrap", 2))
    )



class ILOMCtrlAlertSNMPVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )



class ILOMCtrlBaudRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud115200", 5),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud9600", 1))
    )



class ILOMCtrlFlowControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 4),
          ("software", 3),
          ("unknown", 1))
    )



class ILOMCtrlFirmwareUpdateStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("imageVerificationFailed", 2),
          ("inProgress", 3),
          ("other", 5),
          ("success", 4),
          ("tftpError", 1))
    )



class ILOMCtrlFirmwareUpdateAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearProperties", 1),
          ("initiate", 2))
    )



class ILOMCtrlResetToDefaultsAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("factory", 3),
          ("none", 1))
    )



class ILOMCtrlRedundancyStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("initializing", 1),
          ("other", 5),
          ("standAlone", 4),
          ("standby", 3))
    )



class ILOMCtrlRedundancyAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiateFailover", 2),
          ("ready", 1))
    )



class ILOMCtrlSPARCDiagsLevel(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advsettings", 3),
          ("max", 2),
          ("min", 1))
    )



class ILOMCtrlSPARCDiagsLevelAdv(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("maximum", 4),
          ("minimum", 2),
          ("normal", 3),
          ("other", 5))
    )



class ILOMCtrlSPARCDiagsTrigger(Integer32, TextualConvention):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("allResets", 1),
          ("errorTest", 5),
          ("hwChange", 9),
          ("hwChangeanderrorTest", 11),
          ("hwChangeandpowerOnReset", 10),
          ("none", 2),
          ("powerOnReset", 4),
          ("userReset", 3),
          ("userResetanderrorTest", 7),
          ("userResetandpowerOnReset", 6),
          ("userTestandpowerOnReset", 8))
    )



class ILOMCtrlSPARCDiagsMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("off", 1),
          ("service", 3),
          ("unknown", 4))
    )



class ILOMCtrlSPARCDiagsVerbosity(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advsettings", 3),
          ("max", 2),
          ("min", 1))
    )



class ILOMCtrlSPARCDiagsVerbosityAdv(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("debug", 5),
          ("maximum", 4),
          ("minimum", 2),
          ("none", 1),
          ("normal", 3))
    )



class ILOMCtrlSPARCHostAutoRestartPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dumpcore", 3),
          ("none", 1),
          ("reset", 2))
    )



class ILOMCtrlSPARCHostBootRestart(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reset", 2))
    )



class ILOMCtrlSPARCHostBootFailRecovery(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("powercycle", 2),
          ("poweroff", 3))
    )



class ILOMCtrlSPARCHostSendBreakAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("break", 2),
          ("dumpcore", 3),
          ("nop", 1))
    )



class ILOMCtrlSPARCHostIoReconfigurePolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("nextboot", 2),
          ("true", 3))
    )



class ILOMCtrlSPARCBootModeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("resetNvram", 2))
    )



class ILOMCtrlSPARCKeySwitchState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("diag", 3),
          ("locked", 4),
          ("normal", 1),
          ("standby", 2))
    )



class ILOMCtrlSPARCDiagsAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )



class ILOMCtrlSshKeyGenType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 3),
          ("none", 1),
          ("rsa", 2))
    )



class ILOMCtrlThdAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nop", 3),
          ("resume", 2),
          ("suspend", 1))
    )



class ILOMCtrlBackupAndRestoreAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("restore", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Ilom_ObjectIdentity = ObjectIdentity
ilom = _Ilom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175)
)
_IlomCtrlClients_ObjectIdentity = ObjectIdentity
ilomCtrlClients = _IlomCtrlClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1)
)
_IlomCtrlNtp_ObjectIdentity = ObjectIdentity
ilomCtrlNtp = _IlomCtrlNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 1)
)
_IlomCtrlDeviceNTPServerOneIP_Type = IpAddress
_IlomCtrlDeviceNTPServerOneIP_Object = MibScalar
ilomCtrlDeviceNTPServerOneIP = _IlomCtrlDeviceNTPServerOneIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 1, 1),
    _IlomCtrlDeviceNTPServerOneIP_Type()
)
ilomCtrlDeviceNTPServerOneIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDeviceNTPServerOneIP.setStatus("current")
_IlomCtrlDeviceNTPServerTwoIP_Type = IpAddress
_IlomCtrlDeviceNTPServerTwoIP_Object = MibScalar
ilomCtrlDeviceNTPServerTwoIP = _IlomCtrlDeviceNTPServerTwoIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 1, 2),
    _IlomCtrlDeviceNTPServerTwoIP_Type()
)
ilomCtrlDeviceNTPServerTwoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDeviceNTPServerTwoIP.setStatus("current")
_IlomCtrlLdap_ObjectIdentity = ObjectIdentity
ilomCtrlLdap = _IlomCtrlLdap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2)
)
_IlomCtrlLdapEnabled_Type = TruthValue
_IlomCtrlLdapEnabled_Object = MibScalar
ilomCtrlLdapEnabled = _IlomCtrlLdapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 1),
    _IlomCtrlLdapEnabled_Type()
)
ilomCtrlLdapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapEnabled.setStatus("current")
_IlomCtrlLdapServerIP_Type = IpAddress
_IlomCtrlLdapServerIP_Object = MibScalar
ilomCtrlLdapServerIP = _IlomCtrlLdapServerIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 2),
    _IlomCtrlLdapServerIP_Type()
)
ilomCtrlLdapServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapServerIP.setStatus("current")


class _IlomCtrlLdapPortNumber_Type(Integer32):
    """Custom type ilomCtrlLdapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlLdapPortNumber_Type.__name__ = "Integer32"
_IlomCtrlLdapPortNumber_Object = MibScalar
ilomCtrlLdapPortNumber = _IlomCtrlLdapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 3),
    _IlomCtrlLdapPortNumber_Type()
)
ilomCtrlLdapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapPortNumber.setStatus("current")
_IlomCtrlLdapBindDn_Type = SnmpAdminString
_IlomCtrlLdapBindDn_Object = MibScalar
ilomCtrlLdapBindDn = _IlomCtrlLdapBindDn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 4),
    _IlomCtrlLdapBindDn_Type()
)
ilomCtrlLdapBindDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapBindDn.setStatus("current")
_IlomCtrlLdapBindPassword_Type = SnmpAdminString
_IlomCtrlLdapBindPassword_Object = MibScalar
ilomCtrlLdapBindPassword = _IlomCtrlLdapBindPassword_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 5),
    _IlomCtrlLdapBindPassword_Type()
)
ilomCtrlLdapBindPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapBindPassword.setStatus("current")
_IlomCtrlLdapSearchBase_Type = SnmpAdminString
_IlomCtrlLdapSearchBase_Object = MibScalar
ilomCtrlLdapSearchBase = _IlomCtrlLdapSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 6),
    _IlomCtrlLdapSearchBase_Type()
)
ilomCtrlLdapSearchBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSearchBase.setStatus("current")
_IlomCtrlLdapDefaultRole_Type = ILOMCtrlUserRole
_IlomCtrlLdapDefaultRole_Object = MibScalar
ilomCtrlLdapDefaultRole = _IlomCtrlLdapDefaultRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 7),
    _IlomCtrlLdapDefaultRole_Type()
)
ilomCtrlLdapDefaultRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapDefaultRole.setStatus("deprecated")
_IlomCtrlLdapDefaultRoles_Type = ILOMCtrlUserRoles
_IlomCtrlLdapDefaultRoles_Object = MibScalar
ilomCtrlLdapDefaultRoles = _IlomCtrlLdapDefaultRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 2, 8),
    _IlomCtrlLdapDefaultRoles_Type()
)
ilomCtrlLdapDefaultRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapDefaultRoles.setStatus("current")
_IlomCtrlRadius_ObjectIdentity = ObjectIdentity
ilomCtrlRadius = _IlomCtrlRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3)
)
_IlomCtrlRadiusEnabled_Type = TruthValue
_IlomCtrlRadiusEnabled_Object = MibScalar
ilomCtrlRadiusEnabled = _IlomCtrlRadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3, 1),
    _IlomCtrlRadiusEnabled_Type()
)
ilomCtrlRadiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRadiusEnabled.setStatus("current")
_IlomCtrlRadiusServerIP_Type = IpAddress
_IlomCtrlRadiusServerIP_Object = MibScalar
ilomCtrlRadiusServerIP = _IlomCtrlRadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3, 2),
    _IlomCtrlRadiusServerIP_Type()
)
ilomCtrlRadiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRadiusServerIP.setStatus("current")


class _IlomCtrlRadiusPortNumber_Type(Integer32):
    """Custom type ilomCtrlRadiusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlRadiusPortNumber_Type.__name__ = "Integer32"
_IlomCtrlRadiusPortNumber_Object = MibScalar
ilomCtrlRadiusPortNumber = _IlomCtrlRadiusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3, 3),
    _IlomCtrlRadiusPortNumber_Type()
)
ilomCtrlRadiusPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRadiusPortNumber.setStatus("current")
_IlomCtrlRadiusSecret_Type = SnmpAdminString
_IlomCtrlRadiusSecret_Object = MibScalar
ilomCtrlRadiusSecret = _IlomCtrlRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3, 4),
    _IlomCtrlRadiusSecret_Type()
)
ilomCtrlRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRadiusSecret.setStatus("current")
_IlomCtrlRadiusDefaultRole_Type = ILOMCtrlUserRole
_IlomCtrlRadiusDefaultRole_Object = MibScalar
ilomCtrlRadiusDefaultRole = _IlomCtrlRadiusDefaultRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3, 5),
    _IlomCtrlRadiusDefaultRole_Type()
)
ilomCtrlRadiusDefaultRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRadiusDefaultRole.setStatus("deprecated")
_IlomCtrlRadiusDefaultRoles_Type = ILOMCtrlUserRoles
_IlomCtrlRadiusDefaultRoles_Object = MibScalar
ilomCtrlRadiusDefaultRoles = _IlomCtrlRadiusDefaultRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 3, 6),
    _IlomCtrlRadiusDefaultRoles_Type()
)
ilomCtrlRadiusDefaultRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRadiusDefaultRoles.setStatus("current")
_IlomCtrlRemoteSyslog_ObjectIdentity = ObjectIdentity
ilomCtrlRemoteSyslog = _IlomCtrlRemoteSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 4)
)
_IlomCtrlRemoteSyslogDest1_Type = IpAddress
_IlomCtrlRemoteSyslogDest1_Object = MibScalar
ilomCtrlRemoteSyslogDest1 = _IlomCtrlRemoteSyslogDest1_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 4, 1),
    _IlomCtrlRemoteSyslogDest1_Type()
)
ilomCtrlRemoteSyslogDest1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRemoteSyslogDest1.setStatus("current")
_IlomCtrlRemoteSyslogDest2_Type = IpAddress
_IlomCtrlRemoteSyslogDest2_Object = MibScalar
ilomCtrlRemoteSyslogDest2 = _IlomCtrlRemoteSyslogDest2_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 4, 2),
    _IlomCtrlRemoteSyslogDest2_Type()
)
ilomCtrlRemoteSyslogDest2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRemoteSyslogDest2.setStatus("current")
_IlomCtrlActiveDirectory_ObjectIdentity = ObjectIdentity
ilomCtrlActiveDirectory = _IlomCtrlActiveDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5)
)
_IlomCtrlActiveDirectoryEnabled_Type = TruthValue
_IlomCtrlActiveDirectoryEnabled_Object = MibScalar
ilomCtrlActiveDirectoryEnabled = _IlomCtrlActiveDirectoryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 1),
    _IlomCtrlActiveDirectoryEnabled_Type()
)
ilomCtrlActiveDirectoryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryEnabled.setStatus("current")
_IlomCtrlActiveDirectoryIP_Type = IpAddress
_IlomCtrlActiveDirectoryIP_Object = MibScalar
ilomCtrlActiveDirectoryIP = _IlomCtrlActiveDirectoryIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 2),
    _IlomCtrlActiveDirectoryIP_Type()
)
ilomCtrlActiveDirectoryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryIP.setStatus("current")


class _IlomCtrlActiveDirectoryPortNumber_Type(Integer32):
    """Custom type ilomCtrlActiveDirectoryPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlActiveDirectoryPortNumber_Type.__name__ = "Integer32"
_IlomCtrlActiveDirectoryPortNumber_Object = MibScalar
ilomCtrlActiveDirectoryPortNumber = _IlomCtrlActiveDirectoryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 3),
    _IlomCtrlActiveDirectoryPortNumber_Type()
)
ilomCtrlActiveDirectoryPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryPortNumber.setStatus("current")
_IlomCtrlActiveDirectoryDefaultRole_Type = ILOMCtrlUserRole
_IlomCtrlActiveDirectoryDefaultRole_Object = MibScalar
ilomCtrlActiveDirectoryDefaultRole = _IlomCtrlActiveDirectoryDefaultRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 4),
    _IlomCtrlActiveDirectoryDefaultRole_Type()
)
ilomCtrlActiveDirectoryDefaultRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryDefaultRole.setStatus("deprecated")
_IlomCtrlActiveDirectoryCertFileURI_Type = SnmpAdminString
_IlomCtrlActiveDirectoryCertFileURI_Object = MibScalar
ilomCtrlActiveDirectoryCertFileURI = _IlomCtrlActiveDirectoryCertFileURI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 5),
    _IlomCtrlActiveDirectoryCertFileURI_Type()
)
ilomCtrlActiveDirectoryCertFileURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertFileURI.setStatus("current")


class _IlomCtrlActiveDirectoryTimeout_Type(Integer32):
    """Custom type ilomCtrlActiveDirectoryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IlomCtrlActiveDirectoryTimeout_Type.__name__ = "Integer32"
_IlomCtrlActiveDirectoryTimeout_Object = MibScalar
ilomCtrlActiveDirectoryTimeout = _IlomCtrlActiveDirectoryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 6),
    _IlomCtrlActiveDirectoryTimeout_Type()
)
ilomCtrlActiveDirectoryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryTimeout.setStatus("current")
_IlomCtrlActiveDirectoryStrictCertEnabled_Type = TruthValue
_IlomCtrlActiveDirectoryStrictCertEnabled_Object = MibScalar
ilomCtrlActiveDirectoryStrictCertEnabled = _IlomCtrlActiveDirectoryStrictCertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 7),
    _IlomCtrlActiveDirectoryStrictCertEnabled_Type()
)
ilomCtrlActiveDirectoryStrictCertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryStrictCertEnabled.setStatus("current")
_IlomCtrlActiveDirectoryCertFileStatus_Type = DisplayString
_IlomCtrlActiveDirectoryCertFileStatus_Object = MibScalar
ilomCtrlActiveDirectoryCertFileStatus = _IlomCtrlActiveDirectoryCertFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 8),
    _IlomCtrlActiveDirectoryCertFileStatus_Type()
)
ilomCtrlActiveDirectoryCertFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertFileStatus.setStatus("current")
_IlomCtrlActiveDirUserDomainTable_Object = MibTable
ilomCtrlActiveDirUserDomainTable = _IlomCtrlActiveDirUserDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 9)
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirUserDomainTable.setStatus("current")
_IlomCtrlActiveDirUserDomainEntry_Object = MibTableRow
ilomCtrlActiveDirUserDomainEntry = _IlomCtrlActiveDirUserDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 9, 1)
)
ilomCtrlActiveDirUserDomainEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirUserDomainId"),
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirUserDomainEntry.setStatus("current")


class _IlomCtrlActiveDirUserDomainId_Type(Integer32):
    """Custom type ilomCtrlActiveDirUserDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlActiveDirUserDomainId_Type.__name__ = "Integer32"
_IlomCtrlActiveDirUserDomainId_Object = MibTableColumn
ilomCtrlActiveDirUserDomainId = _IlomCtrlActiveDirUserDomainId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 9, 1, 1),
    _IlomCtrlActiveDirUserDomainId_Type()
)
ilomCtrlActiveDirUserDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirUserDomainId.setStatus("current")
_IlomCtrlActiveDirUserDomain_Type = SnmpAdminString
_IlomCtrlActiveDirUserDomain_Object = MibTableColumn
ilomCtrlActiveDirUserDomain = _IlomCtrlActiveDirUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 9, 1, 2),
    _IlomCtrlActiveDirUserDomain_Type()
)
ilomCtrlActiveDirUserDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirUserDomain.setStatus("current")
_IlomCtrlActiveDirAdminGroupsTable_Object = MibTable
ilomCtrlActiveDirAdminGroupsTable = _IlomCtrlActiveDirAdminGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 10)
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAdminGroupsTable.setStatus("current")
_IlomCtrlActiveDirAdminGroupsEntry_Object = MibTableRow
ilomCtrlActiveDirAdminGroupsEntry = _IlomCtrlActiveDirAdminGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 10, 1)
)
ilomCtrlActiveDirAdminGroupsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAdminGroupId"),
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAdminGroupsEntry.setStatus("current")


class _IlomCtrlActiveDirAdminGroupId_Type(Integer32):
    """Custom type ilomCtrlActiveDirAdminGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlActiveDirAdminGroupId_Type.__name__ = "Integer32"
_IlomCtrlActiveDirAdminGroupId_Object = MibTableColumn
ilomCtrlActiveDirAdminGroupId = _IlomCtrlActiveDirAdminGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 10, 1, 1),
    _IlomCtrlActiveDirAdminGroupId_Type()
)
ilomCtrlActiveDirAdminGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAdminGroupId.setStatus("current")
_IlomCtrlActiveDirAdminGroupName_Type = SnmpAdminString
_IlomCtrlActiveDirAdminGroupName_Object = MibTableColumn
ilomCtrlActiveDirAdminGroupName = _IlomCtrlActiveDirAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 10, 1, 2),
    _IlomCtrlActiveDirAdminGroupName_Type()
)
ilomCtrlActiveDirAdminGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAdminGroupName.setStatus("current")
_IlomCtrlActiveDirOperatorGroupsTable_Object = MibTable
ilomCtrlActiveDirOperatorGroupsTable = _IlomCtrlActiveDirOperatorGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 11)
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirOperatorGroupsTable.setStatus("current")
_IlomCtrlActiveDirOperatorGroupsEntry_Object = MibTableRow
ilomCtrlActiveDirOperatorGroupsEntry = _IlomCtrlActiveDirOperatorGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 11, 1)
)
ilomCtrlActiveDirOperatorGroupsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirOperatorGroupId"),
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirOperatorGroupsEntry.setStatus("current")


class _IlomCtrlActiveDirOperatorGroupId_Type(Integer32):
    """Custom type ilomCtrlActiveDirOperatorGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlActiveDirOperatorGroupId_Type.__name__ = "Integer32"
_IlomCtrlActiveDirOperatorGroupId_Object = MibTableColumn
ilomCtrlActiveDirOperatorGroupId = _IlomCtrlActiveDirOperatorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 11, 1, 1),
    _IlomCtrlActiveDirOperatorGroupId_Type()
)
ilomCtrlActiveDirOperatorGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirOperatorGroupId.setStatus("current")
_IlomCtrlActiveDirOperatorGroupName_Type = SnmpAdminString
_IlomCtrlActiveDirOperatorGroupName_Object = MibTableColumn
ilomCtrlActiveDirOperatorGroupName = _IlomCtrlActiveDirOperatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 11, 1, 2),
    _IlomCtrlActiveDirOperatorGroupName_Type()
)
ilomCtrlActiveDirOperatorGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirOperatorGroupName.setStatus("current")
_IlomCtrlActiveDirAlternateServerTable_Object = MibTable
ilomCtrlActiveDirAlternateServerTable = _IlomCtrlActiveDirAlternateServerTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12)
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerTable.setStatus("current")
_IlomCtrlActiveDirAlternateServerEntry_Object = MibTableRow
ilomCtrlActiveDirAlternateServerEntry = _IlomCtrlActiveDirAlternateServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1)
)
ilomCtrlActiveDirAlternateServerEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerId"),
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerEntry.setStatus("current")


class _IlomCtrlActiveDirAlternateServerId_Type(Integer32):
    """Custom type ilomCtrlActiveDirAlternateServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlActiveDirAlternateServerId_Type.__name__ = "Integer32"
_IlomCtrlActiveDirAlternateServerId_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerId = _IlomCtrlActiveDirAlternateServerId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 1),
    _IlomCtrlActiveDirAlternateServerId_Type()
)
ilomCtrlActiveDirAlternateServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerId.setStatus("current")
_IlomCtrlActiveDirAlternateServerIp_Type = IpAddress
_IlomCtrlActiveDirAlternateServerIp_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerIp = _IlomCtrlActiveDirAlternateServerIp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 2),
    _IlomCtrlActiveDirAlternateServerIp_Type()
)
ilomCtrlActiveDirAlternateServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerIp.setStatus("current")


class _IlomCtrlActiveDirAlternateServerPort_Type(Integer32):
    """Custom type ilomCtrlActiveDirAlternateServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlActiveDirAlternateServerPort_Type.__name__ = "Integer32"
_IlomCtrlActiveDirAlternateServerPort_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerPort = _IlomCtrlActiveDirAlternateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 3),
    _IlomCtrlActiveDirAlternateServerPort_Type()
)
ilomCtrlActiveDirAlternateServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerPort.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertStatus_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertStatus_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertStatus = _IlomCtrlActiveDirAlternateServerCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 4),
    _IlomCtrlActiveDirAlternateServerCertStatus_Type()
)
ilomCtrlActiveDirAlternateServerCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertStatus.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertURI_Type = SnmpAdminString
_IlomCtrlActiveDirAlternateServerCertURI_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertURI = _IlomCtrlActiveDirAlternateServerCertURI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 5),
    _IlomCtrlActiveDirAlternateServerCertURI_Type()
)
ilomCtrlActiveDirAlternateServerCertURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertURI.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertClear_Type = TruthValue
_IlomCtrlActiveDirAlternateServerCertClear_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertClear = _IlomCtrlActiveDirAlternateServerCertClear_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 6),
    _IlomCtrlActiveDirAlternateServerCertClear_Type()
)
ilomCtrlActiveDirAlternateServerCertClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertClear.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertVersion_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertVersion_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertVersion = _IlomCtrlActiveDirAlternateServerCertVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 7),
    _IlomCtrlActiveDirAlternateServerCertVersion_Type()
)
ilomCtrlActiveDirAlternateServerCertVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertVersion.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertSerialNo_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertSerialNo_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertSerialNo = _IlomCtrlActiveDirAlternateServerCertSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 8),
    _IlomCtrlActiveDirAlternateServerCertSerialNo_Type()
)
ilomCtrlActiveDirAlternateServerCertSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertSerialNo.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertIssuer_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertIssuer_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertIssuer = _IlomCtrlActiveDirAlternateServerCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 9),
    _IlomCtrlActiveDirAlternateServerCertIssuer_Type()
)
ilomCtrlActiveDirAlternateServerCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertIssuer.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertSubject_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertSubject_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertSubject = _IlomCtrlActiveDirAlternateServerCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 10),
    _IlomCtrlActiveDirAlternateServerCertSubject_Type()
)
ilomCtrlActiveDirAlternateServerCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertSubject.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertValidBegin_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertValidBegin_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertValidBegin = _IlomCtrlActiveDirAlternateServerCertValidBegin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 11),
    _IlomCtrlActiveDirAlternateServerCertValidBegin_Type()
)
ilomCtrlActiveDirAlternateServerCertValidBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertValidBegin.setStatus("current")
_IlomCtrlActiveDirAlternateServerCertValidEnd_Type = DisplayString
_IlomCtrlActiveDirAlternateServerCertValidEnd_Object = MibTableColumn
ilomCtrlActiveDirAlternateServerCertValidEnd = _IlomCtrlActiveDirAlternateServerCertValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 12, 1, 12),
    _IlomCtrlActiveDirAlternateServerCertValidEnd_Type()
)
ilomCtrlActiveDirAlternateServerCertValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirAlternateServerCertValidEnd.setStatus("current")


class _IlomCtrlActiveDirectoryLogDetail_Type(Integer32):
    """Custom type ilomCtrlActiveDirectoryLogDetail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("none", 1),
          ("trace", 5))
    )


_IlomCtrlActiveDirectoryLogDetail_Type.__name__ = "Integer32"
_IlomCtrlActiveDirectoryLogDetail_Object = MibScalar
ilomCtrlActiveDirectoryLogDetail = _IlomCtrlActiveDirectoryLogDetail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 13),
    _IlomCtrlActiveDirectoryLogDetail_Type()
)
ilomCtrlActiveDirectoryLogDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryLogDetail.setStatus("current")
_IlomCtrlActiveDirectoryDefaultRoles_Type = ILOMCtrlUserRoles
_IlomCtrlActiveDirectoryDefaultRoles_Object = MibScalar
ilomCtrlActiveDirectoryDefaultRoles = _IlomCtrlActiveDirectoryDefaultRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 14),
    _IlomCtrlActiveDirectoryDefaultRoles_Type()
)
ilomCtrlActiveDirectoryDefaultRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryDefaultRoles.setStatus("current")
_IlomCtrlActiveDirCustomGroupsTable_Object = MibTable
ilomCtrlActiveDirCustomGroupsTable = _IlomCtrlActiveDirCustomGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 15)
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirCustomGroupsTable.setStatus("current")
_IlomCtrlActiveDirCustomGroupsEntry_Object = MibTableRow
ilomCtrlActiveDirCustomGroupsEntry = _IlomCtrlActiveDirCustomGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 15, 1)
)
ilomCtrlActiveDirCustomGroupsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirCustomGroupId"),
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirCustomGroupsEntry.setStatus("current")


class _IlomCtrlActiveDirCustomGroupId_Type(Integer32):
    """Custom type ilomCtrlActiveDirCustomGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlActiveDirCustomGroupId_Type.__name__ = "Integer32"
_IlomCtrlActiveDirCustomGroupId_Object = MibTableColumn
ilomCtrlActiveDirCustomGroupId = _IlomCtrlActiveDirCustomGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 15, 1, 1),
    _IlomCtrlActiveDirCustomGroupId_Type()
)
ilomCtrlActiveDirCustomGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirCustomGroupId.setStatus("current")
_IlomCtrlActiveDirCustomGroupName_Type = SnmpAdminString
_IlomCtrlActiveDirCustomGroupName_Object = MibTableColumn
ilomCtrlActiveDirCustomGroupName = _IlomCtrlActiveDirCustomGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 15, 1, 2),
    _IlomCtrlActiveDirCustomGroupName_Type()
)
ilomCtrlActiveDirCustomGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirCustomGroupName.setStatus("current")
_IlomCtrlActiveDirCustomGroupRoles_Type = ILOMCtrlUserRoles
_IlomCtrlActiveDirCustomGroupRoles_Object = MibTableColumn
ilomCtrlActiveDirCustomGroupRoles = _IlomCtrlActiveDirCustomGroupRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 15, 1, 3),
    _IlomCtrlActiveDirCustomGroupRoles_Type()
)
ilomCtrlActiveDirCustomGroupRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirCustomGroupRoles.setStatus("current")
_IlomCtrlActiveDirectoryCertClear_Type = TruthValue
_IlomCtrlActiveDirectoryCertClear_Object = MibScalar
ilomCtrlActiveDirectoryCertClear = _IlomCtrlActiveDirectoryCertClear_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 16),
    _IlomCtrlActiveDirectoryCertClear_Type()
)
ilomCtrlActiveDirectoryCertClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertClear.setStatus("current")
_IlomCtrlActiveDirectoryCertVersion_Type = DisplayString
_IlomCtrlActiveDirectoryCertVersion_Object = MibScalar
ilomCtrlActiveDirectoryCertVersion = _IlomCtrlActiveDirectoryCertVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 17),
    _IlomCtrlActiveDirectoryCertVersion_Type()
)
ilomCtrlActiveDirectoryCertVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertVersion.setStatus("current")
_IlomCtrlActiveDirectoryCertSerialNo_Type = DisplayString
_IlomCtrlActiveDirectoryCertSerialNo_Object = MibScalar
ilomCtrlActiveDirectoryCertSerialNo = _IlomCtrlActiveDirectoryCertSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 18),
    _IlomCtrlActiveDirectoryCertSerialNo_Type()
)
ilomCtrlActiveDirectoryCertSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertSerialNo.setStatus("current")
_IlomCtrlActiveDirectoryCertIssuer_Type = DisplayString
_IlomCtrlActiveDirectoryCertIssuer_Object = MibScalar
ilomCtrlActiveDirectoryCertIssuer = _IlomCtrlActiveDirectoryCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 19),
    _IlomCtrlActiveDirectoryCertIssuer_Type()
)
ilomCtrlActiveDirectoryCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertIssuer.setStatus("current")
_IlomCtrlActiveDirectoryCertSubject_Type = DisplayString
_IlomCtrlActiveDirectoryCertSubject_Object = MibScalar
ilomCtrlActiveDirectoryCertSubject = _IlomCtrlActiveDirectoryCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 20),
    _IlomCtrlActiveDirectoryCertSubject_Type()
)
ilomCtrlActiveDirectoryCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertSubject.setStatus("current")
_IlomCtrlActiveDirectoryCertValidBegin_Type = DisplayString
_IlomCtrlActiveDirectoryCertValidBegin_Object = MibScalar
ilomCtrlActiveDirectoryCertValidBegin = _IlomCtrlActiveDirectoryCertValidBegin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 21),
    _IlomCtrlActiveDirectoryCertValidBegin_Type()
)
ilomCtrlActiveDirectoryCertValidBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertValidBegin.setStatus("current")
_IlomCtrlActiveDirectoryCertValidEnd_Type = DisplayString
_IlomCtrlActiveDirectoryCertValidEnd_Object = MibScalar
ilomCtrlActiveDirectoryCertValidEnd = _IlomCtrlActiveDirectoryCertValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 22),
    _IlomCtrlActiveDirectoryCertValidEnd_Type()
)
ilomCtrlActiveDirectoryCertValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirectoryCertValidEnd.setStatus("current")
_IlomCtrlActiveDirDnsLocatorEnabled_Type = TruthValue
_IlomCtrlActiveDirDnsLocatorEnabled_Object = MibScalar
ilomCtrlActiveDirDnsLocatorEnabled = _IlomCtrlActiveDirDnsLocatorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 23),
    _IlomCtrlActiveDirDnsLocatorEnabled_Type()
)
ilomCtrlActiveDirDnsLocatorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirDnsLocatorEnabled.setStatus("current")
_IlomCtrlActiveDirDnsLocatorQueryTable_Object = MibTable
ilomCtrlActiveDirDnsLocatorQueryTable = _IlomCtrlActiveDirDnsLocatorQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 24)
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirDnsLocatorQueryTable.setStatus("current")
_IlomCtrlActiveDirDnsLocatorQueryEntry_Object = MibTableRow
ilomCtrlActiveDirDnsLocatorQueryEntry = _IlomCtrlActiveDirDnsLocatorQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 24, 1)
)
ilomCtrlActiveDirDnsLocatorQueryEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirDnsLocatorQueryId"),
)
if mibBuilder.loadTexts:
    ilomCtrlActiveDirDnsLocatorQueryEntry.setStatus("current")


class _IlomCtrlActiveDirDnsLocatorQueryId_Type(Integer32):
    """Custom type ilomCtrlActiveDirDnsLocatorQueryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlActiveDirDnsLocatorQueryId_Type.__name__ = "Integer32"
_IlomCtrlActiveDirDnsLocatorQueryId_Object = MibTableColumn
ilomCtrlActiveDirDnsLocatorQueryId = _IlomCtrlActiveDirDnsLocatorQueryId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 24, 1, 1),
    _IlomCtrlActiveDirDnsLocatorQueryId_Type()
)
ilomCtrlActiveDirDnsLocatorQueryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirDnsLocatorQueryId.setStatus("current")
_IlomCtrlActiveDirDnsLocatorQueryService_Type = SnmpAdminString
_IlomCtrlActiveDirDnsLocatorQueryService_Object = MibTableColumn
ilomCtrlActiveDirDnsLocatorQueryService = _IlomCtrlActiveDirDnsLocatorQueryService_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 24, 1, 2),
    _IlomCtrlActiveDirDnsLocatorQueryService_Type()
)
ilomCtrlActiveDirDnsLocatorQueryService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirDnsLocatorQueryService.setStatus("current")
_IlomCtrlActiveDirExpSearchEnabled_Type = TruthValue
_IlomCtrlActiveDirExpSearchEnabled_Object = MibScalar
ilomCtrlActiveDirExpSearchEnabled = _IlomCtrlActiveDirExpSearchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 25),
    _IlomCtrlActiveDirExpSearchEnabled_Type()
)
ilomCtrlActiveDirExpSearchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirExpSearchEnabled.setStatus("current")
_IlomCtrlActiveDirStrictCredentialErrorEnabled_Type = TruthValue
_IlomCtrlActiveDirStrictCredentialErrorEnabled_Object = MibScalar
ilomCtrlActiveDirStrictCredentialErrorEnabled = _IlomCtrlActiveDirStrictCredentialErrorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 5, 26),
    _IlomCtrlActiveDirStrictCredentialErrorEnabled_Type()
)
ilomCtrlActiveDirStrictCredentialErrorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlActiveDirStrictCredentialErrorEnabled.setStatus("current")
_IlomCtrlSMTP_ObjectIdentity = ObjectIdentity
ilomCtrlSMTP = _IlomCtrlSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 6)
)
_IlomCtrlSMTPEnabled_Type = TruthValue
_IlomCtrlSMTPEnabled_Object = MibScalar
ilomCtrlSMTPEnabled = _IlomCtrlSMTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 6, 1),
    _IlomCtrlSMTPEnabled_Type()
)
ilomCtrlSMTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSMTPEnabled.setStatus("current")
_IlomCtrlSMTPServerIP_Type = IpAddress
_IlomCtrlSMTPServerIP_Object = MibScalar
ilomCtrlSMTPServerIP = _IlomCtrlSMTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 6, 2),
    _IlomCtrlSMTPServerIP_Type()
)
ilomCtrlSMTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSMTPServerIP.setStatus("current")


class _IlomCtrlSMTPPortNumber_Type(Integer32):
    """Custom type ilomCtrlSMTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlSMTPPortNumber_Type.__name__ = "Integer32"
_IlomCtrlSMTPPortNumber_Object = MibScalar
ilomCtrlSMTPPortNumber = _IlomCtrlSMTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 6, 3),
    _IlomCtrlSMTPPortNumber_Type()
)
ilomCtrlSMTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSMTPPortNumber.setStatus("current")


class _IlomCtrlSMTPCustomSender_Type(SnmpAdminString):
    """Custom type ilomCtrlSMTPCustomSender based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IlomCtrlSMTPCustomSender_Type.__name__ = "SnmpAdminString"
_IlomCtrlSMTPCustomSender_Object = MibScalar
ilomCtrlSMTPCustomSender = _IlomCtrlSMTPCustomSender_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 6, 4),
    _IlomCtrlSMTPCustomSender_Type()
)
ilomCtrlSMTPCustomSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSMTPCustomSender.setStatus("current")
_IlomCtrlLdapSsl_ObjectIdentity = ObjectIdentity
ilomCtrlLdapSsl = _IlomCtrlLdapSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7)
)
_IlomCtrlLdapSslGlobalObj_ObjectIdentity = ObjectIdentity
ilomCtrlLdapSslGlobalObj = _IlomCtrlLdapSslGlobalObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1)
)
_IlomCtrlLdapSslEnabled_Type = TruthValue
_IlomCtrlLdapSslEnabled_Object = MibScalar
ilomCtrlLdapSslEnabled = _IlomCtrlLdapSslEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 1),
    _IlomCtrlLdapSslEnabled_Type()
)
ilomCtrlLdapSslEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslEnabled.setStatus("current")
_IlomCtrlLdapSslIP_Type = IpAddress
_IlomCtrlLdapSslIP_Object = MibScalar
ilomCtrlLdapSslIP = _IlomCtrlLdapSslIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 2),
    _IlomCtrlLdapSslIP_Type()
)
ilomCtrlLdapSslIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslIP.setStatus("current")


class _IlomCtrlLdapSslPortNumber_Type(Integer32):
    """Custom type ilomCtrlLdapSslPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlLdapSslPortNumber_Type.__name__ = "Integer32"
_IlomCtrlLdapSslPortNumber_Object = MibScalar
ilomCtrlLdapSslPortNumber = _IlomCtrlLdapSslPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 3),
    _IlomCtrlLdapSslPortNumber_Type()
)
ilomCtrlLdapSslPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslPortNumber.setStatus("current")
_IlomCtrlLdapSslDefaultRole_Type = ILOMCtrlUserRole
_IlomCtrlLdapSslDefaultRole_Object = MibScalar
ilomCtrlLdapSslDefaultRole = _IlomCtrlLdapSslDefaultRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 4),
    _IlomCtrlLdapSslDefaultRole_Type()
)
ilomCtrlLdapSslDefaultRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslDefaultRole.setStatus("current")
_IlomCtrlLdapSslCertFileURI_Type = SnmpAdminString
_IlomCtrlLdapSslCertFileURI_Object = MibScalar
ilomCtrlLdapSslCertFileURI = _IlomCtrlLdapSslCertFileURI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 5),
    _IlomCtrlLdapSslCertFileURI_Type()
)
ilomCtrlLdapSslCertFileURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileURI.setStatus("current")


class _IlomCtrlLdapSslTimeout_Type(Integer32):
    """Custom type ilomCtrlLdapSslTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IlomCtrlLdapSslTimeout_Type.__name__ = "Integer32"
_IlomCtrlLdapSslTimeout_Object = MibScalar
ilomCtrlLdapSslTimeout = _IlomCtrlLdapSslTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 6),
    _IlomCtrlLdapSslTimeout_Type()
)
ilomCtrlLdapSslTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslTimeout.setStatus("current")
_IlomCtrlLdapSslStrictCertEnabled_Type = TruthValue
_IlomCtrlLdapSslStrictCertEnabled_Object = MibScalar
ilomCtrlLdapSslStrictCertEnabled = _IlomCtrlLdapSslStrictCertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 7),
    _IlomCtrlLdapSslStrictCertEnabled_Type()
)
ilomCtrlLdapSslStrictCertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslStrictCertEnabled.setStatus("current")
_IlomCtrlLdapSslCertFileStatus_Type = DisplayString
_IlomCtrlLdapSslCertFileStatus_Object = MibScalar
ilomCtrlLdapSslCertFileStatus = _IlomCtrlLdapSslCertFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 8),
    _IlomCtrlLdapSslCertFileStatus_Type()
)
ilomCtrlLdapSslCertFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileStatus.setStatus("current")


class _IlomCtrlLdapSslLogDetail_Type(Integer32):
    """Custom type ilomCtrlLdapSslLogDetail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("none", 1),
          ("trace", 5))
    )


_IlomCtrlLdapSslLogDetail_Type.__name__ = "Integer32"
_IlomCtrlLdapSslLogDetail_Object = MibScalar
ilomCtrlLdapSslLogDetail = _IlomCtrlLdapSslLogDetail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 9),
    _IlomCtrlLdapSslLogDetail_Type()
)
ilomCtrlLdapSslLogDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslLogDetail.setStatus("current")
_IlomCtrlLdapSslDefaultRoles_Type = ILOMCtrlUserRoles
_IlomCtrlLdapSslDefaultRoles_Object = MibScalar
ilomCtrlLdapSslDefaultRoles = _IlomCtrlLdapSslDefaultRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 10),
    _IlomCtrlLdapSslDefaultRoles_Type()
)
ilomCtrlLdapSslDefaultRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslDefaultRoles.setStatus("current")
_IlomCtrlLdapSslCertFileClear_Type = TruthValue
_IlomCtrlLdapSslCertFileClear_Object = MibScalar
ilomCtrlLdapSslCertFileClear = _IlomCtrlLdapSslCertFileClear_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 11),
    _IlomCtrlLdapSslCertFileClear_Type()
)
ilomCtrlLdapSslCertFileClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileClear.setStatus("current")
_IlomCtrlLdapSslCertFileVersion_Type = DisplayString
_IlomCtrlLdapSslCertFileVersion_Object = MibScalar
ilomCtrlLdapSslCertFileVersion = _IlomCtrlLdapSslCertFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 12),
    _IlomCtrlLdapSslCertFileVersion_Type()
)
ilomCtrlLdapSslCertFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileVersion.setStatus("current")
_IlomCtrlLdapSslCertFileSerialNo_Type = DisplayString
_IlomCtrlLdapSslCertFileSerialNo_Object = MibScalar
ilomCtrlLdapSslCertFileSerialNo = _IlomCtrlLdapSslCertFileSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 13),
    _IlomCtrlLdapSslCertFileSerialNo_Type()
)
ilomCtrlLdapSslCertFileSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileSerialNo.setStatus("current")
_IlomCtrlLdapSslCertFileIssuer_Type = DisplayString
_IlomCtrlLdapSslCertFileIssuer_Object = MibScalar
ilomCtrlLdapSslCertFileIssuer = _IlomCtrlLdapSslCertFileIssuer_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 14),
    _IlomCtrlLdapSslCertFileIssuer_Type()
)
ilomCtrlLdapSslCertFileIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileIssuer.setStatus("current")
_IlomCtrlLdapSslCertFileSubject_Type = DisplayString
_IlomCtrlLdapSslCertFileSubject_Object = MibScalar
ilomCtrlLdapSslCertFileSubject = _IlomCtrlLdapSslCertFileSubject_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 15),
    _IlomCtrlLdapSslCertFileSubject_Type()
)
ilomCtrlLdapSslCertFileSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileSubject.setStatus("current")
_IlomCtrlLdapSslCertFileValidBegin_Type = DisplayString
_IlomCtrlLdapSslCertFileValidBegin_Object = MibScalar
ilomCtrlLdapSslCertFileValidBegin = _IlomCtrlLdapSslCertFileValidBegin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 16),
    _IlomCtrlLdapSslCertFileValidBegin_Type()
)
ilomCtrlLdapSslCertFileValidBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileValidBegin.setStatus("current")
_IlomCtrlLdapSslCertFileValidEnd_Type = DisplayString
_IlomCtrlLdapSslCertFileValidEnd_Object = MibScalar
ilomCtrlLdapSslCertFileValidEnd = _IlomCtrlLdapSslCertFileValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 17),
    _IlomCtrlLdapSslCertFileValidEnd_Type()
)
ilomCtrlLdapSslCertFileValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCertFileValidEnd.setStatus("current")
_IlomCtrlLdapSslOptUsrMappingEnabled_Type = TruthValue
_IlomCtrlLdapSslOptUsrMappingEnabled_Object = MibScalar
ilomCtrlLdapSslOptUsrMappingEnabled = _IlomCtrlLdapSslOptUsrMappingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 18),
    _IlomCtrlLdapSslOptUsrMappingEnabled_Type()
)
ilomCtrlLdapSslOptUsrMappingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOptUsrMappingEnabled.setStatus("current")


class _IlomCtrlLdapSslOptUsrMappingAttrInfo_Type(SnmpAdminString):
    """Custom type ilomCtrlLdapSslOptUsrMappingAttrInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IlomCtrlLdapSslOptUsrMappingAttrInfo_Type.__name__ = "SnmpAdminString"
_IlomCtrlLdapSslOptUsrMappingAttrInfo_Object = MibScalar
ilomCtrlLdapSslOptUsrMappingAttrInfo = _IlomCtrlLdapSslOptUsrMappingAttrInfo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 19),
    _IlomCtrlLdapSslOptUsrMappingAttrInfo_Type()
)
ilomCtrlLdapSslOptUsrMappingAttrInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOptUsrMappingAttrInfo.setStatus("current")


class _IlomCtrlLdapSslOptUsrMappingBindDn_Type(SnmpAdminString):
    """Custom type ilomCtrlLdapSslOptUsrMappingBindDn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IlomCtrlLdapSslOptUsrMappingBindDn_Type.__name__ = "SnmpAdminString"
_IlomCtrlLdapSslOptUsrMappingBindDn_Object = MibScalar
ilomCtrlLdapSslOptUsrMappingBindDn = _IlomCtrlLdapSslOptUsrMappingBindDn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 20),
    _IlomCtrlLdapSslOptUsrMappingBindDn_Type()
)
ilomCtrlLdapSslOptUsrMappingBindDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOptUsrMappingBindDn.setStatus("current")


class _IlomCtrlLdapSslOptUsrMappingBindPw_Type(SnmpAdminString):
    """Custom type ilomCtrlLdapSslOptUsrMappingBindPw based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IlomCtrlLdapSslOptUsrMappingBindPw_Type.__name__ = "SnmpAdminString"
_IlomCtrlLdapSslOptUsrMappingBindPw_Object = MibScalar
ilomCtrlLdapSslOptUsrMappingBindPw = _IlomCtrlLdapSslOptUsrMappingBindPw_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 21),
    _IlomCtrlLdapSslOptUsrMappingBindPw_Type()
)
ilomCtrlLdapSslOptUsrMappingBindPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOptUsrMappingBindPw.setStatus("current")


class _IlomCtrlLdapSslOptUsrMappingSearchBase_Type(SnmpAdminString):
    """Custom type ilomCtrlLdapSslOptUsrMappingSearchBase based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IlomCtrlLdapSslOptUsrMappingSearchBase_Type.__name__ = "SnmpAdminString"
_IlomCtrlLdapSslOptUsrMappingSearchBase_Object = MibScalar
ilomCtrlLdapSslOptUsrMappingSearchBase = _IlomCtrlLdapSslOptUsrMappingSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 1, 22),
    _IlomCtrlLdapSslOptUsrMappingSearchBase_Type()
)
ilomCtrlLdapSslOptUsrMappingSearchBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOptUsrMappingSearchBase.setStatus("current")
_IlomCtrlLdapSslUserDomainTable_Object = MibTable
ilomCtrlLdapSslUserDomainTable = _IlomCtrlLdapSslUserDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslUserDomainTable.setStatus("current")
_IlomCtrlLdapSslUserDomainEntry_Object = MibTableRow
ilomCtrlLdapSslUserDomainEntry = _IlomCtrlLdapSslUserDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 2, 1)
)
ilomCtrlLdapSslUserDomainEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslUserDomainId"),
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslUserDomainEntry.setStatus("current")


class _IlomCtrlLdapSslUserDomainId_Type(Integer32):
    """Custom type ilomCtrlLdapSslUserDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlLdapSslUserDomainId_Type.__name__ = "Integer32"
_IlomCtrlLdapSslUserDomainId_Object = MibTableColumn
ilomCtrlLdapSslUserDomainId = _IlomCtrlLdapSslUserDomainId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 2, 1, 1),
    _IlomCtrlLdapSslUserDomainId_Type()
)
ilomCtrlLdapSslUserDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslUserDomainId.setStatus("current")
_IlomCtrlLdapSslUserDomain_Type = SnmpAdminString
_IlomCtrlLdapSslUserDomain_Object = MibTableColumn
ilomCtrlLdapSslUserDomain = _IlomCtrlLdapSslUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 2, 1, 2),
    _IlomCtrlLdapSslUserDomain_Type()
)
ilomCtrlLdapSslUserDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslUserDomain.setStatus("current")
_IlomCtrlLdapSslAdminGroupsTable_Object = MibTable
ilomCtrlLdapSslAdminGroupsTable = _IlomCtrlLdapSslAdminGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAdminGroupsTable.setStatus("current")
_IlomCtrlLdapSslAdminGroupsEntry_Object = MibTableRow
ilomCtrlLdapSslAdminGroupsEntry = _IlomCtrlLdapSslAdminGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 3, 1)
)
ilomCtrlLdapSslAdminGroupsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAdminGroupId"),
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAdminGroupsEntry.setStatus("current")


class _IlomCtrlLdapSslAdminGroupId_Type(Integer32):
    """Custom type ilomCtrlLdapSslAdminGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlLdapSslAdminGroupId_Type.__name__ = "Integer32"
_IlomCtrlLdapSslAdminGroupId_Object = MibTableColumn
ilomCtrlLdapSslAdminGroupId = _IlomCtrlLdapSslAdminGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 3, 1, 1),
    _IlomCtrlLdapSslAdminGroupId_Type()
)
ilomCtrlLdapSslAdminGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAdminGroupId.setStatus("current")
_IlomCtrlLdapSslAdminGroupName_Type = SnmpAdminString
_IlomCtrlLdapSslAdminGroupName_Object = MibTableColumn
ilomCtrlLdapSslAdminGroupName = _IlomCtrlLdapSslAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 3, 1, 2),
    _IlomCtrlLdapSslAdminGroupName_Type()
)
ilomCtrlLdapSslAdminGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAdminGroupName.setStatus("current")
_IlomCtrlLdapSslOperatorGroupsTable_Object = MibTable
ilomCtrlLdapSslOperatorGroupsTable = _IlomCtrlLdapSslOperatorGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOperatorGroupsTable.setStatus("current")
_IlomCtrlLdapSslOperatorGroupsEntry_Object = MibTableRow
ilomCtrlLdapSslOperatorGroupsEntry = _IlomCtrlLdapSslOperatorGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 4, 1)
)
ilomCtrlLdapSslOperatorGroupsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOperatorGroupId"),
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOperatorGroupsEntry.setStatus("current")


class _IlomCtrlLdapSslOperatorGroupId_Type(Integer32):
    """Custom type ilomCtrlLdapSslOperatorGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlLdapSslOperatorGroupId_Type.__name__ = "Integer32"
_IlomCtrlLdapSslOperatorGroupId_Object = MibTableColumn
ilomCtrlLdapSslOperatorGroupId = _IlomCtrlLdapSslOperatorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 4, 1, 1),
    _IlomCtrlLdapSslOperatorGroupId_Type()
)
ilomCtrlLdapSslOperatorGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOperatorGroupId.setStatus("current")
_IlomCtrlLdapSslOperatorGroupName_Type = SnmpAdminString
_IlomCtrlLdapSslOperatorGroupName_Object = MibTableColumn
ilomCtrlLdapSslOperatorGroupName = _IlomCtrlLdapSslOperatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 4, 1, 2),
    _IlomCtrlLdapSslOperatorGroupName_Type()
)
ilomCtrlLdapSslOperatorGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslOperatorGroupName.setStatus("current")
_IlomCtrlLdapSslAlternateServerTable_Object = MibTable
ilomCtrlLdapSslAlternateServerTable = _IlomCtrlLdapSslAlternateServerTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5)
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerTable.setStatus("current")
_IlomCtrlLdapSslAlternateServerEntry_Object = MibTableRow
ilomCtrlLdapSslAlternateServerEntry = _IlomCtrlLdapSslAlternateServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1)
)
ilomCtrlLdapSslAlternateServerEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerId"),
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerEntry.setStatus("current")


class _IlomCtrlLdapSslAlternateServerId_Type(Integer32):
    """Custom type ilomCtrlLdapSslAlternateServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlLdapSslAlternateServerId_Type.__name__ = "Integer32"
_IlomCtrlLdapSslAlternateServerId_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerId = _IlomCtrlLdapSslAlternateServerId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 1),
    _IlomCtrlLdapSslAlternateServerId_Type()
)
ilomCtrlLdapSslAlternateServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerId.setStatus("current")
_IlomCtrlLdapSslAlternateServerIp_Type = IpAddress
_IlomCtrlLdapSslAlternateServerIp_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerIp = _IlomCtrlLdapSslAlternateServerIp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 2),
    _IlomCtrlLdapSslAlternateServerIp_Type()
)
ilomCtrlLdapSslAlternateServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerIp.setStatus("current")


class _IlomCtrlLdapSslAlternateServerPort_Type(Integer32):
    """Custom type ilomCtrlLdapSslAlternateServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlLdapSslAlternateServerPort_Type.__name__ = "Integer32"
_IlomCtrlLdapSslAlternateServerPort_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerPort = _IlomCtrlLdapSslAlternateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 3),
    _IlomCtrlLdapSslAlternateServerPort_Type()
)
ilomCtrlLdapSslAlternateServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerPort.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertStatus_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertStatus_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertStatus = _IlomCtrlLdapSslAlternateServerCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 4),
    _IlomCtrlLdapSslAlternateServerCertStatus_Type()
)
ilomCtrlLdapSslAlternateServerCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertStatus.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertURI_Type = SnmpAdminString
_IlomCtrlLdapSslAlternateServerCertURI_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertURI = _IlomCtrlLdapSslAlternateServerCertURI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 5),
    _IlomCtrlLdapSslAlternateServerCertURI_Type()
)
ilomCtrlLdapSslAlternateServerCertURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertURI.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertClear_Type = TruthValue
_IlomCtrlLdapSslAlternateServerCertClear_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertClear = _IlomCtrlLdapSslAlternateServerCertClear_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 6),
    _IlomCtrlLdapSslAlternateServerCertClear_Type()
)
ilomCtrlLdapSslAlternateServerCertClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertClear.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertVersion_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertVersion_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertVersion = _IlomCtrlLdapSslAlternateServerCertVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 7),
    _IlomCtrlLdapSslAlternateServerCertVersion_Type()
)
ilomCtrlLdapSslAlternateServerCertVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertVersion.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertSerialNo_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertSerialNo_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertSerialNo = _IlomCtrlLdapSslAlternateServerCertSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 8),
    _IlomCtrlLdapSslAlternateServerCertSerialNo_Type()
)
ilomCtrlLdapSslAlternateServerCertSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertSerialNo.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertIssuer_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertIssuer_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertIssuer = _IlomCtrlLdapSslAlternateServerCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 9),
    _IlomCtrlLdapSslAlternateServerCertIssuer_Type()
)
ilomCtrlLdapSslAlternateServerCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertIssuer.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertSubject_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertSubject_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertSubject = _IlomCtrlLdapSslAlternateServerCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 10),
    _IlomCtrlLdapSslAlternateServerCertSubject_Type()
)
ilomCtrlLdapSslAlternateServerCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertSubject.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertValidBegin_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertValidBegin_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertValidBegin = _IlomCtrlLdapSslAlternateServerCertValidBegin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 11),
    _IlomCtrlLdapSslAlternateServerCertValidBegin_Type()
)
ilomCtrlLdapSslAlternateServerCertValidBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertValidBegin.setStatus("current")
_IlomCtrlLdapSslAlternateServerCertValidEnd_Type = DisplayString
_IlomCtrlLdapSslAlternateServerCertValidEnd_Object = MibTableColumn
ilomCtrlLdapSslAlternateServerCertValidEnd = _IlomCtrlLdapSslAlternateServerCertValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 5, 1, 12),
    _IlomCtrlLdapSslAlternateServerCertValidEnd_Type()
)
ilomCtrlLdapSslAlternateServerCertValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslAlternateServerCertValidEnd.setStatus("current")
_IlomCtrlLdapSslCustomGroupsTable_Object = MibTable
ilomCtrlLdapSslCustomGroupsTable = _IlomCtrlLdapSslCustomGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 6)
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCustomGroupsTable.setStatus("current")
_IlomCtrlLdapSslCustomGroupsEntry_Object = MibTableRow
ilomCtrlLdapSslCustomGroupsEntry = _IlomCtrlLdapSslCustomGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 6, 1)
)
ilomCtrlLdapSslCustomGroupsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCustomGroupId"),
)
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCustomGroupsEntry.setStatus("current")


class _IlomCtrlLdapSslCustomGroupId_Type(Integer32):
    """Custom type ilomCtrlLdapSslCustomGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IlomCtrlLdapSslCustomGroupId_Type.__name__ = "Integer32"
_IlomCtrlLdapSslCustomGroupId_Object = MibTableColumn
ilomCtrlLdapSslCustomGroupId = _IlomCtrlLdapSslCustomGroupId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 6, 1, 1),
    _IlomCtrlLdapSslCustomGroupId_Type()
)
ilomCtrlLdapSslCustomGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCustomGroupId.setStatus("current")
_IlomCtrlLdapSslCustomGroupName_Type = SnmpAdminString
_IlomCtrlLdapSslCustomGroupName_Object = MibTableColumn
ilomCtrlLdapSslCustomGroupName = _IlomCtrlLdapSslCustomGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 6, 1, 2),
    _IlomCtrlLdapSslCustomGroupName_Type()
)
ilomCtrlLdapSslCustomGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCustomGroupName.setStatus("current")
_IlomCtrlLdapSslCustomGroupRoles_Type = ILOMCtrlUserRoles
_IlomCtrlLdapSslCustomGroupRoles_Object = MibTableColumn
ilomCtrlLdapSslCustomGroupRoles = _IlomCtrlLdapSslCustomGroupRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 7, 6, 1, 3),
    _IlomCtrlLdapSslCustomGroupRoles_Type()
)
ilomCtrlLdapSslCustomGroupRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLdapSslCustomGroupRoles.setStatus("current")
_IlomCtrlDNS_ObjectIdentity = ObjectIdentity
ilomCtrlDNS = _IlomCtrlDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 8)
)
_IlomCtrlDNSNameServers_Type = SnmpAdminString
_IlomCtrlDNSNameServers_Object = MibScalar
ilomCtrlDNSNameServers = _IlomCtrlDNSNameServers_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 8, 1),
    _IlomCtrlDNSNameServers_Type()
)
ilomCtrlDNSNameServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDNSNameServers.setStatus("current")
_IlomCtrlDNSSearchPath_Type = SnmpAdminString
_IlomCtrlDNSSearchPath_Object = MibScalar
ilomCtrlDNSSearchPath = _IlomCtrlDNSSearchPath_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 8, 2),
    _IlomCtrlDNSSearchPath_Type()
)
ilomCtrlDNSSearchPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDNSSearchPath.setStatus("current")
_IlomCtrlDNSdhcpAutoDns_Type = TruthValue
_IlomCtrlDNSdhcpAutoDns_Object = MibScalar
ilomCtrlDNSdhcpAutoDns = _IlomCtrlDNSdhcpAutoDns_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 8, 3),
    _IlomCtrlDNSdhcpAutoDns_Type()
)
ilomCtrlDNSdhcpAutoDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDNSdhcpAutoDns.setStatus("current")


class _IlomCtrlDNSTimeout_Type(Integer32):
    """Custom type ilomCtrlDNSTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IlomCtrlDNSTimeout_Type.__name__ = "Integer32"
_IlomCtrlDNSTimeout_Object = MibScalar
ilomCtrlDNSTimeout = _IlomCtrlDNSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 8, 4),
    _IlomCtrlDNSTimeout_Type()
)
ilomCtrlDNSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDNSTimeout.setStatus("current")


class _IlomCtrlDNSRetries_Type(Integer32):
    """Custom type ilomCtrlDNSRetries based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_IlomCtrlDNSRetries_Type.__name__ = "Integer32"
_IlomCtrlDNSRetries_Object = MibScalar
ilomCtrlDNSRetries = _IlomCtrlDNSRetries_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 1, 8, 5),
    _IlomCtrlDNSRetries_Type()
)
ilomCtrlDNSRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDNSRetries.setStatus("current")
_IlomCtrlServices_ObjectIdentity = ObjectIdentity
ilomCtrlServices = _IlomCtrlServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2)
)
_IlomCtrlHttp_ObjectIdentity = ObjectIdentity
ilomCtrlHttp = _IlomCtrlHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 1)
)
_IlomCtrlHttpEnabled_Type = TruthValue
_IlomCtrlHttpEnabled_Object = MibScalar
ilomCtrlHttpEnabled = _IlomCtrlHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 1, 1),
    _IlomCtrlHttpEnabled_Type()
)
ilomCtrlHttpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlHttpEnabled.setStatus("current")


class _IlomCtrlHttpPortNumber_Type(Integer32):
    """Custom type ilomCtrlHttpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlHttpPortNumber_Type.__name__ = "Integer32"
_IlomCtrlHttpPortNumber_Object = MibScalar
ilomCtrlHttpPortNumber = _IlomCtrlHttpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 1, 2),
    _IlomCtrlHttpPortNumber_Type()
)
ilomCtrlHttpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlHttpPortNumber.setStatus("current")
_IlomCtrlHttpSecureRedirect_Type = TruthValue
_IlomCtrlHttpSecureRedirect_Object = MibScalar
ilomCtrlHttpSecureRedirect = _IlomCtrlHttpSecureRedirect_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 1, 3),
    _IlomCtrlHttpSecureRedirect_Type()
)
ilomCtrlHttpSecureRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlHttpSecureRedirect.setStatus("current")
_IlomCtrlHttps_ObjectIdentity = ObjectIdentity
ilomCtrlHttps = _IlomCtrlHttps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 2)
)
_IlomCtrlHttpsEnabled_Type = TruthValue
_IlomCtrlHttpsEnabled_Object = MibScalar
ilomCtrlHttpsEnabled = _IlomCtrlHttpsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 2, 1),
    _IlomCtrlHttpsEnabled_Type()
)
ilomCtrlHttpsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlHttpsEnabled.setStatus("current")


class _IlomCtrlHttpsPortNumber_Type(Integer32):
    """Custom type ilomCtrlHttpsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlHttpsPortNumber_Type.__name__ = "Integer32"
_IlomCtrlHttpsPortNumber_Object = MibScalar
ilomCtrlHttpsPortNumber = _IlomCtrlHttpsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 2, 2),
    _IlomCtrlHttpsPortNumber_Type()
)
ilomCtrlHttpsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlHttpsPortNumber.setStatus("current")
_IlomCtrlSsh_ObjectIdentity = ObjectIdentity
ilomCtrlSsh = _IlomCtrlSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3)
)
_IlomCtrlSshRsaKeyFingerprint_Type = SnmpAdminString
_IlomCtrlSshRsaKeyFingerprint_Object = MibScalar
ilomCtrlSshRsaKeyFingerprint = _IlomCtrlSshRsaKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 1),
    _IlomCtrlSshRsaKeyFingerprint_Type()
)
ilomCtrlSshRsaKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSshRsaKeyFingerprint.setStatus("current")


class _IlomCtrlSshRsaKeyLength_Type(Integer32):
    """Custom type ilomCtrlSshRsaKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlSshRsaKeyLength_Type.__name__ = "Integer32"
_IlomCtrlSshRsaKeyLength_Object = MibScalar
ilomCtrlSshRsaKeyLength = _IlomCtrlSshRsaKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 2),
    _IlomCtrlSshRsaKeyLength_Type()
)
ilomCtrlSshRsaKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSshRsaKeyLength.setStatus("current")
_IlomCtrlSshDsaKeyFingerprint_Type = SnmpAdminString
_IlomCtrlSshDsaKeyFingerprint_Object = MibScalar
ilomCtrlSshDsaKeyFingerprint = _IlomCtrlSshDsaKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 3),
    _IlomCtrlSshDsaKeyFingerprint_Type()
)
ilomCtrlSshDsaKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSshDsaKeyFingerprint.setStatus("current")


class _IlomCtrlSshDsaKeyLength_Type(Integer32):
    """Custom type ilomCtrlSshDsaKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlSshDsaKeyLength_Type.__name__ = "Integer32"
_IlomCtrlSshDsaKeyLength_Object = MibScalar
ilomCtrlSshDsaKeyLength = _IlomCtrlSshDsaKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 4),
    _IlomCtrlSshDsaKeyLength_Type()
)
ilomCtrlSshDsaKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSshDsaKeyLength.setStatus("current")
_IlomCtrlSshGenerateNewKeyAction_Type = TruthValue
_IlomCtrlSshGenerateNewKeyAction_Object = MibScalar
ilomCtrlSshGenerateNewKeyAction = _IlomCtrlSshGenerateNewKeyAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 5),
    _IlomCtrlSshGenerateNewKeyAction_Type()
)
ilomCtrlSshGenerateNewKeyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSshGenerateNewKeyAction.setStatus("current")
_IlomCtrlSshGenerateNewKeyType_Type = ILOMCtrlSshKeyGenType
_IlomCtrlSshGenerateNewKeyType_Object = MibScalar
ilomCtrlSshGenerateNewKeyType = _IlomCtrlSshGenerateNewKeyType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 6),
    _IlomCtrlSshGenerateNewKeyType_Type()
)
ilomCtrlSshGenerateNewKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSshGenerateNewKeyType.setStatus("current")
_IlomCtrlSshRestartSshdAction_Type = TruthValue
_IlomCtrlSshRestartSshdAction_Object = MibScalar
ilomCtrlSshRestartSshdAction = _IlomCtrlSshRestartSshdAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 7),
    _IlomCtrlSshRestartSshdAction_Type()
)
ilomCtrlSshRestartSshdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSshRestartSshdAction.setStatus("current")
_IlomCtrlSshEnabled_Type = TruthValue
_IlomCtrlSshEnabled_Object = MibScalar
ilomCtrlSshEnabled = _IlomCtrlSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 3, 8),
    _IlomCtrlSshEnabled_Type()
)
ilomCtrlSshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSshEnabled.setStatus("current")
_IlomCtrlSingleSignon_ObjectIdentity = ObjectIdentity
ilomCtrlSingleSignon = _IlomCtrlSingleSignon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 4)
)
_IlomCtrlSingleSignonEnabled_Type = TruthValue
_IlomCtrlSingleSignonEnabled_Object = MibScalar
ilomCtrlSingleSignonEnabled = _IlomCtrlSingleSignonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 2, 4, 1),
    _IlomCtrlSingleSignonEnabled_Type()
)
ilomCtrlSingleSignonEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSingleSignonEnabled.setStatus("current")
_IlomCtrlNetwork_ObjectIdentity = ObjectIdentity
ilomCtrlNetwork = _IlomCtrlNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3)
)
_IlomCtrlNetworkTable_Object = MibTable
ilomCtrlNetworkTable = _IlomCtrlNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlNetworkTable.setStatus("current")
_IlomCtrlNetworkEntry_Object = MibTableRow
ilomCtrlNetworkEntry = _IlomCtrlNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1)
)
ilomCtrlNetworkEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkTarget"),
)
if mibBuilder.loadTexts:
    ilomCtrlNetworkEntry.setStatus("current")
_IlomCtrlNetworkTarget_Type = SnmpAdminString
_IlomCtrlNetworkTarget_Object = MibTableColumn
ilomCtrlNetworkTarget = _IlomCtrlNetworkTarget_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 1),
    _IlomCtrlNetworkTarget_Type()
)
ilomCtrlNetworkTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlNetworkTarget.setStatus("current")
_IlomCtrlNetworkMacAddress_Type = SnmpAdminString
_IlomCtrlNetworkMacAddress_Object = MibTableColumn
ilomCtrlNetworkMacAddress = _IlomCtrlNetworkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 2),
    _IlomCtrlNetworkMacAddress_Type()
)
ilomCtrlNetworkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkMacAddress.setStatus("current")
_IlomCtrlNetworkIpDiscovery_Type = ILOMCtrlNetworkIpDiscovery
_IlomCtrlNetworkIpDiscovery_Object = MibTableColumn
ilomCtrlNetworkIpDiscovery = _IlomCtrlNetworkIpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 3),
    _IlomCtrlNetworkIpDiscovery_Type()
)
ilomCtrlNetworkIpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkIpDiscovery.setStatus("current")
_IlomCtrlNetworkIpAddress_Type = IpAddress
_IlomCtrlNetworkIpAddress_Object = MibTableColumn
ilomCtrlNetworkIpAddress = _IlomCtrlNetworkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 4),
    _IlomCtrlNetworkIpAddress_Type()
)
ilomCtrlNetworkIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkIpAddress.setStatus("current")
_IlomCtrlNetworkIpGateway_Type = IpAddress
_IlomCtrlNetworkIpGateway_Object = MibTableColumn
ilomCtrlNetworkIpGateway = _IlomCtrlNetworkIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 5),
    _IlomCtrlNetworkIpGateway_Type()
)
ilomCtrlNetworkIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkIpGateway.setStatus("current")
_IlomCtrlNetworkIpNetmask_Type = IpAddress
_IlomCtrlNetworkIpNetmask_Object = MibTableColumn
ilomCtrlNetworkIpNetmask = _IlomCtrlNetworkIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 6),
    _IlomCtrlNetworkIpNetmask_Type()
)
ilomCtrlNetworkIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkIpNetmask.setStatus("current")
_IlomCtrlNetworkPendingIpDiscovery_Type = ILOMCtrlNetworkIpDiscovery
_IlomCtrlNetworkPendingIpDiscovery_Object = MibTableColumn
ilomCtrlNetworkPendingIpDiscovery = _IlomCtrlNetworkPendingIpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 7),
    _IlomCtrlNetworkPendingIpDiscovery_Type()
)
ilomCtrlNetworkPendingIpDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkPendingIpDiscovery.setStatus("current")
_IlomCtrlNetworkPendingIpAddress_Type = IpAddress
_IlomCtrlNetworkPendingIpAddress_Object = MibTableColumn
ilomCtrlNetworkPendingIpAddress = _IlomCtrlNetworkPendingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 8),
    _IlomCtrlNetworkPendingIpAddress_Type()
)
ilomCtrlNetworkPendingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkPendingIpAddress.setStatus("current")
_IlomCtrlNetworkPendingIpGateway_Type = IpAddress
_IlomCtrlNetworkPendingIpGateway_Object = MibTableColumn
ilomCtrlNetworkPendingIpGateway = _IlomCtrlNetworkPendingIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 9),
    _IlomCtrlNetworkPendingIpGateway_Type()
)
ilomCtrlNetworkPendingIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkPendingIpGateway.setStatus("current")
_IlomCtrlNetworkPendingIpNetmask_Type = IpAddress
_IlomCtrlNetworkPendingIpNetmask_Object = MibTableColumn
ilomCtrlNetworkPendingIpNetmask = _IlomCtrlNetworkPendingIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 10),
    _IlomCtrlNetworkPendingIpNetmask_Type()
)
ilomCtrlNetworkPendingIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkPendingIpNetmask.setStatus("current")
_IlomCtrlNetworkCommitPending_Type = TruthValue
_IlomCtrlNetworkCommitPending_Object = MibTableColumn
ilomCtrlNetworkCommitPending = _IlomCtrlNetworkCommitPending_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 11),
    _IlomCtrlNetworkCommitPending_Type()
)
ilomCtrlNetworkCommitPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkCommitPending.setStatus("current")
_IlomCtrlNetworkOutOfBandMacAddress_Type = SnmpAdminString
_IlomCtrlNetworkOutOfBandMacAddress_Object = MibTableColumn
ilomCtrlNetworkOutOfBandMacAddress = _IlomCtrlNetworkOutOfBandMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 12),
    _IlomCtrlNetworkOutOfBandMacAddress_Type()
)
ilomCtrlNetworkOutOfBandMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkOutOfBandMacAddress.setStatus("current")
_IlomCtrlNetworkSidebandMacAddress_Type = SnmpAdminString
_IlomCtrlNetworkSidebandMacAddress_Object = MibTableColumn
ilomCtrlNetworkSidebandMacAddress = _IlomCtrlNetworkSidebandMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 13),
    _IlomCtrlNetworkSidebandMacAddress_Type()
)
ilomCtrlNetworkSidebandMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkSidebandMacAddress.setStatus("current")
_IlomCtrlNetworkPendingManagementPort_Type = SnmpAdminString
_IlomCtrlNetworkPendingManagementPort_Object = MibTableColumn
ilomCtrlNetworkPendingManagementPort = _IlomCtrlNetworkPendingManagementPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 14),
    _IlomCtrlNetworkPendingManagementPort_Type()
)
ilomCtrlNetworkPendingManagementPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkPendingManagementPort.setStatus("current")
_IlomCtrlNetworkManagementPort_Type = SnmpAdminString
_IlomCtrlNetworkManagementPort_Object = MibTableColumn
ilomCtrlNetworkManagementPort = _IlomCtrlNetworkManagementPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 15),
    _IlomCtrlNetworkManagementPort_Type()
)
ilomCtrlNetworkManagementPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkManagementPort.setStatus("current")
_IlomCtrlNetworkDHCPServerAddr_Type = IpAddress
_IlomCtrlNetworkDHCPServerAddr_Object = MibTableColumn
ilomCtrlNetworkDHCPServerAddr = _IlomCtrlNetworkDHCPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 16),
    _IlomCtrlNetworkDHCPServerAddr_Type()
)
ilomCtrlNetworkDHCPServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlNetworkDHCPServerAddr.setStatus("current")
_IlomCtrlNetworkState_Type = TruthValue
_IlomCtrlNetworkState_Object = MibTableColumn
ilomCtrlNetworkState = _IlomCtrlNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 3, 1, 1, 17),
    _IlomCtrlNetworkState_Type()
)
ilomCtrlNetworkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNetworkState.setStatus("current")
_IlomCtrlUsers_ObjectIdentity = ObjectIdentity
ilomCtrlUsers = _IlomCtrlUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4)
)
_IlomCtrlLocalUserAuthTable_Object = MibTable
ilomCtrlLocalUserAuthTable = _IlomCtrlLocalUserAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthTable.setStatus("deprecated")
_IlomCtrlLocalUserAuthEntry_Object = MibTableRow
ilomCtrlLocalUserAuthEntry = _IlomCtrlLocalUserAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1, 1)
)
ilomCtrlLocalUserAuthEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserAuthUsername"),
)
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthEntry.setStatus("deprecated")
_IlomCtrlLocalUserAuthUsername_Type = SnmpAdminString
_IlomCtrlLocalUserAuthUsername_Object = MibTableColumn
ilomCtrlLocalUserAuthUsername = _IlomCtrlLocalUserAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1, 1, 1),
    _IlomCtrlLocalUserAuthUsername_Type()
)
ilomCtrlLocalUserAuthUsername.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthUsername.setStatus("deprecated")
_IlomCtrlLocalUserAuthPassword_Type = SnmpAdminString
_IlomCtrlLocalUserAuthPassword_Object = MibTableColumn
ilomCtrlLocalUserAuthPassword = _IlomCtrlLocalUserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1, 1, 2),
    _IlomCtrlLocalUserAuthPassword_Type()
)
ilomCtrlLocalUserAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthPassword.setStatus("deprecated")
_IlomCtrlLocalUserAuthRole_Type = ILOMCtrlUserRole
_IlomCtrlLocalUserAuthRole_Object = MibTableColumn
ilomCtrlLocalUserAuthRole = _IlomCtrlLocalUserAuthRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1, 1, 3),
    _IlomCtrlLocalUserAuthRole_Type()
)
ilomCtrlLocalUserAuthRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthRole.setStatus("deprecated")
_IlomCtrlLocalUserAuthRowStatus_Type = RowStatus
_IlomCtrlLocalUserAuthRowStatus_Object = MibTableColumn
ilomCtrlLocalUserAuthRowStatus = _IlomCtrlLocalUserAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1, 1, 4),
    _IlomCtrlLocalUserAuthRowStatus_Type()
)
ilomCtrlLocalUserAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthRowStatus.setStatus("deprecated")
_IlomCtrlLocalUserAuthCLIMode_Type = ILOMCtrlLocalUserAuthCLIMode
_IlomCtrlLocalUserAuthCLIMode_Object = MibTableColumn
ilomCtrlLocalUserAuthCLIMode = _IlomCtrlLocalUserAuthCLIMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 1, 1, 5),
    _IlomCtrlLocalUserAuthCLIMode_Type()
)
ilomCtrlLocalUserAuthCLIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserAuthCLIMode.setStatus("deprecated")
_IlomCtrlLocalUserTable_Object = MibTable
ilomCtrlLocalUserTable = _IlomCtrlLocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2)
)
if mibBuilder.loadTexts:
    ilomCtrlLocalUserTable.setStatus("current")
_IlomCtrlLocalUserEntry_Object = MibTableRow
ilomCtrlLocalUserEntry = _IlomCtrlLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2, 1)
)
ilomCtrlLocalUserEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserUsername"),
)
if mibBuilder.loadTexts:
    ilomCtrlLocalUserEntry.setStatus("current")
_IlomCtrlLocalUserUsername_Type = ILOMCtrlLocalUserUsername
_IlomCtrlLocalUserUsername_Object = MibTableColumn
ilomCtrlLocalUserUsername = _IlomCtrlLocalUserUsername_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2, 1, 1),
    _IlomCtrlLocalUserUsername_Type()
)
ilomCtrlLocalUserUsername.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserUsername.setStatus("current")
_IlomCtrlLocalUserPassword_Type = ILOMCtrlLocalUserPassword
_IlomCtrlLocalUserPassword_Object = MibTableColumn
ilomCtrlLocalUserPassword = _IlomCtrlLocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2, 1, 2),
    _IlomCtrlLocalUserPassword_Type()
)
ilomCtrlLocalUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserPassword.setStatus("current")
_IlomCtrlLocalUserRoles_Type = ILOMCtrlUserRoles
_IlomCtrlLocalUserRoles_Object = MibTableColumn
ilomCtrlLocalUserRoles = _IlomCtrlLocalUserRoles_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2, 1, 3),
    _IlomCtrlLocalUserRoles_Type()
)
ilomCtrlLocalUserRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserRoles.setStatus("current")
_IlomCtrlLocalUserRowStatus_Type = RowStatus
_IlomCtrlLocalUserRowStatus_Object = MibTableColumn
ilomCtrlLocalUserRowStatus = _IlomCtrlLocalUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2, 1, 4),
    _IlomCtrlLocalUserRowStatus_Type()
)
ilomCtrlLocalUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserRowStatus.setStatus("current")
_IlomCtrlLocalUserCLIMode_Type = ILOMCtrlLocalUserAuthCLIMode
_IlomCtrlLocalUserCLIMode_Object = MibTableColumn
ilomCtrlLocalUserCLIMode = _IlomCtrlLocalUserCLIMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 4, 2, 1, 5),
    _IlomCtrlLocalUserCLIMode_Type()
)
ilomCtrlLocalUserCLIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlLocalUserCLIMode.setStatus("current")
_IlomCtrlSessions_ObjectIdentity = ObjectIdentity
ilomCtrlSessions = _IlomCtrlSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5)
)
_IlomCtrlSessionsTable_Object = MibTable
ilomCtrlSessionsTable = _IlomCtrlSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlSessionsTable.setStatus("current")
_IlomCtrlSessionsEntry_Object = MibTableRow
ilomCtrlSessionsEntry = _IlomCtrlSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5, 1, 1)
)
ilomCtrlSessionsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlSessionsId"),
)
if mibBuilder.loadTexts:
    ilomCtrlSessionsEntry.setStatus("current")


class _IlomCtrlSessionsId_Type(Integer32):
    """Custom type ilomCtrlSessionsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlSessionsId_Type.__name__ = "Integer32"
_IlomCtrlSessionsId_Object = MibTableColumn
ilomCtrlSessionsId = _IlomCtrlSessionsId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5, 1, 1, 1),
    _IlomCtrlSessionsId_Type()
)
ilomCtrlSessionsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlSessionsId.setStatus("current")
_IlomCtrlSessionsUsername_Type = SnmpAdminString
_IlomCtrlSessionsUsername_Object = MibTableColumn
ilomCtrlSessionsUsername = _IlomCtrlSessionsUsername_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5, 1, 1, 2),
    _IlomCtrlSessionsUsername_Type()
)
ilomCtrlSessionsUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSessionsUsername.setStatus("current")
_IlomCtrlSessionsConnectionType_Type = ILOMCtrlSessionsConnectionType
_IlomCtrlSessionsConnectionType_Object = MibTableColumn
ilomCtrlSessionsConnectionType = _IlomCtrlSessionsConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5, 1, 1, 3),
    _IlomCtrlSessionsConnectionType_Type()
)
ilomCtrlSessionsConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSessionsConnectionType.setStatus("current")
_IlomCtrlSessionsLoginTime_Type = DateAndTime
_IlomCtrlSessionsLoginTime_Object = MibTableColumn
ilomCtrlSessionsLoginTime = _IlomCtrlSessionsLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 5, 1, 1, 4),
    _IlomCtrlSessionsLoginTime_Type()
)
ilomCtrlSessionsLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSessionsLoginTime.setStatus("current")
_IlomCtrlFirmwareMgmt_ObjectIdentity = ObjectIdentity
ilomCtrlFirmwareMgmt = _IlomCtrlFirmwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6)
)
_IlomCtrlFirmwareMgmtVersion_Type = SnmpAdminString
_IlomCtrlFirmwareMgmtVersion_Object = MibScalar
ilomCtrlFirmwareMgmtVersion = _IlomCtrlFirmwareMgmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 1),
    _IlomCtrlFirmwareMgmtVersion_Type()
)
ilomCtrlFirmwareMgmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareMgmtVersion.setStatus("current")


class _IlomCtrlFirmwareBuildNumber_Type(Integer32):
    """Custom type ilomCtrlFirmwareBuildNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlFirmwareBuildNumber_Type.__name__ = "Integer32"
_IlomCtrlFirmwareBuildNumber_Object = MibScalar
ilomCtrlFirmwareBuildNumber = _IlomCtrlFirmwareBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 2),
    _IlomCtrlFirmwareBuildNumber_Type()
)
ilomCtrlFirmwareBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareBuildNumber.setStatus("current")
_IlomCtrlFirmwareBuildDate_Type = SnmpAdminString
_IlomCtrlFirmwareBuildDate_Object = MibScalar
ilomCtrlFirmwareBuildDate = _IlomCtrlFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 3),
    _IlomCtrlFirmwareBuildDate_Type()
)
ilomCtrlFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareBuildDate.setStatus("current")
_IlomCtrlFirmwareTFTPServerIP_Type = IpAddress
_IlomCtrlFirmwareTFTPServerIP_Object = MibScalar
ilomCtrlFirmwareTFTPServerIP = _IlomCtrlFirmwareTFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 4),
    _IlomCtrlFirmwareTFTPServerIP_Type()
)
ilomCtrlFirmwareTFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareTFTPServerIP.setStatus("current")
_IlomCtrlFirmwareTFTPFileName_Type = SnmpAdminString
_IlomCtrlFirmwareTFTPFileName_Object = MibScalar
ilomCtrlFirmwareTFTPFileName = _IlomCtrlFirmwareTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 5),
    _IlomCtrlFirmwareTFTPFileName_Type()
)
ilomCtrlFirmwareTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareTFTPFileName.setStatus("current")
_IlomCtrlFirmwarePreserveConfig_Type = TruthValue
_IlomCtrlFirmwarePreserveConfig_Object = MibScalar
ilomCtrlFirmwarePreserveConfig = _IlomCtrlFirmwarePreserveConfig_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 6),
    _IlomCtrlFirmwarePreserveConfig_Type()
)
ilomCtrlFirmwarePreserveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlFirmwarePreserveConfig.setStatus("current")
_IlomCtrlFirmwareMgmtStatus_Type = ILOMCtrlFirmwareUpdateStatus
_IlomCtrlFirmwareMgmtStatus_Object = MibScalar
ilomCtrlFirmwareMgmtStatus = _IlomCtrlFirmwareMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 7),
    _IlomCtrlFirmwareMgmtStatus_Type()
)
ilomCtrlFirmwareMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareMgmtStatus.setStatus("current")
_IlomCtrlFirmwareMgmtAction_Type = ILOMCtrlFirmwareUpdateAction
_IlomCtrlFirmwareMgmtAction_Object = MibScalar
ilomCtrlFirmwareMgmtAction = _IlomCtrlFirmwareMgmtAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 8),
    _IlomCtrlFirmwareMgmtAction_Type()
)
ilomCtrlFirmwareMgmtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareMgmtAction.setStatus("current")
_IlomCtrlFirmwareMgmtFilesystemVersion_Type = SnmpAdminString
_IlomCtrlFirmwareMgmtFilesystemVersion_Object = MibScalar
ilomCtrlFirmwareMgmtFilesystemVersion = _IlomCtrlFirmwareMgmtFilesystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 9),
    _IlomCtrlFirmwareMgmtFilesystemVersion_Type()
)
ilomCtrlFirmwareMgmtFilesystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareMgmtFilesystemVersion.setStatus("current")
_IlomCtrlFirmwareDelayBIOS_Type = TruthValue
_IlomCtrlFirmwareDelayBIOS_Object = MibScalar
ilomCtrlFirmwareDelayBIOS = _IlomCtrlFirmwareDelayBIOS_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 6, 10),
    _IlomCtrlFirmwareDelayBIOS_Type()
)
ilomCtrlFirmwareDelayBIOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlFirmwareDelayBIOS.setStatus("current")
_IlomCtrlLogs_ObjectIdentity = ObjectIdentity
ilomCtrlLogs = _IlomCtrlLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7)
)
_IlomCtrlEventLog_ObjectIdentity = ObjectIdentity
ilomCtrlEventLog = _IlomCtrlEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1)
)
_IlomCtrlEventLogTable_Object = MibTable
ilomCtrlEventLogTable = _IlomCtrlEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlEventLogTable.setStatus("current")
_IlomCtrlEventLogEntry_Object = MibTableRow
ilomCtrlEventLogEntry = _IlomCtrlEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1)
)
ilomCtrlEventLogEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogRecordID"),
)
if mibBuilder.loadTexts:
    ilomCtrlEventLogEntry.setStatus("current")
_IlomCtrlEventLogRecordID_Type = Unsigned32
_IlomCtrlEventLogRecordID_Object = MibTableColumn
ilomCtrlEventLogRecordID = _IlomCtrlEventLogRecordID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1, 1),
    _IlomCtrlEventLogRecordID_Type()
)
ilomCtrlEventLogRecordID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlEventLogRecordID.setStatus("current")
_IlomCtrlEventLogType_Type = ILOMCtrlEventLogType
_IlomCtrlEventLogType_Object = MibTableColumn
ilomCtrlEventLogType = _IlomCtrlEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1, 2),
    _IlomCtrlEventLogType_Type()
)
ilomCtrlEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlEventLogType.setStatus("current")
_IlomCtrlEventLogTimestamp_Type = DateAndTime
_IlomCtrlEventLogTimestamp_Object = MibTableColumn
ilomCtrlEventLogTimestamp = _IlomCtrlEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1, 3),
    _IlomCtrlEventLogTimestamp_Type()
)
ilomCtrlEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlEventLogTimestamp.setStatus("current")
_IlomCtrlEventLogClass_Type = ILOMCtrlEventLogClass
_IlomCtrlEventLogClass_Object = MibTableColumn
ilomCtrlEventLogClass = _IlomCtrlEventLogClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1, 4),
    _IlomCtrlEventLogClass_Type()
)
ilomCtrlEventLogClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlEventLogClass.setStatus("current")
_IlomCtrlEventLogSeverity_Type = ILOMCtrlEventSeverity
_IlomCtrlEventLogSeverity_Object = MibTableColumn
ilomCtrlEventLogSeverity = _IlomCtrlEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1, 5),
    _IlomCtrlEventLogSeverity_Type()
)
ilomCtrlEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlEventLogSeverity.setStatus("current")
_IlomCtrlEventLogDescription_Type = SnmpAdminString
_IlomCtrlEventLogDescription_Object = MibTableColumn
ilomCtrlEventLogDescription = _IlomCtrlEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 1, 1, 6),
    _IlomCtrlEventLogDescription_Type()
)
ilomCtrlEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlEventLogDescription.setStatus("current")
_IlomCtrlEventLogClear_Type = TruthValue
_IlomCtrlEventLogClear_Object = MibScalar
ilomCtrlEventLogClear = _IlomCtrlEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 7, 1, 2),
    _IlomCtrlEventLogClear_Type()
)
ilomCtrlEventLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlEventLogClear.setStatus("current")
_IlomCtrlAlerts_ObjectIdentity = ObjectIdentity
ilomCtrlAlerts = _IlomCtrlAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8)
)
_IlomCtrlAlertsTable_Object = MibTable
ilomCtrlAlertsTable = _IlomCtrlAlertsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlAlertsTable.setStatus("current")
_IlomCtrlAlertsEntry_Object = MibTableRow
ilomCtrlAlertsEntry = _IlomCtrlAlertsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1)
)
ilomCtrlAlertsEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertID"),
)
if mibBuilder.loadTexts:
    ilomCtrlAlertsEntry.setStatus("current")


class _IlomCtrlAlertID_Type(Integer32):
    """Custom type ilomCtrlAlertID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlAlertID_Type.__name__ = "Integer32"
_IlomCtrlAlertID_Object = MibTableColumn
ilomCtrlAlertID = _IlomCtrlAlertID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 1),
    _IlomCtrlAlertID_Type()
)
ilomCtrlAlertID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlAlertID.setStatus("current")
_IlomCtrlAlertSeverity_Type = ILOMCtrlEventSeverity
_IlomCtrlAlertSeverity_Object = MibTableColumn
ilomCtrlAlertSeverity = _IlomCtrlAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 2),
    _IlomCtrlAlertSeverity_Type()
)
ilomCtrlAlertSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertSeverity.setStatus("current")
_IlomCtrlAlertType_Type = ILOMCtrlAlertType
_IlomCtrlAlertType_Object = MibTableColumn
ilomCtrlAlertType = _IlomCtrlAlertType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 3),
    _IlomCtrlAlertType_Type()
)
ilomCtrlAlertType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertType.setStatus("current")
_IlomCtrlAlertDestinationIP_Type = IpAddress
_IlomCtrlAlertDestinationIP_Object = MibTableColumn
ilomCtrlAlertDestinationIP = _IlomCtrlAlertDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 4),
    _IlomCtrlAlertDestinationIP_Type()
)
ilomCtrlAlertDestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertDestinationIP.setStatus("current")
_IlomCtrlAlertDestinationEmail_Type = SnmpAdminString
_IlomCtrlAlertDestinationEmail_Object = MibTableColumn
ilomCtrlAlertDestinationEmail = _IlomCtrlAlertDestinationEmail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 5),
    _IlomCtrlAlertDestinationEmail_Type()
)
ilomCtrlAlertDestinationEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertDestinationEmail.setStatus("current")
_IlomCtrlAlertSNMPVersion_Type = ILOMCtrlAlertSNMPVersion
_IlomCtrlAlertSNMPVersion_Object = MibTableColumn
ilomCtrlAlertSNMPVersion = _IlomCtrlAlertSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 6),
    _IlomCtrlAlertSNMPVersion_Type()
)
ilomCtrlAlertSNMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertSNMPVersion.setStatus("current")
_IlomCtrlAlertSNMPCommunityOrUsername_Type = SnmpAdminString
_IlomCtrlAlertSNMPCommunityOrUsername_Object = MibTableColumn
ilomCtrlAlertSNMPCommunityOrUsername = _IlomCtrlAlertSNMPCommunityOrUsername_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 7),
    _IlomCtrlAlertSNMPCommunityOrUsername_Type()
)
ilomCtrlAlertSNMPCommunityOrUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertSNMPCommunityOrUsername.setStatus("current")


class _IlomCtrlAlertDestinationPort_Type(Integer32):
    """Custom type ilomCtrlAlertDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlAlertDestinationPort_Type.__name__ = "Integer32"
_IlomCtrlAlertDestinationPort_Object = MibTableColumn
ilomCtrlAlertDestinationPort = _IlomCtrlAlertDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 8),
    _IlomCtrlAlertDestinationPort_Type()
)
ilomCtrlAlertDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertDestinationPort.setStatus("current")
_IlomCtrlAlertEmailEventClassFilter_Type = SnmpAdminString
_IlomCtrlAlertEmailEventClassFilter_Object = MibTableColumn
ilomCtrlAlertEmailEventClassFilter = _IlomCtrlAlertEmailEventClassFilter_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 9),
    _IlomCtrlAlertEmailEventClassFilter_Type()
)
ilomCtrlAlertEmailEventClassFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertEmailEventClassFilter.setStatus("current")
_IlomCtrlAlertEmailEventTypeFilter_Type = SnmpAdminString
_IlomCtrlAlertEmailEventTypeFilter_Object = MibTableColumn
ilomCtrlAlertEmailEventTypeFilter = _IlomCtrlAlertEmailEventTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 10),
    _IlomCtrlAlertEmailEventTypeFilter_Type()
)
ilomCtrlAlertEmailEventTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertEmailEventTypeFilter.setStatus("current")


class _IlomCtrlAlertEmailCustomSender_Type(SnmpAdminString):
    """Custom type ilomCtrlAlertEmailCustomSender based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IlomCtrlAlertEmailCustomSender_Type.__name__ = "SnmpAdminString"
_IlomCtrlAlertEmailCustomSender_Object = MibTableColumn
ilomCtrlAlertEmailCustomSender = _IlomCtrlAlertEmailCustomSender_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 11),
    _IlomCtrlAlertEmailCustomSender_Type()
)
ilomCtrlAlertEmailCustomSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertEmailCustomSender.setStatus("current")


class _IlomCtrlAlertEmailMessagePrefix_Type(SnmpAdminString):
    """Custom type ilomCtrlAlertEmailMessagePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IlomCtrlAlertEmailMessagePrefix_Type.__name__ = "SnmpAdminString"
_IlomCtrlAlertEmailMessagePrefix_Object = MibTableColumn
ilomCtrlAlertEmailMessagePrefix = _IlomCtrlAlertEmailMessagePrefix_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 8, 1, 1, 12),
    _IlomCtrlAlertEmailMessagePrefix_Type()
)
ilomCtrlAlertEmailMessagePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlAlertEmailMessagePrefix.setStatus("current")
_IlomCtrlClock_ObjectIdentity = ObjectIdentity
ilomCtrlClock = _IlomCtrlClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 9)
)
_IlomCtrlDateAndTime_Type = DateAndTime
_IlomCtrlDateAndTime_Object = MibScalar
ilomCtrlDateAndTime = _IlomCtrlDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 9, 1),
    _IlomCtrlDateAndTime_Type()
)
ilomCtrlDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlDateAndTime.setStatus("current")
_IlomCtrlNTPEnabled_Type = TruthValue
_IlomCtrlNTPEnabled_Object = MibScalar
ilomCtrlNTPEnabled = _IlomCtrlNTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 9, 2),
    _IlomCtrlNTPEnabled_Type()
)
ilomCtrlNTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlNTPEnabled.setStatus("current")
_IlomCtrlTimezone_Type = SnmpAdminString
_IlomCtrlTimezone_Object = MibScalar
ilomCtrlTimezone = _IlomCtrlTimezone_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 9, 3),
    _IlomCtrlTimezone_Type()
)
ilomCtrlTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlTimezone.setStatus("current")
_IlomCtrlSerial_ObjectIdentity = ObjectIdentity
ilomCtrlSerial = _IlomCtrlSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 10)
)
_IlomCtrlSerialInternalPortPresent_Type = TruthValue
_IlomCtrlSerialInternalPortPresent_Object = MibScalar
ilomCtrlSerialInternalPortPresent = _IlomCtrlSerialInternalPortPresent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 10, 1),
    _IlomCtrlSerialInternalPortPresent_Type()
)
ilomCtrlSerialInternalPortPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSerialInternalPortPresent.setStatus("current")
_IlomCtrlSerialInternalPortBaudRate_Type = ILOMCtrlBaudRate
_IlomCtrlSerialInternalPortBaudRate_Object = MibScalar
ilomCtrlSerialInternalPortBaudRate = _IlomCtrlSerialInternalPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 10, 2),
    _IlomCtrlSerialInternalPortBaudRate_Type()
)
ilomCtrlSerialInternalPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSerialInternalPortBaudRate.setStatus("current")
_IlomCtrlSerialExternalPortPresent_Type = TruthValue
_IlomCtrlSerialExternalPortPresent_Object = MibScalar
ilomCtrlSerialExternalPortPresent = _IlomCtrlSerialExternalPortPresent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 10, 3),
    _IlomCtrlSerialExternalPortPresent_Type()
)
ilomCtrlSerialExternalPortPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSerialExternalPortPresent.setStatus("current")
_IlomCtrlSerialExternalPortBaudRate_Type = ILOMCtrlBaudRate
_IlomCtrlSerialExternalPortBaudRate_Object = MibScalar
ilomCtrlSerialExternalPortBaudRate = _IlomCtrlSerialExternalPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 10, 4),
    _IlomCtrlSerialExternalPortBaudRate_Type()
)
ilomCtrlSerialExternalPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSerialExternalPortBaudRate.setStatus("current")
_IlomCtrlSerialExternalPortFlowControl_Type = ILOMCtrlFlowControl
_IlomCtrlSerialExternalPortFlowControl_Object = MibScalar
ilomCtrlSerialExternalPortFlowControl = _IlomCtrlSerialExternalPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 10, 5),
    _IlomCtrlSerialExternalPortFlowControl_Type()
)
ilomCtrlSerialExternalPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSerialExternalPortFlowControl.setStatus("current")
_IlomCtrlPowerReset_ObjectIdentity = ObjectIdentity
ilomCtrlPowerReset = _IlomCtrlPowerReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11)
)
_IlomCtrlPowerControl_ObjectIdentity = ObjectIdentity
ilomCtrlPowerControl = _IlomCtrlPowerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 1)
)
_IlomCtrlPowerTable_Object = MibTable
ilomCtrlPowerTable = _IlomCtrlPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 1, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlPowerTable.setStatus("current")
_IlomCtrlPowerEntry_Object = MibTableRow
ilomCtrlPowerEntry = _IlomCtrlPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 1, 1, 1)
)
ilomCtrlPowerEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlPowerTarget"),
)
if mibBuilder.loadTexts:
    ilomCtrlPowerEntry.setStatus("current")
_IlomCtrlPowerTarget_Type = SnmpAdminString
_IlomCtrlPowerTarget_Object = MibTableColumn
ilomCtrlPowerTarget = _IlomCtrlPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 1, 1, 1, 1),
    _IlomCtrlPowerTarget_Type()
)
ilomCtrlPowerTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlPowerTarget.setStatus("current")
_IlomCtrlPowerAction_Type = ILOMCtrlPowerAction
_IlomCtrlPowerAction_Object = MibTableColumn
ilomCtrlPowerAction = _IlomCtrlPowerAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 1, 1, 1, 2),
    _IlomCtrlPowerAction_Type()
)
ilomCtrlPowerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlPowerAction.setStatus("current")
_IlomCtrlResetControl_ObjectIdentity = ObjectIdentity
ilomCtrlResetControl = _IlomCtrlResetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 2)
)
_IlomCtrlResetTable_Object = MibTable
ilomCtrlResetTable = _IlomCtrlResetTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 2, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlResetTable.setStatus("current")
_IlomCtrlResetEntry_Object = MibTableRow
ilomCtrlResetEntry = _IlomCtrlResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 2, 1, 1)
)
ilomCtrlResetEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlResetTarget"),
)
if mibBuilder.loadTexts:
    ilomCtrlResetEntry.setStatus("current")
_IlomCtrlResetTarget_Type = SnmpAdminString
_IlomCtrlResetTarget_Object = MibTableColumn
ilomCtrlResetTarget = _IlomCtrlResetTarget_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 2, 1, 1, 1),
    _IlomCtrlResetTarget_Type()
)
ilomCtrlResetTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlResetTarget.setStatus("current")
_IlomCtrlResetAction_Type = ILOMCtrlResetAction
_IlomCtrlResetAction_Object = MibTableColumn
ilomCtrlResetAction = _IlomCtrlResetAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 11, 2, 1, 1, 2),
    _IlomCtrlResetAction_Type()
)
ilomCtrlResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlResetAction.setStatus("current")
_IlomCtrlRedundancy_ObjectIdentity = ObjectIdentity
ilomCtrlRedundancy = _IlomCtrlRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 12)
)
_IlomCtrlRedundancyStatus_Type = ILOMCtrlRedundancyStatus
_IlomCtrlRedundancyStatus_Object = MibScalar
ilomCtrlRedundancyStatus = _IlomCtrlRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 12, 1),
    _IlomCtrlRedundancyStatus_Type()
)
ilomCtrlRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlRedundancyStatus.setStatus("current")
_IlomCtrlRedundancyAction_Type = ILOMCtrlRedundancyAction
_IlomCtrlRedundancyAction_Object = MibScalar
ilomCtrlRedundancyAction = _IlomCtrlRedundancyAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 12, 2),
    _IlomCtrlRedundancyAction_Type()
)
ilomCtrlRedundancyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlRedundancyAction.setStatus("current")
_IlomCtrlRedundancyFRUName_Type = DisplayString
_IlomCtrlRedundancyFRUName_Object = MibScalar
ilomCtrlRedundancyFRUName = _IlomCtrlRedundancyFRUName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 12, 3),
    _IlomCtrlRedundancyFRUName_Type()
)
ilomCtrlRedundancyFRUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlRedundancyFRUName.setStatus("current")
_IlomCtrlPolicy_ObjectIdentity = ObjectIdentity
ilomCtrlPolicy = _IlomCtrlPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13)
)
_IlomCtrlPolicyTable_Object = MibTable
ilomCtrlPolicyTable = _IlomCtrlPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13, 1)
)
if mibBuilder.loadTexts:
    ilomCtrlPolicyTable.setStatus("current")
_IlomCtrlPolicyEntry_Object = MibTableRow
ilomCtrlPolicyEntry = _IlomCtrlPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13, 1, 1)
)
ilomCtrlPolicyEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlPolicyId"),
)
if mibBuilder.loadTexts:
    ilomCtrlPolicyEntry.setStatus("current")


class _IlomCtrlPolicyId_Type(Integer32):
    """Custom type ilomCtrlPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IlomCtrlPolicyId_Type.__name__ = "Integer32"
_IlomCtrlPolicyId_Object = MibTableColumn
ilomCtrlPolicyId = _IlomCtrlPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13, 1, 1, 1),
    _IlomCtrlPolicyId_Type()
)
ilomCtrlPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlPolicyId.setStatus("current")
_IlomCtrlPolicyShortStr_Type = DisplayString
_IlomCtrlPolicyShortStr_Object = MibTableColumn
ilomCtrlPolicyShortStr = _IlomCtrlPolicyShortStr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13, 1, 1, 2),
    _IlomCtrlPolicyShortStr_Type()
)
ilomCtrlPolicyShortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlPolicyShortStr.setStatus("current")
_IlomCtrlPolicyLongStr_Type = DisplayString
_IlomCtrlPolicyLongStr_Object = MibTableColumn
ilomCtrlPolicyLongStr = _IlomCtrlPolicyLongStr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13, 1, 1, 3),
    _IlomCtrlPolicyLongStr_Type()
)
ilomCtrlPolicyLongStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlPolicyLongStr.setStatus("current")
_IlomCtrlPolicyEnabled_Type = TruthValue
_IlomCtrlPolicyEnabled_Object = MibTableColumn
ilomCtrlPolicyEnabled = _IlomCtrlPolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 13, 1, 1, 4),
    _IlomCtrlPolicyEnabled_Type()
)
ilomCtrlPolicyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlPolicyEnabled.setStatus("current")
_IlomCtrlConfigMgmt_ObjectIdentity = ObjectIdentity
ilomCtrlConfigMgmt = _IlomCtrlConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14)
)
_IlomCtrlResetToDefaultsAction_Type = ILOMCtrlResetToDefaultsAction
_IlomCtrlResetToDefaultsAction_Object = MibScalar
ilomCtrlResetToDefaultsAction = _IlomCtrlResetToDefaultsAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14, 1),
    _IlomCtrlResetToDefaultsAction_Type()
)
ilomCtrlResetToDefaultsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlResetToDefaultsAction.setStatus("current")
_IlomCtrlBackupAndRestore_ObjectIdentity = ObjectIdentity
ilomCtrlBackupAndRestore = _IlomCtrlBackupAndRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14, 2)
)
_IlomCtrlBackupAndRestoreTargetURI_Type = SnmpAdminString
_IlomCtrlBackupAndRestoreTargetURI_Object = MibScalar
ilomCtrlBackupAndRestoreTargetURI = _IlomCtrlBackupAndRestoreTargetURI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14, 2, 1),
    _IlomCtrlBackupAndRestoreTargetURI_Type()
)
ilomCtrlBackupAndRestoreTargetURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlBackupAndRestoreTargetURI.setStatus("current")
_IlomCtrlBackupAndRestorePassphrase_Type = SnmpAdminString
_IlomCtrlBackupAndRestorePassphrase_Object = MibScalar
ilomCtrlBackupAndRestorePassphrase = _IlomCtrlBackupAndRestorePassphrase_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14, 2, 2),
    _IlomCtrlBackupAndRestorePassphrase_Type()
)
ilomCtrlBackupAndRestorePassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlBackupAndRestorePassphrase.setStatus("current")
_IlomCtrlBackupAndRestoreAction_Type = ILOMCtrlBackupAndRestoreAction
_IlomCtrlBackupAndRestoreAction_Object = MibScalar
ilomCtrlBackupAndRestoreAction = _IlomCtrlBackupAndRestoreAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14, 2, 3),
    _IlomCtrlBackupAndRestoreAction_Type()
)
ilomCtrlBackupAndRestoreAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlBackupAndRestoreAction.setStatus("current")
_IlomCtrlBackupAndRestoreActionStatus_Type = SnmpAdminString
_IlomCtrlBackupAndRestoreActionStatus_Object = MibScalar
ilomCtrlBackupAndRestoreActionStatus = _IlomCtrlBackupAndRestoreActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 14, 2, 4),
    _IlomCtrlBackupAndRestoreActionStatus_Type()
)
ilomCtrlBackupAndRestoreActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlBackupAndRestoreActionStatus.setStatus("current")
_IlomCtrlSPARC_ObjectIdentity = ObjectIdentity
ilomCtrlSPARC = _IlomCtrlSPARC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15)
)
_IlomCtrlSPARCDiags_ObjectIdentity = ObjectIdentity
ilomCtrlSPARCDiags = _IlomCtrlSPARCDiags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1)
)
_IlomCtrlSPARCDiagsLevel_Type = ILOMCtrlSPARCDiagsLevel
_IlomCtrlSPARCDiagsLevel_Object = MibScalar
ilomCtrlSPARCDiagsLevel = _IlomCtrlSPARCDiagsLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 1),
    _IlomCtrlSPARCDiagsLevel_Type()
)
ilomCtrlSPARCDiagsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsLevel.setStatus("deprecated")
_IlomCtrlSPARCDiagsTrigger_Type = ILOMCtrlSPARCDiagsTrigger
_IlomCtrlSPARCDiagsTrigger_Object = MibScalar
ilomCtrlSPARCDiagsTrigger = _IlomCtrlSPARCDiagsTrigger_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 2),
    _IlomCtrlSPARCDiagsTrigger_Type()
)
ilomCtrlSPARCDiagsTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsTrigger.setStatus("current")
_IlomCtrlSPARCDiagsVerbosity_Type = ILOMCtrlSPARCDiagsVerbosity
_IlomCtrlSPARCDiagsVerbosity_Object = MibScalar
ilomCtrlSPARCDiagsVerbosity = _IlomCtrlSPARCDiagsVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 3),
    _IlomCtrlSPARCDiagsVerbosity_Type()
)
ilomCtrlSPARCDiagsVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsVerbosity.setStatus("deprecated")
_IlomCtrlSPARCDiagsMode_Type = ILOMCtrlSPARCDiagsMode
_IlomCtrlSPARCDiagsMode_Object = MibScalar
ilomCtrlSPARCDiagsMode = _IlomCtrlSPARCDiagsMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 4),
    _IlomCtrlSPARCDiagsMode_Type()
)
ilomCtrlSPARCDiagsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsMode.setStatus("current")
_IlomCtrlSPARCDiagsPowerOnLevel_Type = ILOMCtrlSPARCDiagsLevelAdv
_IlomCtrlSPARCDiagsPowerOnLevel_Object = MibScalar
ilomCtrlSPARCDiagsPowerOnLevel = _IlomCtrlSPARCDiagsPowerOnLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 5),
    _IlomCtrlSPARCDiagsPowerOnLevel_Type()
)
ilomCtrlSPARCDiagsPowerOnLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsPowerOnLevel.setStatus("current")
_IlomCtrlSPARCDiagsUserResetLevel_Type = ILOMCtrlSPARCDiagsLevelAdv
_IlomCtrlSPARCDiagsUserResetLevel_Object = MibScalar
ilomCtrlSPARCDiagsUserResetLevel = _IlomCtrlSPARCDiagsUserResetLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 6),
    _IlomCtrlSPARCDiagsUserResetLevel_Type()
)
ilomCtrlSPARCDiagsUserResetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsUserResetLevel.setStatus("current")
_IlomCtrlSPARCDiagsErrorResetLevel_Type = ILOMCtrlSPARCDiagsLevelAdv
_IlomCtrlSPARCDiagsErrorResetLevel_Object = MibScalar
ilomCtrlSPARCDiagsErrorResetLevel = _IlomCtrlSPARCDiagsErrorResetLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 7),
    _IlomCtrlSPARCDiagsErrorResetLevel_Type()
)
ilomCtrlSPARCDiagsErrorResetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsErrorResetLevel.setStatus("current")
_IlomCtrlSPARCDiagsPowerOnVerbosity_Type = ILOMCtrlSPARCDiagsVerbosityAdv
_IlomCtrlSPARCDiagsPowerOnVerbosity_Object = MibScalar
ilomCtrlSPARCDiagsPowerOnVerbosity = _IlomCtrlSPARCDiagsPowerOnVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 8),
    _IlomCtrlSPARCDiagsPowerOnVerbosity_Type()
)
ilomCtrlSPARCDiagsPowerOnVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsPowerOnVerbosity.setStatus("current")
_IlomCtrlSPARCDiagsUserResetVerbosity_Type = ILOMCtrlSPARCDiagsVerbosityAdv
_IlomCtrlSPARCDiagsUserResetVerbosity_Object = MibScalar
ilomCtrlSPARCDiagsUserResetVerbosity = _IlomCtrlSPARCDiagsUserResetVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 9),
    _IlomCtrlSPARCDiagsUserResetVerbosity_Type()
)
ilomCtrlSPARCDiagsUserResetVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsUserResetVerbosity.setStatus("current")
_IlomCtrlSPARCDiagsErrorResetVerbosity_Type = ILOMCtrlSPARCDiagsVerbosityAdv
_IlomCtrlSPARCDiagsErrorResetVerbosity_Object = MibScalar
ilomCtrlSPARCDiagsErrorResetVerbosity = _IlomCtrlSPARCDiagsErrorResetVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 10),
    _IlomCtrlSPARCDiagsErrorResetVerbosity_Type()
)
ilomCtrlSPARCDiagsErrorResetVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsErrorResetVerbosity.setStatus("current")


class _IlomCtrlSPARCDiagsStatus_Type(Integer32):
    """Custom type ilomCtrlSPARCDiagsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IlomCtrlSPARCDiagsStatus_Type.__name__ = "Integer32"
_IlomCtrlSPARCDiagsStatus_Object = MibScalar
ilomCtrlSPARCDiagsStatus = _IlomCtrlSPARCDiagsStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 11),
    _IlomCtrlSPARCDiagsStatus_Type()
)
ilomCtrlSPARCDiagsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsStatus.setStatus("current")
_IlomCtrlSPARCDiagsAction_Type = ILOMCtrlSPARCDiagsAction
_IlomCtrlSPARCDiagsAction_Object = MibScalar
ilomCtrlSPARCDiagsAction = _IlomCtrlSPARCDiagsAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 12),
    _IlomCtrlSPARCDiagsAction_Type()
)
ilomCtrlSPARCDiagsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsAction.setStatus("current")
_IlomCtrlSPARCDiagsHwChangeLevel_Type = ILOMCtrlSPARCDiagsLevelAdv
_IlomCtrlSPARCDiagsHwChangeLevel_Object = MibScalar
ilomCtrlSPARCDiagsHwChangeLevel = _IlomCtrlSPARCDiagsHwChangeLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 13),
    _IlomCtrlSPARCDiagsHwChangeLevel_Type()
)
ilomCtrlSPARCDiagsHwChangeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsHwChangeLevel.setStatus("current")
_IlomCtrlSPARCDiagsHwChangeVerbosity_Type = ILOMCtrlSPARCDiagsVerbosityAdv
_IlomCtrlSPARCDiagsHwChangeVerbosity_Object = MibScalar
ilomCtrlSPARCDiagsHwChangeVerbosity = _IlomCtrlSPARCDiagsHwChangeVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 1, 14),
    _IlomCtrlSPARCDiagsHwChangeVerbosity_Type()
)
ilomCtrlSPARCDiagsHwChangeVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCDiagsHwChangeVerbosity.setStatus("current")
_IlomCtrlSPARCHostControl_ObjectIdentity = ObjectIdentity
ilomCtrlSPARCHostControl = _IlomCtrlSPARCHostControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2)
)
_IlomCtrlSPARCHostMACAddress_Type = SnmpAdminString
_IlomCtrlSPARCHostMACAddress_Object = MibScalar
ilomCtrlSPARCHostMACAddress = _IlomCtrlSPARCHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 1),
    _IlomCtrlSPARCHostMACAddress_Type()
)
ilomCtrlSPARCHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostMACAddress.setStatus("current")
_IlomCtrlSPARCHostOBPVersion_Type = SnmpAdminString
_IlomCtrlSPARCHostOBPVersion_Object = MibScalar
ilomCtrlSPARCHostOBPVersion = _IlomCtrlSPARCHostOBPVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 3),
    _IlomCtrlSPARCHostOBPVersion_Type()
)
ilomCtrlSPARCHostOBPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostOBPVersion.setStatus("current")
_IlomCtrlSPARCHostPOSTVersion_Type = SnmpAdminString
_IlomCtrlSPARCHostPOSTVersion_Object = MibScalar
ilomCtrlSPARCHostPOSTVersion = _IlomCtrlSPARCHostPOSTVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 4),
    _IlomCtrlSPARCHostPOSTVersion_Type()
)
ilomCtrlSPARCHostPOSTVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostPOSTVersion.setStatus("current")
_IlomCtrlSPARCHostAutoRunOnError_Type = TruthValue
_IlomCtrlSPARCHostAutoRunOnError_Object = MibScalar
ilomCtrlSPARCHostAutoRunOnError = _IlomCtrlSPARCHostAutoRunOnError_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 6),
    _IlomCtrlSPARCHostAutoRunOnError_Type()
)
ilomCtrlSPARCHostAutoRunOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostAutoRunOnError.setStatus("current")
_IlomCtrlSPARCHostPOSTStatus_Type = SnmpAdminString
_IlomCtrlSPARCHostPOSTStatus_Object = MibScalar
ilomCtrlSPARCHostPOSTStatus = _IlomCtrlSPARCHostPOSTStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 7),
    _IlomCtrlSPARCHostPOSTStatus_Type()
)
ilomCtrlSPARCHostPOSTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostPOSTStatus.setStatus("current")
_IlomCtrlSPARCHostAutoRestartPolicy_Type = ILOMCtrlSPARCHostAutoRestartPolicy
_IlomCtrlSPARCHostAutoRestartPolicy_Object = MibScalar
ilomCtrlSPARCHostAutoRestartPolicy = _IlomCtrlSPARCHostAutoRestartPolicy_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 8),
    _IlomCtrlSPARCHostAutoRestartPolicy_Type()
)
ilomCtrlSPARCHostAutoRestartPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostAutoRestartPolicy.setStatus("current")
_IlomCtrlSPARCHostOSBootStatus_Type = SnmpAdminString
_IlomCtrlSPARCHostOSBootStatus_Object = MibScalar
ilomCtrlSPARCHostOSBootStatus = _IlomCtrlSPARCHostOSBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 9),
    _IlomCtrlSPARCHostOSBootStatus_Type()
)
ilomCtrlSPARCHostOSBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostOSBootStatus.setStatus("current")


class _IlomCtrlSPARCHostBootTimeout_Type(Integer32):
    """Custom type ilomCtrlSPARCHostBootTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_IlomCtrlSPARCHostBootTimeout_Type.__name__ = "Integer32"
_IlomCtrlSPARCHostBootTimeout_Object = MibScalar
ilomCtrlSPARCHostBootTimeout = _IlomCtrlSPARCHostBootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 10),
    _IlomCtrlSPARCHostBootTimeout_Type()
)
ilomCtrlSPARCHostBootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostBootTimeout.setStatus("current")
_IlomCtrlSPARCHostBootRestart_Type = ILOMCtrlSPARCHostBootRestart
_IlomCtrlSPARCHostBootRestart_Object = MibScalar
ilomCtrlSPARCHostBootRestart = _IlomCtrlSPARCHostBootRestart_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 11),
    _IlomCtrlSPARCHostBootRestart_Type()
)
ilomCtrlSPARCHostBootRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostBootRestart.setStatus("current")


class _IlomCtrlSPARCHostMaxBootFail_Type(Integer32):
    """Custom type ilomCtrlSPARCHostMaxBootFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_IlomCtrlSPARCHostMaxBootFail_Type.__name__ = "Integer32"
_IlomCtrlSPARCHostMaxBootFail_Object = MibScalar
ilomCtrlSPARCHostMaxBootFail = _IlomCtrlSPARCHostMaxBootFail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 12),
    _IlomCtrlSPARCHostMaxBootFail_Type()
)
ilomCtrlSPARCHostMaxBootFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostMaxBootFail.setStatus("current")
_IlomCtrlSPARCHostBootFailRecovery_Type = ILOMCtrlSPARCHostBootFailRecovery
_IlomCtrlSPARCHostBootFailRecovery_Object = MibScalar
ilomCtrlSPARCHostBootFailRecovery = _IlomCtrlSPARCHostBootFailRecovery_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 13),
    _IlomCtrlSPARCHostBootFailRecovery_Type()
)
ilomCtrlSPARCHostBootFailRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostBootFailRecovery.setStatus("current")
_IlomCtrlSPARCHostHypervisorVersion_Type = SnmpAdminString
_IlomCtrlSPARCHostHypervisorVersion_Object = MibScalar
ilomCtrlSPARCHostHypervisorVersion = _IlomCtrlSPARCHostHypervisorVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 14),
    _IlomCtrlSPARCHostHypervisorVersion_Type()
)
ilomCtrlSPARCHostHypervisorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostHypervisorVersion.setStatus("current")
_IlomCtrlSPARCHostSysFwVersion_Type = SnmpAdminString
_IlomCtrlSPARCHostSysFwVersion_Object = MibScalar
ilomCtrlSPARCHostSysFwVersion = _IlomCtrlSPARCHostSysFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 15),
    _IlomCtrlSPARCHostSysFwVersion_Type()
)
ilomCtrlSPARCHostSysFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostSysFwVersion.setStatus("current")
_IlomCtrlSPARCHostSendBreakAction_Type = ILOMCtrlSPARCHostSendBreakAction
_IlomCtrlSPARCHostSendBreakAction_Object = MibScalar
ilomCtrlSPARCHostSendBreakAction = _IlomCtrlSPARCHostSendBreakAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 16),
    _IlomCtrlSPARCHostSendBreakAction_Type()
)
ilomCtrlSPARCHostSendBreakAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostSendBreakAction.setStatus("current")
_IlomCtrlSPARCHostIoReconfigurePolicy_Type = ILOMCtrlSPARCHostIoReconfigurePolicy
_IlomCtrlSPARCHostIoReconfigurePolicy_Object = MibScalar
ilomCtrlSPARCHostIoReconfigurePolicy = _IlomCtrlSPARCHostIoReconfigurePolicy_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 17),
    _IlomCtrlSPARCHostIoReconfigurePolicy_Type()
)
ilomCtrlSPARCHostIoReconfigurePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostIoReconfigurePolicy.setStatus("current")
_IlomCtrlSPARCHostGMVersion_Type = SnmpAdminString
_IlomCtrlSPARCHostGMVersion_Object = MibScalar
ilomCtrlSPARCHostGMVersion = _IlomCtrlSPARCHostGMVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 2, 18),
    _IlomCtrlSPARCHostGMVersion_Type()
)
ilomCtrlSPARCHostGMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCHostGMVersion.setStatus("current")
_IlomCtrlSPARCBootMode_ObjectIdentity = ObjectIdentity
ilomCtrlSPARCBootMode = _IlomCtrlSPARCBootMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 3)
)
_IlomCtrlSPARCBootModeState_Type = ILOMCtrlSPARCBootModeState
_IlomCtrlSPARCBootModeState_Object = MibScalar
ilomCtrlSPARCBootModeState = _IlomCtrlSPARCBootModeState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 3, 1),
    _IlomCtrlSPARCBootModeState_Type()
)
ilomCtrlSPARCBootModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCBootModeState.setStatus("current")


class _IlomCtrlSPARCBootModeScript_Type(SnmpAdminString):
    """Custom type ilomCtrlSPARCBootModeScript based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IlomCtrlSPARCBootModeScript_Type.__name__ = "SnmpAdminString"
_IlomCtrlSPARCBootModeScript_Object = MibScalar
ilomCtrlSPARCBootModeScript = _IlomCtrlSPARCBootModeScript_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 3, 2),
    _IlomCtrlSPARCBootModeScript_Type()
)
ilomCtrlSPARCBootModeScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCBootModeScript.setStatus("current")
_IlomCtrlSPARCBootModeExpires_Type = DateAndTime
_IlomCtrlSPARCBootModeExpires_Object = MibScalar
ilomCtrlSPARCBootModeExpires = _IlomCtrlSPARCBootModeExpires_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 3, 3),
    _IlomCtrlSPARCBootModeExpires_Type()
)
ilomCtrlSPARCBootModeExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlSPARCBootModeExpires.setStatus("current")


class _IlomCtrlSPARCBootModeLDOMConfig_Type(SnmpAdminString):
    """Custom type ilomCtrlSPARCBootModeLDOMConfig based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IlomCtrlSPARCBootModeLDOMConfig_Type.__name__ = "SnmpAdminString"
_IlomCtrlSPARCBootModeLDOMConfig_Object = MibScalar
ilomCtrlSPARCBootModeLDOMConfig = _IlomCtrlSPARCBootModeLDOMConfig_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 3, 4),
    _IlomCtrlSPARCBootModeLDOMConfig_Type()
)
ilomCtrlSPARCBootModeLDOMConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCBootModeLDOMConfig.setStatus("current")
_IlomCtrlSPARCKeySwitch_ObjectIdentity = ObjectIdentity
ilomCtrlSPARCKeySwitch = _IlomCtrlSPARCKeySwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 4)
)
_IlomCtrlSPARCKeySwitchState_Type = ILOMCtrlSPARCKeySwitchState
_IlomCtrlSPARCKeySwitchState_Object = MibScalar
ilomCtrlSPARCKeySwitchState = _IlomCtrlSPARCKeySwitchState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 15, 4, 1),
    _IlomCtrlSPARCKeySwitchState_Type()
)
ilomCtrlSPARCKeySwitchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSPARCKeySwitchState.setStatus("current")
_IlomCtrlIdentification_ObjectIdentity = ObjectIdentity
ilomCtrlIdentification = _IlomCtrlIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 16)
)
_IlomCtrlSystemIdentifier_Type = SnmpAdminString
_IlomCtrlSystemIdentifier_Object = MibScalar
ilomCtrlSystemIdentifier = _IlomCtrlSystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 16, 1),
    _IlomCtrlSystemIdentifier_Type()
)
ilomCtrlSystemIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlSystemIdentifier.setStatus("current")
_IlomCtrlHostName_Type = SnmpAdminString
_IlomCtrlHostName_Object = MibScalar
ilomCtrlHostName = _IlomCtrlHostName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 16, 2),
    _IlomCtrlHostName_Type()
)
ilomCtrlHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlHostName.setStatus("current")
_IlomCtrlThd_ObjectIdentity = ObjectIdentity
ilomCtrlThd = _IlomCtrlThd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17)
)
_IlomCtrlThdState_Type = SnmpAdminString
_IlomCtrlThdState_Object = MibScalar
ilomCtrlThdState = _IlomCtrlThdState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 1),
    _IlomCtrlThdState_Type()
)
ilomCtrlThdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlThdState.setStatus("current")
_IlomCtrlThdAction_Type = ILOMCtrlThdAction
_IlomCtrlThdAction_Object = MibScalar
ilomCtrlThdAction = _IlomCtrlThdAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 2),
    _IlomCtrlThdAction_Type()
)
ilomCtrlThdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlThdAction.setStatus("current")
_IlomCtrlThdModulesTable_Object = MibTable
ilomCtrlThdModulesTable = _IlomCtrlThdModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 3)
)
if mibBuilder.loadTexts:
    ilomCtrlThdModulesTable.setStatus("current")
_IlomCtrlThdModulesEntry_Object = MibTableRow
ilomCtrlThdModulesEntry = _IlomCtrlThdModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 3, 1)
)
ilomCtrlThdModulesEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlThdModuleName"),
)
if mibBuilder.loadTexts:
    ilomCtrlThdModulesEntry.setStatus("current")
_IlomCtrlThdModuleName_Type = ILOMCtrlTargetIndex
_IlomCtrlThdModuleName_Object = MibTableColumn
ilomCtrlThdModuleName = _IlomCtrlThdModuleName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 3, 1, 1),
    _IlomCtrlThdModuleName_Type()
)
ilomCtrlThdModuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlThdModuleName.setStatus("current")
_IlomCtrlThdModuleDesc_Type = SnmpAdminString
_IlomCtrlThdModuleDesc_Object = MibTableColumn
ilomCtrlThdModuleDesc = _IlomCtrlThdModuleDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 3, 1, 2),
    _IlomCtrlThdModuleDesc_Type()
)
ilomCtrlThdModuleDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlThdModuleDesc.setStatus("current")
_IlomCtrlThdModuleState_Type = SnmpAdminString
_IlomCtrlThdModuleState_Object = MibTableColumn
ilomCtrlThdModuleState = _IlomCtrlThdModuleState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 3, 1, 3),
    _IlomCtrlThdModuleState_Type()
)
ilomCtrlThdModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlThdModuleState.setStatus("current")
_IlomCtrlThdModuleAction_Type = ILOMCtrlThdAction
_IlomCtrlThdModuleAction_Object = MibTableColumn
ilomCtrlThdModuleAction = _IlomCtrlThdModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 3, 1, 4),
    _IlomCtrlThdModuleAction_Type()
)
ilomCtrlThdModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlThdModuleAction.setStatus("current")
_IlomCtrlThdInstanceTable_Object = MibTable
ilomCtrlThdInstanceTable = _IlomCtrlThdInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 4)
)
if mibBuilder.loadTexts:
    ilomCtrlThdInstanceTable.setStatus("current")
_IlomCtrlThdInstanceEntry_Object = MibTableRow
ilomCtrlThdInstanceEntry = _IlomCtrlThdInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 4, 1)
)
ilomCtrlThdInstanceEntry.setIndexNames(
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlThdModName"),
    (0, "SUN-ILOM-CONTROL-MIB", "ilomCtrlThdInstanceName"),
)
if mibBuilder.loadTexts:
    ilomCtrlThdInstanceEntry.setStatus("current")
_IlomCtrlThdModName_Type = ILOMCtrlModTargetIndex
_IlomCtrlThdModName_Object = MibTableColumn
ilomCtrlThdModName = _IlomCtrlThdModName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 4, 1, 1),
    _IlomCtrlThdModName_Type()
)
ilomCtrlThdModName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlThdModName.setStatus("current")
_IlomCtrlThdInstanceName_Type = ILOMCtrlInstanceTargetIndex
_IlomCtrlThdInstanceName_Object = MibTableColumn
ilomCtrlThdInstanceName = _IlomCtrlThdInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 4, 1, 2),
    _IlomCtrlThdInstanceName_Type()
)
ilomCtrlThdInstanceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ilomCtrlThdInstanceName.setStatus("current")
_IlomCtrlThdInstanceState_Type = SnmpAdminString
_IlomCtrlThdInstanceState_Object = MibTableColumn
ilomCtrlThdInstanceState = _IlomCtrlThdInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 4, 1, 3),
    _IlomCtrlThdInstanceState_Type()
)
ilomCtrlThdInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilomCtrlThdInstanceState.setStatus("current")
_IlomCtrlThdInstanceAction_Type = ILOMCtrlThdAction
_IlomCtrlThdInstanceAction_Object = MibTableColumn
ilomCtrlThdInstanceAction = _IlomCtrlThdInstanceAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 17, 4, 1, 4),
    _IlomCtrlThdInstanceAction_Type()
)
ilomCtrlThdInstanceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilomCtrlThdInstanceAction.setStatus("current")
_IlomCtrlConformances_ObjectIdentity = ObjectIdentity
ilomCtrlConformances = _IlomCtrlConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 18)
)
_IlomCtrlCompliances_ObjectIdentity = ObjectIdentity
ilomCtrlCompliances = _IlomCtrlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 18, 1)
)
_IlomCtrlGroups_ObjectIdentity = ObjectIdentity
ilomCtrlGroups = _IlomCtrlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 18, 2)
)

# Managed Objects groups

ilomCtrlDeprecatedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 18, 2, 1)
)
ilomCtrlDeprecatedObjectsGroup.setObjects(
      *(("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapDefaultRole"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRadiusDefaultRole"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserAuthPassword"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserAuthRole"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserAuthRowStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserAuthCLIMode"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsLevel"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsVerbosity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryDefaultRole"))
)
if mibBuilder.loadTexts:
    ilomCtrlDeprecatedObjectsGroup.setStatus("deprecated")

ilomCtrlObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 102, 18, 2, 2)
)
ilomCtrlObjectsGroup.setObjects(
      *(("SUN-ILOM-CONTROL-MIB", "ilomCtrlDeviceNTPServerOneIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDeviceNTPServerTwoIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapServerIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapBindDn"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapBindPassword"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSearchBase"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapDefaultRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRadiusEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRadiusServerIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRadiusPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRadiusSecret"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRadiusDefaultRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRemoteSyslogDest1"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRemoteSyslogDest2"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertFileURI"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryTimeout"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryStrictCertEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertFileStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirUserDomain"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAdminGroupName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirOperatorGroupName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirCustomGroupName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirCustomGroupRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerIp"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerPort"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertURI"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertClear"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertSerialNo"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertIssuer"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertSubject"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertValidBegin"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirAlternateServerCertValidEnd"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryLogDetail"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryDefaultRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertClear"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertSerialNo"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertIssuer"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertSubject"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertValidBegin"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirectoryCertValidEnd"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirDnsLocatorEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirDnsLocatorQueryService"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirExpSearchEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlActiveDirStrictCredentialErrorEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSMTPEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSMTPServerIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSMTPPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSMTPCustomSender"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslDefaultRole"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileURI"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslTimeout"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslStrictCertEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslLogDetail"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslDefaultRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileClear"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileSerialNo"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileIssuer"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileSubject"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileValidBegin"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCertFileValidEnd"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOptUsrMappingEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOptUsrMappingAttrInfo"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOptUsrMappingBindDn"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOptUsrMappingBindPw"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOptUsrMappingSearchBase"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslUserDomain"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAdminGroupName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslOperatorGroupName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCustomGroupName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslCustomGroupRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerIp"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerPort"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertURI"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertClear"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertSerialNo"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertIssuer"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertSubject"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertValidBegin"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLdapSslAlternateServerCertValidEnd"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlHttpEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlHttpPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlHttpSecureRedirect"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlHttpsEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlHttpsPortNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshRsaKeyFingerprint"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshRsaKeyLength"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshDsaKeyFingerprint"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshDsaKeyLength"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshGenerateNewKeyAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshGenerateNewKeyType"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshRestartSshdAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSshEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSingleSignonEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkMacAddress"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkIpDiscovery"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkIpAddress"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkIpGateway"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkIpNetmask"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkPendingIpDiscovery"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkPendingIpAddress"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkPendingIpGateway"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkPendingIpNetmask"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkCommitPending"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkDHCPServerAddr"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkPendingManagementPort"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkManagementPort"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkOutOfBandMacAddress"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkSidebandMacAddress"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNetworkState"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserPassword"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserRoles"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserRowStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlLocalUserCLIMode"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSessionsUsername"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSessionsConnectionType"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSessionsLoginTime"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareMgmtVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareBuildNumber"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareBuildDate"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareTFTPServerIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareTFTPFileName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwarePreserveConfig"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareMgmtStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareMgmtAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareMgmtFilesystemVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlFirmwareDelayBIOS"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogType"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogTimestamp"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogClass"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogSeverity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogDescription"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlEventLogClear"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertSeverity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertType"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertDestinationIP"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertDestinationPort"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertDestinationEmail"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertSNMPVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertSNMPCommunityOrUsername"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertEmailEventClassFilter"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertEmailEventTypeFilter"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertEmailCustomSender"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlAlertEmailMessagePrefix"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDateAndTime"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlNTPEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlTimezone"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSerialInternalPortPresent"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSerialInternalPortBaudRate"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSerialExternalPortPresent"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSerialExternalPortBaudRate"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSerialExternalPortFlowControl"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlPowerAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlResetAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRedundancyStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRedundancyAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlRedundancyFRUName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlPolicyShortStr"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlPolicyLongStr"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlPolicyEnabled"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlResetToDefaultsAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsTrigger"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsMode"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsPowerOnLevel"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsUserResetLevel"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsErrorResetLevel"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsPowerOnVerbosity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsUserResetVerbosity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsErrorResetVerbosity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsHwChangeLevel"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCDiagsHwChangeVerbosity"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostMACAddress"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostOBPVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostPOSTVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostAutoRunOnError"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostPOSTStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostAutoRestartPolicy"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostIoReconfigurePolicy"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostOSBootStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostBootTimeout"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostBootRestart"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostMaxBootFail"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostBootFailRecovery"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostHypervisorVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostSysFwVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostGMVersion"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCHostSendBreakAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCBootModeState"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCBootModeScript"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCBootModeExpires"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCBootModeLDOMConfig"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSPARCKeySwitchState"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlSystemIdentifier"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlHostName"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdState"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdModuleDesc"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdModuleState"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdModuleAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdInstanceState"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlThdInstanceAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlBackupAndRestoreTargetURI"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlBackupAndRestorePassphrase"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlBackupAndRestoreAction"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlBackupAndRestoreActionStatus"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDNSNameServers"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDNSSearchPath"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDNSdhcpAutoDns"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDNSTimeout"),
        ("SUN-ILOM-CONTROL-MIB", "ilomCtrlDNSRetries"))
)
if mibBuilder.loadTexts:
    ilomCtrlObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-ILOM-CONTROL-MIB",
    **{"ILOMCtrlTargetIndex": ILOMCtrlTargetIndex,
       "ILOMCtrlModTargetIndex": ILOMCtrlModTargetIndex,
       "ILOMCtrlInstanceTargetIndex": ILOMCtrlInstanceTargetIndex,
       "ILOMCtrlSessionsConnectionType": ILOMCtrlSessionsConnectionType,
       "ILOMCtrlLocalUserUsername": ILOMCtrlLocalUserUsername,
       "ILOMCtrlLocalUserPassword": ILOMCtrlLocalUserPassword,
       "ILOMCtrlUserRole": ILOMCtrlUserRole,
       "ILOMCtrlUserRoles": ILOMCtrlUserRoles,
       "ILOMCtrlLocalUserAuthCLIMode": ILOMCtrlLocalUserAuthCLIMode,
       "ILOMCtrlPowerAction": ILOMCtrlPowerAction,
       "ILOMCtrlResetAction": ILOMCtrlResetAction,
       "ILOMCtrlNetworkIpDiscovery": ILOMCtrlNetworkIpDiscovery,
       "ILOMCtrlEventLogType": ILOMCtrlEventLogType,
       "ILOMCtrlEventLogClass": ILOMCtrlEventLogClass,
       "ILOMCtrlEventSeverity": ILOMCtrlEventSeverity,
       "ILOMCtrlAlertType": ILOMCtrlAlertType,
       "ILOMCtrlAlertSNMPVersion": ILOMCtrlAlertSNMPVersion,
       "ILOMCtrlBaudRate": ILOMCtrlBaudRate,
       "ILOMCtrlFlowControl": ILOMCtrlFlowControl,
       "ILOMCtrlFirmwareUpdateStatus": ILOMCtrlFirmwareUpdateStatus,
       "ILOMCtrlFirmwareUpdateAction": ILOMCtrlFirmwareUpdateAction,
       "ILOMCtrlResetToDefaultsAction": ILOMCtrlResetToDefaultsAction,
       "ILOMCtrlRedundancyStatus": ILOMCtrlRedundancyStatus,
       "ILOMCtrlRedundancyAction": ILOMCtrlRedundancyAction,
       "ILOMCtrlSPARCDiagsLevel": ILOMCtrlSPARCDiagsLevel,
       "ILOMCtrlSPARCDiagsLevelAdv": ILOMCtrlSPARCDiagsLevelAdv,
       "ILOMCtrlSPARCDiagsTrigger": ILOMCtrlSPARCDiagsTrigger,
       "ILOMCtrlSPARCDiagsMode": ILOMCtrlSPARCDiagsMode,
       "ILOMCtrlSPARCDiagsVerbosity": ILOMCtrlSPARCDiagsVerbosity,
       "ILOMCtrlSPARCDiagsVerbosityAdv": ILOMCtrlSPARCDiagsVerbosityAdv,
       "ILOMCtrlSPARCHostAutoRestartPolicy": ILOMCtrlSPARCHostAutoRestartPolicy,
       "ILOMCtrlSPARCHostBootRestart": ILOMCtrlSPARCHostBootRestart,
       "ILOMCtrlSPARCHostBootFailRecovery": ILOMCtrlSPARCHostBootFailRecovery,
       "ILOMCtrlSPARCHostSendBreakAction": ILOMCtrlSPARCHostSendBreakAction,
       "ILOMCtrlSPARCHostIoReconfigurePolicy": ILOMCtrlSPARCHostIoReconfigurePolicy,
       "ILOMCtrlSPARCBootModeState": ILOMCtrlSPARCBootModeState,
       "ILOMCtrlSPARCKeySwitchState": ILOMCtrlSPARCKeySwitchState,
       "ILOMCtrlSPARCDiagsAction": ILOMCtrlSPARCDiagsAction,
       "ILOMCtrlSshKeyGenType": ILOMCtrlSshKeyGenType,
       "ILOMCtrlThdAction": ILOMCtrlThdAction,
       "ILOMCtrlBackupAndRestoreAction": ILOMCtrlBackupAndRestoreAction,
       "sun": sun,
       "products": products,
       "ilom": ilom,
       "ilomCtrlMIB": ilomCtrlMIB,
       "ilomCtrlClients": ilomCtrlClients,
       "ilomCtrlNtp": ilomCtrlNtp,
       "ilomCtrlDeviceNTPServerOneIP": ilomCtrlDeviceNTPServerOneIP,
       "ilomCtrlDeviceNTPServerTwoIP": ilomCtrlDeviceNTPServerTwoIP,
       "ilomCtrlLdap": ilomCtrlLdap,
       "ilomCtrlLdapEnabled": ilomCtrlLdapEnabled,
       "ilomCtrlLdapServerIP": ilomCtrlLdapServerIP,
       "ilomCtrlLdapPortNumber": ilomCtrlLdapPortNumber,
       "ilomCtrlLdapBindDn": ilomCtrlLdapBindDn,
       "ilomCtrlLdapBindPassword": ilomCtrlLdapBindPassword,
       "ilomCtrlLdapSearchBase": ilomCtrlLdapSearchBase,
       "ilomCtrlLdapDefaultRole": ilomCtrlLdapDefaultRole,
       "ilomCtrlLdapDefaultRoles": ilomCtrlLdapDefaultRoles,
       "ilomCtrlRadius": ilomCtrlRadius,
       "ilomCtrlRadiusEnabled": ilomCtrlRadiusEnabled,
       "ilomCtrlRadiusServerIP": ilomCtrlRadiusServerIP,
       "ilomCtrlRadiusPortNumber": ilomCtrlRadiusPortNumber,
       "ilomCtrlRadiusSecret": ilomCtrlRadiusSecret,
       "ilomCtrlRadiusDefaultRole": ilomCtrlRadiusDefaultRole,
       "ilomCtrlRadiusDefaultRoles": ilomCtrlRadiusDefaultRoles,
       "ilomCtrlRemoteSyslog": ilomCtrlRemoteSyslog,
       "ilomCtrlRemoteSyslogDest1": ilomCtrlRemoteSyslogDest1,
       "ilomCtrlRemoteSyslogDest2": ilomCtrlRemoteSyslogDest2,
       "ilomCtrlActiveDirectory": ilomCtrlActiveDirectory,
       "ilomCtrlActiveDirectoryEnabled": ilomCtrlActiveDirectoryEnabled,
       "ilomCtrlActiveDirectoryIP": ilomCtrlActiveDirectoryIP,
       "ilomCtrlActiveDirectoryPortNumber": ilomCtrlActiveDirectoryPortNumber,
       "ilomCtrlActiveDirectoryDefaultRole": ilomCtrlActiveDirectoryDefaultRole,
       "ilomCtrlActiveDirectoryCertFileURI": ilomCtrlActiveDirectoryCertFileURI,
       "ilomCtrlActiveDirectoryTimeout": ilomCtrlActiveDirectoryTimeout,
       "ilomCtrlActiveDirectoryStrictCertEnabled": ilomCtrlActiveDirectoryStrictCertEnabled,
       "ilomCtrlActiveDirectoryCertFileStatus": ilomCtrlActiveDirectoryCertFileStatus,
       "ilomCtrlActiveDirUserDomainTable": ilomCtrlActiveDirUserDomainTable,
       "ilomCtrlActiveDirUserDomainEntry": ilomCtrlActiveDirUserDomainEntry,
       "ilomCtrlActiveDirUserDomainId": ilomCtrlActiveDirUserDomainId,
       "ilomCtrlActiveDirUserDomain": ilomCtrlActiveDirUserDomain,
       "ilomCtrlActiveDirAdminGroupsTable": ilomCtrlActiveDirAdminGroupsTable,
       "ilomCtrlActiveDirAdminGroupsEntry": ilomCtrlActiveDirAdminGroupsEntry,
       "ilomCtrlActiveDirAdminGroupId": ilomCtrlActiveDirAdminGroupId,
       "ilomCtrlActiveDirAdminGroupName": ilomCtrlActiveDirAdminGroupName,
       "ilomCtrlActiveDirOperatorGroupsTable": ilomCtrlActiveDirOperatorGroupsTable,
       "ilomCtrlActiveDirOperatorGroupsEntry": ilomCtrlActiveDirOperatorGroupsEntry,
       "ilomCtrlActiveDirOperatorGroupId": ilomCtrlActiveDirOperatorGroupId,
       "ilomCtrlActiveDirOperatorGroupName": ilomCtrlActiveDirOperatorGroupName,
       "ilomCtrlActiveDirAlternateServerTable": ilomCtrlActiveDirAlternateServerTable,
       "ilomCtrlActiveDirAlternateServerEntry": ilomCtrlActiveDirAlternateServerEntry,
       "ilomCtrlActiveDirAlternateServerId": ilomCtrlActiveDirAlternateServerId,
       "ilomCtrlActiveDirAlternateServerIp": ilomCtrlActiveDirAlternateServerIp,
       "ilomCtrlActiveDirAlternateServerPort": ilomCtrlActiveDirAlternateServerPort,
       "ilomCtrlActiveDirAlternateServerCertStatus": ilomCtrlActiveDirAlternateServerCertStatus,
       "ilomCtrlActiveDirAlternateServerCertURI": ilomCtrlActiveDirAlternateServerCertURI,
       "ilomCtrlActiveDirAlternateServerCertClear": ilomCtrlActiveDirAlternateServerCertClear,
       "ilomCtrlActiveDirAlternateServerCertVersion": ilomCtrlActiveDirAlternateServerCertVersion,
       "ilomCtrlActiveDirAlternateServerCertSerialNo": ilomCtrlActiveDirAlternateServerCertSerialNo,
       "ilomCtrlActiveDirAlternateServerCertIssuer": ilomCtrlActiveDirAlternateServerCertIssuer,
       "ilomCtrlActiveDirAlternateServerCertSubject": ilomCtrlActiveDirAlternateServerCertSubject,
       "ilomCtrlActiveDirAlternateServerCertValidBegin": ilomCtrlActiveDirAlternateServerCertValidBegin,
       "ilomCtrlActiveDirAlternateServerCertValidEnd": ilomCtrlActiveDirAlternateServerCertValidEnd,
       "ilomCtrlActiveDirectoryLogDetail": ilomCtrlActiveDirectoryLogDetail,
       "ilomCtrlActiveDirectoryDefaultRoles": ilomCtrlActiveDirectoryDefaultRoles,
       "ilomCtrlActiveDirCustomGroupsTable": ilomCtrlActiveDirCustomGroupsTable,
       "ilomCtrlActiveDirCustomGroupsEntry": ilomCtrlActiveDirCustomGroupsEntry,
       "ilomCtrlActiveDirCustomGroupId": ilomCtrlActiveDirCustomGroupId,
       "ilomCtrlActiveDirCustomGroupName": ilomCtrlActiveDirCustomGroupName,
       "ilomCtrlActiveDirCustomGroupRoles": ilomCtrlActiveDirCustomGroupRoles,
       "ilomCtrlActiveDirectoryCertClear": ilomCtrlActiveDirectoryCertClear,
       "ilomCtrlActiveDirectoryCertVersion": ilomCtrlActiveDirectoryCertVersion,
       "ilomCtrlActiveDirectoryCertSerialNo": ilomCtrlActiveDirectoryCertSerialNo,
       "ilomCtrlActiveDirectoryCertIssuer": ilomCtrlActiveDirectoryCertIssuer,
       "ilomCtrlActiveDirectoryCertSubject": ilomCtrlActiveDirectoryCertSubject,
       "ilomCtrlActiveDirectoryCertValidBegin": ilomCtrlActiveDirectoryCertValidBegin,
       "ilomCtrlActiveDirectoryCertValidEnd": ilomCtrlActiveDirectoryCertValidEnd,
       "ilomCtrlActiveDirDnsLocatorEnabled": ilomCtrlActiveDirDnsLocatorEnabled,
       "ilomCtrlActiveDirDnsLocatorQueryTable": ilomCtrlActiveDirDnsLocatorQueryTable,
       "ilomCtrlActiveDirDnsLocatorQueryEntry": ilomCtrlActiveDirDnsLocatorQueryEntry,
       "ilomCtrlActiveDirDnsLocatorQueryId": ilomCtrlActiveDirDnsLocatorQueryId,
       "ilomCtrlActiveDirDnsLocatorQueryService": ilomCtrlActiveDirDnsLocatorQueryService,
       "ilomCtrlActiveDirExpSearchEnabled": ilomCtrlActiveDirExpSearchEnabled,
       "ilomCtrlActiveDirStrictCredentialErrorEnabled": ilomCtrlActiveDirStrictCredentialErrorEnabled,
       "ilomCtrlSMTP": ilomCtrlSMTP,
       "ilomCtrlSMTPEnabled": ilomCtrlSMTPEnabled,
       "ilomCtrlSMTPServerIP": ilomCtrlSMTPServerIP,
       "ilomCtrlSMTPPortNumber": ilomCtrlSMTPPortNumber,
       "ilomCtrlSMTPCustomSender": ilomCtrlSMTPCustomSender,
       "ilomCtrlLdapSsl": ilomCtrlLdapSsl,
       "ilomCtrlLdapSslGlobalObj": ilomCtrlLdapSslGlobalObj,
       "ilomCtrlLdapSslEnabled": ilomCtrlLdapSslEnabled,
       "ilomCtrlLdapSslIP": ilomCtrlLdapSslIP,
       "ilomCtrlLdapSslPortNumber": ilomCtrlLdapSslPortNumber,
       "ilomCtrlLdapSslDefaultRole": ilomCtrlLdapSslDefaultRole,
       "ilomCtrlLdapSslCertFileURI": ilomCtrlLdapSslCertFileURI,
       "ilomCtrlLdapSslTimeout": ilomCtrlLdapSslTimeout,
       "ilomCtrlLdapSslStrictCertEnabled": ilomCtrlLdapSslStrictCertEnabled,
       "ilomCtrlLdapSslCertFileStatus": ilomCtrlLdapSslCertFileStatus,
       "ilomCtrlLdapSslLogDetail": ilomCtrlLdapSslLogDetail,
       "ilomCtrlLdapSslDefaultRoles": ilomCtrlLdapSslDefaultRoles,
       "ilomCtrlLdapSslCertFileClear": ilomCtrlLdapSslCertFileClear,
       "ilomCtrlLdapSslCertFileVersion": ilomCtrlLdapSslCertFileVersion,
       "ilomCtrlLdapSslCertFileSerialNo": ilomCtrlLdapSslCertFileSerialNo,
       "ilomCtrlLdapSslCertFileIssuer": ilomCtrlLdapSslCertFileIssuer,
       "ilomCtrlLdapSslCertFileSubject": ilomCtrlLdapSslCertFileSubject,
       "ilomCtrlLdapSslCertFileValidBegin": ilomCtrlLdapSslCertFileValidBegin,
       "ilomCtrlLdapSslCertFileValidEnd": ilomCtrlLdapSslCertFileValidEnd,
       "ilomCtrlLdapSslOptUsrMappingEnabled": ilomCtrlLdapSslOptUsrMappingEnabled,
       "ilomCtrlLdapSslOptUsrMappingAttrInfo": ilomCtrlLdapSslOptUsrMappingAttrInfo,
       "ilomCtrlLdapSslOptUsrMappingBindDn": ilomCtrlLdapSslOptUsrMappingBindDn,
       "ilomCtrlLdapSslOptUsrMappingBindPw": ilomCtrlLdapSslOptUsrMappingBindPw,
       "ilomCtrlLdapSslOptUsrMappingSearchBase": ilomCtrlLdapSslOptUsrMappingSearchBase,
       "ilomCtrlLdapSslUserDomainTable": ilomCtrlLdapSslUserDomainTable,
       "ilomCtrlLdapSslUserDomainEntry": ilomCtrlLdapSslUserDomainEntry,
       "ilomCtrlLdapSslUserDomainId": ilomCtrlLdapSslUserDomainId,
       "ilomCtrlLdapSslUserDomain": ilomCtrlLdapSslUserDomain,
       "ilomCtrlLdapSslAdminGroupsTable": ilomCtrlLdapSslAdminGroupsTable,
       "ilomCtrlLdapSslAdminGroupsEntry": ilomCtrlLdapSslAdminGroupsEntry,
       "ilomCtrlLdapSslAdminGroupId": ilomCtrlLdapSslAdminGroupId,
       "ilomCtrlLdapSslAdminGroupName": ilomCtrlLdapSslAdminGroupName,
       "ilomCtrlLdapSslOperatorGroupsTable": ilomCtrlLdapSslOperatorGroupsTable,
       "ilomCtrlLdapSslOperatorGroupsEntry": ilomCtrlLdapSslOperatorGroupsEntry,
       "ilomCtrlLdapSslOperatorGroupId": ilomCtrlLdapSslOperatorGroupId,
       "ilomCtrlLdapSslOperatorGroupName": ilomCtrlLdapSslOperatorGroupName,
       "ilomCtrlLdapSslAlternateServerTable": ilomCtrlLdapSslAlternateServerTable,
       "ilomCtrlLdapSslAlternateServerEntry": ilomCtrlLdapSslAlternateServerEntry,
       "ilomCtrlLdapSslAlternateServerId": ilomCtrlLdapSslAlternateServerId,
       "ilomCtrlLdapSslAlternateServerIp": ilomCtrlLdapSslAlternateServerIp,
       "ilomCtrlLdapSslAlternateServerPort": ilomCtrlLdapSslAlternateServerPort,
       "ilomCtrlLdapSslAlternateServerCertStatus": ilomCtrlLdapSslAlternateServerCertStatus,
       "ilomCtrlLdapSslAlternateServerCertURI": ilomCtrlLdapSslAlternateServerCertURI,
       "ilomCtrlLdapSslAlternateServerCertClear": ilomCtrlLdapSslAlternateServerCertClear,
       "ilomCtrlLdapSslAlternateServerCertVersion": ilomCtrlLdapSslAlternateServerCertVersion,
       "ilomCtrlLdapSslAlternateServerCertSerialNo": ilomCtrlLdapSslAlternateServerCertSerialNo,
       "ilomCtrlLdapSslAlternateServerCertIssuer": ilomCtrlLdapSslAlternateServerCertIssuer,
       "ilomCtrlLdapSslAlternateServerCertSubject": ilomCtrlLdapSslAlternateServerCertSubject,
       "ilomCtrlLdapSslAlternateServerCertValidBegin": ilomCtrlLdapSslAlternateServerCertValidBegin,
       "ilomCtrlLdapSslAlternateServerCertValidEnd": ilomCtrlLdapSslAlternateServerCertValidEnd,
       "ilomCtrlLdapSslCustomGroupsTable": ilomCtrlLdapSslCustomGroupsTable,
       "ilomCtrlLdapSslCustomGroupsEntry": ilomCtrlLdapSslCustomGroupsEntry,
       "ilomCtrlLdapSslCustomGroupId": ilomCtrlLdapSslCustomGroupId,
       "ilomCtrlLdapSslCustomGroupName": ilomCtrlLdapSslCustomGroupName,
       "ilomCtrlLdapSslCustomGroupRoles": ilomCtrlLdapSslCustomGroupRoles,
       "ilomCtrlDNS": ilomCtrlDNS,
       "ilomCtrlDNSNameServers": ilomCtrlDNSNameServers,
       "ilomCtrlDNSSearchPath": ilomCtrlDNSSearchPath,
       "ilomCtrlDNSdhcpAutoDns": ilomCtrlDNSdhcpAutoDns,
       "ilomCtrlDNSTimeout": ilomCtrlDNSTimeout,
       "ilomCtrlDNSRetries": ilomCtrlDNSRetries,
       "ilomCtrlServices": ilomCtrlServices,
       "ilomCtrlHttp": ilomCtrlHttp,
       "ilomCtrlHttpEnabled": ilomCtrlHttpEnabled,
       "ilomCtrlHttpPortNumber": ilomCtrlHttpPortNumber,
       "ilomCtrlHttpSecureRedirect": ilomCtrlHttpSecureRedirect,
       "ilomCtrlHttps": ilomCtrlHttps,
       "ilomCtrlHttpsEnabled": ilomCtrlHttpsEnabled,
       "ilomCtrlHttpsPortNumber": ilomCtrlHttpsPortNumber,
       "ilomCtrlSsh": ilomCtrlSsh,
       "ilomCtrlSshRsaKeyFingerprint": ilomCtrlSshRsaKeyFingerprint,
       "ilomCtrlSshRsaKeyLength": ilomCtrlSshRsaKeyLength,
       "ilomCtrlSshDsaKeyFingerprint": ilomCtrlSshDsaKeyFingerprint,
       "ilomCtrlSshDsaKeyLength": ilomCtrlSshDsaKeyLength,
       "ilomCtrlSshGenerateNewKeyAction": ilomCtrlSshGenerateNewKeyAction,
       "ilomCtrlSshGenerateNewKeyType": ilomCtrlSshGenerateNewKeyType,
       "ilomCtrlSshRestartSshdAction": ilomCtrlSshRestartSshdAction,
       "ilomCtrlSshEnabled": ilomCtrlSshEnabled,
       "ilomCtrlSingleSignon": ilomCtrlSingleSignon,
       "ilomCtrlSingleSignonEnabled": ilomCtrlSingleSignonEnabled,
       "ilomCtrlNetwork": ilomCtrlNetwork,
       "ilomCtrlNetworkTable": ilomCtrlNetworkTable,
       "ilomCtrlNetworkEntry": ilomCtrlNetworkEntry,
       "ilomCtrlNetworkTarget": ilomCtrlNetworkTarget,
       "ilomCtrlNetworkMacAddress": ilomCtrlNetworkMacAddress,
       "ilomCtrlNetworkIpDiscovery": ilomCtrlNetworkIpDiscovery,
       "ilomCtrlNetworkIpAddress": ilomCtrlNetworkIpAddress,
       "ilomCtrlNetworkIpGateway": ilomCtrlNetworkIpGateway,
       "ilomCtrlNetworkIpNetmask": ilomCtrlNetworkIpNetmask,
       "ilomCtrlNetworkPendingIpDiscovery": ilomCtrlNetworkPendingIpDiscovery,
       "ilomCtrlNetworkPendingIpAddress": ilomCtrlNetworkPendingIpAddress,
       "ilomCtrlNetworkPendingIpGateway": ilomCtrlNetworkPendingIpGateway,
       "ilomCtrlNetworkPendingIpNetmask": ilomCtrlNetworkPendingIpNetmask,
       "ilomCtrlNetworkCommitPending": ilomCtrlNetworkCommitPending,
       "ilomCtrlNetworkOutOfBandMacAddress": ilomCtrlNetworkOutOfBandMacAddress,
       "ilomCtrlNetworkSidebandMacAddress": ilomCtrlNetworkSidebandMacAddress,
       "ilomCtrlNetworkPendingManagementPort": ilomCtrlNetworkPendingManagementPort,
       "ilomCtrlNetworkManagementPort": ilomCtrlNetworkManagementPort,
       "ilomCtrlNetworkDHCPServerAddr": ilomCtrlNetworkDHCPServerAddr,
       "ilomCtrlNetworkState": ilomCtrlNetworkState,
       "ilomCtrlUsers": ilomCtrlUsers,
       "ilomCtrlLocalUserAuthTable": ilomCtrlLocalUserAuthTable,
       "ilomCtrlLocalUserAuthEntry": ilomCtrlLocalUserAuthEntry,
       "ilomCtrlLocalUserAuthUsername": ilomCtrlLocalUserAuthUsername,
       "ilomCtrlLocalUserAuthPassword": ilomCtrlLocalUserAuthPassword,
       "ilomCtrlLocalUserAuthRole": ilomCtrlLocalUserAuthRole,
       "ilomCtrlLocalUserAuthRowStatus": ilomCtrlLocalUserAuthRowStatus,
       "ilomCtrlLocalUserAuthCLIMode": ilomCtrlLocalUserAuthCLIMode,
       "ilomCtrlLocalUserTable": ilomCtrlLocalUserTable,
       "ilomCtrlLocalUserEntry": ilomCtrlLocalUserEntry,
       "ilomCtrlLocalUserUsername": ilomCtrlLocalUserUsername,
       "ilomCtrlLocalUserPassword": ilomCtrlLocalUserPassword,
       "ilomCtrlLocalUserRoles": ilomCtrlLocalUserRoles,
       "ilomCtrlLocalUserRowStatus": ilomCtrlLocalUserRowStatus,
       "ilomCtrlLocalUserCLIMode": ilomCtrlLocalUserCLIMode,
       "ilomCtrlSessions": ilomCtrlSessions,
       "ilomCtrlSessionsTable": ilomCtrlSessionsTable,
       "ilomCtrlSessionsEntry": ilomCtrlSessionsEntry,
       "ilomCtrlSessionsId": ilomCtrlSessionsId,
       "ilomCtrlSessionsUsername": ilomCtrlSessionsUsername,
       "ilomCtrlSessionsConnectionType": ilomCtrlSessionsConnectionType,
       "ilomCtrlSessionsLoginTime": ilomCtrlSessionsLoginTime,
       "ilomCtrlFirmwareMgmt": ilomCtrlFirmwareMgmt,
       "ilomCtrlFirmwareMgmtVersion": ilomCtrlFirmwareMgmtVersion,
       "ilomCtrlFirmwareBuildNumber": ilomCtrlFirmwareBuildNumber,
       "ilomCtrlFirmwareBuildDate": ilomCtrlFirmwareBuildDate,
       "ilomCtrlFirmwareTFTPServerIP": ilomCtrlFirmwareTFTPServerIP,
       "ilomCtrlFirmwareTFTPFileName": ilomCtrlFirmwareTFTPFileName,
       "ilomCtrlFirmwarePreserveConfig": ilomCtrlFirmwarePreserveConfig,
       "ilomCtrlFirmwareMgmtStatus": ilomCtrlFirmwareMgmtStatus,
       "ilomCtrlFirmwareMgmtAction": ilomCtrlFirmwareMgmtAction,
       "ilomCtrlFirmwareMgmtFilesystemVersion": ilomCtrlFirmwareMgmtFilesystemVersion,
       "ilomCtrlFirmwareDelayBIOS": ilomCtrlFirmwareDelayBIOS,
       "ilomCtrlLogs": ilomCtrlLogs,
       "ilomCtrlEventLog": ilomCtrlEventLog,
       "ilomCtrlEventLogTable": ilomCtrlEventLogTable,
       "ilomCtrlEventLogEntry": ilomCtrlEventLogEntry,
       "ilomCtrlEventLogRecordID": ilomCtrlEventLogRecordID,
       "ilomCtrlEventLogType": ilomCtrlEventLogType,
       "ilomCtrlEventLogTimestamp": ilomCtrlEventLogTimestamp,
       "ilomCtrlEventLogClass": ilomCtrlEventLogClass,
       "ilomCtrlEventLogSeverity": ilomCtrlEventLogSeverity,
       "ilomCtrlEventLogDescription": ilomCtrlEventLogDescription,
       "ilomCtrlEventLogClear": ilomCtrlEventLogClear,
       "ilomCtrlAlerts": ilomCtrlAlerts,
       "ilomCtrlAlertsTable": ilomCtrlAlertsTable,
       "ilomCtrlAlertsEntry": ilomCtrlAlertsEntry,
       "ilomCtrlAlertID": ilomCtrlAlertID,
       "ilomCtrlAlertSeverity": ilomCtrlAlertSeverity,
       "ilomCtrlAlertType": ilomCtrlAlertType,
       "ilomCtrlAlertDestinationIP": ilomCtrlAlertDestinationIP,
       "ilomCtrlAlertDestinationEmail": ilomCtrlAlertDestinationEmail,
       "ilomCtrlAlertSNMPVersion": ilomCtrlAlertSNMPVersion,
       "ilomCtrlAlertSNMPCommunityOrUsername": ilomCtrlAlertSNMPCommunityOrUsername,
       "ilomCtrlAlertDestinationPort": ilomCtrlAlertDestinationPort,
       "ilomCtrlAlertEmailEventClassFilter": ilomCtrlAlertEmailEventClassFilter,
       "ilomCtrlAlertEmailEventTypeFilter": ilomCtrlAlertEmailEventTypeFilter,
       "ilomCtrlAlertEmailCustomSender": ilomCtrlAlertEmailCustomSender,
       "ilomCtrlAlertEmailMessagePrefix": ilomCtrlAlertEmailMessagePrefix,
       "ilomCtrlClock": ilomCtrlClock,
       "ilomCtrlDateAndTime": ilomCtrlDateAndTime,
       "ilomCtrlNTPEnabled": ilomCtrlNTPEnabled,
       "ilomCtrlTimezone": ilomCtrlTimezone,
       "ilomCtrlSerial": ilomCtrlSerial,
       "ilomCtrlSerialInternalPortPresent": ilomCtrlSerialInternalPortPresent,
       "ilomCtrlSerialInternalPortBaudRate": ilomCtrlSerialInternalPortBaudRate,
       "ilomCtrlSerialExternalPortPresent": ilomCtrlSerialExternalPortPresent,
       "ilomCtrlSerialExternalPortBaudRate": ilomCtrlSerialExternalPortBaudRate,
       "ilomCtrlSerialExternalPortFlowControl": ilomCtrlSerialExternalPortFlowControl,
       "ilomCtrlPowerReset": ilomCtrlPowerReset,
       "ilomCtrlPowerControl": ilomCtrlPowerControl,
       "ilomCtrlPowerTable": ilomCtrlPowerTable,
       "ilomCtrlPowerEntry": ilomCtrlPowerEntry,
       "ilomCtrlPowerTarget": ilomCtrlPowerTarget,
       "ilomCtrlPowerAction": ilomCtrlPowerAction,
       "ilomCtrlResetControl": ilomCtrlResetControl,
       "ilomCtrlResetTable": ilomCtrlResetTable,
       "ilomCtrlResetEntry": ilomCtrlResetEntry,
       "ilomCtrlResetTarget": ilomCtrlResetTarget,
       "ilomCtrlResetAction": ilomCtrlResetAction,
       "ilomCtrlRedundancy": ilomCtrlRedundancy,
       "ilomCtrlRedundancyStatus": ilomCtrlRedundancyStatus,
       "ilomCtrlRedundancyAction": ilomCtrlRedundancyAction,
       "ilomCtrlRedundancyFRUName": ilomCtrlRedundancyFRUName,
       "ilomCtrlPolicy": ilomCtrlPolicy,
       "ilomCtrlPolicyTable": ilomCtrlPolicyTable,
       "ilomCtrlPolicyEntry": ilomCtrlPolicyEntry,
       "ilomCtrlPolicyId": ilomCtrlPolicyId,
       "ilomCtrlPolicyShortStr": ilomCtrlPolicyShortStr,
       "ilomCtrlPolicyLongStr": ilomCtrlPolicyLongStr,
       "ilomCtrlPolicyEnabled": ilomCtrlPolicyEnabled,
       "ilomCtrlConfigMgmt": ilomCtrlConfigMgmt,
       "ilomCtrlResetToDefaultsAction": ilomCtrlResetToDefaultsAction,
       "ilomCtrlBackupAndRestore": ilomCtrlBackupAndRestore,
       "ilomCtrlBackupAndRestoreTargetURI": ilomCtrlBackupAndRestoreTargetURI,
       "ilomCtrlBackupAndRestorePassphrase": ilomCtrlBackupAndRestorePassphrase,
       "ilomCtrlBackupAndRestoreAction": ilomCtrlBackupAndRestoreAction,
       "ilomCtrlBackupAndRestoreActionStatus": ilomCtrlBackupAndRestoreActionStatus,
       "ilomCtrlSPARC": ilomCtrlSPARC,
       "ilomCtrlSPARCDiags": ilomCtrlSPARCDiags,
       "ilomCtrlSPARCDiagsLevel": ilomCtrlSPARCDiagsLevel,
       "ilomCtrlSPARCDiagsTrigger": ilomCtrlSPARCDiagsTrigger,
       "ilomCtrlSPARCDiagsVerbosity": ilomCtrlSPARCDiagsVerbosity,
       "ilomCtrlSPARCDiagsMode": ilomCtrlSPARCDiagsMode,
       "ilomCtrlSPARCDiagsPowerOnLevel": ilomCtrlSPARCDiagsPowerOnLevel,
       "ilomCtrlSPARCDiagsUserResetLevel": ilomCtrlSPARCDiagsUserResetLevel,
       "ilomCtrlSPARCDiagsErrorResetLevel": ilomCtrlSPARCDiagsErrorResetLevel,
       "ilomCtrlSPARCDiagsPowerOnVerbosity": ilomCtrlSPARCDiagsPowerOnVerbosity,
       "ilomCtrlSPARCDiagsUserResetVerbosity": ilomCtrlSPARCDiagsUserResetVerbosity,
       "ilomCtrlSPARCDiagsErrorResetVerbosity": ilomCtrlSPARCDiagsErrorResetVerbosity,
       "ilomCtrlSPARCDiagsStatus": ilomCtrlSPARCDiagsStatus,
       "ilomCtrlSPARCDiagsAction": ilomCtrlSPARCDiagsAction,
       "ilomCtrlSPARCDiagsHwChangeLevel": ilomCtrlSPARCDiagsHwChangeLevel,
       "ilomCtrlSPARCDiagsHwChangeVerbosity": ilomCtrlSPARCDiagsHwChangeVerbosity,
       "ilomCtrlSPARCHostControl": ilomCtrlSPARCHostControl,
       "ilomCtrlSPARCHostMACAddress": ilomCtrlSPARCHostMACAddress,
       "ilomCtrlSPARCHostOBPVersion": ilomCtrlSPARCHostOBPVersion,
       "ilomCtrlSPARCHostPOSTVersion": ilomCtrlSPARCHostPOSTVersion,
       "ilomCtrlSPARCHostAutoRunOnError": ilomCtrlSPARCHostAutoRunOnError,
       "ilomCtrlSPARCHostPOSTStatus": ilomCtrlSPARCHostPOSTStatus,
       "ilomCtrlSPARCHostAutoRestartPolicy": ilomCtrlSPARCHostAutoRestartPolicy,
       "ilomCtrlSPARCHostOSBootStatus": ilomCtrlSPARCHostOSBootStatus,
       "ilomCtrlSPARCHostBootTimeout": ilomCtrlSPARCHostBootTimeout,
       "ilomCtrlSPARCHostBootRestart": ilomCtrlSPARCHostBootRestart,
       "ilomCtrlSPARCHostMaxBootFail": ilomCtrlSPARCHostMaxBootFail,
       "ilomCtrlSPARCHostBootFailRecovery": ilomCtrlSPARCHostBootFailRecovery,
       "ilomCtrlSPARCHostHypervisorVersion": ilomCtrlSPARCHostHypervisorVersion,
       "ilomCtrlSPARCHostSysFwVersion": ilomCtrlSPARCHostSysFwVersion,
       "ilomCtrlSPARCHostSendBreakAction": ilomCtrlSPARCHostSendBreakAction,
       "ilomCtrlSPARCHostIoReconfigurePolicy": ilomCtrlSPARCHostIoReconfigurePolicy,
       "ilomCtrlSPARCHostGMVersion": ilomCtrlSPARCHostGMVersion,
       "ilomCtrlSPARCBootMode": ilomCtrlSPARCBootMode,
       "ilomCtrlSPARCBootModeState": ilomCtrlSPARCBootModeState,
       "ilomCtrlSPARCBootModeScript": ilomCtrlSPARCBootModeScript,
       "ilomCtrlSPARCBootModeExpires": ilomCtrlSPARCBootModeExpires,
       "ilomCtrlSPARCBootModeLDOMConfig": ilomCtrlSPARCBootModeLDOMConfig,
       "ilomCtrlSPARCKeySwitch": ilomCtrlSPARCKeySwitch,
       "ilomCtrlSPARCKeySwitchState": ilomCtrlSPARCKeySwitchState,
       "ilomCtrlIdentification": ilomCtrlIdentification,
       "ilomCtrlSystemIdentifier": ilomCtrlSystemIdentifier,
       "ilomCtrlHostName": ilomCtrlHostName,
       "ilomCtrlThd": ilomCtrlThd,
       "ilomCtrlThdState": ilomCtrlThdState,
       "ilomCtrlThdAction": ilomCtrlThdAction,
       "ilomCtrlThdModulesTable": ilomCtrlThdModulesTable,
       "ilomCtrlThdModulesEntry": ilomCtrlThdModulesEntry,
       "ilomCtrlThdModuleName": ilomCtrlThdModuleName,
       "ilomCtrlThdModuleDesc": ilomCtrlThdModuleDesc,
       "ilomCtrlThdModuleState": ilomCtrlThdModuleState,
       "ilomCtrlThdModuleAction": ilomCtrlThdModuleAction,
       "ilomCtrlThdInstanceTable": ilomCtrlThdInstanceTable,
       "ilomCtrlThdInstanceEntry": ilomCtrlThdInstanceEntry,
       "ilomCtrlThdModName": ilomCtrlThdModName,
       "ilomCtrlThdInstanceName": ilomCtrlThdInstanceName,
       "ilomCtrlThdInstanceState": ilomCtrlThdInstanceState,
       "ilomCtrlThdInstanceAction": ilomCtrlThdInstanceAction,
       "ilomCtrlConformances": ilomCtrlConformances,
       "ilomCtrlCompliances": ilomCtrlCompliances,
       "ilomCtrlGroups": ilomCtrlGroups,
       "ilomCtrlDeprecatedObjectsGroup": ilomCtrlDeprecatedObjectsGroup,
       "ilomCtrlObjectsGroup": ilomCtrlObjectsGroup}
)
