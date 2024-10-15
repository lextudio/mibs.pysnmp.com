# SNMP MIB module (DOCS-RPHY-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-RPHY-PTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:05 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(IfDirection,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "IfDirection")

(docsRphyRpdDevInfoUniqueId,) = mibBuilder.importSymbols(
    "DOCS-RPHY-MIB",
    "docsRphyRpdDevInfoUniqueId")

(IANAPhysicalClass,) = mibBuilder.importSymbols(
    "IANA-ENTITY-MIB",
    "IANAPhysicalClass")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber",
    "InetVersion")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(UUIDorZero,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUIDorZero")


# MODULE-IDENTITY

docsRphyPtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32)
)
docsRphyPtpMib.setRevisions(
        ("2017-04-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsRphyPtpNotifications_ObjectIdentity = ObjectIdentity
docsRphyPtpNotifications = _DocsRphyPtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 0)
)
_DocsRphyPtpObjects_ObjectIdentity = ObjectIdentity
docsRphyPtpObjects = _DocsRphyPtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1)
)
_DocsRphyPtpRpdMibObjects_ObjectIdentity = ObjectIdentity
docsRphyPtpRpdMibObjects = _DocsRphyPtpRpdMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1)
)
_DocsRphyPtpRpdCurrentDataSetTable_Object = MibTable
docsRphyPtpRpdCurrentDataSetTable = _DocsRphyPtpRpdCurrentDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetTable.setStatus("current")
_DocsRphyPtpRpdCurrentDataSetEntry_Object = MibTableRow
docsRphyPtpRpdCurrentDataSetEntry = _DocsRphyPtpRpdCurrentDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 1, 1)
)
docsRphyPtpRpdCurrentDataSetEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetEntry.setStatus("current")
_DocsRphyPtpRpdCurrentDataSetStepsRemoved_Type = Unsigned32
_DocsRphyPtpRpdCurrentDataSetStepsRemoved_Object = MibTableColumn
docsRphyPtpRpdCurrentDataSetStepsRemoved = _DocsRphyPtpRpdCurrentDataSetStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 1, 1, 1),
    _DocsRphyPtpRpdCurrentDataSetStepsRemoved_Type()
)
docsRphyPtpRpdCurrentDataSetStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetStepsRemoved.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetStepsRemoved.setUnits("steps")
_DocsRphyPtpRpdCurrentDataSetOffsetFromMaster_Type = Integer32
_DocsRphyPtpRpdCurrentDataSetOffsetFromMaster_Object = MibTableColumn
docsRphyPtpRpdCurrentDataSetOffsetFromMaster = _DocsRphyPtpRpdCurrentDataSetOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 1, 1, 2),
    _DocsRphyPtpRpdCurrentDataSetOffsetFromMaster_Type()
)
docsRphyPtpRpdCurrentDataSetOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetOffsetFromMaster.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetOffsetFromMaster.setUnits("Nanoseconds")
_DocsRphyPtpRpdCurrentDataSetMeanPathDelay_Type = Unsigned32
_DocsRphyPtpRpdCurrentDataSetMeanPathDelay_Object = MibTableColumn
docsRphyPtpRpdCurrentDataSetMeanPathDelay = _DocsRphyPtpRpdCurrentDataSetMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 1, 1, 3),
    _DocsRphyPtpRpdCurrentDataSetMeanPathDelay_Type()
)
docsRphyPtpRpdCurrentDataSetMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdCurrentDataSetMeanPathDelay.setUnits("Nanoseconds")
_DocsRphyPtpRpdClockStatusTable_Object = MibTable
docsRphyPtpRpdClockStatusTable = _DocsRphyPtpRpdClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusTable.setStatus("current")
_DocsRphyPtpRpdClockStatusEntry_Object = MibTableRow
docsRphyPtpRpdClockStatusEntry = _DocsRphyPtpRpdClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1)
)
docsRphyPtpRpdClockStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusEntry.setStatus("current")


class _DocsRphyPtpRpdClockStatusClockState_Type(Integer32):
    """Custom type docsRphyPtpRpdClockStatusClockState based on Integer32"""
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
        *(("acquiring", 3),
          ("freerun", 1),
          ("freqLocked", 4),
          ("holdover", 2),
          ("phaseAligned", 5))
    )


_DocsRphyPtpRpdClockStatusClockState_Type.__name__ = "Integer32"
_DocsRphyPtpRpdClockStatusClockState_Object = MibTableColumn
docsRphyPtpRpdClockStatusClockState = _DocsRphyPtpRpdClockStatusClockState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1, 1),
    _DocsRphyPtpRpdClockStatusClockState_Type()
)
docsRphyPtpRpdClockStatusClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusClockState.setStatus("current")
_DocsRphyPtpRpdClockStatusLastStateChange_Type = TimeTicks
_DocsRphyPtpRpdClockStatusLastStateChange_Object = MibTableColumn
docsRphyPtpRpdClockStatusLastStateChange = _DocsRphyPtpRpdClockStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1, 2),
    _DocsRphyPtpRpdClockStatusLastStateChange_Type()
)
docsRphyPtpRpdClockStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusLastStateChange.setStatus("current")
_DocsRphyPtpRpdClockStatusPacketsSent_Type = Counter64
_DocsRphyPtpRpdClockStatusPacketsSent_Object = MibTableColumn
docsRphyPtpRpdClockStatusPacketsSent = _DocsRphyPtpRpdClockStatusPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1, 3),
    _DocsRphyPtpRpdClockStatusPacketsSent_Type()
)
docsRphyPtpRpdClockStatusPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusPacketsSent.setUnits("Packets")
_DocsRphyPtpRpdClockStatusPacketsReceived_Type = Counter64
_DocsRphyPtpRpdClockStatusPacketsReceived_Object = MibTableColumn
docsRphyPtpRpdClockStatusPacketsReceived = _DocsRphyPtpRpdClockStatusPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1, 4),
    _DocsRphyPtpRpdClockStatusPacketsReceived_Type()
)
docsRphyPtpRpdClockStatusPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusPacketsReceived.setUnits("Packets")
_DocsRphyPtpRpdClockStatusComputedPhaseOffset_Type = Unsigned32
_DocsRphyPtpRpdClockStatusComputedPhaseOffset_Object = MibTableColumn
docsRphyPtpRpdClockStatusComputedPhaseOffset = _DocsRphyPtpRpdClockStatusComputedPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1, 5),
    _DocsRphyPtpRpdClockStatusComputedPhaseOffset_Type()
)
docsRphyPtpRpdClockStatusComputedPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusComputedPhaseOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusComputedPhaseOffset.setUnits("Nanoseconds")
_DocsRphyPtpRpdClockStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyPtpRpdClockStatusCounterDiscontinuityTime_Object = MibTableColumn
docsRphyPtpRpdClockStatusCounterDiscontinuityTime = _DocsRphyPtpRpdClockStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 2, 1, 6),
    _DocsRphyPtpRpdClockStatusCounterDiscontinuityTime_Type()
)
docsRphyPtpRpdClockStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusCounterDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdClockStatusCounterDiscontinuityTime.setUnits("TimeTicks")
_DocsRphyPtpRpdPortDataSetTable_Object = MibTable
docsRphyPtpRpdPortDataSetTable = _DocsRphyPtpRpdPortDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 3)
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortDataSetTable.setStatus("current")
_DocsRphyPtpRpdPortDataSetEntry_Object = MibTableRow
docsRphyPtpRpdPortDataSetEntry = _DocsRphyPtpRpdPortDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 3, 1)
)
docsRphyPtpRpdPortDataSetEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortDataSetPortNumber"),
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortDataSetEntry.setStatus("current")


class _DocsRphyPtpRpdPortDataSetPortNumber_Type(Unsigned32):
    """Custom type docsRphyPtpRpdPortDataSetPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyPtpRpdPortDataSetPortNumber_Type.__name__ = "Unsigned32"
_DocsRphyPtpRpdPortDataSetPortNumber_Object = MibTableColumn
docsRphyPtpRpdPortDataSetPortNumber = _DocsRphyPtpRpdPortDataSetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 3, 1, 1),
    _DocsRphyPtpRpdPortDataSetPortNumber_Type()
)
docsRphyPtpRpdPortDataSetPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortDataSetPortNumber.setStatus("current")


class _DocsRphyPtpRpdPortDataSetPortState_Type(Unsigned32):
    """Custom type docsRphyPtpRpdPortDataSetPortState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpRpdPortDataSetPortState_Type.__name__ = "Unsigned32"
