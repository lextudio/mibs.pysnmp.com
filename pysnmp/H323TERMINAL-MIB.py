# SNMP MIB module (H323TERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H323TERMINAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:47 2024
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
 experimental,
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
    "experimental",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

h323TerminalMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 323, 3)
)
h323TerminalMIB.setRevisions(
        ("1998-05-25 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323TerminalDescr_ObjectIdentity = ObjectIdentity
h323TerminalDescr = _H323TerminalDescr_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 1)
)


class _H323t35CountryCode_Type(Integer32):
    """Custom type h323t35CountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H323t35CountryCode_Type.__name__ = "Integer32"
_H323t35CountryCode_Object = MibScalar
h323t35CountryCode = _H323t35CountryCode_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 1),
    _H323t35CountryCode_Type()
)
h323t35CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323t35CountryCode.setStatus("current")


class _H323t35CountryCodeExtention_Type(Integer32):
    """Custom type h323t35CountryCodeExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H323t35CountryCodeExtention_Type.__name__ = "Integer32"
_H323t35CountryCodeExtention_Object = MibScalar
h323t35CountryCodeExtention = _H323t35CountryCodeExtention_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 2),
    _H323t35CountryCodeExtention_Type()
)
h323t35CountryCodeExtention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323t35CountryCodeExtention.setStatus("current")


class _H323t35ManufacturerCode_Type(Integer32):
    """Custom type h323t35ManufacturerCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H323t35ManufacturerCode_Type.__name__ = "Integer32"
_H323t35ManufacturerCode_Object = MibScalar
h323t35ManufacturerCode = _H323t35ManufacturerCode_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 3),
    _H323t35ManufacturerCode_Type()
)
h323t35ManufacturerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323t35ManufacturerCode.setStatus("current")
_H323TerminalUptime_Type = TimeTicks
_H323TerminalUptime_Object = MibScalar
h323TerminalUptime = _H323TerminalUptime_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 4),
    _H323TerminalUptime_Type()
)
h323TerminalUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalUptime.setStatus("current")
_H323TerminalLocalTime_Type = DateAndTime
_H323TerminalLocalTime_Object = MibScalar
h323TerminalLocalTime = _H323TerminalLocalTime_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 5),
    _H323TerminalLocalTime_Type()
)
h323TerminalLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalLocalTime.setStatus("current")
_H323TerminalDiagnostics_Type = Integer32
_H323TerminalDiagnostics_Object = MibScalar
h323TerminalDiagnostics = _H323TerminalDiagnostics_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 6),
    _H323TerminalDiagnostics_Type()
)
h323TerminalDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalDiagnostics.setStatus("current")


class _H323TerminalStatus_Type(Integer32):
    """Custom type h323TerminalStatus based on Integer32"""
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
        *(("callHangUp", 3),
          ("callSetup", 1),
          ("callinProgress", 2),
          ("idle", 4))
    )


_H323TerminalStatus_Type.__name__ = "Integer32"
_H323TerminalStatus_Object = MibScalar
h323TerminalStatus = _H323TerminalStatus_Object(
    (1, 3, 6, 1, 3, 323, 3, 1, 7),
    _H323TerminalStatus_Type()
)
h323TerminalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalStatus.setStatus("current")
_H323TerminalCaps_ObjectIdentity = ObjectIdentity
h323TerminalCaps = _H323TerminalCaps_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 2)
)
_H323TerminalMaxLineRate_Type = Integer32
_H323TerminalMaxLineRate_Object = MibScalar
h323TerminalMaxLineRate = _H323TerminalMaxLineRate_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 1),
    _H323TerminalMaxLineRate_Type()
)
h323TerminalMaxLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalMaxLineRate.setStatus("current")
_H323TerminalVideoCaps_Type = Integer32
_H323TerminalVideoCaps_Object = MibScalar
h323TerminalVideoCaps = _H323TerminalVideoCaps_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 2),
    _H323TerminalVideoCaps_Type()
)
h323TerminalVideoCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalVideoCaps.setStatus("current")
_H323TerminalMaxVideoRate_Type = Integer32
_H323TerminalMaxVideoRate_Object = MibScalar
h323TerminalMaxVideoRate = _H323TerminalMaxVideoRate_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 3),
    _H323TerminalMaxVideoRate_Type()
)
h323TerminalMaxVideoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalMaxVideoRate.setStatus("current")
_H323TerminalAudioCaps_Type = Integer32
_H323TerminalAudioCaps_Object = MibScalar
h323TerminalAudioCaps = _H323TerminalAudioCaps_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 4),
    _H323TerminalAudioCaps_Type()
)
h323TerminalAudioCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalAudioCaps.setStatus("current")
_H323TerminalDataCaps_Type = Integer32
_H323TerminalDataCaps_Object = MibScalar
h323TerminalDataCaps = _H323TerminalDataCaps_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 5),
    _H323TerminalDataCaps_Type()
)
h323TerminalDataCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalDataCaps.setStatus("current")
_H323TerminalEncrypCaps_Type = Integer32
_H323TerminalEncrypCaps_Object = MibScalar
h323TerminalEncrypCaps = _H323TerminalEncrypCaps_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 6),
    _H323TerminalEncrypCaps_Type()
)
h323TerminalEncrypCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalEncrypCaps.setStatus("current")
_H323TerminalRDCCaps_Type = Integer32
_H323TerminalRDCCaps_Object = MibScalar
h323TerminalRDCCaps = _H323TerminalRDCCaps_Object(
    (1, 3, 6, 1, 3, 323, 3, 2, 7),
    _H323TerminalRDCCaps_Type()
)
h323TerminalRDCCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TerminalRDCCaps.setStatus("current")
_H323TerminalConfig_ObjectIdentity = ObjectIdentity
h323TerminalConfig = _H323TerminalConfig_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 3)
)


class _H323TerminalSiteName_Type(DisplayString):
    """Custom type h323TerminalSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323TerminalSiteName_Type.__name__ = "DisplayString"
