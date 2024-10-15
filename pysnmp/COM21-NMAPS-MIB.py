# SNMP MIB module (COM21-NMAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-NMAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:41 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(com21Nmaps,) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21Nmaps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21NmapsVarBinds_ObjectIdentity = ObjectIdentity
com21NmapsVarBinds = _Com21NmapsVarBinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1)
)
_NmapsAlertMessage_Type = DisplayString
_NmapsAlertMessage_Object = MibScalar
nmapsAlertMessage = _NmapsAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1, 1),
    _NmapsAlertMessage_Type()
)
nmapsAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmapsAlertMessage.setStatus("mandatory")
_NmapsMacAddress_Type = MacAddress
_NmapsMacAddress_Object = MibScalar
nmapsMacAddress = _NmapsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1, 2),
    _NmapsMacAddress_Type()
)
nmapsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmapsMacAddress.setStatus("mandatory")
_NmapsDaemonName_Type = DisplayString
_NmapsDaemonName_Object = MibScalar
nmapsDaemonName = _NmapsDaemonName_Object(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1, 3),
    _NmapsDaemonName_Type()
)
nmapsDaemonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmapsDaemonName.setStatus("mandatory")


class _NmapsDaemonPid_Type(Integer32):
    """Custom type nmapsDaemonPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_NmapsDaemonPid_Type.__name__ = "Integer32"
_NmapsDaemonPid_Object = MibScalar
nmapsDaemonPid = _NmapsDaemonPid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1, 4),
    _NmapsDaemonPid_Type()
)
nmapsDaemonPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmapsDaemonPid.setStatus("mandatory")
_NmapsIpAddress_Type = IpAddress
_NmapsIpAddress_Object = MibScalar
nmapsIpAddress = _NmapsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1, 5),
    _NmapsIpAddress_Type()
)
nmapsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmapsIpAddress.setStatus("mandatory")


class _NmapsDaemonForcePoll_Type(Integer32):
    """Custom type nmapsDaemonForcePoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("optional", 0),
          ("required", 1))
    )


_NmapsDaemonForcePoll_Type.__name__ = "Integer32"
_NmapsDaemonForcePoll_Object = MibScalar
nmapsDaemonForcePoll = _NmapsDaemonForcePoll_Object(
    (1, 3, 6, 1, 4, 1, 1141, 5, 1, 6),
    _NmapsDaemonForcePoll_Type()
)
nmapsDaemonForcePoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmapsDaemonForcePoll.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nmapsStuTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 1)
)
if mibBuilder.loadTexts:
    nmapsStuTopologyChange.setStatus(
        ""
    )

nmapsStuDuplicateMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 2)
)
nmapsStuDuplicateMac.setObjects(
    ("COM21-NMAPS-MIB", "nmapsMacAddress")
)
if mibBuilder.loadTexts:
    nmapsStuDuplicateMac.setStatus(
        ""
    )

nmapsDaemonDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 3)
)
nmapsDaemonDown.setObjects(
      *(("COM21-NMAPS-MIB", "nmapsDaemonName"),
        ("COM21-NMAPS-MIB", "nmapsDaemonPid"))
)
if mibBuilder.loadTexts:
    nmapsDaemonDown.setStatus(
        ""
    )

nmapsDaemonUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 4)
)
nmapsDaemonUp.setObjects(
      *(("COM21-NMAPS-MIB", "nmapsDaemonName"),
        ("COM21-NMAPS-MIB", "nmapsDaemonPid"))
)
if mibBuilder.loadTexts:
    nmapsDaemonUp.setStatus(
        ""
    )

nmapsUpdateHcxInDb = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 5)
)
nmapsUpdateHcxInDb.setObjects(
    ("COM21-NMAPS-MIB", "nmapsDaemonForcePoll")
)
if mibBuilder.loadTexts:
    nmapsUpdateHcxInDb.setStatus(
        ""
    )

nmapsUpdateStusInDb = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 6)
)
nmapsUpdateStusInDb.setObjects(
    ("COM21-NMAPS-MIB", "nmapsDaemonForcePoll")
)
if mibBuilder.loadTexts:
    nmapsUpdateStusInDb.setStatus(
        ""
    )

nmapsConfiguredStuMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 7)
)
nmapsConfiguredStuMissing.setObjects(
    ("COM21-NMAPS-MIB", "nmapsMacAddress")
)
if mibBuilder.loadTexts:
    nmapsConfiguredStuMissing.setStatus(
        ""
    )

nmapsDebugAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 101)
)
nmapsDebugAlert.setObjects(
    ("COM21-NMAPS-MIB", "nmapsAlertMessage")
)
if mibBuilder.loadTexts:
    nmapsDebugAlert.setStatus(
        ""
    )

nmapsInfoAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 102)
)
nmapsInfoAlert.setObjects(
    ("COM21-NMAPS-MIB", "nmapsAlertMessage")
)
if mibBuilder.loadTexts:
    nmapsInfoAlert.setStatus(
        ""
    )

nmapsWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 103)
)
nmapsWarningAlert.setObjects(
    ("COM21-NMAPS-MIB", "nmapsAlertMessage")
)
if mibBuilder.loadTexts:
    nmapsWarningAlert.setStatus(
        ""
    )

nmapsErrorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 104)
)
nmapsErrorAlert.setObjects(
    ("COM21-NMAPS-MIB", "nmapsAlertMessage")
)
if mibBuilder.loadTexts:
    nmapsErrorAlert.setStatus(
        ""
    )

nmapsFatalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 105)
)
nmapsFatalAlert.setObjects(
    ("COM21-NMAPS-MIB", "nmapsAlertMessage")
)
if mibBuilder.loadTexts:
    nmapsFatalAlert.setStatus(
        ""
    )

nmapsDisasterAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 5, 0, 106)
)
nmapsDisasterAlert.setObjects(
    ("COM21-NMAPS-MIB", "nmapsAlertMessage")
)
if mibBuilder.loadTexts:
    nmapsDisasterAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-NMAPS-MIB",
    **{"nmapsStuTopologyChange": nmapsStuTopologyChange,
       "nmapsStuDuplicateMac": nmapsStuDuplicateMac,
       "nmapsDaemonDown": nmapsDaemonDown,
       "nmapsDaemonUp": nmapsDaemonUp,
       "nmapsUpdateHcxInDb": nmapsUpdateHcxInDb,
       "nmapsUpdateStusInDb": nmapsUpdateStusInDb,
       "nmapsConfiguredStuMissing": nmapsConfiguredStuMissing,
       "nmapsDebugAlert": nmapsDebugAlert,
       "nmapsInfoAlert": nmapsInfoAlert,
       "nmapsWarningAlert": nmapsWarningAlert,
       "nmapsErrorAlert": nmapsErrorAlert,
       "nmapsFatalAlert": nmapsFatalAlert,
       "nmapsDisasterAlert": nmapsDisasterAlert,
       "com21NmapsVarBinds": com21NmapsVarBinds,
       "nmapsAlertMessage": nmapsAlertMessage,
       "nmapsMacAddress": nmapsMacAddress,
       "nmapsDaemonName": nmapsDaemonName,
       "nmapsDaemonPid": nmapsDaemonPid,
       "nmapsIpAddress": nmapsIpAddress,
       "nmapsDaemonForcePoll": nmapsDaemonForcePoll}
)