_DocsRphyPtpRpdPortDataSetPortState_Object = MibTableColumn
docsRphyPtpRpdPortDataSetPortState = _DocsRphyPtpRpdPortDataSetPortState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 3, 1, 2),
    _DocsRphyPtpRpdPortDataSetPortState_Type()
)
docsRphyPtpRpdPortDataSetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortDataSetPortState.setStatus("current")
_DocsRphyPtpRpdPortDataSetMeanPathDelay_Type = Integer32
_DocsRphyPtpRpdPortDataSetMeanPathDelay_Object = MibTableColumn
docsRphyPtpRpdPortDataSetMeanPathDelay = _DocsRphyPtpRpdPortDataSetMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 3, 1, 3),
    _DocsRphyPtpRpdPortDataSetMeanPathDelay_Type()
)
docsRphyPtpRpdPortDataSetMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortDataSetMeanPathDelay.setStatus("current")
_DocsRphyPtpRpdPtpPortStatusTable_Object = MibTable
docsRphyPtpRpdPtpPortStatusTable = _DocsRphyPtpRpdPtpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusTable.setStatus("current")
_DocsRphyPtpRpdPtpPortStatusEntry_Object = MibTableRow
docsRphyPtpRpdPtpPortStatusEntry = _DocsRphyPtpRpdPtpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1)
)
docsRphyPtpRpdPtpPortStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusPortNumber"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex"),
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusEntry.setStatus("current")


class _DocsRphyPtpRpdPtpPortStatusPortNumber_Type(Unsigned32):
    """Custom type docsRphyPtpRpdPtpPortStatusPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpRpdPtpPortStatusPortNumber_Type.__name__ = "Unsigned32"
_DocsRphyPtpRpdPtpPortStatusPortNumber_Object = MibTableColumn
docsRphyPtpRpdPtpPortStatusPortNumber = _DocsRphyPtpRpdPtpPortStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1, 1),
    _DocsRphyPtpRpdPtpPortStatusPortNumber_Type()
)
docsRphyPtpRpdPtpPortStatusPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusPortNumber.setStatus("current")


class _DocsRphyPtpRpdPtpPortStatusRpdEnetPortIndex_Type(Unsigned32):
    """Custom type docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpRpdPtpPortStatusRpdEnetPortIndex_Type.__name__ = "Unsigned32"
_DocsRphyPtpRpdPtpPortStatusRpdEnetPortIndex_Object = MibTableColumn
docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex = _DocsRphyPtpRpdPtpPortStatusRpdEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1, 2),
    _DocsRphyPtpRpdPtpPortStatusRpdEnetPortIndex_Type()
)
docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex.setStatus("current")
_DocsRphyPtpRpdPtpPortStatusRpdPtpPortIndex_Type = Unsigned32
_DocsRphyPtpRpdPtpPortStatusRpdPtpPortIndex_Object = MibTableColumn
docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex = _DocsRphyPtpRpdPtpPortStatusRpdPtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1, 3),
    _DocsRphyPtpRpdPtpPortStatusRpdPtpPortIndex_Type()
)
docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex.setStatus("current")
_DocsRphyPtpRpdPtpPortStatusPacketsSent_Type = Counter64
_DocsRphyPtpRpdPtpPortStatusPacketsSent_Object = MibTableColumn
docsRphyPtpRpdPtpPortStatusPacketsSent = _DocsRphyPtpRpdPtpPortStatusPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1, 4),
    _DocsRphyPtpRpdPtpPortStatusPacketsSent_Type()
)
docsRphyPtpRpdPtpPortStatusPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusPacketsSent.setUnits("Packets")
_DocsRphyPtpRpdPtpPortStatusPacketsReceived_Type = Counter64
_DocsRphyPtpRpdPtpPortStatusPacketsReceived_Object = MibTableColumn
docsRphyPtpRpdPtpPortStatusPacketsReceived = _DocsRphyPtpRpdPtpPortStatusPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1, 5),
    _DocsRphyPtpRpdPtpPortStatusPacketsReceived_Type()
)
docsRphyPtpRpdPtpPortStatusPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusPacketsReceived.setUnits("Packets")
_DocsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime_Object = MibTableColumn
docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime = _DocsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 4, 1, 6),
    _DocsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime_Type()
)
docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime.setUnits("TimeTicks")
_DocsRphyPtpRpdPortMasterClockStatusTable_Object = MibTable
docsRphyPtpRpdPortMasterClockStatusTable = _DocsRphyPtpRpdPortMasterClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5)
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusTable.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusEntry_Object = MibTableRow
docsRphyPtpRpdPortMasterClockStatusEntry = _DocsRphyPtpRpdPortMasterClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1)
)
docsRphyPtpRpdPortMasterClockStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusMasterPriority"),
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusEntry.setStatus("current")


class _DocsRphyPtpRpdPortMasterClockStatusMasterPriority_Type(Unsigned32):
    """Custom type docsRphyPtpRpdPortMasterClockStatusMasterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DocsRphyPtpRpdPortMasterClockStatusMasterPriority_Type.__name__ = "Unsigned32"
_DocsRphyPtpRpdPortMasterClockStatusMasterPriority_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusMasterPriority = _DocsRphyPtpRpdPortMasterClockStatusMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 1),
    _DocsRphyPtpRpdPortMasterClockStatusMasterPriority_Type()
)
docsRphyPtpRpdPortMasterClockStatusMasterPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusMasterPriority.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusPacketsSent_Type = Counter64
_DocsRphyPtpRpdPortMasterClockStatusPacketsSent_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusPacketsSent = _DocsRphyPtpRpdPortMasterClockStatusPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 2),
    _DocsRphyPtpRpdPortMasterClockStatusPacketsSent_Type()
)
docsRphyPtpRpdPortMasterClockStatusPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusPacketsSent.setUnits("Packets")
_DocsRphyPtpRpdPortMasterClockStatusPacketsReceived_Type = Counter64
_DocsRphyPtpRpdPortMasterClockStatusPacketsReceived_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusPacketsReceived = _DocsRphyPtpRpdPortMasterClockStatusPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 3),
    _DocsRphyPtpRpdPortMasterClockStatusPacketsReceived_Type()
)
docsRphyPtpRpdPortMasterClockStatusPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusPacketsReceived.setUnits("Packets")


class _DocsRphyPtpRpdPortMasterClockStatusMasterClockId_Type(OctetString):
    """Custom type docsRphyPtpRpdPortMasterClockStatusMasterClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsRphyPtpRpdPortMasterClockStatusMasterClockId_Type.__name__ = "OctetString"
_DocsRphyPtpRpdPortMasterClockStatusMasterClockId_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusMasterClockId = _DocsRphyPtpRpdPortMasterClockStatusMasterClockId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 4),
    _DocsRphyPtpRpdPortMasterClockStatusMasterClockId_Type()
)
docsRphyPtpRpdPortMasterClockStatusMasterClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusMasterClockId.setStatus("current")


