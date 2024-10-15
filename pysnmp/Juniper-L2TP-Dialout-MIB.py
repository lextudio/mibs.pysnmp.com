# SNMP MIB module (Juniper-L2TP-Dialout-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-L2TP-Dialout-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:42 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniL2tpDialoutMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62)
)
juniL2tpDialoutMIB.setRevisions(
        ("2002-11-14 20:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniL2tpDialoutDomainName(OctetString, TextualConvention):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



# MIB Managed Objects in the order of their OIDs

_JuniL2tpDialoutMIBNotifications_ObjectIdentity = ObjectIdentity
juniL2tpDialoutMIBNotifications = _JuniL2tpDialoutMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 0)
)
_JuniL2tpDialoutMIBObjects_ObjectIdentity = ObjectIdentity
juniL2tpDialoutMIBObjects = _JuniL2tpDialoutMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1)
)
_JuniL2tpDialoutGeneral_ObjectIdentity = ObjectIdentity
juniL2tpDialoutGeneral = _JuniL2tpDialoutGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 1)
)


class _JuniL2tpDialoutConnectingTimerValue_Type(Integer32):
    """Custom type juniL2tpDialoutConnectingTimerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_JuniL2tpDialoutConnectingTimerValue_Type.__name__ = "Integer32"
_JuniL2tpDialoutConnectingTimerValue_Object = MibScalar
juniL2tpDialoutConnectingTimerValue = _JuniL2tpDialoutConnectingTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 1, 1),
    _JuniL2tpDialoutConnectingTimerValue_Type()
)
juniL2tpDialoutConnectingTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpDialoutConnectingTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpDialoutConnectingTimerValue.setUnits("seconds")


class _JuniL2tpDialoutDormantTimerValue_Type(Integer32):
    """Custom type juniL2tpDialoutDormantTimerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_JuniL2tpDialoutDormantTimerValue_Type.__name__ = "Integer32"
_JuniL2tpDialoutDormantTimerValue_Object = MibScalar
juniL2tpDialoutDormantTimerValue = _JuniL2tpDialoutDormantTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 1, 2),
    _JuniL2tpDialoutDormantTimerValue_Type()
)
juniL2tpDialoutDormantTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpDialoutDormantTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpDialoutDormantTimerValue.setUnits("seconds")
_JuniL2tpDialoutTarget_ObjectIdentity = ObjectIdentity
juniL2tpDialoutTarget = _JuniL2tpDialoutTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2)
)
_JuniL2tpDialoutTargetConfigTable_Object = MibTable
juniL2tpDialoutTargetConfigTable = _JuniL2tpDialoutTargetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetConfigTable.setStatus("current")
_JuniL2tpDialoutTargetConfigEntry_Object = MibTableRow
juniL2tpDialoutTargetConfigEntry = _JuniL2tpDialoutTargetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1)
)
juniL2tpDialoutTargetConfigEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetRouterIndex"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetIpAddress"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetIpAddressMask"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetConfigEntry.setStatus("current")
_JuniL2tpDialoutTargetRouterIndex_Type = Unsigned32
_JuniL2tpDialoutTargetRouterIndex_Object = MibTableColumn
juniL2tpDialoutTargetRouterIndex = _JuniL2tpDialoutTargetRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1, 1),
    _JuniL2tpDialoutTargetRouterIndex_Type()
)
juniL2tpDialoutTargetRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetRouterIndex.setStatus("current")
_JuniL2tpDialoutTargetIpAddress_Type = IpAddress
_JuniL2tpDialoutTargetIpAddress_Object = MibTableColumn
juniL2tpDialoutTargetIpAddress = _JuniL2tpDialoutTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1, 2),
    _JuniL2tpDialoutTargetIpAddress_Type()
)
juniL2tpDialoutTargetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetIpAddress.setStatus("current")
_JuniL2tpDialoutTargetIpAddressMask_Type = IpAddress
_JuniL2tpDialoutTargetIpAddressMask_Object = MibTableColumn
juniL2tpDialoutTargetIpAddressMask = _JuniL2tpDialoutTargetIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1, 3),
    _JuniL2tpDialoutTargetIpAddressMask_Type()
)
juniL2tpDialoutTargetIpAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetIpAddressMask.setStatus("current")
_JuniL2tpDialoutTargetDomainName_Type = JuniL2tpDialoutDomainName
_JuniL2tpDialoutTargetDomainName_Object = MibTableColumn
juniL2tpDialoutTargetDomainName = _JuniL2tpDialoutTargetDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1, 4),
    _JuniL2tpDialoutTargetDomainName_Type()
)
juniL2tpDialoutTargetDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetDomainName.setStatus("current")
_JuniL2tpDialoutTargetProfileName_Type = DisplayString
_JuniL2tpDialoutTargetProfileName_Object = MibTableColumn
juniL2tpDialoutTargetProfileName = _JuniL2tpDialoutTargetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1, 5),
    _JuniL2tpDialoutTargetProfileName_Type()
)
juniL2tpDialoutTargetProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetProfileName.setStatus("current")
_JuniL2tpDialoutTargetRowStatus_Type = RowStatus
_JuniL2tpDialoutTargetRowStatus_Object = MibTableColumn
juniL2tpDialoutTargetRowStatus = _JuniL2tpDialoutTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 1, 1, 6),
    _JuniL2tpDialoutTargetRowStatus_Type()
)
juniL2tpDialoutTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetRowStatus.setStatus("current")
_JuniL2tpDialoutTargetStatusTable_Object = MibTable
juniL2tpDialoutTargetStatusTable = _JuniL2tpDialoutTargetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatusTable.setStatus("current")
_JuniL2tpDialoutTargetStatusEntry_Object = MibTableRow
juniL2tpDialoutTargetStatusEntry = _JuniL2tpDialoutTargetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 2, 1)
)
juniL2tpDialoutTargetStatusEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatusRouterIndex"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatusIpAddress"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatusIpAddressMask"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatusEntry.setStatus("current")
_JuniL2tpDialoutTargetStatusRouterIndex_Type = Unsigned32
_JuniL2tpDialoutTargetStatusRouterIndex_Object = MibTableColumn
juniL2tpDialoutTargetStatusRouterIndex = _JuniL2tpDialoutTargetStatusRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 2, 1, 1),
    _JuniL2tpDialoutTargetStatusRouterIndex_Type()
)
juniL2tpDialoutTargetStatusRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatusRouterIndex.setStatus("current")
_JuniL2tpDialoutTargetStatusIpAddress_Type = IpAddress
_JuniL2tpDialoutTargetStatusIpAddress_Object = MibTableColumn
juniL2tpDialoutTargetStatusIpAddress = _JuniL2tpDialoutTargetStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 2, 1, 2),
    _JuniL2tpDialoutTargetStatusIpAddress_Type()
)
juniL2tpDialoutTargetStatusIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatusIpAddress.setStatus("current")
_JuniL2tpDialoutTargetStatusIpAddressMask_Type = IpAddress
_JuniL2tpDialoutTargetStatusIpAddressMask_Object = MibTableColumn
juniL2tpDialoutTargetStatusIpAddressMask = _JuniL2tpDialoutTargetStatusIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 2, 1, 3),
    _JuniL2tpDialoutTargetStatusIpAddressMask_Type()
)
juniL2tpDialoutTargetStatusIpAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatusIpAddressMask.setStatus("current")


