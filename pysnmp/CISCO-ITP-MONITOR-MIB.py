# SNMP MIB module (CISCO-ITP-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:30 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379)
)
ciscoItpmMIB.setRevisions(
        ("2004-07-20 00:00",
         "2003-10-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoItpmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoItpmMIBNotifs = _CiscoItpmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 0)
)
_CiscoItpmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpmMIBObjects = _CiscoItpmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1)
)
_CItpmConn_ObjectIdentity = ObjectIdentity
cItpmConn = _CItpmConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1)
)
_CItpmConnTable_Object = MibTable
cItpmConnTable = _CItpmConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cItpmConnTable.setStatus("current")
_CItpmConnTableEntry_Object = MibTableRow
cItpmConnTableEntry = _CItpmConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1)
)
cItpmConnTableEntry.setIndexNames(
    (0, "CISCO-ITP-MONITOR-MIB", "cItpmConnPortNumber"),
)
if mibBuilder.loadTexts:
    cItpmConnTableEntry.setStatus("current")
_CItpmConnPortNumber_Type = InetPortNumber
_CItpmConnPortNumber_Object = MibTableColumn
cItpmConnPortNumber = _CItpmConnPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 1),
    _CItpmConnPortNumber_Type()
)
cItpmConnPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpmConnPortNumber.setStatus("current")


class _CItpmConnKeepAlive_Type(Unsigned32):
    """Custom type cItpmConnKeepAlive based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CItpmConnKeepAlive_Type.__name__ = "Unsigned32"
_CItpmConnKeepAlive_Object = MibTableColumn
cItpmConnKeepAlive = _CItpmConnKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 2),
    _CItpmConnKeepAlive_Type()
)
cItpmConnKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmConnKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnKeepAlive.setUnits("milliseconds")


class _CItpmConnMaxQDepth_Type(Unsigned32):
    """Custom type cItpmConnMaxQDepth based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_CItpmConnMaxQDepth_Type.__name__ = "Unsigned32"
_CItpmConnMaxQDepth_Object = MibTableColumn
cItpmConnMaxQDepth = _CItpmConnMaxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 3),
    _CItpmConnMaxQDepth_Type()
)
cItpmConnMaxQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmConnMaxQDepth.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnMaxQDepth.setUnits("packets")


class _CItpmConnCongOnset_Type(Unsigned32):
    """Custom type cItpmConnCongOnset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_CItpmConnCongOnset_Type.__name__ = "Unsigned32"
_CItpmConnCongOnset_Object = MibTableColumn
cItpmConnCongOnset = _CItpmConnCongOnset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 4),
    _CItpmConnCongOnset_Type()
)
cItpmConnCongOnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmConnCongOnset.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnCongOnset.setUnits("packets")


class _CItpmConnCongAbate_Type(Unsigned32):
    """Custom type cItpmConnCongAbate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CItpmConnCongAbate_Type.__name__ = "Unsigned32"
_CItpmConnCongAbate_Object = MibTableColumn
cItpmConnCongAbate = _CItpmConnCongAbate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 5),
    _CItpmConnCongAbate_Type()
)
cItpmConnCongAbate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmConnCongAbate.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnCongAbate.setUnits("packets")


class _CItpmConnRcvWindowSize_Type(Unsigned32):
    """Custom type cItpmConnRcvWindowSize based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_CItpmConnRcvWindowSize_Type.__name__ = "Unsigned32"
_CItpmConnRcvWindowSize_Object = MibTableColumn
cItpmConnRcvWindowSize = _CItpmConnRcvWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 6),
    _CItpmConnRcvWindowSize_Type()
)
cItpmConnRcvWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmConnRcvWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnRcvWindowSize.setUnits("bytes")


class _CItpmConnFastStart_Type(TruthValue):
    """Custom type cItpmConnFastStart based on TruthValue"""


_CItpmConnFastStart_Object = MibTableColumn
cItpmConnFastStart = _CItpmConnFastStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 7),
    _CItpmConnFastStart_Type()
)
cItpmConnFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmConnFastStart.setStatus("current")


class _CItpmConnQueueDepth_Type(Gauge32):
    """Custom type cItpmConnQueueDepth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CItpmConnQueueDepth_Type.__name__ = "Gauge32"
_CItpmConnQueueDepth_Object = MibTableColumn
cItpmConnQueueDepth = _CItpmConnQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 8),
    _CItpmConnQueueDepth_Type()
)
cItpmConnQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmConnQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnQueueDepth.setUnits("packets")