class _DocsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber_Type(Unsigned32):
    """Custom type docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber_Type.__name__ = "Unsigned32"
_DocsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber = _DocsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 5),
    _DocsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber_Type()
)
docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusTwoStepFlag_Type = TruthValue
_DocsRphyPtpRpdPortMasterClockStatusTwoStepFlag_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusTwoStepFlag = _DocsRphyPtpRpdPortMasterClockStatusTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 6),
    _DocsRphyPtpRpdPortMasterClockStatusTwoStepFlag_Type()
)
docsRphyPtpRpdPortMasterClockStatusTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusTwoStepFlag.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusIsBmc_Type = TruthValue
_DocsRphyPtpRpdPortMasterClockStatusIsBmc_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusIsBmc = _DocsRphyPtpRpdPortMasterClockStatusIsBmc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 7),
    _DocsRphyPtpRpdPortMasterClockStatusIsBmc_Type()
)
docsRphyPtpRpdPortMasterClockStatusIsBmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusIsBmc.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusIsMasterConnected_Type = TruthValue
_DocsRphyPtpRpdPortMasterClockStatusIsMasterConnected_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusIsMasterConnected = _DocsRphyPtpRpdPortMasterClockStatusIsMasterConnected_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 8),
    _DocsRphyPtpRpdPortMasterClockStatusIsMasterConnected_Type()
)
docsRphyPtpRpdPortMasterClockStatusIsMasterConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusIsMasterConnected.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusStatusDomain_Type = Unsigned32
_DocsRphyPtpRpdPortMasterClockStatusStatusDomain_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusStatusDomain = _DocsRphyPtpRpdPortMasterClockStatusStatusDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 9),
    _DocsRphyPtpRpdPortMasterClockStatusStatusDomain_Type()
)
docsRphyPtpRpdPortMasterClockStatusStatusDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusStatusDomain.setStatus("current")
_DocsRphyPtpRpdPortMasterClockStatusFreqOffset_Type = Unsigned32
_DocsRphyPtpRpdPortMasterClockStatusFreqOffset_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusFreqOffset = _DocsRphyPtpRpdPortMasterClockStatusFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 10),
    _DocsRphyPtpRpdPortMasterClockStatusFreqOffset_Type()
)
docsRphyPtpRpdPortMasterClockStatusFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusFreqOffset.setUnits("PPM")
_DocsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime_Object = MibTableColumn
docsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime = _DocsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 1, 5, 1, 11),
    _DocsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime_Type()
)
docsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime.setStatus("current")
_DocsRphyPtpCcapMibObjects_ObjectIdentity = ObjectIdentity
docsRphyPtpCcapMibObjects = _DocsRphyPtpCcapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2)
)
_DocsRphyPtpCcapDefaultDataSet_ObjectIdentity = ObjectIdentity
docsRphyPtpCcapDefaultDataSet = _DocsRphyPtpCcapDefaultDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1)
)
_DocsRphyPtpCcapDefaultDataSetTwoStepFlag_Type = TruthValue
_DocsRphyPtpCcapDefaultDataSetTwoStepFlag_Object = MibScalar
docsRphyPtpCcapDefaultDataSetTwoStepFlag = _DocsRphyPtpCcapDefaultDataSetTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 1),
    _DocsRphyPtpCcapDefaultDataSetTwoStepFlag_Type()
)
docsRphyPtpCcapDefaultDataSetTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetTwoStepFlag.setStatus("current")


class _DocsRphyPtpCcapDefaultDataSetClockIdentity_Type(OctetString):
    """Custom type docsRphyPtpCcapDefaultDataSetClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsRphyPtpCcapDefaultDataSetClockIdentity_Type.__name__ = "OctetString"
_DocsRphyPtpCcapDefaultDataSetClockIdentity_Object = MibScalar
docsRphyPtpCcapDefaultDataSetClockIdentity = _DocsRphyPtpCcapDefaultDataSetClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 2),
    _DocsRphyPtpCcapDefaultDataSetClockIdentity_Type()
)
docsRphyPtpCcapDefaultDataSetClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetClockIdentity.setStatus("current")
_DocsRphyPtpCcapDefaultDataSetPriority1_Type = Unsigned32
_DocsRphyPtpCcapDefaultDataSetPriority1_Object = MibScalar
docsRphyPtpCcapDefaultDataSetPriority1 = _DocsRphyPtpCcapDefaultDataSetPriority1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 3),
    _DocsRphyPtpCcapDefaultDataSetPriority1_Type()
)
docsRphyPtpCcapDefaultDataSetPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetPriority1.setStatus("current")
_DocsRphyPtpCcapDefaultDataSetPriority2_Type = Unsigned32
_DocsRphyPtpCcapDefaultDataSetPriority2_Object = MibScalar
docsRphyPtpCcapDefaultDataSetPriority2 = _DocsRphyPtpCcapDefaultDataSetPriority2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 4),
    _DocsRphyPtpCcapDefaultDataSetPriority2_Type()
)
docsRphyPtpCcapDefaultDataSetPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetPriority2.setStatus("current")
_DocsRphyPtpCcapDefaultDataSetSlaveOnly_Type = TruthValue
_DocsRphyPtpCcapDefaultDataSetSlaveOnly_Object = MibScalar
docsRphyPtpCcapDefaultDataSetSlaveOnly = _DocsRphyPtpCcapDefaultDataSetSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 5),
    _DocsRphyPtpCcapDefaultDataSetSlaveOnly_Type()
)
docsRphyPtpCcapDefaultDataSetSlaveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetSlaveOnly.setStatus("current")


class _DocsRphyPtpCcapDefaultDataSetQualityClass_Type(Unsigned32):
    """Custom type docsRphyPtpCcapDefaultDataSetQualityClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpCcapDefaultDataSetQualityClass_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapDefaultDataSetQualityClass_Object = MibScalar
docsRphyPtpCcapDefaultDataSetQualityClass = _DocsRphyPtpCcapDefaultDataSetQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 6),
    _DocsRphyPtpCcapDefaultDataSetQualityClass_Type()
)
docsRphyPtpCcapDefaultDataSetQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetQualityClass.setStatus("current")
_DocsRphyPtpCcapDefaultDataSetQualityAccuracy_Type = Unsigned32
_DocsRphyPtpCcapDefaultDataSetQualityAccuracy_Object = MibScalar
docsRphyPtpCcapDefaultDataSetQualityAccuracy = _DocsRphyPtpCcapDefaultDataSetQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 7),
    _DocsRphyPtpCcapDefaultDataSetQualityAccuracy_Type()
)
docsRphyPtpCcapDefaultDataSetQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetQualityAccuracy.setStatus("current")


class _DocsRphyPtpCcapDefaultDataSetQualityOffset_Type(Unsigned32):
    """Custom type docsRphyPtpCcapDefaultDataSetQualityOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyPtpCcapDefaultDataSetQualityOffset_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapDefaultDataSetQualityOffset_Object = MibScalar
docsRphyPtpCcapDefaultDataSetQualityOffset = _DocsRphyPtpCcapDefaultDataSetQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 1, 8),
    _DocsRphyPtpCcapDefaultDataSetQualityOffset_Type()
)
docsRphyPtpCcapDefaultDataSetQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapDefaultDataSetQualityOffset.setStatus("current")
_DocsRphyPtpCcapCurrentDataSet_ObjectIdentity = ObjectIdentity
docsRphyPtpCcapCurrentDataSet = _DocsRphyPtpCcapCurrentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 2)
)
_DocsRphyPtpCcapCurrentDataSetStepsRemoved_Type = Unsigned32
_DocsRphyPtpCcapCurrentDataSetStepsRemoved_Object = MibScalar
docsRphyPtpCcapCurrentDataSetStepsRemoved = _DocsRphyPtpCcapCurrentDataSetStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 2, 1),
    _DocsRphyPtpCcapCurrentDataSetStepsRemoved_Type()
)
docsRphyPtpCcapCurrentDataSetStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCurrentDataSetStepsRemoved.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCurrentDataSetStepsRemoved.setUnits("steps")
_DocsRphyPtpCcapCurrentDataSetOffsetFromMaster_Type = Integer32
_DocsRphyPtpCcapCurrentDataSetOffsetFromMaster_Object = MibScalar
docsRphyPtpCcapCurrentDataSetOffsetFromMaster = _DocsRphyPtpCcapCurrentDataSetOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 2, 2),
    _DocsRphyPtpCcapCurrentDataSetOffsetFromMaster_Type()
)
docsRphyPtpCcapCurrentDataSetOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCurrentDataSetOffsetFromMaster.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCurrentDataSetOffsetFromMaster.setUnits("Nanoseconds")
_DocsRphyPtpCcapCurrentDataSetMeanPathDelay_Type = Unsigned32
_DocsRphyPtpCcapCurrentDataSetMeanPathDelay_Object = MibScalar
docsRphyPtpCcapCurrentDataSetMeanPathDelay = _DocsRphyPtpCcapCurrentDataSetMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 2, 3),
    _DocsRphyPtpCcapCurrentDataSetMeanPathDelay_Type()
)
docsRphyPtpCcapCurrentDataSetMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCurrentDataSetMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCurrentDataSetMeanPathDelay.setUnits("Nanoseconds")
_DocsRphyPtpCcapParentDataSet_ObjectIdentity = ObjectIdentity
docsRphyPtpCcapParentDataSet = _DocsRphyPtpCcapParentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3)
)