_H323TerminalSiteName_Object = MibScalar
h323TerminalSiteName = _H323TerminalSiteName_Object(
    (1, 3, 6, 1, 3, 323, 3, 3, 1),
    _H323TerminalSiteName_Type()
)
h323TerminalSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalSiteName.setStatus("current")


class _H323TerminalVideoSystem_Type(Integer32):
    """Custom type h323TerminalVideoSystem based on Integer32"""
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
        *(("ntsc", 1),
          ("others", 4),
          ("pal", 2),
          ("secam", 3))
    )


_H323TerminalVideoSystem_Type.__name__ = "Integer32"
_H323TerminalVideoSystem_Object = MibScalar
h323TerminalVideoSystem = _H323TerminalVideoSystem_Object(
    (1, 3, 6, 1, 3, 323, 3, 3, 2),
    _H323TerminalVideoSystem_Type()
)
h323TerminalVideoSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalVideoSystem.setStatus("current")
_H323TerminalfType_Type = Integer32
_H323TerminalfType_Object = MibScalar
h323TerminalfType = _H323TerminalfType_Object(
    (1, 3, 6, 1, 3, 323, 3, 3, 3),
    _H323TerminalfType_Type()
)
h323TerminalfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalfType.setStatus("current")
_H323TerminalIPAddress_Type = IpAddress
_H323TerminalIPAddress_Object = MibScalar
h323TerminalIPAddress = _H323TerminalIPAddress_Object(
    (1, 3, 6, 1, 3, 323, 3, 3, 4),
    _H323TerminalIPAddress_Type()
)
h323TerminalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalIPAddress.setStatus("current")
_H323TerminalControl_ObjectIdentity = ObjectIdentity
h323TerminalControl = _H323TerminalControl_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 4)
)


class _H323TerminalAdminControl_Type(Integer32):
    """Custom type h323TerminalAdminControl based on Integer32"""
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
        *(("diagnose", 3),
          ("reset", 2),
          ("run", 1),
          ("stop", 4))
    )