class _JuniL2tpDialoutTargetStatus_Type(Integer32):
    """Custom type juniL2tpDialoutTargetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("inService", 2),
          ("inhibited", 1))
    )


_JuniL2tpDialoutTargetStatus_Type.__name__ = "Integer32"
_JuniL2tpDialoutTargetStatus_Object = MibTableColumn
juniL2tpDialoutTargetStatus = _JuniL2tpDialoutTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 2, 1, 4),
    _JuniL2tpDialoutTargetStatus_Type()
)
juniL2tpDialoutTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatus.setStatus("current")
_JuniL2tpDialoutTargetSystemStatistics_ObjectIdentity = ObjectIdentity
juniL2tpDialoutTargetSystemStatistics = _JuniL2tpDialoutTargetSystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3)
)
_JuniL2tpDialoutTargetsActive_Type = Gauge32
_JuniL2tpDialoutTargetsActive_Object = MibScalar
juniL2tpDialoutTargetsActive = _JuniL2tpDialoutTargetsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 1),
    _JuniL2tpDialoutTargetsActive_Type()
)
juniL2tpDialoutTargetsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetsActive.setStatus("current")
_JuniL2tpDialoutTargetsCreated_Type = Counter32
_JuniL2tpDialoutTargetsCreated_Object = MibScalar
juniL2tpDialoutTargetsCreated = _JuniL2tpDialoutTargetsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 2),
    _JuniL2tpDialoutTargetsCreated_Type()
)
juniL2tpDialoutTargetsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetsCreated.setStatus("current")
_JuniL2tpDialoutTargetsRemoved_Type = Counter32
_JuniL2tpDialoutTargetsRemoved_Object = MibScalar
juniL2tpDialoutTargetsRemoved = _JuniL2tpDialoutTargetsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 3),
    _JuniL2tpDialoutTargetsRemoved_Type()
)
juniL2tpDialoutTargetsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetsRemoved.setStatus("current")
_JuniL2tpDialoutTargetsDown_Type = Gauge32
_JuniL2tpDialoutTargetsDown_Object = MibScalar
juniL2tpDialoutTargetsDown = _JuniL2tpDialoutTargetsDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 4),
    _JuniL2tpDialoutTargetsDown_Type()
)
juniL2tpDialoutTargetsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetsDown.setStatus("current")
_JuniL2tpDialoutTargetsInhibited_Type = Gauge32
_JuniL2tpDialoutTargetsInhibited_Object = MibScalar
juniL2tpDialoutTargetsInhibited = _JuniL2tpDialoutTargetsInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 5),
    _JuniL2tpDialoutTargetsInhibited_Type()
)
juniL2tpDialoutTargetsInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetsInhibited.setStatus("current")
_JuniL2tpDialoutTargetsInService_Type = Gauge32
_JuniL2tpDialoutTargetsInService_Object = MibScalar
juniL2tpDialoutTargetsInService = _JuniL2tpDialoutTargetsInService_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 6),
    _JuniL2tpDialoutTargetsInService_Type()
)
juniL2tpDialoutTargetsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetsInService.setStatus("current")
_JuniL2tpDialoutTargetTriggersDiscarded_Type = Counter32
_JuniL2tpDialoutTargetTriggersDiscarded_Object = MibScalar
juniL2tpDialoutTargetTriggersDiscarded = _JuniL2tpDialoutTargetTriggersDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 3, 7),
    _JuniL2tpDialoutTargetTriggersDiscarded_Type()
)
juniL2tpDialoutTargetTriggersDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetTriggersDiscarded.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTable_Object = MibTable
juniL2tpDialoutTargetStatisticsTable = _JuniL2tpDialoutTargetStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTable.setStatus("current")
_JuniL2tpDialoutTargetStatisticsEntry_Object = MibTableRow
juniL2tpDialoutTargetStatisticsEntry = _JuniL2tpDialoutTargetStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1)
)
juniL2tpDialoutTargetStatisticsEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsRouterIndex"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsIpAddress"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsIpAddressMask"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsEntry.setStatus("current")
_JuniL2tpDialoutTargetStatisticsRouterIndex_Type = Unsigned32
_JuniL2tpDialoutTargetStatisticsRouterIndex_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsRouterIndex = _JuniL2tpDialoutTargetStatisticsRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 1),
    _JuniL2tpDialoutTargetStatisticsRouterIndex_Type()
)
juniL2tpDialoutTargetStatisticsRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsRouterIndex.setStatus("current")
_JuniL2tpDialoutTargetStatisticsIpAddress_Type = IpAddress
_JuniL2tpDialoutTargetStatisticsIpAddress_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsIpAddress = _JuniL2tpDialoutTargetStatisticsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 2),
    _JuniL2tpDialoutTargetStatisticsIpAddress_Type()
)
juniL2tpDialoutTargetStatisticsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsIpAddress.setStatus("current")
_JuniL2tpDialoutTargetStatisticsIpAddressMask_Type = IpAddress
_JuniL2tpDialoutTargetStatisticsIpAddressMask_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsIpAddressMask = _JuniL2tpDialoutTargetStatisticsIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 3),
    _JuniL2tpDialoutTargetStatisticsIpAddressMask_Type()
)
juniL2tpDialoutTargetStatisticsIpAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsIpAddressMask.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTargetsActive_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsTargetsActive_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTargetsActive = _JuniL2tpDialoutTargetStatisticsTargetsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 4),
    _JuniL2tpDialoutTargetStatisticsTargetsActive_Type()
)
juniL2tpDialoutTargetStatisticsTargetsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTargetsActive.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTargetsCreated_Type = Counter32
_JuniL2tpDialoutTargetStatisticsTargetsCreated_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTargetsCreated = _JuniL2tpDialoutTargetStatisticsTargetsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 5),
    _JuniL2tpDialoutTargetStatisticsTargetsCreated_Type()
)
juniL2tpDialoutTargetStatisticsTargetsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTargetsCreated.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTargetsRemoved_Type = Counter32
_JuniL2tpDialoutTargetStatisticsTargetsRemoved_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTargetsRemoved = _JuniL2tpDialoutTargetStatisticsTargetsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 6),
    _JuniL2tpDialoutTargetStatisticsTargetsRemoved_Type()
)
juniL2tpDialoutTargetStatisticsTargetsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTargetsRemoved.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTargetsDown_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsTargetsDown_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTargetsDown = _JuniL2tpDialoutTargetStatisticsTargetsDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 7),
    _JuniL2tpDialoutTargetStatisticsTargetsDown_Type()
)
juniL2tpDialoutTargetStatisticsTargetsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTargetsDown.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTargetsInhibited_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsTargetsInhibited_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTargetsInhibited = _JuniL2tpDialoutTargetStatisticsTargetsInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 8),
    _JuniL2tpDialoutTargetStatisticsTargetsInhibited_Type()
)
juniL2tpDialoutTargetStatisticsTargetsInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTargetsInhibited.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTargetsInService_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsTargetsInService_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTargetsInService = _JuniL2tpDialoutTargetStatisticsTargetsInService_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 9),
    _JuniL2tpDialoutTargetStatisticsTargetsInService_Type()
)
juniL2tpDialoutTargetStatisticsTargetsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTargetsInService.setStatus("current")
_JuniL2tpDialoutTargetStatisticsSessionsActive_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsSessionsActive_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsSessionsActive = _JuniL2tpDialoutTargetStatisticsSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 10),
    _JuniL2tpDialoutTargetStatisticsSessionsActive_Type()
)
juniL2tpDialoutTargetStatisticsSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsSessionsActive.setStatus("current")
_JuniL2tpDialoutTargetStatisticsSessionsCreated_Type = Counter32
_JuniL2tpDialoutTargetStatisticsSessionsCreated_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsSessionsCreated = _JuniL2tpDialoutTargetStatisticsSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 11),
    _JuniL2tpDialoutTargetStatisticsSessionsCreated_Type()
)
juniL2tpDialoutTargetStatisticsSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsSessionsCreated.setStatus("current")
_JuniL2tpDialoutTargetStatisticsSessionsRemoved_Type = Counter32
_JuniL2tpDialoutTargetStatisticsSessionsRemoved_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsSessionsRemoved = _JuniL2tpDialoutTargetStatisticsSessionsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 12),
    _JuniL2tpDialoutTargetStatisticsSessionsRemoved_Type()
)
juniL2tpDialoutTargetStatisticsSessionsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsSessionsRemoved.setStatus("current")
_JuniL2tpDialoutTargetStatisticsSessionsReset_Type = Counter32
_JuniL2tpDialoutTargetStatisticsSessionsReset_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsSessionsReset = _JuniL2tpDialoutTargetStatisticsSessionsReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 13),
    _JuniL2tpDialoutTargetStatisticsSessionsReset_Type()
)
juniL2tpDialoutTargetStatisticsSessionsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsSessionsReset.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTriggersReceived_Type = Counter32
_JuniL2tpDialoutTargetStatisticsTriggersReceived_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTriggersReceived = _JuniL2tpDialoutTargetStatisticsTriggersReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 14),
    _JuniL2tpDialoutTargetStatisticsTriggersReceived_Type()
)
juniL2tpDialoutTargetStatisticsTriggersReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTriggersReceived.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTriggersEnqueued_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsTriggersEnqueued_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTriggersEnqueued = _JuniL2tpDialoutTargetStatisticsTriggersEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 15),
    _JuniL2tpDialoutTargetStatisticsTriggersEnqueued_Type()
)
juniL2tpDialoutTargetStatisticsTriggersEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTriggersEnqueued.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTriggersDiscarded_Type = Counter32
_JuniL2tpDialoutTargetStatisticsTriggersDiscarded_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTriggersDiscarded = _JuniL2tpDialoutTargetStatisticsTriggersDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 16),
    _JuniL2tpDialoutTargetStatisticsTriggersDiscarded_Type()
)
juniL2tpDialoutTargetStatisticsTriggersDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTriggersDiscarded.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTriggersForwarded_Type = Counter32
_JuniL2tpDialoutTargetStatisticsTriggersForwarded_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTriggersForwarded = _JuniL2tpDialoutTargetStatisticsTriggersForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 17),
    _JuniL2tpDialoutTargetStatisticsTriggersForwarded_Type()
)
juniL2tpDialoutTargetStatisticsTriggersForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTriggersForwarded.setStatus("current")
_JuniL2tpDialoutTargetStatisticsTriggersMaxEnqueued_Type = Gauge32
_JuniL2tpDialoutTargetStatisticsTriggersMaxEnqueued_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsTriggersMaxEnqueued = _JuniL2tpDialoutTargetStatisticsTriggersMaxEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 18),
    _JuniL2tpDialoutTargetStatisticsTriggersMaxEnqueued_Type()
)
juniL2tpDialoutTargetStatisticsTriggersMaxEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsTriggersMaxEnqueued.setStatus("current")
_JuniL2tpDialoutTargetStatisticsAuthenticationRequests_Type = Counter32
_JuniL2tpDialoutTargetStatisticsAuthenticationRequests_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsAuthenticationRequests = _JuniL2tpDialoutTargetStatisticsAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 19),
    _JuniL2tpDialoutTargetStatisticsAuthenticationRequests_Type()
)
juniL2tpDialoutTargetStatisticsAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsAuthenticationRequests.setStatus("current")
_JuniL2tpDialoutTargetStatisticsAuthenticationNoResources_Type = Counter32
_JuniL2tpDialoutTargetStatisticsAuthenticationNoResources_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsAuthenticationNoResources = _JuniL2tpDialoutTargetStatisticsAuthenticationNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 20),
    _JuniL2tpDialoutTargetStatisticsAuthenticationNoResources_Type()
)
juniL2tpDialoutTargetStatisticsAuthenticationNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsAuthenticationNoResources.setStatus("current")
_JuniL2tpDialoutTargetStatisticsAuthenticationGrants_Type = Counter32
_JuniL2tpDialoutTargetStatisticsAuthenticationGrants_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsAuthenticationGrants = _JuniL2tpDialoutTargetStatisticsAuthenticationGrants_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 21),
    _JuniL2tpDialoutTargetStatisticsAuthenticationGrants_Type()
)
juniL2tpDialoutTargetStatisticsAuthenticationGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsAuthenticationGrants.setStatus("current")
_JuniL2tpDialoutTargetStatisticsAuthenticationDenies_Type = Counter32
_JuniL2tpDialoutTargetStatisticsAuthenticationDenies_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsAuthenticationDenies = _JuniL2tpDialoutTargetStatisticsAuthenticationDenies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 22),
    _JuniL2tpDialoutTargetStatisticsAuthenticationDenies_Type()
)
juniL2tpDialoutTargetStatisticsAuthenticationDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsAuthenticationDenies.setStatus("current")
_JuniL2tpDialoutTargetStatisticsDialoutsRequested_Type = Counter32
_JuniL2tpDialoutTargetStatisticsDialoutsRequested_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsDialoutsRequested = _JuniL2tpDialoutTargetStatisticsDialoutsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 23),
    _JuniL2tpDialoutTargetStatisticsDialoutsRequested_Type()
)
juniL2tpDialoutTargetStatisticsDialoutsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsDialoutsRequested.setStatus("current")
_JuniL2tpDialoutTargetStatisticsDialoutsRejected_Type = Counter32
_JuniL2tpDialoutTargetStatisticsDialoutsRejected_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsDialoutsRejected = _JuniL2tpDialoutTargetStatisticsDialoutsRejected_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 24),
    _JuniL2tpDialoutTargetStatisticsDialoutsRejected_Type()
)
juniL2tpDialoutTargetStatisticsDialoutsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsDialoutsRejected.setStatus("current")
_JuniL2tpDialoutTargetStatisticsDialoutsEstablished_Type = Counter32
_JuniL2tpDialoutTargetStatisticsDialoutsEstablished_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsDialoutsEstablished = _JuniL2tpDialoutTargetStatisticsDialoutsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 25),
    _JuniL2tpDialoutTargetStatisticsDialoutsEstablished_Type()
)
juniL2tpDialoutTargetStatisticsDialoutsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsDialoutsEstablished.setStatus("current")
_JuniL2tpDialoutTargetStatisticsDialoutsTimedout_Type = Counter32
_JuniL2tpDialoutTargetStatisticsDialoutsTimedout_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsDialoutsTimedout = _JuniL2tpDialoutTargetStatisticsDialoutsTimedout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 26),
    _JuniL2tpDialoutTargetStatisticsDialoutsTimedout_Type()
)
juniL2tpDialoutTargetStatisticsDialoutsTimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsDialoutsTimedout.setStatus("current")
_JuniL2tpDialoutTargetStatisticsDialoutsTornDown_Type = Counter32
_JuniL2tpDialoutTargetStatisticsDialoutsTornDown_Object = MibTableColumn
juniL2tpDialoutTargetStatisticsDialoutsTornDown = _JuniL2tpDialoutTargetStatisticsDialoutsTornDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 2, 4, 1, 27),
    _JuniL2tpDialoutTargetStatisticsDialoutsTornDown_Type()
)
juniL2tpDialoutTargetStatisticsDialoutsTornDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsDialoutsTornDown.setStatus("current")
_JuniL2tpDialoutTriggerBuffer_ObjectIdentity = ObjectIdentity
juniL2tpDialoutTriggerBuffer = _JuniL2tpDialoutTriggerBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 3)
)
_JuniL2tpDialoutTriggerBufferTable_Object = MibTable
juniL2tpDialoutTriggerBufferTable = _JuniL2tpDialoutTriggerBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTriggerBufferTable.setStatus("current")
_JuniL2tpDialoutTriggerBufferEntry_Object = MibTableRow
juniL2tpDialoutTriggerBufferEntry = _JuniL2tpDialoutTriggerBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 3, 1, 1)
)
juniL2tpDialoutTriggerBufferEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTriggerBufferRouterIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTriggerBufferEntry.setStatus("current")
_JuniL2tpDialoutTriggerBufferRouterIndex_Type = Unsigned32
_JuniL2tpDialoutTriggerBufferRouterIndex_Object = MibTableColumn
juniL2tpDialoutTriggerBufferRouterIndex = _JuniL2tpDialoutTriggerBufferRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 3, 1, 1, 1),
    _JuniL2tpDialoutTriggerBufferRouterIndex_Type()
)
juniL2tpDialoutTriggerBufferRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutTriggerBufferRouterIndex.setStatus("current")


class _JuniL2tpDialoutTriggerBufferCount_Type(Gauge32):
    """Custom type juniL2tpDialoutTriggerBufferCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_JuniL2tpDialoutTriggerBufferCount_Type.__name__ = "Gauge32"
_JuniL2tpDialoutTriggerBufferCount_Object = MibTableColumn
juniL2tpDialoutTriggerBufferCount = _JuniL2tpDialoutTriggerBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 3, 1, 1, 2),
    _JuniL2tpDialoutTriggerBufferCount_Type()
)
juniL2tpDialoutTriggerBufferCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDialoutTriggerBufferCount.setStatus("current")
_JuniL2tpDialoutSession_ObjectIdentity = ObjectIdentity
juniL2tpDialoutSession = _JuniL2tpDialoutSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4)
)
_JuniL2tpDialoutSessionConfigTable_Object = MibTable
juniL2tpDialoutSessionConfigTable = _JuniL2tpDialoutSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigTable.setStatus("current")
_JuniL2tpDialoutSessionConfigEntry_Object = MibTableRow
juniL2tpDialoutSessionConfigEntry = _JuniL2tpDialoutSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1)
)
juniL2tpDialoutSessionConfigEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionConfigHandle"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionConfigTargetIpAddress"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionConfigTargetIpAddressMask"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionConfigRouterIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigEntry.setStatus("current")
_JuniL2tpDialoutSessionConfigHandle_Type = IpAddress
_JuniL2tpDialoutSessionConfigHandle_Object = MibTableColumn
juniL2tpDialoutSessionConfigHandle = _JuniL2tpDialoutSessionConfigHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1, 1),
    _JuniL2tpDialoutSessionConfigHandle_Type()
)
juniL2tpDialoutSessionConfigHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigHandle.setStatus("current")
_JuniL2tpDialoutSessionConfigTargetIpAddress_Type = IpAddress
_JuniL2tpDialoutSessionConfigTargetIpAddress_Object = MibTableColumn
juniL2tpDialoutSessionConfigTargetIpAddress = _JuniL2tpDialoutSessionConfigTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1, 2),
    _JuniL2tpDialoutSessionConfigTargetIpAddress_Type()
)
juniL2tpDialoutSessionConfigTargetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigTargetIpAddress.setStatus("current")
_JuniL2tpDialoutSessionConfigTargetIpAddressMask_Type = IpAddress
_JuniL2tpDialoutSessionConfigTargetIpAddressMask_Object = MibTableColumn
juniL2tpDialoutSessionConfigTargetIpAddressMask = _JuniL2tpDialoutSessionConfigTargetIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1, 3),
    _JuniL2tpDialoutSessionConfigTargetIpAddressMask_Type()
)
juniL2tpDialoutSessionConfigTargetIpAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigTargetIpAddressMask.setStatus("current")
_JuniL2tpDialoutSessionConfigRouterIndex_Type = Unsigned32
_JuniL2tpDialoutSessionConfigRouterIndex_Object = MibTableColumn
juniL2tpDialoutSessionConfigRouterIndex = _JuniL2tpDialoutSessionConfigRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1, 4),
    _JuniL2tpDialoutSessionConfigRouterIndex_Type()
)
juniL2tpDialoutSessionConfigRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigRouterIndex.setStatus("current")