class _DocsRphyPtpCcapParentDataSetParentClockId_Type(OctetString):
    """Custom type docsRphyPtpCcapParentDataSetParentClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsRphyPtpCcapParentDataSetParentClockId_Type.__name__ = "OctetString"
_DocsRphyPtpCcapParentDataSetParentClockId_Object = MibScalar
docsRphyPtpCcapParentDataSetParentClockId = _DocsRphyPtpCcapParentDataSetParentClockId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 1),
    _DocsRphyPtpCcapParentDataSetParentClockId_Type()
)
docsRphyPtpCcapParentDataSetParentClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetParentClockId.setStatus("current")
_DocsRphyPtpCcapParentDataSetParentPortNumber_Type = Unsigned32
_DocsRphyPtpCcapParentDataSetParentPortNumber_Object = MibScalar
docsRphyPtpCcapParentDataSetParentPortNumber = _DocsRphyPtpCcapParentDataSetParentPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 2),
    _DocsRphyPtpCcapParentDataSetParentPortNumber_Type()
)
docsRphyPtpCcapParentDataSetParentPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetParentPortNumber.setStatus("current")
_DocsRphyPtpCcapParentDataSetParentStats_Type = TruthValue
_DocsRphyPtpCcapParentDataSetParentStats_Object = MibScalar
docsRphyPtpCcapParentDataSetParentStats = _DocsRphyPtpCcapParentDataSetParentStats_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 3),
    _DocsRphyPtpCcapParentDataSetParentStats_Type()
)
docsRphyPtpCcapParentDataSetParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetParentStats.setStatus("current")
_DocsRphyPtpCcapParentDataSetClockOffset_Type = Integer32
_DocsRphyPtpCcapParentDataSetClockOffset_Object = MibScalar
docsRphyPtpCcapParentDataSetClockOffset = _DocsRphyPtpCcapParentDataSetClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 4),
    _DocsRphyPtpCcapParentDataSetClockOffset_Type()
)
docsRphyPtpCcapParentDataSetClockOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetClockOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetClockOffset.setUnits("Nanoseconds")
_DocsRphyPtpCcapParentDataSetPhaseChangeRate_Type = Integer32
_DocsRphyPtpCcapParentDataSetPhaseChangeRate_Object = MibScalar
docsRphyPtpCcapParentDataSetPhaseChangeRate = _DocsRphyPtpCcapParentDataSetPhaseChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 5),
    _DocsRphyPtpCcapParentDataSetPhaseChangeRate_Type()
)
docsRphyPtpCcapParentDataSetPhaseChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetPhaseChangeRate.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetPhaseChangeRate.setUnits("Nanoseconds")


class _DocsRphyPtpCcapParentDataSetGmClockIdentity_Type(OctetString):
    """Custom type docsRphyPtpCcapParentDataSetGmClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsRphyPtpCcapParentDataSetGmClockIdentity_Type.__name__ = "OctetString"
_DocsRphyPtpCcapParentDataSetGmClockIdentity_Object = MibScalar
docsRphyPtpCcapParentDataSetGmClockIdentity = _DocsRphyPtpCcapParentDataSetGmClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 6),
    _DocsRphyPtpCcapParentDataSetGmClockIdentity_Type()
)
docsRphyPtpCcapParentDataSetGmClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetGmClockIdentity.setStatus("current")
_DocsRphyPtpCcapParentDataSetGmPriority1_Type = Unsigned32
_DocsRphyPtpCcapParentDataSetGmPriority1_Object = MibScalar
docsRphyPtpCcapParentDataSetGmPriority1 = _DocsRphyPtpCcapParentDataSetGmPriority1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 7),
    _DocsRphyPtpCcapParentDataSetGmPriority1_Type()
)
docsRphyPtpCcapParentDataSetGmPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetGmPriority1.setStatus("current")
_DocsRphyPtpCcapParentDataSetGmPriority2_Type = Unsigned32
_DocsRphyPtpCcapParentDataSetGmPriority2_Object = MibScalar
docsRphyPtpCcapParentDataSetGmPriority2 = _DocsRphyPtpCcapParentDataSetGmPriority2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 8),
    _DocsRphyPtpCcapParentDataSetGmPriority2_Type()
)
docsRphyPtpCcapParentDataSetGmPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetGmPriority2.setStatus("current")
_DocsRphyPtpCcapParentDataSetGmQualityClass_Type = Unsigned32
_DocsRphyPtpCcapParentDataSetGmQualityClass_Object = MibScalar
docsRphyPtpCcapParentDataSetGmQualityClass = _DocsRphyPtpCcapParentDataSetGmQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 9),
    _DocsRphyPtpCcapParentDataSetGmQualityClass_Type()
)
docsRphyPtpCcapParentDataSetGmQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetGmQualityClass.setStatus("current")
_DocsRphyPtpCcapParentDataSetGmQualityAccuracy_Type = Unsigned32
_DocsRphyPtpCcapParentDataSetGmQualityAccuracy_Object = MibScalar
docsRphyPtpCcapParentDataSetGmQualityAccuracy = _DocsRphyPtpCcapParentDataSetGmQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 10),
    _DocsRphyPtpCcapParentDataSetGmQualityAccuracy_Type()
)
docsRphyPtpCcapParentDataSetGmQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetGmQualityAccuracy.setStatus("current")
_DocsRphyPtpCcapParentDataSetGmQualityOffset_Type = Unsigned32
_DocsRphyPtpCcapParentDataSetGmQualityOffset_Object = MibScalar
docsRphyPtpCcapParentDataSetGmQualityOffset = _DocsRphyPtpCcapParentDataSetGmQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 3, 11),
    _DocsRphyPtpCcapParentDataSetGmQualityOffset_Type()
)
docsRphyPtpCcapParentDataSetGmQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapParentDataSetGmQualityOffset.setStatus("current")
_DocsRphyPtpCcapTimeProperties_ObjectIdentity = ObjectIdentity
docsRphyPtpCcapTimeProperties = _DocsRphyPtpCcapTimeProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4)
)
_DocsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid_Type = TruthValue
_DocsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid_Object = MibScalar
docsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid = _DocsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 1),
    _DocsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid_Type()
)
docsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid.setStatus("current")
_DocsRphyPtpCcapTimePropertiesCurrentUtcOffset_Type = Integer32
_DocsRphyPtpCcapTimePropertiesCurrentUtcOffset_Object = MibScalar
docsRphyPtpCcapTimePropertiesCurrentUtcOffset = _DocsRphyPtpCcapTimePropertiesCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 2),
    _DocsRphyPtpCcapTimePropertiesCurrentUtcOffset_Type()
)
docsRphyPtpCcapTimePropertiesCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesCurrentUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesCurrentUtcOffset.setUnits("Seconds")
_DocsRphyPtpCcapTimePropertiesLeap59_Type = TruthValue
_DocsRphyPtpCcapTimePropertiesLeap59_Object = MibScalar
docsRphyPtpCcapTimePropertiesLeap59 = _DocsRphyPtpCcapTimePropertiesLeap59_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 3),
    _DocsRphyPtpCcapTimePropertiesLeap59_Type()
)
docsRphyPtpCcapTimePropertiesLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesLeap59.setStatus("current")
_DocsRphyPtpCcapTimePropertiesLeap61_Type = TruthValue
_DocsRphyPtpCcapTimePropertiesLeap61_Object = MibScalar
docsRphyPtpCcapTimePropertiesLeap61 = _DocsRphyPtpCcapTimePropertiesLeap61_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 4),
    _DocsRphyPtpCcapTimePropertiesLeap61_Type()
)
docsRphyPtpCcapTimePropertiesLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesLeap61.setStatus("current")
_DocsRphyPtpCcapTimePropertiesTimeTraceable_Type = TruthValue
_DocsRphyPtpCcapTimePropertiesTimeTraceable_Object = MibScalar
docsRphyPtpCcapTimePropertiesTimeTraceable = _DocsRphyPtpCcapTimePropertiesTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 5),
    _DocsRphyPtpCcapTimePropertiesTimeTraceable_Type()
)
docsRphyPtpCcapTimePropertiesTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesTimeTraceable.setStatus("current")