_H323TerminalAdminControl_Type.__name__ = "Integer32"
_H323TerminalAdminControl_Object = MibScalar
h323TerminalAdminControl = _H323TerminalAdminControl_Object(
    (1, 3, 6, 1, 3, 323, 3, 4, 1),
    _H323TerminalAdminControl_Type()
)
h323TerminalAdminControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalAdminControl.setStatus("current")
_H323TerminalCallSetUp_Type = Integer32
_H323TerminalCallSetUp_Object = MibScalar
h323TerminalCallSetUp = _H323TerminalCallSetUp_Object(
    (1, 3, 6, 1, 3, 323, 3, 4, 2),
    _H323TerminalCallSetUp_Type()
)
h323TerminalCallSetUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalCallSetUp.setStatus("current")
_H323TerminalCallHangup_Type = Integer32
_H323TerminalCallHangup_Object = MibScalar
h323TerminalCallHangup = _H323TerminalCallHangup_Object(
    (1, 3, 6, 1, 3, 323, 3, 4, 3),
    _H323TerminalCallHangup_Type()
)
h323TerminalCallHangup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323TerminalCallHangup.setStatus("current")


class _H323EnableLocalLoopback_Type(Integer32):
    """Custom type h323EnableLocalLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H323EnableLocalLoopback_Type.__name__ = "Integer32"
_H323EnableLocalLoopback_Object = MibScalar
h323EnableLocalLoopback = _H323EnableLocalLoopback_Object(
    (1, 3, 6, 1, 3, 323, 3, 4, 4),
    _H323EnableLocalLoopback_Type()
)
h323EnableLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323EnableLocalLoopback.setStatus("current")


class _H323EnableRemoteLoopback_Type(Integer32):
    """Custom type h323EnableRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H323EnableRemoteLoopback_Type.__name__ = "Integer32"
_H323EnableRemoteLoopback_Object = MibScalar
h323EnableRemoteLoopback = _H323EnableRemoteLoopback_Object(
    (1, 3, 6, 1, 3, 323, 3, 4, 5),
    _H323EnableRemoteLoopback_Type()
)
h323EnableRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323EnableRemoteLoopback.setStatus("current")
_H323TerminalMIBConfs_ObjectIdentity = ObjectIdentity
h323TerminalMIBConfs = _H323TerminalMIBConfs_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 5)
)
_H323TerminalMIBGroups_ObjectIdentity = ObjectIdentity
h323TerminalMIBGroups = _H323TerminalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 5, 1)
)
_H323TerminalMIBCompl_ObjectIdentity = ObjectIdentity
h323TerminalMIBCompl = _H323TerminalMIBCompl_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3, 5, 2)
)

# Managed Objects groups

h323TerminalDesrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 323, 3, 5, 1, 1)
)
h323TerminalDesrGroup.setObjects(
      *(("H323TERMINAL-MIB", "h323t35CountryCode"),
        ("H323TERMINAL-MIB", "h323t35CountryCodeExtention"),
        ("H323TERMINAL-MIB", "h323t35ManufacturerCode"),
        ("H323TERMINAL-MIB", "h323TerminalUptime"),
        ("H323TERMINAL-MIB", "h323TerminalLocalTime"),
        ("H323TERMINAL-MIB", "h323TerminalDiagnostics"),
        ("H323TERMINAL-MIB", "h323TerminalStatus"))
)
if mibBuilder.loadTexts:
    h323TerminalDesrGroup.setStatus("current")

h323TerminalCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 323, 3, 5, 1, 2)
)
h323TerminalCapsGroup.setObjects(
      *(("H323TERMINAL-MIB", "h323TerminalMaxLineRate"),
        ("H323TERMINAL-MIB", "h323TerminalVideoCaps"),
        ("H323TERMINAL-MIB", "h323TerminalMaxVideoRate"),
        ("H323TERMINAL-MIB", "h323TerminalAudioCaps"),
        ("H323TERMINAL-MIB", "h323TerminalDataCaps"),
        ("H323TERMINAL-MIB", "h323TerminalEncrypCaps"),
        ("H323TERMINAL-MIB", "h323TerminalRDCCaps"))
)
if mibBuilder.loadTexts:
    h323TerminalCapsGroup.setStatus("current")

