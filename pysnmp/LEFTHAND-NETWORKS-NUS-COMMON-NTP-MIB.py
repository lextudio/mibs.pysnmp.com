# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:45 2024
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonNTP,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonNTP")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNusCommonNTPModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtpCount_Type = Integer32
_NtpCount_Object = MibScalar
ntpCount = _NtpCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 1),
    _NtpCount_Type()
)
ntpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpCount.setStatus("current")
_NtpTable_Object = MibTable
ntpTable = _NtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ntpTable.setStatus("current")
_NtpEntry_Object = MibTableRow
ntpEntry = _NtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1)
)
ntpEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-NTP-MIB", "ntpIndex"),
)
if mibBuilder.loadTexts:
    ntpEntry.setStatus("current")
_NtpIndex_Type = Integer32
_NtpIndex_Object = MibTableColumn
ntpIndex = _NtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 1),
    _NtpIndex_Type()
)
ntpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpIndex.setStatus("current")
_NtpPreferred_Type = TruthValue
_NtpPreferred_Object = MibTableColumn
ntpPreferred = _NtpPreferred_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 2),
    _NtpPreferred_Type()
)
ntpPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPreferred.setStatus("current")
_NtpServer_Type = OctetString
_NtpServer_Object = MibTableColumn
ntpServer = _NtpServer_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 3),
    _NtpServer_Type()
)
ntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer.setStatus("current")
_NtpRowStatus_Type = RowStatus
_NtpRowStatus_Object = MibTableColumn
ntpRowStatus = _NtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 4),
    _NtpRowStatus_Type()
)
ntpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpRowStatus.setStatus("current")
_NtpStart_Type = TruthValue
_NtpStart_Object = MibScalar
ntpStart = _NtpStart_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 3),
    _NtpStart_Type()
)
ntpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpStart.setStatus("current")
_NtpStop_Type = TruthValue
_NtpStop_Object = MibScalar
ntpStop = _NtpStop_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 4),
    _NtpStop_Type()
)
ntpStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpStop.setStatus("current")
_NtpRestart_Type = TruthValue
_NtpRestart_Object = MibScalar
ntpRestart = _NtpRestart_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 5),
    _NtpRestart_Type()
)
ntpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpRestart.setStatus("current")
_NtpCheck_Type = TruthValue
_NtpCheck_Object = MibScalar
ntpCheck = _NtpCheck_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 6),
    _NtpCheck_Type()
)
ntpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCheck.setStatus("current")
_TimeGMTTime_Type = OctetString
_TimeGMTTime_Object = MibScalar
timeGMTTime = _TimeGMTTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 7),
    _TimeGMTTime_Type()
)
timeGMTTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeGMTTime.setStatus("current")
_TimeTimeZone_Type = OctetString
_TimeTimeZone_Object = MibScalar
timeTimeZone = _TimeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 8),
    _TimeTimeZone_Type()
)
timeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeTimeZone.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-NTP-MIB",
    **{"lhnNusCommonNTPModule": lhnNusCommonNTPModule,
       "ntpCount": ntpCount,
       "ntpTable": ntpTable,
       "ntpEntry": ntpEntry,
       "ntpIndex": ntpIndex,
       "ntpPreferred": ntpPreferred,
       "ntpServer": ntpServer,
       "ntpRowStatus": ntpRowStatus,
       "ntpStart": ntpStart,
       "ntpStop": ntpStop,
       "ntpRestart": ntpRestart,
       "ntpCheck": ntpCheck,
       "timeGMTTime": timeGMTTime,
       "timeTimeZone": timeTimeZone}
)