class _DocsRphyPtpCcapTimePropertiesFreqTraceable_Type(TruthValue):
    """Custom type docsRphyPtpCcapTimePropertiesFreqTraceable based on TruthValue"""


_DocsRphyPtpCcapTimePropertiesFreqTraceable_Object = MibScalar
docsRphyPtpCcapTimePropertiesFreqTraceable = _DocsRphyPtpCcapTimePropertiesFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 6),
    _DocsRphyPtpCcapTimePropertiesFreqTraceable_Type()
)
docsRphyPtpCcapTimePropertiesFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesFreqTraceable.setStatus("current")
_DocsRphyPtpCcapTimePropertiesPtpTimescale_Type = TruthValue
_DocsRphyPtpCcapTimePropertiesPtpTimescale_Object = MibScalar
docsRphyPtpCcapTimePropertiesPtpTimescale = _DocsRphyPtpCcapTimePropertiesPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 7),
    _DocsRphyPtpCcapTimePropertiesPtpTimescale_Type()
)
docsRphyPtpCcapTimePropertiesPtpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesPtpTimescale.setStatus("current")


class _DocsRphyPtpCcapTimePropertiesTimeSource_Type(Unsigned32):
    """Custom type docsRphyPtpCcapTimePropertiesTimeSource based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpCcapTimePropertiesTimeSource_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapTimePropertiesTimeSource_Object = MibScalar
docsRphyPtpCcapTimePropertiesTimeSource = _DocsRphyPtpCcapTimePropertiesTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 4, 8),
    _DocsRphyPtpCcapTimePropertiesTimeSource_Type()
)
docsRphyPtpCcapTimePropertiesTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapTimePropertiesTimeSource.setStatus("current")
_DocsRphyPtpCcapPortDataSetTable_Object = MibTable
docsRphyPtpCcapPortDataSetTable = _DocsRphyPtpCcapPortDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 5)
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortDataSetTable.setStatus("current")
_DocsRphyPtpCcapPortDataSetEntry_Object = MibTableRow
docsRphyPtpCcapPortDataSetEntry = _DocsRphyPtpCcapPortDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 5, 1)
)
docsRphyPtpCcapPortDataSetEntry.setIndexNames(
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortDataSetPortNumber"),
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortDataSetEntry.setStatus("current")


class _DocsRphyPtpCcapPortDataSetPortNumber_Type(Unsigned32):
    """Custom type docsRphyPtpCcapPortDataSetPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyPtpCcapPortDataSetPortNumber_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapPortDataSetPortNumber_Object = MibTableColumn
docsRphyPtpCcapPortDataSetPortNumber = _DocsRphyPtpCcapPortDataSetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 5, 1, 1),
    _DocsRphyPtpCcapPortDataSetPortNumber_Type()
)
docsRphyPtpCcapPortDataSetPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortDataSetPortNumber.setStatus("current")


class _DocsRphyPtpCcapPortDataSetPortState_Type(Unsigned32):
    """Custom type docsRphyPtpCcapPortDataSetPortState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpCcapPortDataSetPortState_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapPortDataSetPortState_Object = MibTableColumn
docsRphyPtpCcapPortDataSetPortState = _DocsRphyPtpCcapPortDataSetPortState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 5, 1, 2),
    _DocsRphyPtpCcapPortDataSetPortState_Type()
)
docsRphyPtpCcapPortDataSetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortDataSetPortState.setStatus("current")
_DocsRphyPtpCcapPortDataSetMeanPathDelay_Type = Integer32
_DocsRphyPtpCcapPortDataSetMeanPathDelay_Object = MibTableColumn
docsRphyPtpCcapPortDataSetMeanPathDelay = _DocsRphyPtpCcapPortDataSetMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 5, 1, 3),
    _DocsRphyPtpCcapPortDataSetMeanPathDelay_Type()
)
docsRphyPtpCcapPortDataSetMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortDataSetMeanPathDelay.setStatus("current")
_DocsRphyPtpCcapClockStatus_ObjectIdentity = ObjectIdentity
docsRphyPtpCcapClockStatus = _DocsRphyPtpCcapClockStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6)
)


class _DocsRphyPtpCcapClockStatusClockState_Type(Integer32):
    """Custom type docsRphyPtpCcapClockStatusClockState based on Integer32"""
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
        *(("acquiring", 3),
          ("freerun", 1),
          ("freqLocked", 4),
          ("holdover", 2),
          ("phaseAligned", 5))
    )


_DocsRphyPtpCcapClockStatusClockState_Type.__name__ = "Integer32"
_DocsRphyPtpCcapClockStatusClockState_Object = MibScalar
docsRphyPtpCcapClockStatusClockState = _DocsRphyPtpCcapClockStatusClockState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6, 1),
    _DocsRphyPtpCcapClockStatusClockState_Type()
)
docsRphyPtpCcapClockStatusClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusClockState.setStatus("current")
_DocsRphyPtpCcapClockStatusLastStateChange_Type = TimeTicks
_DocsRphyPtpCcapClockStatusLastStateChange_Object = MibScalar
docsRphyPtpCcapClockStatusLastStateChange = _DocsRphyPtpCcapClockStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6, 2),
    _DocsRphyPtpCcapClockStatusLastStateChange_Type()
)
docsRphyPtpCcapClockStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusLastStateChange.setStatus("current")
_DocsRphyPtpCcapClockStatusPacketsSent_Type = Counter64
_DocsRphyPtpCcapClockStatusPacketsSent_Object = MibScalar
docsRphyPtpCcapClockStatusPacketsSent = _DocsRphyPtpCcapClockStatusPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6, 3),
    _DocsRphyPtpCcapClockStatusPacketsSent_Type()
)
docsRphyPtpCcapClockStatusPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusPacketsSent.setUnits("Packets")
_DocsRphyPtpCcapClockStatusPacketsReceived_Type = Counter64
_DocsRphyPtpCcapClockStatusPacketsReceived_Object = MibScalar
docsRphyPtpCcapClockStatusPacketsReceived = _DocsRphyPtpCcapClockStatusPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6, 4),
    _DocsRphyPtpCcapClockStatusPacketsReceived_Type()
)
docsRphyPtpCcapClockStatusPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusPacketsReceived.setUnits("Packets")
_DocsRphyPtpCcapClockStatusComputedPhaseOffset_Type = Unsigned32
_DocsRphyPtpCcapClockStatusComputedPhaseOffset_Object = MibScalar
docsRphyPtpCcapClockStatusComputedPhaseOffset = _DocsRphyPtpCcapClockStatusComputedPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6, 5),
    _DocsRphyPtpCcapClockStatusComputedPhaseOffset_Type()
)
docsRphyPtpCcapClockStatusComputedPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusComputedPhaseOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusComputedPhaseOffset.setUnits("Nanoseconds")
_DocsRphyPtpCcapClockStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyPtpCcapClockStatusCounterDiscontinuityTime_Object = MibScalar
docsRphyPtpCcapClockStatusCounterDiscontinuityTime = _DocsRphyPtpCcapClockStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 6, 6),
    _DocsRphyPtpCcapClockStatusCounterDiscontinuityTime_Type()
)
docsRphyPtpCcapClockStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusCounterDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapClockStatusCounterDiscontinuityTime.setUnits("TimeTicks")
_DocsRphyPtpCcapCorePtpPortStatusTable_Object = MibTable
docsRphyPtpCcapCorePtpPortStatusTable = _DocsRphyPtpCcapCorePtpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 7)
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusTable.setStatus("current")
_DocsRphyPtpCcapCorePtpPortStatusEntry_Object = MibTableRow
docsRphyPtpCcapCorePtpPortStatusEntry = _DocsRphyPtpCcapCorePtpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 7, 1)
)
docsRphyPtpCcapCorePtpPortStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCorePtpPortStatusPortNumber"),
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusEntry.setStatus("current")


class _DocsRphyPtpCcapCorePtpPortStatusPortNumber_Type(Unsigned32):
    """Custom type docsRphyPtpCcapCorePtpPortStatusPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyPtpCcapCorePtpPortStatusPortNumber_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapCorePtpPortStatusPortNumber_Object = MibTableColumn