class _JuniL2tpDialoutSessionConfigControl_Type(Integer32):
    """Custom type juniL2tpDialoutSessionConfigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("operational", 0),
          ("reset", 1))
    )


_JuniL2tpDialoutSessionConfigControl_Type.__name__ = "Integer32"
_JuniL2tpDialoutSessionConfigControl_Object = MibTableColumn
juniL2tpDialoutSessionConfigControl = _JuniL2tpDialoutSessionConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1, 5),
    _JuniL2tpDialoutSessionConfigControl_Type()
)
juniL2tpDialoutSessionConfigControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigControl.setStatus("current")
_JuniL2tpDialoutSessionConfigRowStatus_Type = RowStatus
_JuniL2tpDialoutSessionConfigRowStatus_Object = MibTableColumn
juniL2tpDialoutSessionConfigRowStatus = _JuniL2tpDialoutSessionConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 1, 1, 6),
    _JuniL2tpDialoutSessionConfigRowStatus_Type()
)
juniL2tpDialoutSessionConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionConfigRowStatus.setStatus("current")
_JuniL2tpDialoutSessionStatusTable_Object = MibTable
juniL2tpDialoutSessionStatusTable = _JuniL2tpDialoutSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatusTable.setStatus("current")
_JuniL2tpDialoutSessionStatusEntry_Object = MibTableRow
juniL2tpDialoutSessionStatusEntry = _JuniL2tpDialoutSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2, 1)
)
juniL2tpDialoutSessionStatusEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatusHandle"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatusTargetIpAddress"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatusTargetIpAddressMask"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatusRouterIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatusEntry.setStatus("current")
_JuniL2tpDialoutSessionStatusHandle_Type = IpAddress
_JuniL2tpDialoutSessionStatusHandle_Object = MibTableColumn
juniL2tpDialoutSessionStatusHandle = _JuniL2tpDialoutSessionStatusHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2, 1, 1),
    _JuniL2tpDialoutSessionStatusHandle_Type()
)
juniL2tpDialoutSessionStatusHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatusHandle.setStatus("current")
_JuniL2tpDialoutSessionStatusTargetIpAddress_Type = IpAddress
_JuniL2tpDialoutSessionStatusTargetIpAddress_Object = MibTableColumn
juniL2tpDialoutSessionStatusTargetIpAddress = _JuniL2tpDialoutSessionStatusTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2, 1, 2),
    _JuniL2tpDialoutSessionStatusTargetIpAddress_Type()
)
juniL2tpDialoutSessionStatusTargetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatusTargetIpAddress.setStatus("current")
_JuniL2tpDialoutSessionStatusTargetIpAddressMask_Type = IpAddress
_JuniL2tpDialoutSessionStatusTargetIpAddressMask_Object = MibTableColumn
juniL2tpDialoutSessionStatusTargetIpAddressMask = _JuniL2tpDialoutSessionStatusTargetIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2, 1, 3),
    _JuniL2tpDialoutSessionStatusTargetIpAddressMask_Type()
)
juniL2tpDialoutSessionStatusTargetIpAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatusTargetIpAddressMask.setStatus("current")
_JuniL2tpDialoutSessionStatusRouterIndex_Type = Unsigned32
_JuniL2tpDialoutSessionStatusRouterIndex_Object = MibTableColumn
juniL2tpDialoutSessionStatusRouterIndex = _JuniL2tpDialoutSessionStatusRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2, 1, 4),
    _JuniL2tpDialoutSessionStatusRouterIndex_Type()
)
juniL2tpDialoutSessionStatusRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatusRouterIndex.setStatus("current")


class _JuniL2tpDialoutSessionStatus_Type(Integer32):
    """Custom type juniL2tpDialoutSessionStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 3),
          ("connecting", 4),
          ("dormant", 1),
          ("failed", 8),
          ("inService", 5),
          ("inhibited", 6),
          ("pending", 2),
          ("postInhibited", 7))
    )