class _CItpmConnMonitorState_Type(Integer32):
    """Custom type cItpmConnMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CItpmConnMonitorState_Type.__name__ = "Integer32"
_CItpmConnMonitorState_Object = MibTableColumn
cItpmConnMonitorState = _CItpmConnMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 9),
    _CItpmConnMonitorState_Type()
)
cItpmConnMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmConnMonitorState.setStatus("current")
_CItpmConnCongestion_Type = TruthValue
_CItpmConnCongestion_Object = MibTableColumn
cItpmConnCongestion = _CItpmConnCongestion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 10),
    _CItpmConnCongestion_Type()
)
cItpmConnCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmConnCongestion.setStatus("current")
_CItpmConnCongCounts_Type = Counter32
_CItpmConnCongCounts_Object = MibTableColumn
cItpmConnCongCounts = _CItpmConnCongCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 1, 1, 11),
    _CItpmConnCongCounts_Type()
)
cItpmConnCongCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmConnCongCounts.setStatus("current")
if mibBuilder.loadTexts:
    cItpmConnCongCounts.setUnits("occurences")
_CItpmLinkTable_Object = MibTable
cItpmLinkTable = _CItpmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cItpmLinkTable.setStatus("current")
_CItpmLinkTableEntry_Object = MibTableRow
cItpmLinkTableEntry = _CItpmLinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1)
)
cItpmLinkTableEntry.setIndexNames(
    (0, "CISCO-ITP-MONITOR-MIB", "cItpmConnPortNumber"),
    (0, "CISCO-ITP-MONITOR-MIB", "cItpmLinkNumber"),
)
if mibBuilder.loadTexts:
    cItpmLinkTableEntry.setStatus("current")


class _CItpmLinkNumber_Type(Unsigned32):
    """Custom type cItpmLinkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CItpmLinkNumber_Type.__name__ = "Unsigned32"
_CItpmLinkNumber_Object = MibTableColumn
cItpmLinkNumber = _CItpmLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 1),
    _CItpmLinkNumber_Type()
)
cItpmLinkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpmLinkNumber.setStatus("current")


class _CItpmLinkDescription_Type(SnmpAdminString):
    """Custom type cItpmLinkDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CItpmLinkDescription_Type.__name__ = "SnmpAdminString"
_CItpmLinkDescription_Object = MibTableColumn
cItpmLinkDescription = _CItpmLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 2),
    _CItpmLinkDescription_Type()
)
cItpmLinkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkDescription.setStatus("current")


class _CItpmLinkSlotNumber_Type(Unsigned32):
    """Custom type cItpmLinkSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CItpmLinkSlotNumber_Type.__name__ = "Unsigned32"
_CItpmLinkSlotNumber_Object = MibTableColumn
cItpmLinkSlotNumber = _CItpmLinkSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 3),
    _CItpmLinkSlotNumber_Type()
)
cItpmLinkSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkSlotNumber.setStatus("current")