docsRphyPtpCcapCorePtpPortStatusPortNumber = _DocsRphyPtpCcapCorePtpPortStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 7, 1, 1),
    _DocsRphyPtpCcapCorePtpPortStatusPortNumber_Type()
)
docsRphyPtpCcapCorePtpPortStatusPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusPortNumber.setStatus("current")
_DocsRphyPtpCcapCorePtpPortStatusPacketsSent_Type = Counter64
_DocsRphyPtpCcapCorePtpPortStatusPacketsSent_Object = MibTableColumn
docsRphyPtpCcapCorePtpPortStatusPacketsSent = _DocsRphyPtpCcapCorePtpPortStatusPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 7, 1, 2),
    _DocsRphyPtpCcapCorePtpPortStatusPacketsSent_Type()
)
docsRphyPtpCcapCorePtpPortStatusPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusPacketsSent.setUnits("Packets")
_DocsRphyPtpCcapCorePtpPortStatusPacketsReceived_Type = Counter64
_DocsRphyPtpCcapCorePtpPortStatusPacketsReceived_Object = MibTableColumn
docsRphyPtpCcapCorePtpPortStatusPacketsReceived = _DocsRphyPtpCcapCorePtpPortStatusPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 7, 1, 3),
    _DocsRphyPtpCcapCorePtpPortStatusPacketsReceived_Type()
)
docsRphyPtpCcapCorePtpPortStatusPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusPacketsReceived.setUnits("Packets")
_DocsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime_Object = MibTableColumn
docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime = _DocsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 7, 1, 4),
    _DocsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime_Type()
)
docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime.setUnits("TimeTicks")
_DocsRphyPtpCcapPortMasterClockStatusTable_Object = MibTable
docsRphyPtpCcapPortMasterClockStatusTable = _DocsRphyPtpCcapPortMasterClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8)
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusTable.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusEntry_Object = MibTableRow
docsRphyPtpCcapPortMasterClockStatusEntry = _DocsRphyPtpCcapPortMasterClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1)
)
docsRphyPtpCcapPortMasterClockStatusEntry.setIndexNames(
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCorePtpPortStatusPortNumber"),
    (0, "DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusMasterPriority"),
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusEntry.setStatus("current")


class _DocsRphyPtpCcapPortMasterClockStatusMasterPriority_Type(Unsigned32):
    """Custom type docsRphyPtpCcapPortMasterClockStatusMasterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DocsRphyPtpCcapPortMasterClockStatusMasterPriority_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapPortMasterClockStatusMasterPriority_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusMasterPriority = _DocsRphyPtpCcapPortMasterClockStatusMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 1),
    _DocsRphyPtpCcapPortMasterClockStatusMasterPriority_Type()
)
docsRphyPtpCcapPortMasterClockStatusMasterPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusMasterPriority.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusPacketsSent_Type = Counter64
_DocsRphyPtpCcapPortMasterClockStatusPacketsSent_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusPacketsSent = _DocsRphyPtpCcapPortMasterClockStatusPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 2),
    _DocsRphyPtpCcapPortMasterClockStatusPacketsSent_Type()
)
docsRphyPtpCcapPortMasterClockStatusPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusPacketsSent.setUnits("Packets")
_DocsRphyPtpCcapPortMasterClockStatusPacketsReceived_Type = Counter64
_DocsRphyPtpCcapPortMasterClockStatusPacketsReceived_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusPacketsReceived = _DocsRphyPtpCcapPortMasterClockStatusPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 3),
    _DocsRphyPtpCcapPortMasterClockStatusPacketsReceived_Type()
)
docsRphyPtpCcapPortMasterClockStatusPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusPacketsReceived.setUnits("Packets")


class _DocsRphyPtpCcapPortMasterClockStatusMasterClockId_Type(OctetString):
    """Custom type docsRphyPtpCcapPortMasterClockStatusMasterClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsRphyPtpCcapPortMasterClockStatusMasterClockId_Type.__name__ = "OctetString"
_DocsRphyPtpCcapPortMasterClockStatusMasterClockId_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusMasterClockId = _DocsRphyPtpCcapPortMasterClockStatusMasterClockId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 4),
    _DocsRphyPtpCcapPortMasterClockStatusMasterClockId_Type()
)
docsRphyPtpCcapPortMasterClockStatusMasterClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusMasterClockId.setStatus("current")