_JuniL2tpDialoutSessionStatus_Type.__name__ = "Integer32"
_JuniL2tpDialoutSessionStatus_Object = MibTableColumn
juniL2tpDialoutSessionStatus = _JuniL2tpDialoutSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 2, 1, 5),
    _JuniL2tpDialoutSessionStatus_Type()
)
juniL2tpDialoutSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatus.setStatus("current")
_JuniL2tpDialoutSessionSystemStatistics_ObjectIdentity = ObjectIdentity
juniL2tpDialoutSessionSystemStatistics = _JuniL2tpDialoutSessionSystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3)
)
_JuniL2tpDialoutSessionsActive_Type = Gauge32
_JuniL2tpDialoutSessionsActive_Object = MibScalar
juniL2tpDialoutSessionsActive = _JuniL2tpDialoutSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 1),
    _JuniL2tpDialoutSessionsActive_Type()
)
juniL2tpDialoutSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionsActive.setStatus("current")
_JuniL2tpDialoutSessionsCreated_Type = Counter32
_JuniL2tpDialoutSessionsCreated_Object = MibScalar
juniL2tpDialoutSessionsCreated = _JuniL2tpDialoutSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 2),
    _JuniL2tpDialoutSessionsCreated_Type()
)
juniL2tpDialoutSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionsCreated.setStatus("current")
_JuniL2tpDialoutSessionsRemoved_Type = Counter32
_JuniL2tpDialoutSessionsRemoved_Object = MibScalar
juniL2tpDialoutSessionsRemoved = _JuniL2tpDialoutSessionsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 3),
    _JuniL2tpDialoutSessionsRemoved_Type()
)
juniL2tpDialoutSessionsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionsRemoved.setStatus("current")
_JuniL2tpDialoutSessionsReset_Type = Counter32
_JuniL2tpDialoutSessionsReset_Object = MibScalar
juniL2tpDialoutSessionsReset = _JuniL2tpDialoutSessionsReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 4),
    _JuniL2tpDialoutSessionsReset_Type()
)
juniL2tpDialoutSessionsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionsReset.setStatus("current")
_JuniL2tpDialoutSessionTriggersReceived_Type = Counter32
_JuniL2tpDialoutSessionTriggersReceived_Object = MibScalar
juniL2tpDialoutSessionTriggersReceived = _JuniL2tpDialoutSessionTriggersReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 5),
    _JuniL2tpDialoutSessionTriggersReceived_Type()
)
juniL2tpDialoutSessionTriggersReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionTriggersReceived.setStatus("current")
_JuniL2tpDialoutSessionTriggersEnqueued_Type = Counter32
_JuniL2tpDialoutSessionTriggersEnqueued_Object = MibScalar
juniL2tpDialoutSessionTriggersEnqueued = _JuniL2tpDialoutSessionTriggersEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 6),
    _JuniL2tpDialoutSessionTriggersEnqueued_Type()
)
juniL2tpDialoutSessionTriggersEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionTriggersEnqueued.setStatus("current")
_JuniL2tpDialoutSessionTriggersDiscarded_Type = Counter32
_JuniL2tpDialoutSessionTriggersDiscarded_Object = MibScalar
juniL2tpDialoutSessionTriggersDiscarded = _JuniL2tpDialoutSessionTriggersDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 7),
    _JuniL2tpDialoutSessionTriggersDiscarded_Type()
)
juniL2tpDialoutSessionTriggersDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionTriggersDiscarded.setStatus("current")
_JuniL2tpDialoutSessionTriggersForwarded_Type = Counter32
_JuniL2tpDialoutSessionTriggersForwarded_Object = MibScalar
juniL2tpDialoutSessionTriggersForwarded = _JuniL2tpDialoutSessionTriggersForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 8),
    _JuniL2tpDialoutSessionTriggersForwarded_Type()
)
juniL2tpDialoutSessionTriggersForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionTriggersForwarded.setStatus("current")
_JuniL2tpDialoutSessionTriggersMaxEnqueued_Type = Gauge32
_JuniL2tpDialoutSessionTriggersMaxEnqueued_Object = MibScalar
juniL2tpDialoutSessionTriggersMaxEnqueued = _JuniL2tpDialoutSessionTriggersMaxEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 9),
    _JuniL2tpDialoutSessionTriggersMaxEnqueued_Type()
)
juniL2tpDialoutSessionTriggersMaxEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionTriggersMaxEnqueued.setStatus("current")
_JuniL2tpDialoutSessionAuthenticationRequests_Type = Counter32
_JuniL2tpDialoutSessionAuthenticationRequests_Object = MibScalar
juniL2tpDialoutSessionAuthenticationRequests = _JuniL2tpDialoutSessionAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 10),
    _JuniL2tpDialoutSessionAuthenticationRequests_Type()
)
juniL2tpDialoutSessionAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionAuthenticationRequests.setStatus("current")
_JuniL2tpDialoutSessionAuthenticationNoResources_Type = Counter32
_JuniL2tpDialoutSessionAuthenticationNoResources_Object = MibScalar
juniL2tpDialoutSessionAuthenticationNoResources = _JuniL2tpDialoutSessionAuthenticationNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 11),
    _JuniL2tpDialoutSessionAuthenticationNoResources_Type()
)
juniL2tpDialoutSessionAuthenticationNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionAuthenticationNoResources.setStatus("current")
_JuniL2tpDialoutSessionAuthenticationGrants_Type = Counter32
_JuniL2tpDialoutSessionAuthenticationGrants_Object = MibScalar
juniL2tpDialoutSessionAuthenticationGrants = _JuniL2tpDialoutSessionAuthenticationGrants_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 12),
    _JuniL2tpDialoutSessionAuthenticationGrants_Type()
)
juniL2tpDialoutSessionAuthenticationGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionAuthenticationGrants.setStatus("current")
_JuniL2tpDialoutSessionAuthenticationDenies_Type = Counter32
_JuniL2tpDialoutSessionAuthenticationDenies_Object = MibScalar
juniL2tpDialoutSessionAuthenticationDenies = _JuniL2tpDialoutSessionAuthenticationDenies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 13),
    _JuniL2tpDialoutSessionAuthenticationDenies_Type()
)
juniL2tpDialoutSessionAuthenticationDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionAuthenticationDenies.setStatus("current")
_JuniL2tpDialoutSessionDialoutsRequested_Type = Counter32
_JuniL2tpDialoutSessionDialoutsRequested_Object = MibScalar
juniL2tpDialoutSessionDialoutsRequested = _JuniL2tpDialoutSessionDialoutsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 14),
    _JuniL2tpDialoutSessionDialoutsRequested_Type()
)
juniL2tpDialoutSessionDialoutsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionDialoutsRequested.setStatus("current")
_JuniL2tpDialoutSessionDialoutsRejected_Type = Counter32
_JuniL2tpDialoutSessionDialoutsRejected_Object = MibScalar
juniL2tpDialoutSessionDialoutsRejected = _JuniL2tpDialoutSessionDialoutsRejected_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 15),
    _JuniL2tpDialoutSessionDialoutsRejected_Type()
)
juniL2tpDialoutSessionDialoutsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionDialoutsRejected.setStatus("current")
_JuniL2tpDialoutSessionDialoutsEstablished_Type = Counter32
_JuniL2tpDialoutSessionDialoutsEstablished_Object = MibScalar
juniL2tpDialoutSessionDialoutsEstablished = _JuniL2tpDialoutSessionDialoutsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 16),
    _JuniL2tpDialoutSessionDialoutsEstablished_Type()
)
juniL2tpDialoutSessionDialoutsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionDialoutsEstablished.setStatus("current")
_JuniL2tpDialoutSessionDialoutsTimedout_Type = Counter32
_JuniL2tpDialoutSessionDialoutsTimedout_Object = MibScalar
juniL2tpDialoutSessionDialoutsTimedout = _JuniL2tpDialoutSessionDialoutsTimedout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 17),
    _JuniL2tpDialoutSessionDialoutsTimedout_Type()
)
juniL2tpDialoutSessionDialoutsTimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionDialoutsTimedout.setStatus("current")
_JuniL2tpDialoutSessionDialoutsTornDown_Type = Counter32
_JuniL2tpDialoutSessionDialoutsTornDown_Object = MibScalar
juniL2tpDialoutSessionDialoutsTornDown = _JuniL2tpDialoutSessionDialoutsTornDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 3, 18),
    _JuniL2tpDialoutSessionDialoutsTornDown_Type()
)
juniL2tpDialoutSessionDialoutsTornDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionDialoutsTornDown.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTable_Object = MibTable
juniL2tpDialoutSessionStatisticsTable = _JuniL2tpDialoutSessionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTable.setStatus("current")
_JuniL2tpDialoutSessionStatisticsEntry_Object = MibTableRow
juniL2tpDialoutSessionStatisticsEntry = _JuniL2tpDialoutSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1)
)
juniL2tpDialoutSessionStatisticsEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsHandle"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTargetIpAddress"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTargetIpAddressMask"),
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsRouterIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsEntry.setStatus("current")
_JuniL2tpDialoutSessionStatisticsHandle_Type = IpAddress
_JuniL2tpDialoutSessionStatisticsHandle_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsHandle = _JuniL2tpDialoutSessionStatisticsHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 1),
    _JuniL2tpDialoutSessionStatisticsHandle_Type()
)
juniL2tpDialoutSessionStatisticsHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsHandle.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTargetIpAddress_Type = IpAddress
_JuniL2tpDialoutSessionStatisticsTargetIpAddress_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTargetIpAddress = _JuniL2tpDialoutSessionStatisticsTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 2),
    _JuniL2tpDialoutSessionStatisticsTargetIpAddress_Type()
)
juniL2tpDialoutSessionStatisticsTargetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTargetIpAddress.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTargetIpAddressMask_Type = IpAddress
_JuniL2tpDialoutSessionStatisticsTargetIpAddressMask_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTargetIpAddressMask = _JuniL2tpDialoutSessionStatisticsTargetIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 3),
    _JuniL2tpDialoutSessionStatisticsTargetIpAddressMask_Type()
)
juniL2tpDialoutSessionStatisticsTargetIpAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTargetIpAddressMask.setStatus("current")
_JuniL2tpDialoutSessionStatisticsRouterIndex_Type = Unsigned32
_JuniL2tpDialoutSessionStatisticsRouterIndex_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsRouterIndex = _JuniL2tpDialoutSessionStatisticsRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 4),
    _JuniL2tpDialoutSessionStatisticsRouterIndex_Type()
)
juniL2tpDialoutSessionStatisticsRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsRouterIndex.setStatus("current")
_JuniL2tpDialoutSessionStatisticsSessionsActive_Type = Gauge32
_JuniL2tpDialoutSessionStatisticsSessionsActive_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsSessionsActive = _JuniL2tpDialoutSessionStatisticsSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 5),
    _JuniL2tpDialoutSessionStatisticsSessionsActive_Type()
)
juniL2tpDialoutSessionStatisticsSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsSessionsActive.setStatus("current")
_JuniL2tpDialoutSessionStatisticsSessionsCreated_Type = Counter32
_JuniL2tpDialoutSessionStatisticsSessionsCreated_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsSessionsCreated = _JuniL2tpDialoutSessionStatisticsSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 6),
    _JuniL2tpDialoutSessionStatisticsSessionsCreated_Type()
)
juniL2tpDialoutSessionStatisticsSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsSessionsCreated.setStatus("current")
_JuniL2tpDialoutSessionStatisticsSessionsRemoved_Type = Counter32
_JuniL2tpDialoutSessionStatisticsSessionsRemoved_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsSessionsRemoved = _JuniL2tpDialoutSessionStatisticsSessionsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 7),
    _JuniL2tpDialoutSessionStatisticsSessionsRemoved_Type()
)
juniL2tpDialoutSessionStatisticsSessionsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsSessionsRemoved.setStatus("current")
_JuniL2tpDialoutSessionStatisticsSessionsReset_Type = Counter32
_JuniL2tpDialoutSessionStatisticsSessionsReset_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsSessionsReset = _JuniL2tpDialoutSessionStatisticsSessionsReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 8),
    _JuniL2tpDialoutSessionStatisticsSessionsReset_Type()
)
juniL2tpDialoutSessionStatisticsSessionsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsSessionsReset.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTriggersReceived_Type = Counter32
_JuniL2tpDialoutSessionStatisticsTriggersReceived_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTriggersReceived = _JuniL2tpDialoutSessionStatisticsTriggersReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 9),
    _JuniL2tpDialoutSessionStatisticsTriggersReceived_Type()
)
juniL2tpDialoutSessionStatisticsTriggersReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTriggersReceived.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTriggersEnqueued_Type = Gauge32
_JuniL2tpDialoutSessionStatisticsTriggersEnqueued_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTriggersEnqueued = _JuniL2tpDialoutSessionStatisticsTriggersEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 10),
    _JuniL2tpDialoutSessionStatisticsTriggersEnqueued_Type()
)
juniL2tpDialoutSessionStatisticsTriggersEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTriggersEnqueued.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTriggersDiscarded_Type = Counter32
_JuniL2tpDialoutSessionStatisticsTriggersDiscarded_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTriggersDiscarded = _JuniL2tpDialoutSessionStatisticsTriggersDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 11),
    _JuniL2tpDialoutSessionStatisticsTriggersDiscarded_Type()
)
juniL2tpDialoutSessionStatisticsTriggersDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTriggersDiscarded.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTriggersForwarded_Type = Counter32
_JuniL2tpDialoutSessionStatisticsTriggersForwarded_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTriggersForwarded = _JuniL2tpDialoutSessionStatisticsTriggersForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 12),
    _JuniL2tpDialoutSessionStatisticsTriggersForwarded_Type()
)
juniL2tpDialoutSessionStatisticsTriggersForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTriggersForwarded.setStatus("current")
_JuniL2tpDialoutSessionStatisticsTriggersMaxEnqueued_Type = Gauge32
_JuniL2tpDialoutSessionStatisticsTriggersMaxEnqueued_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsTriggersMaxEnqueued = _JuniL2tpDialoutSessionStatisticsTriggersMaxEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 13),
    _JuniL2tpDialoutSessionStatisticsTriggersMaxEnqueued_Type()
)
juniL2tpDialoutSessionStatisticsTriggersMaxEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsTriggersMaxEnqueued.setStatus("current")
_JuniL2tpDialoutSessionStatisticsAuthenticationRequests_Type = Counter32
_JuniL2tpDialoutSessionStatisticsAuthenticationRequests_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsAuthenticationRequests = _JuniL2tpDialoutSessionStatisticsAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 14),
    _JuniL2tpDialoutSessionStatisticsAuthenticationRequests_Type()
)
juniL2tpDialoutSessionStatisticsAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsAuthenticationRequests.setStatus("current")
_JuniL2tpDialoutSessionStatisticsAuthenticationNoResources_Type = Counter32
_JuniL2tpDialoutSessionStatisticsAuthenticationNoResources_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsAuthenticationNoResources = _JuniL2tpDialoutSessionStatisticsAuthenticationNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 15),
    _JuniL2tpDialoutSessionStatisticsAuthenticationNoResources_Type()
)
juniL2tpDialoutSessionStatisticsAuthenticationNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsAuthenticationNoResources.setStatus("current")
_JuniL2tpDialoutSessionStatisticsAuthenticationGrants_Type = Counter32
_JuniL2tpDialoutSessionStatisticsAuthenticationGrants_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsAuthenticationGrants = _JuniL2tpDialoutSessionStatisticsAuthenticationGrants_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 16),
    _JuniL2tpDialoutSessionStatisticsAuthenticationGrants_Type()
)
juniL2tpDialoutSessionStatisticsAuthenticationGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsAuthenticationGrants.setStatus("current")
_JuniL2tpDialoutSessionStatisticsAuthenticationDenies_Type = Counter32
_JuniL2tpDialoutSessionStatisticsAuthenticationDenies_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsAuthenticationDenies = _JuniL2tpDialoutSessionStatisticsAuthenticationDenies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 17),
    _JuniL2tpDialoutSessionStatisticsAuthenticationDenies_Type()
)
juniL2tpDialoutSessionStatisticsAuthenticationDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsAuthenticationDenies.setStatus("current")
_JuniL2tpDialoutSessionStatisticsDialoutsRequested_Type = Counter32
_JuniL2tpDialoutSessionStatisticsDialoutsRequested_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsDialoutsRequested = _JuniL2tpDialoutSessionStatisticsDialoutsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 18),
    _JuniL2tpDialoutSessionStatisticsDialoutsRequested_Type()
)
juniL2tpDialoutSessionStatisticsDialoutsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsDialoutsRequested.setStatus("current")
_JuniL2tpDialoutSessionStatisticsDialoutsRejected_Type = Counter32
_JuniL2tpDialoutSessionStatisticsDialoutsRejected_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsDialoutsRejected = _JuniL2tpDialoutSessionStatisticsDialoutsRejected_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 19),
    _JuniL2tpDialoutSessionStatisticsDialoutsRejected_Type()
)
juniL2tpDialoutSessionStatisticsDialoutsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsDialoutsRejected.setStatus("current")
_JuniL2tpDialoutSessionStatisticsDialoutsEstablished_Type = Counter32
_JuniL2tpDialoutSessionStatisticsDialoutsEstablished_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsDialoutsEstablished = _JuniL2tpDialoutSessionStatisticsDialoutsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 20),
    _JuniL2tpDialoutSessionStatisticsDialoutsEstablished_Type()
)
juniL2tpDialoutSessionStatisticsDialoutsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsDialoutsEstablished.setStatus("current")
_JuniL2tpDialoutSessionStatisticsDialoutsTimedout_Type = Counter32
_JuniL2tpDialoutSessionStatisticsDialoutsTimedout_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsDialoutsTimedout = _JuniL2tpDialoutSessionStatisticsDialoutsTimedout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 21),
    _JuniL2tpDialoutSessionStatisticsDialoutsTimedout_Type()
)
juniL2tpDialoutSessionStatisticsDialoutsTimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsDialoutsTimedout.setStatus("current")
_JuniL2tpDialoutSessionStatisticsDialoutsTornDown_Type = Counter32
_JuniL2tpDialoutSessionStatisticsDialoutsTornDown_Object = MibTableColumn
juniL2tpDialoutSessionStatisticsDialoutsTornDown = _JuniL2tpDialoutSessionStatisticsDialoutsTornDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 4, 4, 1, 22),
    _JuniL2tpDialoutSessionStatisticsDialoutsTornDown_Type()
)
juniL2tpDialoutSessionStatisticsDialoutsTornDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsDialoutsTornDown.setStatus("current")
_JuniL2tpDialoutVRouter_ObjectIdentity = ObjectIdentity
juniL2tpDialoutVRouter = _JuniL2tpDialoutVRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5)
)
_JuniL2tpDialoutVRouterStatusTable_Object = MibTable
juniL2tpDialoutVRouterStatusTable = _JuniL2tpDialoutVRouterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatusTable.setStatus("current")
_JuniL2tpDialoutVRouterStatusEntry_Object = MibTableRow
juniL2tpDialoutVRouterStatusEntry = _JuniL2tpDialoutVRouterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 1, 1)
)
juniL2tpDialoutVRouterStatusEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatusRouterIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatusEntry.setStatus("current")
_JuniL2tpDialoutVRouterStatusRouterIndex_Type = Unsigned32
_JuniL2tpDialoutVRouterStatusRouterIndex_Object = MibTableColumn
juniL2tpDialoutVRouterStatusRouterIndex = _JuniL2tpDialoutVRouterStatusRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 1, 1, 1),
    _JuniL2tpDialoutVRouterStatusRouterIndex_Type()
)
juniL2tpDialoutVRouterStatusRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatusRouterIndex.setStatus("current")