class _CItpmLinkStatus_Type(Integer32):
    """Custom type cItpmLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CItpmLinkStatus_Type.__name__ = "Integer32"
_CItpmLinkStatus_Object = MibTableColumn
cItpmLinkStatus = _CItpmLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 4),
    _CItpmLinkStatus_Type()
)
cItpmLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkStatus.setStatus("current")
_CItpmLinkRcvdMsus_Type = Counter32
_CItpmLinkRcvdMsus_Object = MibTableColumn
cItpmLinkRcvdMsus = _CItpmLinkRcvdMsus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 5),
    _CItpmLinkRcvdMsus_Type()
)
cItpmLinkRcvdMsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkRcvdMsus.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkRcvdMsus.setUnits("MSUs")
_CItpmLinkRcvdMsuDrops_Type = Counter32
_CItpmLinkRcvdMsuDrops_Object = MibTableColumn
cItpmLinkRcvdMsuDrops = _CItpmLinkRcvdMsuDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 6),
    _CItpmLinkRcvdMsuDrops_Type()
)
cItpmLinkRcvdMsuDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkRcvdMsuDrops.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkRcvdMsuDrops.setUnits("MSUs")
_CItpmLinkRcvdMsuRate_Type = Gauge32
_CItpmLinkRcvdMsuRate_Object = MibTableColumn
cItpmLinkRcvdMsuRate = _CItpmLinkRcvdMsuRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 7),
    _CItpmLinkRcvdMsuRate_Type()
)
cItpmLinkRcvdMsuRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkRcvdMsuRate.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkRcvdMsuRate.setUnits("MSUs per second")
_CItpmLinkRcvdBitsRate_Type = Gauge32
_CItpmLinkRcvdBitsRate_Object = MibTableColumn
cItpmLinkRcvdBitsRate = _CItpmLinkRcvdBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 8),
    _CItpmLinkRcvdBitsRate_Type()
)
cItpmLinkRcvdBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkRcvdBitsRate.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkRcvdBitsRate.setUnits("bits per second")
_CItpmLinkSentMsus_Type = Counter32
_CItpmLinkSentMsus_Object = MibTableColumn
cItpmLinkSentMsus = _CItpmLinkSentMsus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 9),
    _CItpmLinkSentMsus_Type()
)
cItpmLinkSentMsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkSentMsus.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkSentMsus.setUnits("MSUs")
_CItpmLinkSentMsuDrops_Type = Counter32
_CItpmLinkSentMsuDrops_Object = MibTableColumn
cItpmLinkSentMsuDrops = _CItpmLinkSentMsuDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 10),
    _CItpmLinkSentMsuDrops_Type()
)
cItpmLinkSentMsuDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkSentMsuDrops.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkSentMsuDrops.setUnits("MSUs")
_CItpmLinkSentMsuRate_Type = Gauge32
_CItpmLinkSentMsuRate_Object = MibTableColumn
cItpmLinkSentMsuRate = _CItpmLinkSentMsuRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 11),
    _CItpmLinkSentMsuRate_Type()
)
cItpmLinkSentMsuRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkSentMsuRate.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkSentMsuRate.setUnits("MSUs per second")
_CItpmLinkSentBitsRate_Type = Gauge32
_CItpmLinkSentBitsRate_Object = MibTableColumn
cItpmLinkSentBitsRate = _CItpmLinkSentBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 1, 2, 1, 12),
    _CItpmLinkSentBitsRate_Type()
)
cItpmLinkSentBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpmLinkSentBitsRate.setStatus("current")
if mibBuilder.loadTexts:
    cItpmLinkSentBitsRate.setUnits("bits per second")
_CItpmLink_ObjectIdentity = ObjectIdentity
cItpmLink = _CItpmLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 2)
)


class _CItpmCongestionNotifEnabled_Type(TruthValue):
    """Custom type cItpmCongestionNotifEnabled based on TruthValue"""


_CItpmCongestionNotifEnabled_Object = MibScalar
cItpmCongestionNotifEnabled = _CItpmCongestionNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 3),
    _CItpmCongestionNotifEnabled_Type()
)
cItpmCongestionNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmCongestionNotifEnabled.setStatus("current")


class _CItpmMonitorStateNotifEnabled_Type(TruthValue):
    """Custom type cItpmMonitorStateNotifEnabled based on TruthValue"""


_CItpmMonitorStateNotifEnabled_Object = MibScalar
cItpmMonitorStateNotifEnabled = _CItpmMonitorStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 1, 4),
    _CItpmMonitorStateNotifEnabled_Type()
)
cItpmMonitorStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpmMonitorStateNotifEnabled.setStatus("current")
_CiscoItpmMIBConform_ObjectIdentity = ObjectIdentity
ciscoItpmMIBConform = _CiscoItpmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2)
)
_CiscoItpmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpmMIBCompliances = _CiscoItpmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 1)
)
_CiscoItpmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpmMIBGroups = _CiscoItpmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 2)
)

# Managed Objects groups

ciscoItpmConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 2, 1)
)
ciscoItpmConnGroup.setObjects(
      *(("CISCO-ITP-MONITOR-MIB", "cItpmCongestionNotifEnabled"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnKeepAlive"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnMaxQDepth"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongOnset"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongAbate"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnRcvWindowSize"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnFastStart"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnQueueDepth"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnMonitorState"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongestion"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongCounts"))
)
if mibBuilder.loadTexts:
    ciscoItpmConnGroup.setStatus("deprecated")

ciscoItpmLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 2, 2)
)
ciscoItpmLinkGroup.setObjects(
      *(("CISCO-ITP-MONITOR-MIB", "cItpmLinkDescription"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkSlotNumber"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkStatus"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkRcvdMsus"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkRcvdMsuDrops"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkRcvdMsuRate"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkRcvdBitsRate"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkSentMsus"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkSentMsuDrops"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkSentMsuRate"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmLinkSentBitsRate"))
)
if mibBuilder.loadTexts:
    ciscoItpmLinkGroup.setStatus("current")

ciscoItpmConnGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 2, 4)
)
ciscoItpmConnGroupRev1.setObjects(
      *(("CISCO-ITP-MONITOR-MIB", "cItpmCongestionNotifEnabled"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmMonitorStateNotifEnabled"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnKeepAlive"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnMaxQDepth"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongOnset"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongAbate"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnRcvWindowSize"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnFastStart"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnQueueDepth"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnMonitorState"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongestion"),
        ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongCounts"))
)
if mibBuilder.loadTexts:
    ciscoItpmConnGroupRev1.setStatus("current")


# Notification objects

ciscoItpMonitorCongestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 0, 1)
)
ciscoItpMonitorCongestion.setObjects(
    ("CISCO-ITP-MONITOR-MIB", "cItpmConnCongestion")
)
if mibBuilder.loadTexts:
    ciscoItpMonitorCongestion.setStatus(
        "current"
    )

ciscoItpMonitorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 0, 2)
)
ciscoItpMonitorState.setObjects(
    ("CISCO-ITP-MONITOR-MIB", "cItpmConnMonitorState")
)
if mibBuilder.loadTexts:
    ciscoItpMonitorState.setStatus(
        "current"
    )


# Notifications groups

ciscoItpmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 2, 3)
)
ciscoItpmNotificationsGroup.setObjects(
    ("CISCO-ITP-MONITOR-MIB", "ciscoItpMonitorCongestion")
)
if mibBuilder.loadTexts:
    ciscoItpmNotificationsGroup.setStatus(
        "deprecated"
    )

ciscoItpmNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 2, 5)
)
ciscoItpmNotificationsGroupRev1.setObjects(
      *(("CISCO-ITP-MONITOR-MIB", "ciscoItpMonitorCongestion"),
        ("CISCO-ITP-MONITOR-MIB", "ciscoItpMonitorState"))
)
if mibBuilder.loadTexts:
    ciscoItpmNotificationsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoItpmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoItpmMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 379, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoItpmMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-MONITOR-MIB",
    **{"ciscoItpmMIB": ciscoItpmMIB,
       "ciscoItpmMIBNotifs": ciscoItpmMIBNotifs,
       "ciscoItpMonitorCongestion": ciscoItpMonitorCongestion,
       "ciscoItpMonitorState": ciscoItpMonitorState,
       "ciscoItpmMIBObjects": ciscoItpmMIBObjects,
       "cItpmConn": cItpmConn,
       "cItpmConnTable": cItpmConnTable,
       "cItpmConnTableEntry": cItpmConnTableEntry,
       "cItpmConnPortNumber": cItpmConnPortNumber,
       "cItpmConnKeepAlive": cItpmConnKeepAlive,
       "cItpmConnMaxQDepth": cItpmConnMaxQDepth,
       "cItpmConnCongOnset": cItpmConnCongOnset,
       "cItpmConnCongAbate": cItpmConnCongAbate,
       "cItpmConnRcvWindowSize": cItpmConnRcvWindowSize,
       "cItpmConnFastStart": cItpmConnFastStart,
       "cItpmConnQueueDepth": cItpmConnQueueDepth,
       "cItpmConnMonitorState": cItpmConnMonitorState,
       "cItpmConnCongestion": cItpmConnCongestion,
       "cItpmConnCongCounts": cItpmConnCongCounts,
       "cItpmLinkTable": cItpmLinkTable,
       "cItpmLinkTableEntry": cItpmLinkTableEntry,
       "cItpmLinkNumber": cItpmLinkNumber,
       "cItpmLinkDescription": cItpmLinkDescription,
       "cItpmLinkSlotNumber": cItpmLinkSlotNumber,
       "cItpmLinkStatus": cItpmLinkStatus,
       "cItpmLinkRcvdMsus": cItpmLinkRcvdMsus,
       "cItpmLinkRcvdMsuDrops": cItpmLinkRcvdMsuDrops,
       "cItpmLinkRcvdMsuRate": cItpmLinkRcvdMsuRate,
       "cItpmLinkRcvdBitsRate": cItpmLinkRcvdBitsRate,
       "cItpmLinkSentMsus": cItpmLinkSentMsus,
       "cItpmLinkSentMsuDrops": cItpmLinkSentMsuDrops,
       "cItpmLinkSentMsuRate": cItpmLinkSentMsuRate,
       "cItpmLinkSentBitsRate": cItpmLinkSentBitsRate,
       "cItpmLink": cItpmLink,
       "cItpmCongestionNotifEnabled": cItpmCongestionNotifEnabled,
       "cItpmMonitorStateNotifEnabled": cItpmMonitorStateNotifEnabled,
       "ciscoItpmMIBConform": ciscoItpmMIBConform,
       "ciscoItpmMIBCompliances": ciscoItpmMIBCompliances,
       "ciscoItpmMIBCompliance": ciscoItpmMIBCompliance,
       "ciscoItpmMIBComplianceRev1": ciscoItpmMIBComplianceRev1,
       "ciscoItpmMIBGroups": ciscoItpmMIBGroups,
       "ciscoItpmConnGroup": ciscoItpmConnGroup,
       "ciscoItpmLinkGroup": ciscoItpmLinkGroup,
       "ciscoItpmNotificationsGroup": ciscoItpmNotificationsGroup,
       "ciscoItpmConnGroupRev1": ciscoItpmConnGroupRev1,
       "ciscoItpmNotificationsGroupRev1": ciscoItpmNotificationsGroupRev1}
)