class _DocsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber_Type(Unsigned32):
    """Custom type docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber_Type.__name__ = "Unsigned32"
_DocsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber = _DocsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 5),
    _DocsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber_Type()
)
docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusTwoStepFlag_Type = TruthValue
_DocsRphyPtpCcapPortMasterClockStatusTwoStepFlag_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusTwoStepFlag = _DocsRphyPtpCcapPortMasterClockStatusTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 6),
    _DocsRphyPtpCcapPortMasterClockStatusTwoStepFlag_Type()
)
docsRphyPtpCcapPortMasterClockStatusTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusTwoStepFlag.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusIsBmc_Type = TruthValue
_DocsRphyPtpCcapPortMasterClockStatusIsBmc_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusIsBmc = _DocsRphyPtpCcapPortMasterClockStatusIsBmc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 7),
    _DocsRphyPtpCcapPortMasterClockStatusIsBmc_Type()
)
docsRphyPtpCcapPortMasterClockStatusIsBmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusIsBmc.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusIsMasterConnected_Type = TruthValue
_DocsRphyPtpCcapPortMasterClockStatusIsMasterConnected_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusIsMasterConnected = _DocsRphyPtpCcapPortMasterClockStatusIsMasterConnected_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 8),
    _DocsRphyPtpCcapPortMasterClockStatusIsMasterConnected_Type()
)
docsRphyPtpCcapPortMasterClockStatusIsMasterConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusIsMasterConnected.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusStatusDomain_Type = Unsigned32
_DocsRphyPtpCcapPortMasterClockStatusStatusDomain_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusStatusDomain = _DocsRphyPtpCcapPortMasterClockStatusStatusDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 9),
    _DocsRphyPtpCcapPortMasterClockStatusStatusDomain_Type()
)
docsRphyPtpCcapPortMasterClockStatusStatusDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusStatusDomain.setStatus("current")
_DocsRphyPtpCcapPortMasterClockStatusFreqOffset_Type = Unsigned32
_DocsRphyPtpCcapPortMasterClockStatusFreqOffset_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusFreqOffset = _DocsRphyPtpCcapPortMasterClockStatusFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 10),
    _DocsRphyPtpCcapPortMasterClockStatusFreqOffset_Type()
)
docsRphyPtpCcapPortMasterClockStatusFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusFreqOffset.setUnits("PPM")
_DocsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime_Type = TimeStamp
_DocsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime_Object = MibTableColumn
docsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime = _DocsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 1, 2, 8, 1, 11),
    _DocsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime_Type()
)
docsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime.setStatus("current")
_DocsRphyPtpConformance_ObjectIdentity = ObjectIdentity
docsRphyPtpConformance = _DocsRphyPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 2)
)
_DocsRphyPtpCompliances_ObjectIdentity = ObjectIdentity
docsRphyPtpCompliances = _DocsRphyPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 2, 1)
)
_DocsRphyPtpGroups_ObjectIdentity = ObjectIdentity
docsRphyPtpGroups = _DocsRphyPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 2, 2)
)

# Managed Objects groups

docsRphyPtpRpdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 2, 2, 1)
)
docsRphyPtpRpdGroup.setObjects(
      *(("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdCurrentDataSetStepsRemoved"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdCurrentDataSetOffsetFromMaster"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdCurrentDataSetMeanPathDelay"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdClockStatusClockState"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdClockStatusLastStateChange"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdClockStatusPacketsSent"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdClockStatusPacketsReceived"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdClockStatusComputedPhaseOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdClockStatusCounterDiscontinuityTime"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortDataSetPortState"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortDataSetMeanPathDelay"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusPacketsSent"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusPacketsReceived"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusPacketsSent"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusPacketsReceived"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusMasterClockId"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusTwoStepFlag"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusIsBmc"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusIsMasterConnected"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusStatusDomain"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusFreqOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    docsRphyPtpRpdGroup.setStatus("current")

docsRphyPtpCcapCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 2, 2, 2)
)
docsRphyPtpCcapCoreGroup.setObjects(
      *(("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetTwoStepFlag"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetClockIdentity"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetPriority1"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetPriority2"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetSlaveOnly"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetQualityClass"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetQualityAccuracy"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapDefaultDataSetQualityOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCurrentDataSetStepsRemoved"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCurrentDataSetOffsetFromMaster"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCurrentDataSetMeanPathDelay"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetParentClockId"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetParentPortNumber"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetParentStats"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetClockOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetPhaseChangeRate"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetGmClockIdentity"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetGmPriority1"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetGmPriority2"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetGmQualityClass"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetGmQualityAccuracy"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapParentDataSetGmQualityOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesCurrentUtcOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesLeap59"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesLeap61"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesTimeTraceable"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesFreqTraceable"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesPtpTimescale"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapTimePropertiesTimeSource"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortDataSetPortState"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortDataSetMeanPathDelay"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapClockStatusClockState"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapClockStatusLastStateChange"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapClockStatusPacketsSent"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapClockStatusPacketsReceived"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapClockStatusComputedPhaseOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapClockStatusCounterDiscontinuityTime"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCorePtpPortStatusPacketsSent"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCorePtpPortStatusPacketsReceived"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusPacketsSent"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusPacketsReceived"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusMasterClockId"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusTwoStepFlag"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusIsBmc"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusIsMasterConnected"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusStatusDomain"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusFreqOffset"),
        ("DOCS-RPHY-PTP-MIB", "docsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    docsRphyPtpCcapCoreGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsRphyPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsRphyPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-RPHY-PTP-MIB",
    **{"docsRphyPtpMib": docsRphyPtpMib,
       "docsRphyPtpNotifications": docsRphyPtpNotifications,
       "docsRphyPtpObjects": docsRphyPtpObjects,
       "docsRphyPtpRpdMibObjects": docsRphyPtpRpdMibObjects,
       "docsRphyPtpRpdCurrentDataSetTable": docsRphyPtpRpdCurrentDataSetTable,
       "docsRphyPtpRpdCurrentDataSetEntry": docsRphyPtpRpdCurrentDataSetEntry,
       "docsRphyPtpRpdCurrentDataSetStepsRemoved": docsRphyPtpRpdCurrentDataSetStepsRemoved,
       "docsRphyPtpRpdCurrentDataSetOffsetFromMaster": docsRphyPtpRpdCurrentDataSetOffsetFromMaster,
       "docsRphyPtpRpdCurrentDataSetMeanPathDelay": docsRphyPtpRpdCurrentDataSetMeanPathDelay,
       "docsRphyPtpRpdClockStatusTable": docsRphyPtpRpdClockStatusTable,
       "docsRphyPtpRpdClockStatusEntry": docsRphyPtpRpdClockStatusEntry,
       "docsRphyPtpRpdClockStatusClockState": docsRphyPtpRpdClockStatusClockState,
       "docsRphyPtpRpdClockStatusLastStateChange": docsRphyPtpRpdClockStatusLastStateChange,
       "docsRphyPtpRpdClockStatusPacketsSent": docsRphyPtpRpdClockStatusPacketsSent,
       "docsRphyPtpRpdClockStatusPacketsReceived": docsRphyPtpRpdClockStatusPacketsReceived,
       "docsRphyPtpRpdClockStatusComputedPhaseOffset": docsRphyPtpRpdClockStatusComputedPhaseOffset,
       "docsRphyPtpRpdClockStatusCounterDiscontinuityTime": docsRphyPtpRpdClockStatusCounterDiscontinuityTime,
       "docsRphyPtpRpdPortDataSetTable": docsRphyPtpRpdPortDataSetTable,
       "docsRphyPtpRpdPortDataSetEntry": docsRphyPtpRpdPortDataSetEntry,
       "docsRphyPtpRpdPortDataSetPortNumber": docsRphyPtpRpdPortDataSetPortNumber,
       "docsRphyPtpRpdPortDataSetPortState": docsRphyPtpRpdPortDataSetPortState,
       "docsRphyPtpRpdPortDataSetMeanPathDelay": docsRphyPtpRpdPortDataSetMeanPathDelay,
       "docsRphyPtpRpdPtpPortStatusTable": docsRphyPtpRpdPtpPortStatusTable,
       "docsRphyPtpRpdPtpPortStatusEntry": docsRphyPtpRpdPtpPortStatusEntry,
       "docsRphyPtpRpdPtpPortStatusPortNumber": docsRphyPtpRpdPtpPortStatusPortNumber,
       "docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex": docsRphyPtpRpdPtpPortStatusRpdEnetPortIndex,
       "docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex": docsRphyPtpRpdPtpPortStatusRpdPtpPortIndex,
       "docsRphyPtpRpdPtpPortStatusPacketsSent": docsRphyPtpRpdPtpPortStatusPacketsSent,
       "docsRphyPtpRpdPtpPortStatusPacketsReceived": docsRphyPtpRpdPtpPortStatusPacketsReceived,
       "docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime": docsRphyPtpRpdPtpPortStatusCounterDiscontinuityTime,
       "docsRphyPtpRpdPortMasterClockStatusTable": docsRphyPtpRpdPortMasterClockStatusTable,
       "docsRphyPtpRpdPortMasterClockStatusEntry": docsRphyPtpRpdPortMasterClockStatusEntry,
       "docsRphyPtpRpdPortMasterClockStatusMasterPriority": docsRphyPtpRpdPortMasterClockStatusMasterPriority,
       "docsRphyPtpRpdPortMasterClockStatusPacketsSent": docsRphyPtpRpdPortMasterClockStatusPacketsSent,
       "docsRphyPtpRpdPortMasterClockStatusPacketsReceived": docsRphyPtpRpdPortMasterClockStatusPacketsReceived,
       "docsRphyPtpRpdPortMasterClockStatusMasterClockId": docsRphyPtpRpdPortMasterClockStatusMasterClockId,
       "docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber": docsRphyPtpRpdPortMasterClockStatusMasterClockPortNumber,
       "docsRphyPtpRpdPortMasterClockStatusTwoStepFlag": docsRphyPtpRpdPortMasterClockStatusTwoStepFlag,
       "docsRphyPtpRpdPortMasterClockStatusIsBmc": docsRphyPtpRpdPortMasterClockStatusIsBmc,
       "docsRphyPtpRpdPortMasterClockStatusIsMasterConnected": docsRphyPtpRpdPortMasterClockStatusIsMasterConnected,
       "docsRphyPtpRpdPortMasterClockStatusStatusDomain": docsRphyPtpRpdPortMasterClockStatusStatusDomain,
       "docsRphyPtpRpdPortMasterClockStatusFreqOffset": docsRphyPtpRpdPortMasterClockStatusFreqOffset,
       "docsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime": docsRphyPtpRpdPortMasterClockStatusCounterDiscontinuityTime,
       "docsRphyPtpCcapMibObjects": docsRphyPtpCcapMibObjects,
       "docsRphyPtpCcapDefaultDataSet": docsRphyPtpCcapDefaultDataSet,
       "docsRphyPtpCcapDefaultDataSetTwoStepFlag": docsRphyPtpCcapDefaultDataSetTwoStepFlag,
       "docsRphyPtpCcapDefaultDataSetClockIdentity": docsRphyPtpCcapDefaultDataSetClockIdentity,
       "docsRphyPtpCcapDefaultDataSetPriority1": docsRphyPtpCcapDefaultDataSetPriority1,
       "docsRphyPtpCcapDefaultDataSetPriority2": docsRphyPtpCcapDefaultDataSetPriority2,
       "docsRphyPtpCcapDefaultDataSetSlaveOnly": docsRphyPtpCcapDefaultDataSetSlaveOnly,
       "docsRphyPtpCcapDefaultDataSetQualityClass": docsRphyPtpCcapDefaultDataSetQualityClass,
       "docsRphyPtpCcapDefaultDataSetQualityAccuracy": docsRphyPtpCcapDefaultDataSetQualityAccuracy,
       "docsRphyPtpCcapDefaultDataSetQualityOffset": docsRphyPtpCcapDefaultDataSetQualityOffset,
       "docsRphyPtpCcapCurrentDataSet": docsRphyPtpCcapCurrentDataSet,
       "docsRphyPtpCcapCurrentDataSetStepsRemoved": docsRphyPtpCcapCurrentDataSetStepsRemoved,
       "docsRphyPtpCcapCurrentDataSetOffsetFromMaster": docsRphyPtpCcapCurrentDataSetOffsetFromMaster,
       "docsRphyPtpCcapCurrentDataSetMeanPathDelay": docsRphyPtpCcapCurrentDataSetMeanPathDelay,
       "docsRphyPtpCcapParentDataSet": docsRphyPtpCcapParentDataSet,
       "docsRphyPtpCcapParentDataSetParentClockId": docsRphyPtpCcapParentDataSetParentClockId,
       "docsRphyPtpCcapParentDataSetParentPortNumber": docsRphyPtpCcapParentDataSetParentPortNumber,
       "docsRphyPtpCcapParentDataSetParentStats": docsRphyPtpCcapParentDataSetParentStats,
       "docsRphyPtpCcapParentDataSetClockOffset": docsRphyPtpCcapParentDataSetClockOffset,
       "docsRphyPtpCcapParentDataSetPhaseChangeRate": docsRphyPtpCcapParentDataSetPhaseChangeRate,
       "docsRphyPtpCcapParentDataSetGmClockIdentity": docsRphyPtpCcapParentDataSetGmClockIdentity,
       "docsRphyPtpCcapParentDataSetGmPriority1": docsRphyPtpCcapParentDataSetGmPriority1,
       "docsRphyPtpCcapParentDataSetGmPriority2": docsRphyPtpCcapParentDataSetGmPriority2,
       "docsRphyPtpCcapParentDataSetGmQualityClass": docsRphyPtpCcapParentDataSetGmQualityClass,
       "docsRphyPtpCcapParentDataSetGmQualityAccuracy": docsRphyPtpCcapParentDataSetGmQualityAccuracy,
       "docsRphyPtpCcapParentDataSetGmQualityOffset": docsRphyPtpCcapParentDataSetGmQualityOffset,
       "docsRphyPtpCcapTimeProperties": docsRphyPtpCcapTimeProperties,
       "docsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid": docsRphyPtpCcapTimePropertiesCurrentUtcOffsetValid,
       "docsRphyPtpCcapTimePropertiesCurrentUtcOffset": docsRphyPtpCcapTimePropertiesCurrentUtcOffset,
       "docsRphyPtpCcapTimePropertiesLeap59": docsRphyPtpCcapTimePropertiesLeap59,
       "docsRphyPtpCcapTimePropertiesLeap61": docsRphyPtpCcapTimePropertiesLeap61,
       "docsRphyPtpCcapTimePropertiesTimeTraceable": docsRphyPtpCcapTimePropertiesTimeTraceable,
       "docsRphyPtpCcapTimePropertiesFreqTraceable": docsRphyPtpCcapTimePropertiesFreqTraceable,
       "docsRphyPtpCcapTimePropertiesPtpTimescale": docsRphyPtpCcapTimePropertiesPtpTimescale,
       "docsRphyPtpCcapTimePropertiesTimeSource": docsRphyPtpCcapTimePropertiesTimeSource,
       "docsRphyPtpCcapPortDataSetTable": docsRphyPtpCcapPortDataSetTable,
       "docsRphyPtpCcapPortDataSetEntry": docsRphyPtpCcapPortDataSetEntry,
       "docsRphyPtpCcapPortDataSetPortNumber": docsRphyPtpCcapPortDataSetPortNumber,
       "docsRphyPtpCcapPortDataSetPortState": docsRphyPtpCcapPortDataSetPortState,
       "docsRphyPtpCcapPortDataSetMeanPathDelay": docsRphyPtpCcapPortDataSetMeanPathDelay,
       "docsRphyPtpCcapClockStatus": docsRphyPtpCcapClockStatus,
       "docsRphyPtpCcapClockStatusClockState": docsRphyPtpCcapClockStatusClockState,
       "docsRphyPtpCcapClockStatusLastStateChange": docsRphyPtpCcapClockStatusLastStateChange,
       "docsRphyPtpCcapClockStatusPacketsSent": docsRphyPtpCcapClockStatusPacketsSent,
       "docsRphyPtpCcapClockStatusPacketsReceived": docsRphyPtpCcapClockStatusPacketsReceived,
       "docsRphyPtpCcapClockStatusComputedPhaseOffset": docsRphyPtpCcapClockStatusComputedPhaseOffset,
       "docsRphyPtpCcapClockStatusCounterDiscontinuityTime": docsRphyPtpCcapClockStatusCounterDiscontinuityTime,
       "docsRphyPtpCcapCorePtpPortStatusTable": docsRphyPtpCcapCorePtpPortStatusTable,
       "docsRphyPtpCcapCorePtpPortStatusEntry": docsRphyPtpCcapCorePtpPortStatusEntry,
       "docsRphyPtpCcapCorePtpPortStatusPortNumber": docsRphyPtpCcapCorePtpPortStatusPortNumber,
       "docsRphyPtpCcapCorePtpPortStatusPacketsSent": docsRphyPtpCcapCorePtpPortStatusPacketsSent,
       "docsRphyPtpCcapCorePtpPortStatusPacketsReceived": docsRphyPtpCcapCorePtpPortStatusPacketsReceived,
       "docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime": docsRphyPtpCcapCorePtpPortStatusCounterDiscontinuityTime,
       "docsRphyPtpCcapPortMasterClockStatusTable": docsRphyPtpCcapPortMasterClockStatusTable,
       "docsRphyPtpCcapPortMasterClockStatusEntry": docsRphyPtpCcapPortMasterClockStatusEntry,
       "docsRphyPtpCcapPortMasterClockStatusMasterPriority": docsRphyPtpCcapPortMasterClockStatusMasterPriority,
       "docsRphyPtpCcapPortMasterClockStatusPacketsSent": docsRphyPtpCcapPortMasterClockStatusPacketsSent,
       "docsRphyPtpCcapPortMasterClockStatusPacketsReceived": docsRphyPtpCcapPortMasterClockStatusPacketsReceived,
       "docsRphyPtpCcapPortMasterClockStatusMasterClockId": docsRphyPtpCcapPortMasterClockStatusMasterClockId,
       "docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber": docsRphyPtpCcapPortMasterClockStatusMasterClockPortNumber,
       "docsRphyPtpCcapPortMasterClockStatusTwoStepFlag": docsRphyPtpCcapPortMasterClockStatusTwoStepFlag,
       "docsRphyPtpCcapPortMasterClockStatusIsBmc": docsRphyPtpCcapPortMasterClockStatusIsBmc,
       "docsRphyPtpCcapPortMasterClockStatusIsMasterConnected": docsRphyPtpCcapPortMasterClockStatusIsMasterConnected,
       "docsRphyPtpCcapPortMasterClockStatusStatusDomain": docsRphyPtpCcapPortMasterClockStatusStatusDomain,
       "docsRphyPtpCcapPortMasterClockStatusFreqOffset": docsRphyPtpCcapPortMasterClockStatusFreqOffset,
       "docsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime": docsRphyPtpCcapPortMasterClockStatusCounterDiscontinuityTime,
       "docsRphyPtpConformance": docsRphyPtpConformance,
       "docsRphyPtpCompliances": docsRphyPtpCompliances,
       "docsRphyPtpCompliance": docsRphyPtpCompliance,
       "docsRphyPtpGroups": docsRphyPtpGroups,
       "docsRphyPtpRpdGroup": docsRphyPtpRpdGroup,
       "docsRphyPtpCcapCoreGroup": docsRphyPtpCcapCoreGroup}
)