class _JuniL2tpDialoutVRouterStatus_Type(Integer32):
    """Custom type juniL2tpDialoutVRouterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("inService", 3),
          ("initFailed", 1),
          ("initPending", 0))
    )


_JuniL2tpDialoutVRouterStatus_Type.__name__ = "Integer32"
_JuniL2tpDialoutVRouterStatus_Object = MibTableColumn
juniL2tpDialoutVRouterStatus = _JuniL2tpDialoutVRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 1, 1, 2),
    _JuniL2tpDialoutVRouterStatus_Type()
)
juniL2tpDialoutVRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatus.setStatus("current")
_JuniL2tpDialoutVRouterSystemStatistics_ObjectIdentity = ObjectIdentity
juniL2tpDialoutVRouterSystemStatistics = _JuniL2tpDialoutVRouterSystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2)
)
_JuniL2tpDialoutVRoutersActive_Type = Gauge32
_JuniL2tpDialoutVRoutersActive_Object = MibScalar
juniL2tpDialoutVRoutersActive = _JuniL2tpDialoutVRoutersActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 1),
    _JuniL2tpDialoutVRoutersActive_Type()
)
juniL2tpDialoutVRoutersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersActive.setStatus("current")
_JuniL2tpDialoutVRoutersCreated_Type = Counter32
_JuniL2tpDialoutVRoutersCreated_Object = MibScalar
juniL2tpDialoutVRoutersCreated = _JuniL2tpDialoutVRoutersCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 2),
    _JuniL2tpDialoutVRoutersCreated_Type()
)
juniL2tpDialoutVRoutersCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersCreated.setStatus("current")
_JuniL2tpDialoutVRoutersRemoved_Type = Counter32
_JuniL2tpDialoutVRoutersRemoved_Object = MibScalar
juniL2tpDialoutVRoutersRemoved = _JuniL2tpDialoutVRoutersRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 3),
    _JuniL2tpDialoutVRoutersRemoved_Type()
)
juniL2tpDialoutVRoutersRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersRemoved.setStatus("current")
_JuniL2tpDialoutVRoutersInitPending_Type = Gauge32
_JuniL2tpDialoutVRoutersInitPending_Object = MibScalar
juniL2tpDialoutVRoutersInitPending = _JuniL2tpDialoutVRoutersInitPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 4),
    _JuniL2tpDialoutVRoutersInitPending_Type()
)
juniL2tpDialoutVRoutersInitPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersInitPending.setStatus("current")
_JuniL2tpDialoutVRoutersInitFailed_Type = Gauge32
_JuniL2tpDialoutVRoutersInitFailed_Object = MibScalar
juniL2tpDialoutVRoutersInitFailed = _JuniL2tpDialoutVRoutersInitFailed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 5),
    _JuniL2tpDialoutVRoutersInitFailed_Type()
)
juniL2tpDialoutVRoutersInitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersInitFailed.setStatus("current")
_JuniL2tpDialoutVRoutersDown_Type = Gauge32
_JuniL2tpDialoutVRoutersDown_Object = MibScalar
juniL2tpDialoutVRoutersDown = _JuniL2tpDialoutVRoutersDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 6),
    _JuniL2tpDialoutVRoutersDown_Type()
)
juniL2tpDialoutVRoutersDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersDown.setStatus("current")
_JuniL2tpDialoutVRoutersInService_Type = Gauge32
_JuniL2tpDialoutVRoutersInService_Object = MibScalar
juniL2tpDialoutVRoutersInService = _JuniL2tpDialoutVRoutersInService_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 7),
    _JuniL2tpDialoutVRoutersInService_Type()
)
juniL2tpDialoutVRoutersInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersInService.setStatus("current")
_JuniL2tpDialoutVRoutersTriggersMissed_Type = Counter32
_JuniL2tpDialoutVRoutersTriggersMissed_Object = MibScalar
juniL2tpDialoutVRoutersTriggersMissed = _JuniL2tpDialoutVRoutersTriggersMissed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 8),
    _JuniL2tpDialoutVRoutersTriggersMissed_Type()
)
juniL2tpDialoutVRoutersTriggersMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersTriggersMissed.setStatus("current")
_JuniL2tpDialoutVRoutersTriggerRouteUnknown_Type = Counter32
_JuniL2tpDialoutVRoutersTriggerRouteUnknown_Object = MibScalar
juniL2tpDialoutVRoutersTriggerRouteUnknown = _JuniL2tpDialoutVRoutersTriggerRouteUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 9),
    _JuniL2tpDialoutVRoutersTriggerRouteUnknown_Type()
)
juniL2tpDialoutVRoutersTriggerRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersTriggerRouteUnknown.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsDormant_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsDormant_Object = MibScalar
juniL2tpDialoutVRoutersSessionsDormant = _JuniL2tpDialoutVRoutersSessionsDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 10),
    _JuniL2tpDialoutVRoutersSessionsDormant_Type()
)
juniL2tpDialoutVRoutersSessionsDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsDormant.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsPending_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsPending_Object = MibScalar
juniL2tpDialoutVRoutersSessionsPending = _JuniL2tpDialoutVRoutersSessionsPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 11),
    _JuniL2tpDialoutVRoutersSessionsPending_Type()
)
juniL2tpDialoutVRoutersSessionsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsPending.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsAuthenticating_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsAuthenticating_Object = MibScalar
juniL2tpDialoutVRoutersSessionsAuthenticating = _JuniL2tpDialoutVRoutersSessionsAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 12),
    _JuniL2tpDialoutVRoutersSessionsAuthenticating_Type()
)
juniL2tpDialoutVRoutersSessionsAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsAuthenticating.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsConnecting_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsConnecting_Object = MibScalar
juniL2tpDialoutVRoutersSessionsConnecting = _JuniL2tpDialoutVRoutersSessionsConnecting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 13),
    _JuniL2tpDialoutVRoutersSessionsConnecting_Type()
)
juniL2tpDialoutVRoutersSessionsConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsConnecting.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsInService_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsInService_Object = MibScalar
juniL2tpDialoutVRoutersSessionsInService = _JuniL2tpDialoutVRoutersSessionsInService_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 14),
    _JuniL2tpDialoutVRoutersSessionsInService_Type()
)
juniL2tpDialoutVRoutersSessionsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsInService.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsInhibited_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsInhibited_Object = MibScalar
juniL2tpDialoutVRoutersSessionsInhibited = _JuniL2tpDialoutVRoutersSessionsInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 15),
    _JuniL2tpDialoutVRoutersSessionsInhibited_Type()
)
juniL2tpDialoutVRoutersSessionsInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsInhibited.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsPostInhibited_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsPostInhibited_Object = MibScalar
juniL2tpDialoutVRoutersSessionsPostInhibited = _JuniL2tpDialoutVRoutersSessionsPostInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 16),
    _JuniL2tpDialoutVRoutersSessionsPostInhibited_Type()
)
juniL2tpDialoutVRoutersSessionsPostInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsPostInhibited.setStatus("current")
_JuniL2tpDialoutVRoutersSessionsFailed_Type = Gauge32
_JuniL2tpDialoutVRoutersSessionsFailed_Object = MibScalar
juniL2tpDialoutVRoutersSessionsFailed = _JuniL2tpDialoutVRoutersSessionsFailed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 2, 17),
    _JuniL2tpDialoutVRoutersSessionsFailed_Type()
)
juniL2tpDialoutVRoutersSessionsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRoutersSessionsFailed.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTable_Object = MibTable
juniL2tpDialoutVRouterStatisticsTable = _JuniL2tpDialoutVRouterStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTable.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsEntry_Object = MibTableRow
juniL2tpDialoutVRouterStatisticsEntry = _JuniL2tpDialoutVRouterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1)
)
juniL2tpDialoutVRouterStatisticsEntry.setIndexNames(
    (0, "Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsRouterIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsEntry.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsRouterIndex_Type = Unsigned32
_JuniL2tpDialoutVRouterStatisticsRouterIndex_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsRouterIndex = _JuniL2tpDialoutVRouterStatisticsRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 1),
    _JuniL2tpDialoutVRouterStatisticsRouterIndex_Type()
)
juniL2tpDialoutVRouterStatisticsRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsRouterIndex.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggersMissed_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTriggersMissed_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggersMissed = _JuniL2tpDialoutVRouterStatisticsTriggersMissed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 2),
    _JuniL2tpDialoutVRouterStatisticsTriggersMissed_Type()
)
juniL2tpDialoutVRouterStatisticsTriggersMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggersMissed.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggerRouteUnknown_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTriggerRouteUnknown_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggerRouteUnknown = _JuniL2tpDialoutVRouterStatisticsTriggerRouteUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 3),
    _JuniL2tpDialoutVRouterStatisticsTriggerRouteUnknown_Type()
)
juniL2tpDialoutVRouterStatisticsTriggerRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggerRouteUnknown.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStateDormant_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStateDormant_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStateDormant = _JuniL2tpDialoutVRouterStatisticsSessionStateDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 4),
    _JuniL2tpDialoutVRouterStatisticsSessionStateDormant_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStateDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStateDormant.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStatePending_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStatePending_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStatePending = _JuniL2tpDialoutVRouterStatisticsSessionStatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 5),
    _JuniL2tpDialoutVRouterStatisticsSessionStatePending_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStatePending.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStateAuthenticating_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStateAuthenticating_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStateAuthenticating = _JuniL2tpDialoutVRouterStatisticsSessionStateAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 6),
    _JuniL2tpDialoutVRouterStatisticsSessionStateAuthenticating_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStateAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStateAuthenticating.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStateConnecting_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStateConnecting_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStateConnecting = _JuniL2tpDialoutVRouterStatisticsSessionStateConnecting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 7),
    _JuniL2tpDialoutVRouterStatisticsSessionStateConnecting_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStateConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStateConnecting.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStateInService_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStateInService_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStateInService = _JuniL2tpDialoutVRouterStatisticsSessionStateInService_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 8),
    _JuniL2tpDialoutVRouterStatisticsSessionStateInService_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStateInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStateInService.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStateInhibited_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStateInhibited_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStateInhibited = _JuniL2tpDialoutVRouterStatisticsSessionStateInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 9),
    _JuniL2tpDialoutVRouterStatisticsSessionStateInhibited_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStateInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStateInhibited.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStatePostInhibited_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStatePostInhibited_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStatePostInhibited = _JuniL2tpDialoutVRouterStatisticsSessionStatePostInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 10),
    _JuniL2tpDialoutVRouterStatisticsSessionStatePostInhibited_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStatePostInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStatePostInhibited.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionStateFailed_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionStateFailed_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionStateFailed = _JuniL2tpDialoutVRouterStatisticsSessionStateFailed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 11),
    _JuniL2tpDialoutVRouterStatisticsSessionStateFailed_Type()
)
juniL2tpDialoutVRouterStatisticsSessionStateFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionStateFailed.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTargetsActive_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsTargetsActive_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTargetsActive = _JuniL2tpDialoutVRouterStatisticsTargetsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 12),
    _JuniL2tpDialoutVRouterStatisticsTargetsActive_Type()
)
juniL2tpDialoutVRouterStatisticsTargetsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTargetsActive.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTargetsCreated_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTargetsCreated_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTargetsCreated = _JuniL2tpDialoutVRouterStatisticsTargetsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 13),
    _JuniL2tpDialoutVRouterStatisticsTargetsCreated_Type()
)
juniL2tpDialoutVRouterStatisticsTargetsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTargetsCreated.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTargetsRemoved_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTargetsRemoved_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTargetsRemoved = _JuniL2tpDialoutVRouterStatisticsTargetsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 14),
    _JuniL2tpDialoutVRouterStatisticsTargetsRemoved_Type()
)
juniL2tpDialoutVRouterStatisticsTargetsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTargetsRemoved.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTargetsDown_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsTargetsDown_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTargetsDown = _JuniL2tpDialoutVRouterStatisticsTargetsDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 15),
    _JuniL2tpDialoutVRouterStatisticsTargetsDown_Type()
)
juniL2tpDialoutVRouterStatisticsTargetsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTargetsDown.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTargetsInhibited_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsTargetsInhibited_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTargetsInhibited = _JuniL2tpDialoutVRouterStatisticsTargetsInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 16),
    _JuniL2tpDialoutVRouterStatisticsTargetsInhibited_Type()
)
juniL2tpDialoutVRouterStatisticsTargetsInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTargetsInhibited.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTargetsInService_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsTargetsInService_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTargetsInService = _JuniL2tpDialoutVRouterStatisticsTargetsInService_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 17),
    _JuniL2tpDialoutVRouterStatisticsTargetsInService_Type()
)
juniL2tpDialoutVRouterStatisticsTargetsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTargetsInService.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionsActive_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsSessionsActive_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionsActive = _JuniL2tpDialoutVRouterStatisticsSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 18),
    _JuniL2tpDialoutVRouterStatisticsSessionsActive_Type()
)
juniL2tpDialoutVRouterStatisticsSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionsActive.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionsCreated_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsSessionsCreated_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionsCreated = _JuniL2tpDialoutVRouterStatisticsSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 19),
    _JuniL2tpDialoutVRouterStatisticsSessionsCreated_Type()
)
juniL2tpDialoutVRouterStatisticsSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionsCreated.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionsRemoved_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsSessionsRemoved_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionsRemoved = _JuniL2tpDialoutVRouterStatisticsSessionsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 20),
    _JuniL2tpDialoutVRouterStatisticsSessionsRemoved_Type()
)
juniL2tpDialoutVRouterStatisticsSessionsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionsRemoved.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsSessionsReset_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsSessionsReset_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsSessionsReset = _JuniL2tpDialoutVRouterStatisticsSessionsReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 21),
    _JuniL2tpDialoutVRouterStatisticsSessionsReset_Type()
)
juniL2tpDialoutVRouterStatisticsSessionsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsSessionsReset.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggersReceived_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTriggersReceived_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggersReceived = _JuniL2tpDialoutVRouterStatisticsTriggersReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 22),
    _JuniL2tpDialoutVRouterStatisticsTriggersReceived_Type()
)
juniL2tpDialoutVRouterStatisticsTriggersReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggersReceived.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggersEnqueued_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsTriggersEnqueued_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggersEnqueued = _JuniL2tpDialoutVRouterStatisticsTriggersEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 23),
    _JuniL2tpDialoutVRouterStatisticsTriggersEnqueued_Type()
)
juniL2tpDialoutVRouterStatisticsTriggersEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggersEnqueued.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggersDiscarded_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTriggersDiscarded_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggersDiscarded = _JuniL2tpDialoutVRouterStatisticsTriggersDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 24),
    _JuniL2tpDialoutVRouterStatisticsTriggersDiscarded_Type()
)
juniL2tpDialoutVRouterStatisticsTriggersDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggersDiscarded.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggersForwarded_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsTriggersForwarded_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggersForwarded = _JuniL2tpDialoutVRouterStatisticsTriggersForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 25),
    _JuniL2tpDialoutVRouterStatisticsTriggersForwarded_Type()
)
juniL2tpDialoutVRouterStatisticsTriggersForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggersForwarded.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued_Type = Gauge32
_JuniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued = _JuniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 26),
    _JuniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued_Type()
)
juniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsAuthenticationRequests_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsAuthenticationRequests_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsAuthenticationRequests = _JuniL2tpDialoutVRouterStatisticsAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 27),
    _JuniL2tpDialoutVRouterStatisticsAuthenticationRequests_Type()
)
juniL2tpDialoutVRouterStatisticsAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsAuthenticationRequests.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsAuthenticationNoResources_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsAuthenticationNoResources_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsAuthenticationNoResources = _JuniL2tpDialoutVRouterStatisticsAuthenticationNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 28),
    _JuniL2tpDialoutVRouterStatisticsAuthenticationNoResources_Type()
)
juniL2tpDialoutVRouterStatisticsAuthenticationNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsAuthenticationNoResources.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsAuthenticationGrants_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsAuthenticationGrants_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsAuthenticationGrants = _JuniL2tpDialoutVRouterStatisticsAuthenticationGrants_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 29),
    _JuniL2tpDialoutVRouterStatisticsAuthenticationGrants_Type()
)
juniL2tpDialoutVRouterStatisticsAuthenticationGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsAuthenticationGrants.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsAuthenticationDenies_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsAuthenticationDenies_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsAuthenticationDenies = _JuniL2tpDialoutVRouterStatisticsAuthenticationDenies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 30),
    _JuniL2tpDialoutVRouterStatisticsAuthenticationDenies_Type()
)
juniL2tpDialoutVRouterStatisticsAuthenticationDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsAuthenticationDenies.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsDialoutsRequested_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsDialoutsRequested_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsDialoutsRequested = _JuniL2tpDialoutVRouterStatisticsDialoutsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 31),
    _JuniL2tpDialoutVRouterStatisticsDialoutsRequested_Type()
)
juniL2tpDialoutVRouterStatisticsDialoutsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsDialoutsRequested.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsDialoutsRejected_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsDialoutsRejected_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsDialoutsRejected = _JuniL2tpDialoutVRouterStatisticsDialoutsRejected_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 32),
    _JuniL2tpDialoutVRouterStatisticsDialoutsRejected_Type()
)
juniL2tpDialoutVRouterStatisticsDialoutsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsDialoutsRejected.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsDialoutsEstablished_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsDialoutsEstablished_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsDialoutsEstablished = _JuniL2tpDialoutVRouterStatisticsDialoutsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 33),
    _JuniL2tpDialoutVRouterStatisticsDialoutsEstablished_Type()
)
juniL2tpDialoutVRouterStatisticsDialoutsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsDialoutsEstablished.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsDialoutsTimedout_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsDialoutsTimedout_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsDialoutsTimedout = _JuniL2tpDialoutVRouterStatisticsDialoutsTimedout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 34),
    _JuniL2tpDialoutVRouterStatisticsDialoutsTimedout_Type()
)
juniL2tpDialoutVRouterStatisticsDialoutsTimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsDialoutsTimedout.setStatus("current")
_JuniL2tpDialoutVRouterStatisticsDialoutsTornDown_Type = Counter32
_JuniL2tpDialoutVRouterStatisticsDialoutsTornDown_Object = MibTableColumn
juniL2tpDialoutVRouterStatisticsDialoutsTornDown = _JuniL2tpDialoutVRouterStatisticsDialoutsTornDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 5, 3, 1, 35),
    _JuniL2tpDialoutVRouterStatisticsDialoutsTornDown_Type()
)
juniL2tpDialoutVRouterStatisticsDialoutsTornDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsDialoutsTornDown.setStatus("current")
_JuniL2tpDialoutSystem_ObjectIdentity = ObjectIdentity
juniL2tpDialoutSystem = _JuniL2tpDialoutSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6)
)


class _JuniL2tpDialoutSystemStatus_Type(Integer32):
    """Custom type juniL2tpDialoutSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("initIncomplete", 0),
          ("restricted", 2))
    )