h323TerminalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 323, 3, 5, 1, 3)
)
h323TerminalConfigGroup.setObjects(
      *(("H323TERMINAL-MIB", "h323TerminalSiteName"),
        ("H323TERMINAL-MIB", "h323TerminalVideoSystem"),
        ("H323TERMINAL-MIB", "h323TerminalfType"),
        ("H323TERMINAL-MIB", "h323TerminalIPAddress"))
)
if mibBuilder.loadTexts:
    h323TerminalConfigGroup.setStatus("current")

h323TerminalControlGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 323, 3, 5, 1, 4)
)
h323TerminalControlGroup.setObjects(
      *(("H323TERMINAL-MIB", "h323TerminalAdminControl"),
        ("H323TERMINAL-MIB", "h323TerminalCallSetUp"),
        ("H323TERMINAL-MIB", "h323TerminalCallHangup"),
        ("H323TERMINAL-MIB", "h323EnableLocalLoopback"),
        ("H323TERMINAL-MIB", "h323EnableRemoteLoopback"))
)
if mibBuilder.loadTexts:
    h323TerminalControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h323TerminalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 323, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    h323TerminalCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H323TERMINAL-MIB",
    **{"h323TerminalMIB": h323TerminalMIB,
       "h323TerminalDescr": h323TerminalDescr,
       "h323t35CountryCode": h323t35CountryCode,
       "h323t35CountryCodeExtention": h323t35CountryCodeExtention,
       "h323t35ManufacturerCode": h323t35ManufacturerCode,
       "h323TerminalUptime": h323TerminalUptime,
       "h323TerminalLocalTime": h323TerminalLocalTime,
       "h323TerminalDiagnostics": h323TerminalDiagnostics,
       "h323TerminalStatus": h323TerminalStatus,
       "h323TerminalCaps": h323TerminalCaps,
       "h323TerminalMaxLineRate": h323TerminalMaxLineRate,
       "h323TerminalVideoCaps": h323TerminalVideoCaps,
       "h323TerminalMaxVideoRate": h323TerminalMaxVideoRate,
       "h323TerminalAudioCaps": h323TerminalAudioCaps,
       "h323TerminalDataCaps": h323TerminalDataCaps,
       "h323TerminalEncrypCaps": h323TerminalEncrypCaps,
       "h323TerminalRDCCaps": h323TerminalRDCCaps,
       "h323TerminalConfig": h323TerminalConfig,
       "h323TerminalSiteName": h323TerminalSiteName,
       "h323TerminalVideoSystem": h323TerminalVideoSystem,
       "h323TerminalfType": h323TerminalfType,
       "h323TerminalIPAddress": h323TerminalIPAddress,
       "h323TerminalControl": h323TerminalControl,
       "h323TerminalAdminControl": h323TerminalAdminControl,
       "h323TerminalCallSetUp": h323TerminalCallSetUp,
       "h323TerminalCallHangup": h323TerminalCallHangup,
       "h323EnableLocalLoopback": h323EnableLocalLoopback,
       "h323EnableRemoteLoopback": h323EnableRemoteLoopback,
       "h323TerminalMIBConfs": h323TerminalMIBConfs,
       "h323TerminalMIBGroups": h323TerminalMIBGroups,
       "h323TerminalDesrGroup": h323TerminalDesrGroup,
       "h323TerminalCapsGroup": h323TerminalCapsGroup,
       "h323TerminalConfigGroup": h323TerminalConfigGroup,
       "h323TerminalControlGroup": h323TerminalControlGroup,
       "h323TerminalMIBCompl": h323TerminalMIBCompl,
       "h323TerminalCompliance": h323TerminalCompliance}
)