_JuniL2tpDialoutSystemStatus_Type.__name__ = "Integer32"
_JuniL2tpDialoutSystemStatus_Object = MibScalar
juniL2tpDialoutSystemStatus = _JuniL2tpDialoutSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 1),
    _JuniL2tpDialoutSystemStatus_Type()
)
juniL2tpDialoutSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemStatus.setStatus("current")
_JuniL2tpDialoutSystemStatistics_ObjectIdentity = ObjectIdentity
juniL2tpDialoutSystemStatistics = _JuniL2tpDialoutSystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2)
)
_JuniL2tpDialoutSystemCurrentSessions_Type = Gauge32
_JuniL2tpDialoutSystemCurrentSessions_Object = MibScalar
juniL2tpDialoutSystemCurrentSessions = _JuniL2tpDialoutSystemCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 1),
    _JuniL2tpDialoutSystemCurrentSessions_Type()
)
juniL2tpDialoutSystemCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemCurrentSessions.setStatus("current")
_JuniL2tpDialoutSystemMaximumSessions_Type = Gauge32
_JuniL2tpDialoutSystemMaximumSessions_Object = MibScalar
juniL2tpDialoutSystemMaximumSessions = _JuniL2tpDialoutSystemMaximumSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 2),
    _JuniL2tpDialoutSystemMaximumSessions_Type()
)
juniL2tpDialoutSystemMaximumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemMaximumSessions.setStatus("current")
_JuniL2tpDialoutSystemSessionsConnecting_Type = Gauge32
_JuniL2tpDialoutSystemSessionsConnecting_Object = MibScalar
juniL2tpDialoutSystemSessionsConnecting = _JuniL2tpDialoutSystemSessionsConnecting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 3),
    _JuniL2tpDialoutSystemSessionsConnecting_Type()
)
juniL2tpDialoutSystemSessionsConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemSessionsConnecting.setStatus("current")
_JuniL2tpDialoutSystemMaximumSessionsConnecting_Type = Gauge32
_JuniL2tpDialoutSystemMaximumSessionsConnecting_Object = MibScalar
juniL2tpDialoutSystemMaximumSessionsConnecting = _JuniL2tpDialoutSystemMaximumSessionsConnecting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 4),
    _JuniL2tpDialoutSystemMaximumSessionsConnecting_Type()
)
juniL2tpDialoutSystemMaximumSessionsConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemMaximumSessionsConnecting.setStatus("current")
_JuniL2tpDialoutSystemSessionsPending_Type = Gauge32
_JuniL2tpDialoutSystemSessionsPending_Object = MibScalar
juniL2tpDialoutSystemSessionsPending = _JuniL2tpDialoutSystemSessionsPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 5),
    _JuniL2tpDialoutSystemSessionsPending_Type()
)
juniL2tpDialoutSystemSessionsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemSessionsPending.setStatus("current")
_JuniL2tpDialoutSystemMaximumSessionsPending_Type = Gauge32
_JuniL2tpDialoutSystemMaximumSessionsPending_Object = MibScalar
juniL2tpDialoutSystemMaximumSessionsPending = _JuniL2tpDialoutSystemMaximumSessionsPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 6),
    _JuniL2tpDialoutSystemMaximumSessionsPending_Type()
)
juniL2tpDialoutSystemMaximumSessionsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemMaximumSessionsPending.setStatus("current")
_JuniL2tpDialoutSystemTargetsInhibited_Type = Gauge32
_JuniL2tpDialoutSystemTargetsInhibited_Object = MibScalar
juniL2tpDialoutSystemTargetsInhibited = _JuniL2tpDialoutSystemTargetsInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 7),
    _JuniL2tpDialoutSystemTargetsInhibited_Type()
)
juniL2tpDialoutSystemTargetsInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemTargetsInhibited.setStatus("current")
_JuniL2tpDialoutSystemMaximumTargetsInhibited_Type = Gauge32
_JuniL2tpDialoutSystemMaximumTargetsInhibited_Object = MibScalar
juniL2tpDialoutSystemMaximumTargetsInhibited = _JuniL2tpDialoutSystemMaximumTargetsInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 8),
    _JuniL2tpDialoutSystemMaximumTargetsInhibited_Type()
)
juniL2tpDialoutSystemMaximumTargetsInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemMaximumTargetsInhibited.setStatus("current")
_JuniL2tpDialoutSystemAuthGrantNoSession_Type = Counter32
_JuniL2tpDialoutSystemAuthGrantNoSession_Object = MibScalar
juniL2tpDialoutSystemAuthGrantNoSession = _JuniL2tpDialoutSystemAuthGrantNoSession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 9),
    _JuniL2tpDialoutSystemAuthGrantNoSession_Type()
)
juniL2tpDialoutSystemAuthGrantNoSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemAuthGrantNoSession.setStatus("current")
_JuniL2tpDialoutSystemAuthDenyNoSession_Type = Counter32
_JuniL2tpDialoutSystemAuthDenyNoSession_Object = MibScalar
juniL2tpDialoutSystemAuthDenyNoSession = _JuniL2tpDialoutSystemAuthDenyNoSession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 1, 6, 2, 10),
    _JuniL2tpDialoutSystemAuthDenyNoSession_Type()
)
juniL2tpDialoutSystemAuthDenyNoSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemAuthDenyNoSession.setStatus("current")
_JuniL2tpDialoutMIBConformance_ObjectIdentity = ObjectIdentity
juniL2tpDialoutMIBConformance = _JuniL2tpDialoutMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2)
)
_JuniL2tpDialoutMIBCompliances_ObjectIdentity = ObjectIdentity
juniL2tpDialoutMIBCompliances = _JuniL2tpDialoutMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 1)
)
_JuniL2tpDialoutMIBGroups_ObjectIdentity = ObjectIdentity
juniL2tpDialoutMIBGroups = _JuniL2tpDialoutMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2)
)

# Managed Objects groups

juniL2tpDialoutTimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 1)
)
juniL2tpDialoutTimersGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutConnectingTimerValue"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutDormantTimerValue"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTimersGroup.setStatus("current")

juniL2tpDialoutTargetConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 2)
)
juniL2tpDialoutTargetConfigGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetDomainName"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetProfileName"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetRowStatus"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetConfigGroup.setStatus("current")

juniL2tpDialoutTriggerBuffersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 3)
)
juniL2tpDialoutTriggerBuffersGroup.setObjects(
    ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTriggerBufferCount")
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTriggerBuffersGroup.setStatus("current")

juniL2tpDialoutSessionControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 4)
)
juniL2tpDialoutSessionControlGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionConfigControl"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionConfigRowStatus"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionControlGroup.setStatus("current")

juniL2tpDialoutStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 5)
)
juniL2tpDialoutStatusGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemStatus"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatus"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatus"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatus"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutStatusGroup.setStatus("current")

juniL2tpDialoutSystemStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 6)
)
juniL2tpDialoutSystemStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemCurrentSessions"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemMaximumSessions"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemSessionsConnecting"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemMaximumSessionsConnecting"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemSessionsPending"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemMaximumSessionsPending"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemTargetsInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemMaximumTargetsInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemAuthGrantNoSession"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSystemAuthDenyNoSession"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemStatisticsGroup.setStatus("current")

juniL2tpDialoutSystemWideVRouterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 7)
)
juniL2tpDialoutSystemWideVRouterStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersInitPending"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersInitFailed"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersDown"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersInService"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersTriggersMissed"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersTriggerRouteUnknown"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsDormant"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsPending"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsAuthenticating"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsConnecting"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsInService"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsPostInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRoutersSessionsFailed"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemWideVRouterStatisticsGroup.setStatus("current")

juniL2tpDialoutSystemWideTargetStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 8)
)
juniL2tpDialoutSystemWideTargetStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetsDown"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetsInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetsInService"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetTriggersDiscarded"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemWideTargetStatisticsGroup.setStatus("current")

juniL2tpDialoutSystemWideSessionStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 9)
)
juniL2tpDialoutSystemWideSessionStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionsReset"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionTriggersReceived"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionTriggersEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionTriggersDiscarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionTriggersForwarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionTriggersMaxEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionAuthenticationRequests"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionAuthenticationNoResources"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionAuthenticationGrants"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionAuthenticationDenies"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionDialoutsRequested"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionDialoutsRejected"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionDialoutsEstablished"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionDialoutsTimedout"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionDialoutsTornDown"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSystemWideSessionStatisticsGroup.setStatus("current")

juniL2tpDialoutVRouterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 10)
)
juniL2tpDialoutVRouterStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggersMissed"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggerRouteUnknown"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStateDormant"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStatePending"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStateAuthenticating"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStateConnecting"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStateInService"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStateInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStatePostInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionStateFailed"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTargetsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTargetsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTargetsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTargetsDown"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTargetsInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTargetsInService"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsSessionsReset"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggersReceived"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggersEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggersDiscarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggersForwarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsAuthenticationRequests"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsAuthenticationNoResources"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsAuthenticationGrants"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsAuthenticationDenies"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsDialoutsRequested"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsDialoutsRejected"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsDialoutsEstablished"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsDialoutsTimedout"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutVRouterStatisticsDialoutsTornDown"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutVRouterStatisticsGroup.setStatus("current")

juniL2tpDialoutTargetStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 11)
)
juniL2tpDialoutTargetStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTargetsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTargetsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTargetsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTargetsDown"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTargetsInhibited"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTargetsInService"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsSessionsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsSessionsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsSessionsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsSessionsReset"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTriggersReceived"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTriggersEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTriggersDiscarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTriggersForwarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsTriggersMaxEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsAuthenticationRequests"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsAuthenticationNoResources"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsAuthenticationGrants"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsAuthenticationDenies"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsDialoutsRequested"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsDialoutsRejected"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsDialoutsEstablished"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsDialoutsTimedout"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutTargetStatisticsDialoutsTornDown"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutTargetStatisticsGroup.setStatus("current")

juniL2tpDialoutSessionStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 2, 12)
)
juniL2tpDialoutSessionStatisticsGroup.setObjects(
      *(("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsSessionsActive"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsSessionsCreated"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsSessionsRemoved"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsSessionsReset"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTriggersReceived"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTriggersEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTriggersDiscarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTriggersForwarded"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsTriggersMaxEnqueued"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsAuthenticationRequests"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsAuthenticationNoResources"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsAuthenticationGrants"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsAuthenticationDenies"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsDialoutsRequested"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsDialoutsRejected"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsDialoutsEstablished"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsDialoutsTimedout"),
        ("Juniper-L2TP-Dialout-MIB", "juniL2tpDialoutSessionStatisticsDialoutsTornDown"))
)
if mibBuilder.loadTexts:
    juniL2tpDialoutSessionStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniL2tpDialoutCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDialoutCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-L2TP-Dialout-MIB",
    **{"JuniL2tpDialoutDomainName": JuniL2tpDialoutDomainName,
       "juniL2tpDialoutMIB": juniL2tpDialoutMIB,
       "juniL2tpDialoutMIBNotifications": juniL2tpDialoutMIBNotifications,
       "juniL2tpDialoutMIBObjects": juniL2tpDialoutMIBObjects,
       "juniL2tpDialoutGeneral": juniL2tpDialoutGeneral,
       "juniL2tpDialoutConnectingTimerValue": juniL2tpDialoutConnectingTimerValue,
       "juniL2tpDialoutDormantTimerValue": juniL2tpDialoutDormantTimerValue,
       "juniL2tpDialoutTarget": juniL2tpDialoutTarget,
       "juniL2tpDialoutTargetConfigTable": juniL2tpDialoutTargetConfigTable,
       "juniL2tpDialoutTargetConfigEntry": juniL2tpDialoutTargetConfigEntry,
       "juniL2tpDialoutTargetRouterIndex": juniL2tpDialoutTargetRouterIndex,
       "juniL2tpDialoutTargetIpAddress": juniL2tpDialoutTargetIpAddress,
       "juniL2tpDialoutTargetIpAddressMask": juniL2tpDialoutTargetIpAddressMask,
       "juniL2tpDialoutTargetDomainName": juniL2tpDialoutTargetDomainName,
       "juniL2tpDialoutTargetProfileName": juniL2tpDialoutTargetProfileName,
       "juniL2tpDialoutTargetRowStatus": juniL2tpDialoutTargetRowStatus,
       "juniL2tpDialoutTargetStatusTable": juniL2tpDialoutTargetStatusTable,
       "juniL2tpDialoutTargetStatusEntry": juniL2tpDialoutTargetStatusEntry,
       "juniL2tpDialoutTargetStatusRouterIndex": juniL2tpDialoutTargetStatusRouterIndex,
       "juniL2tpDialoutTargetStatusIpAddress": juniL2tpDialoutTargetStatusIpAddress,
       "juniL2tpDialoutTargetStatusIpAddressMask": juniL2tpDialoutTargetStatusIpAddressMask,
       "juniL2tpDialoutTargetStatus": juniL2tpDialoutTargetStatus,
       "juniL2tpDialoutTargetSystemStatistics": juniL2tpDialoutTargetSystemStatistics,
       "juniL2tpDialoutTargetsActive": juniL2tpDialoutTargetsActive,
       "juniL2tpDialoutTargetsCreated": juniL2tpDialoutTargetsCreated,
       "juniL2tpDialoutTargetsRemoved": juniL2tpDialoutTargetsRemoved,
       "juniL2tpDialoutTargetsDown": juniL2tpDialoutTargetsDown,
       "juniL2tpDialoutTargetsInhibited": juniL2tpDialoutTargetsInhibited,
       "juniL2tpDialoutTargetsInService": juniL2tpDialoutTargetsInService,
       "juniL2tpDialoutTargetTriggersDiscarded": juniL2tpDialoutTargetTriggersDiscarded,
       "juniL2tpDialoutTargetStatisticsTable": juniL2tpDialoutTargetStatisticsTable,
       "juniL2tpDialoutTargetStatisticsEntry": juniL2tpDialoutTargetStatisticsEntry,
       "juniL2tpDialoutTargetStatisticsRouterIndex": juniL2tpDialoutTargetStatisticsRouterIndex,
       "juniL2tpDialoutTargetStatisticsIpAddress": juniL2tpDialoutTargetStatisticsIpAddress,
       "juniL2tpDialoutTargetStatisticsIpAddressMask": juniL2tpDialoutTargetStatisticsIpAddressMask,
       "juniL2tpDialoutTargetStatisticsTargetsActive": juniL2tpDialoutTargetStatisticsTargetsActive,
       "juniL2tpDialoutTargetStatisticsTargetsCreated": juniL2tpDialoutTargetStatisticsTargetsCreated,
       "juniL2tpDialoutTargetStatisticsTargetsRemoved": juniL2tpDialoutTargetStatisticsTargetsRemoved,
       "juniL2tpDialoutTargetStatisticsTargetsDown": juniL2tpDialoutTargetStatisticsTargetsDown,
       "juniL2tpDialoutTargetStatisticsTargetsInhibited": juniL2tpDialoutTargetStatisticsTargetsInhibited,
       "juniL2tpDialoutTargetStatisticsTargetsInService": juniL2tpDialoutTargetStatisticsTargetsInService,
       "juniL2tpDialoutTargetStatisticsSessionsActive": juniL2tpDialoutTargetStatisticsSessionsActive,
       "juniL2tpDialoutTargetStatisticsSessionsCreated": juniL2tpDialoutTargetStatisticsSessionsCreated,
       "juniL2tpDialoutTargetStatisticsSessionsRemoved": juniL2tpDialoutTargetStatisticsSessionsRemoved,
       "juniL2tpDialoutTargetStatisticsSessionsReset": juniL2tpDialoutTargetStatisticsSessionsReset,
       "juniL2tpDialoutTargetStatisticsTriggersReceived": juniL2tpDialoutTargetStatisticsTriggersReceived,
       "juniL2tpDialoutTargetStatisticsTriggersEnqueued": juniL2tpDialoutTargetStatisticsTriggersEnqueued,
       "juniL2tpDialoutTargetStatisticsTriggersDiscarded": juniL2tpDialoutTargetStatisticsTriggersDiscarded,
       "juniL2tpDialoutTargetStatisticsTriggersForwarded": juniL2tpDialoutTargetStatisticsTriggersForwarded,
       "juniL2tpDialoutTargetStatisticsTriggersMaxEnqueued": juniL2tpDialoutTargetStatisticsTriggersMaxEnqueued,
       "juniL2tpDialoutTargetStatisticsAuthenticationRequests": juniL2tpDialoutTargetStatisticsAuthenticationRequests,
       "juniL2tpDialoutTargetStatisticsAuthenticationNoResources": juniL2tpDialoutTargetStatisticsAuthenticationNoResources,
       "juniL2tpDialoutTargetStatisticsAuthenticationGrants": juniL2tpDialoutTargetStatisticsAuthenticationGrants,
       "juniL2tpDialoutTargetStatisticsAuthenticationDenies": juniL2tpDialoutTargetStatisticsAuthenticationDenies,
       "juniL2tpDialoutTargetStatisticsDialoutsRequested": juniL2tpDialoutTargetStatisticsDialoutsRequested,
       "juniL2tpDialoutTargetStatisticsDialoutsRejected": juniL2tpDialoutTargetStatisticsDialoutsRejected,
       "juniL2tpDialoutTargetStatisticsDialoutsEstablished": juniL2tpDialoutTargetStatisticsDialoutsEstablished,
       "juniL2tpDialoutTargetStatisticsDialoutsTimedout": juniL2tpDialoutTargetStatisticsDialoutsTimedout,
       "juniL2tpDialoutTargetStatisticsDialoutsTornDown": juniL2tpDialoutTargetStatisticsDialoutsTornDown,
       "juniL2tpDialoutTriggerBuffer": juniL2tpDialoutTriggerBuffer,
       "juniL2tpDialoutTriggerBufferTable": juniL2tpDialoutTriggerBufferTable,
       "juniL2tpDialoutTriggerBufferEntry": juniL2tpDialoutTriggerBufferEntry,
       "juniL2tpDialoutTriggerBufferRouterIndex": juniL2tpDialoutTriggerBufferRouterIndex,
       "juniL2tpDialoutTriggerBufferCount": juniL2tpDialoutTriggerBufferCount,
       "juniL2tpDialoutSession": juniL2tpDialoutSession,
       "juniL2tpDialoutSessionConfigTable": juniL2tpDialoutSessionConfigTable,
       "juniL2tpDialoutSessionConfigEntry": juniL2tpDialoutSessionConfigEntry,
       "juniL2tpDialoutSessionConfigHandle": juniL2tpDialoutSessionConfigHandle,
       "juniL2tpDialoutSessionConfigTargetIpAddress": juniL2tpDialoutSessionConfigTargetIpAddress,
       "juniL2tpDialoutSessionConfigTargetIpAddressMask": juniL2tpDialoutSessionConfigTargetIpAddressMask,
       "juniL2tpDialoutSessionConfigRouterIndex": juniL2tpDialoutSessionConfigRouterIndex,
       "juniL2tpDialoutSessionConfigControl": juniL2tpDialoutSessionConfigControl,
       "juniL2tpDialoutSessionConfigRowStatus": juniL2tpDialoutSessionConfigRowStatus,
       "juniL2tpDialoutSessionStatusTable": juniL2tpDialoutSessionStatusTable,
       "juniL2tpDialoutSessionStatusEntry": juniL2tpDialoutSessionStatusEntry,
       "juniL2tpDialoutSessionStatusHandle": juniL2tpDialoutSessionStatusHandle,
       "juniL2tpDialoutSessionStatusTargetIpAddress": juniL2tpDialoutSessionStatusTargetIpAddress,
       "juniL2tpDialoutSessionStatusTargetIpAddressMask": juniL2tpDialoutSessionStatusTargetIpAddressMask,
       "juniL2tpDialoutSessionStatusRouterIndex": juniL2tpDialoutSessionStatusRouterIndex,
       "juniL2tpDialoutSessionStatus": juniL2tpDialoutSessionStatus,
       "juniL2tpDialoutSessionSystemStatistics": juniL2tpDialoutSessionSystemStatistics,
       "juniL2tpDialoutSessionsActive": juniL2tpDialoutSessionsActive,
       "juniL2tpDialoutSessionsCreated": juniL2tpDialoutSessionsCreated,
       "juniL2tpDialoutSessionsRemoved": juniL2tpDialoutSessionsRemoved,
       "juniL2tpDialoutSessionsReset": juniL2tpDialoutSessionsReset,
       "juniL2tpDialoutSessionTriggersReceived": juniL2tpDialoutSessionTriggersReceived,
       "juniL2tpDialoutSessionTriggersEnqueued": juniL2tpDialoutSessionTriggersEnqueued,
       "juniL2tpDialoutSessionTriggersDiscarded": juniL2tpDialoutSessionTriggersDiscarded,
       "juniL2tpDialoutSessionTriggersForwarded": juniL2tpDialoutSessionTriggersForwarded,
       "juniL2tpDialoutSessionTriggersMaxEnqueued": juniL2tpDialoutSessionTriggersMaxEnqueued,
       "juniL2tpDialoutSessionAuthenticationRequests": juniL2tpDialoutSessionAuthenticationRequests,
       "juniL2tpDialoutSessionAuthenticationNoResources": juniL2tpDialoutSessionAuthenticationNoResources,
       "juniL2tpDialoutSessionAuthenticationGrants": juniL2tpDialoutSessionAuthenticationGrants,
       "juniL2tpDialoutSessionAuthenticationDenies": juniL2tpDialoutSessionAuthenticationDenies,
       "juniL2tpDialoutSessionDialoutsRequested": juniL2tpDialoutSessionDialoutsRequested,
       "juniL2tpDialoutSessionDialoutsRejected": juniL2tpDialoutSessionDialoutsRejected,
       "juniL2tpDialoutSessionDialoutsEstablished": juniL2tpDialoutSessionDialoutsEstablished,
       "juniL2tpDialoutSessionDialoutsTimedout": juniL2tpDialoutSessionDialoutsTimedout,
       "juniL2tpDialoutSessionDialoutsTornDown": juniL2tpDialoutSessionDialoutsTornDown,
       "juniL2tpDialoutSessionStatisticsTable": juniL2tpDialoutSessionStatisticsTable,
       "juniL2tpDialoutSessionStatisticsEntry": juniL2tpDialoutSessionStatisticsEntry,
       "juniL2tpDialoutSessionStatisticsHandle": juniL2tpDialoutSessionStatisticsHandle,
       "juniL2tpDialoutSessionStatisticsTargetIpAddress": juniL2tpDialoutSessionStatisticsTargetIpAddress,
       "juniL2tpDialoutSessionStatisticsTargetIpAddressMask": juniL2tpDialoutSessionStatisticsTargetIpAddressMask,
       "juniL2tpDialoutSessionStatisticsRouterIndex": juniL2tpDialoutSessionStatisticsRouterIndex,
       "juniL2tpDialoutSessionStatisticsSessionsActive": juniL2tpDialoutSessionStatisticsSessionsActive,
       "juniL2tpDialoutSessionStatisticsSessionsCreated": juniL2tpDialoutSessionStatisticsSessionsCreated,
       "juniL2tpDialoutSessionStatisticsSessionsRemoved": juniL2tpDialoutSessionStatisticsSessionsRemoved,
       "juniL2tpDialoutSessionStatisticsSessionsReset": juniL2tpDialoutSessionStatisticsSessionsReset,
       "juniL2tpDialoutSessionStatisticsTriggersReceived": juniL2tpDialoutSessionStatisticsTriggersReceived,
       "juniL2tpDialoutSessionStatisticsTriggersEnqueued": juniL2tpDialoutSessionStatisticsTriggersEnqueued,
       "juniL2tpDialoutSessionStatisticsTriggersDiscarded": juniL2tpDialoutSessionStatisticsTriggersDiscarded,
       "juniL2tpDialoutSessionStatisticsTriggersForwarded": juniL2tpDialoutSessionStatisticsTriggersForwarded,
       "juniL2tpDialoutSessionStatisticsTriggersMaxEnqueued": juniL2tpDialoutSessionStatisticsTriggersMaxEnqueued,
       "juniL2tpDialoutSessionStatisticsAuthenticationRequests": juniL2tpDialoutSessionStatisticsAuthenticationRequests,
       "juniL2tpDialoutSessionStatisticsAuthenticationNoResources": juniL2tpDialoutSessionStatisticsAuthenticationNoResources,
       "juniL2tpDialoutSessionStatisticsAuthenticationGrants": juniL2tpDialoutSessionStatisticsAuthenticationGrants,
       "juniL2tpDialoutSessionStatisticsAuthenticationDenies": juniL2tpDialoutSessionStatisticsAuthenticationDenies,
       "juniL2tpDialoutSessionStatisticsDialoutsRequested": juniL2tpDialoutSessionStatisticsDialoutsRequested,
       "juniL2tpDialoutSessionStatisticsDialoutsRejected": juniL2tpDialoutSessionStatisticsDialoutsRejected,
       "juniL2tpDialoutSessionStatisticsDialoutsEstablished": juniL2tpDialoutSessionStatisticsDialoutsEstablished,
       "juniL2tpDialoutSessionStatisticsDialoutsTimedout": juniL2tpDialoutSessionStatisticsDialoutsTimedout,
       "juniL2tpDialoutSessionStatisticsDialoutsTornDown": juniL2tpDialoutSessionStatisticsDialoutsTornDown,
       "juniL2tpDialoutVRouter": juniL2tpDialoutVRouter,
       "juniL2tpDialoutVRouterStatusTable": juniL2tpDialoutVRouterStatusTable,
       "juniL2tpDialoutVRouterStatusEntry": juniL2tpDialoutVRouterStatusEntry,
       "juniL2tpDialoutVRouterStatusRouterIndex": juniL2tpDialoutVRouterStatusRouterIndex,
       "juniL2tpDialoutVRouterStatus": juniL2tpDialoutVRouterStatus,
       "juniL2tpDialoutVRouterSystemStatistics": juniL2tpDialoutVRouterSystemStatistics,
       "juniL2tpDialoutVRoutersActive": juniL2tpDialoutVRoutersActive,
       "juniL2tpDialoutVRoutersCreated": juniL2tpDialoutVRoutersCreated,
       "juniL2tpDialoutVRoutersRemoved": juniL2tpDialoutVRoutersRemoved,
       "juniL2tpDialoutVRoutersInitPending": juniL2tpDialoutVRoutersInitPending,
       "juniL2tpDialoutVRoutersInitFailed": juniL2tpDialoutVRoutersInitFailed,
       "juniL2tpDialoutVRoutersDown": juniL2tpDialoutVRoutersDown,
       "juniL2tpDialoutVRoutersInService": juniL2tpDialoutVRoutersInService,
       "juniL2tpDialoutVRoutersTriggersMissed": juniL2tpDialoutVRoutersTriggersMissed,
       "juniL2tpDialoutVRoutersTriggerRouteUnknown": juniL2tpDialoutVRoutersTriggerRouteUnknown,
       "juniL2tpDialoutVRoutersSessionsDormant": juniL2tpDialoutVRoutersSessionsDormant,
       "juniL2tpDialoutVRoutersSessionsPending": juniL2tpDialoutVRoutersSessionsPending,
       "juniL2tpDialoutVRoutersSessionsAuthenticating": juniL2tpDialoutVRoutersSessionsAuthenticating,
       "juniL2tpDialoutVRoutersSessionsConnecting": juniL2tpDialoutVRoutersSessionsConnecting,
       "juniL2tpDialoutVRoutersSessionsInService": juniL2tpDialoutVRoutersSessionsInService,
       "juniL2tpDialoutVRoutersSessionsInhibited": juniL2tpDialoutVRoutersSessionsInhibited,
       "juniL2tpDialoutVRoutersSessionsPostInhibited": juniL2tpDialoutVRoutersSessionsPostInhibited,
       "juniL2tpDialoutVRoutersSessionsFailed": juniL2tpDialoutVRoutersSessionsFailed,
       "juniL2tpDialoutVRouterStatisticsTable": juniL2tpDialoutVRouterStatisticsTable,
       "juniL2tpDialoutVRouterStatisticsEntry": juniL2tpDialoutVRouterStatisticsEntry,
       "juniL2tpDialoutVRouterStatisticsRouterIndex": juniL2tpDialoutVRouterStatisticsRouterIndex,
       "juniL2tpDialoutVRouterStatisticsTriggersMissed": juniL2tpDialoutVRouterStatisticsTriggersMissed,
       "juniL2tpDialoutVRouterStatisticsTriggerRouteUnknown": juniL2tpDialoutVRouterStatisticsTriggerRouteUnknown,
       "juniL2tpDialoutVRouterStatisticsSessionStateDormant": juniL2tpDialoutVRouterStatisticsSessionStateDormant,
       "juniL2tpDialoutVRouterStatisticsSessionStatePending": juniL2tpDialoutVRouterStatisticsSessionStatePending,
       "juniL2tpDialoutVRouterStatisticsSessionStateAuthenticating": juniL2tpDialoutVRouterStatisticsSessionStateAuthenticating,
       "juniL2tpDialoutVRouterStatisticsSessionStateConnecting": juniL2tpDialoutVRouterStatisticsSessionStateConnecting,
       "juniL2tpDialoutVRouterStatisticsSessionStateInService": juniL2tpDialoutVRouterStatisticsSessionStateInService,
       "juniL2tpDialoutVRouterStatisticsSessionStateInhibited": juniL2tpDialoutVRouterStatisticsSessionStateInhibited,
       "juniL2tpDialoutVRouterStatisticsSessionStatePostInhibited": juniL2tpDialoutVRouterStatisticsSessionStatePostInhibited,
       "juniL2tpDialoutVRouterStatisticsSessionStateFailed": juniL2tpDialoutVRouterStatisticsSessionStateFailed,
       "juniL2tpDialoutVRouterStatisticsTargetsActive": juniL2tpDialoutVRouterStatisticsTargetsActive,
       "juniL2tpDialoutVRouterStatisticsTargetsCreated": juniL2tpDialoutVRouterStatisticsTargetsCreated,
       "juniL2tpDialoutVRouterStatisticsTargetsRemoved": juniL2tpDialoutVRouterStatisticsTargetsRemoved,
       "juniL2tpDialoutVRouterStatisticsTargetsDown": juniL2tpDialoutVRouterStatisticsTargetsDown,
       "juniL2tpDialoutVRouterStatisticsTargetsInhibited": juniL2tpDialoutVRouterStatisticsTargetsInhibited,
       "juniL2tpDialoutVRouterStatisticsTargetsInService": juniL2tpDialoutVRouterStatisticsTargetsInService,
       "juniL2tpDialoutVRouterStatisticsSessionsActive": juniL2tpDialoutVRouterStatisticsSessionsActive,
       "juniL2tpDialoutVRouterStatisticsSessionsCreated": juniL2tpDialoutVRouterStatisticsSessionsCreated,
       "juniL2tpDialoutVRouterStatisticsSessionsRemoved": juniL2tpDialoutVRouterStatisticsSessionsRemoved,
       "juniL2tpDialoutVRouterStatisticsSessionsReset": juniL2tpDialoutVRouterStatisticsSessionsReset,
       "juniL2tpDialoutVRouterStatisticsTriggersReceived": juniL2tpDialoutVRouterStatisticsTriggersReceived,
       "juniL2tpDialoutVRouterStatisticsTriggersEnqueued": juniL2tpDialoutVRouterStatisticsTriggersEnqueued,
       "juniL2tpDialoutVRouterStatisticsTriggersDiscarded": juniL2tpDialoutVRouterStatisticsTriggersDiscarded,
       "juniL2tpDialoutVRouterStatisticsTriggersForwarded": juniL2tpDialoutVRouterStatisticsTriggersForwarded,
       "juniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued": juniL2tpDialoutVRouterStatisticsTriggersMaxEnqueued,
       "juniL2tpDialoutVRouterStatisticsAuthenticationRequests": juniL2tpDialoutVRouterStatisticsAuthenticationRequests,
       "juniL2tpDialoutVRouterStatisticsAuthenticationNoResources": juniL2tpDialoutVRouterStatisticsAuthenticationNoResources,
       "juniL2tpDialoutVRouterStatisticsAuthenticationGrants": juniL2tpDialoutVRouterStatisticsAuthenticationGrants,
       "juniL2tpDialoutVRouterStatisticsAuthenticationDenies": juniL2tpDialoutVRouterStatisticsAuthenticationDenies,
       "juniL2tpDialoutVRouterStatisticsDialoutsRequested": juniL2tpDialoutVRouterStatisticsDialoutsRequested,
       "juniL2tpDialoutVRouterStatisticsDialoutsRejected": juniL2tpDialoutVRouterStatisticsDialoutsRejected,
       "juniL2tpDialoutVRouterStatisticsDialoutsEstablished": juniL2tpDialoutVRouterStatisticsDialoutsEstablished,
       "juniL2tpDialoutVRouterStatisticsDialoutsTimedout": juniL2tpDialoutVRouterStatisticsDialoutsTimedout,
       "juniL2tpDialoutVRouterStatisticsDialoutsTornDown": juniL2tpDialoutVRouterStatisticsDialoutsTornDown,
       "juniL2tpDialoutSystem": juniL2tpDialoutSystem,
       "juniL2tpDialoutSystemStatus": juniL2tpDialoutSystemStatus,
       "juniL2tpDialoutSystemStatistics": juniL2tpDialoutSystemStatistics,
       "juniL2tpDialoutSystemCurrentSessions": juniL2tpDialoutSystemCurrentSessions,
       "juniL2tpDialoutSystemMaximumSessions": juniL2tpDialoutSystemMaximumSessions,
       "juniL2tpDialoutSystemSessionsConnecting": juniL2tpDialoutSystemSessionsConnecting,
       "juniL2tpDialoutSystemMaximumSessionsConnecting": juniL2tpDialoutSystemMaximumSessionsConnecting,
       "juniL2tpDialoutSystemSessionsPending": juniL2tpDialoutSystemSessionsPending,
       "juniL2tpDialoutSystemMaximumSessionsPending": juniL2tpDialoutSystemMaximumSessionsPending,
       "juniL2tpDialoutSystemTargetsInhibited": juniL2tpDialoutSystemTargetsInhibited,
       "juniL2tpDialoutSystemMaximumTargetsInhibited": juniL2tpDialoutSystemMaximumTargetsInhibited,
       "juniL2tpDialoutSystemAuthGrantNoSession": juniL2tpDialoutSystemAuthGrantNoSession,
       "juniL2tpDialoutSystemAuthDenyNoSession": juniL2tpDialoutSystemAuthDenyNoSession,
       "juniL2tpDialoutMIBConformance": juniL2tpDialoutMIBConformance,
       "juniL2tpDialoutMIBCompliances": juniL2tpDialoutMIBCompliances,
       "juniL2tpDialoutCompliance": juniL2tpDialoutCompliance,
       "juniL2tpDialoutMIBGroups": juniL2tpDialoutMIBGroups,
       "juniL2tpDialoutTimersGroup": juniL2tpDialoutTimersGroup,
       "juniL2tpDialoutTargetConfigGroup": juniL2tpDialoutTargetConfigGroup,
       "juniL2tpDialoutTriggerBuffersGroup": juniL2tpDialoutTriggerBuffersGroup,
       "juniL2tpDialoutSessionControlGroup": juniL2tpDialoutSessionControlGroup,
       "juniL2tpDialoutStatusGroup": juniL2tpDialoutStatusGroup,
       "juniL2tpDialoutSystemStatisticsGroup": juniL2tpDialoutSystemStatisticsGroup,
       "juniL2tpDialoutSystemWideVRouterStatisticsGroup": juniL2tpDialoutSystemWideVRouterStatisticsGroup,
       "juniL2tpDialoutSystemWideTargetStatisticsGroup": juniL2tpDialoutSystemWideTargetStatisticsGroup,
       "juniL2tpDialoutSystemWideSessionStatisticsGroup": juniL2tpDialoutSystemWideSessionStatisticsGroup,
       "juniL2tpDialoutVRouterStatisticsGroup": juniL2tpDialoutVRouterStatisticsGroup,
       "juniL2tpDialoutTargetStatisticsGroup": juniL2tpDialoutTargetStatisticsGroup,
       "juniL2tpDialoutSessionStatisticsGroup": juniL2tpDialoutSessionStatisticsGroup}
)
