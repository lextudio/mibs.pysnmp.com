# SNMP MIB module (CISCO-IETF-MEGACO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-MEGACO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:56 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

ciscoIetfMegacoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999)
)
ciscoIetfMegacoMIB.setRevisions(
        ("2003-04-28 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CMediaGatewayId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CMediaGatewayLinkId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CMediaGatewayTermId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIetfMegacoMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfMegacoMIBNotifs = _CiscoIetfMegacoMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 0)
)
_CiscoIetfMegacoMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfMegacoMIBObjects = _CiscoIetfMegacoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1)
)
_CmedConfiguration_ObjectIdentity = ObjectIdentity
cmedConfiguration = _CmedConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1)
)
_CmedLinkIdTable_Object = MibTable
cmedLinkIdTable = _CmedLinkIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmedLinkIdTable.setStatus("current")
_CmedLinkIdEntry_Object = MibTableRow
cmedLinkIdEntry = _CmedLinkIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 1, 1)
)
cmedLinkIdEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
)
if mibBuilder.loadTexts:
    cmedLinkIdEntry.setStatus("current")
_CmedNextLinkId_Type = TestAndIncr
_CmedNextLinkId_Object = MibTableColumn
cmedNextLinkId = _CmedNextLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 1, 1, 1),
    _CmedNextLinkId_Type()
)
cmedNextLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedNextLinkId.setStatus("current")
_CmedGatewayConfigTable_Object = MibTable
cmedGatewayConfigTable = _CmedGatewayConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmedGatewayConfigTable.setStatus("current")
_CmedGatewayConfigEntry_Object = MibTableRow
cmedGatewayConfigEntry = _CmedGatewayConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1)
)
cmedGatewayConfigEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkId"),
)
if mibBuilder.loadTexts:
    cmedGatewayConfigEntry.setStatus("current")
_CmedGatewayId_Type = CMediaGatewayId
_CmedGatewayId_Object = MibTableColumn
cmedGatewayId = _CmedGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 1),
    _CmedGatewayId_Type()
)
cmedGatewayId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedGatewayId.setStatus("current")
_CmedGatewayLinkId_Type = CMediaGatewayLinkId
_CmedGatewayLinkId_Object = MibTableColumn
cmedGatewayLinkId = _CmedGatewayLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 2),
    _CmedGatewayLinkId_Type()
)
cmedGatewayLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedGatewayLinkId.setStatus("current")


class _CmedGatewayLinkName_Type(SnmpAdminString):
    """Custom type cmedGatewayLinkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmedGatewayLinkName_Type.__name__ = "SnmpAdminString"
_CmedGatewayLinkName_Object = MibTableColumn
cmedGatewayLinkName = _CmedGatewayLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 3),
    _CmedGatewayLinkName_Type()
)
cmedGatewayLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayLinkName.setStatus("current")
_CmedGatewayIPAddress_Type = IpAddress
_CmedGatewayIPAddress_Object = MibTableColumn
cmedGatewayIPAddress = _CmedGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 4),
    _CmedGatewayIPAddress_Type()
)
cmedGatewayIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayIPAddress.setStatus("current")


class _CmedGatewayPort_Type(Integer32):
    """Custom type cmedGatewayPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedGatewayPort_Type.__name__ = "Integer32"
_CmedGatewayPort_Object = MibTableColumn
cmedGatewayPort = _CmedGatewayPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 5),
    _CmedGatewayPort_Type()
)
cmedGatewayPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayPort.setStatus("current")


class _CmedGatewayEncodingScheme_Type(Integer32):
    """Custom type cmedGatewayEncodingScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("binary", 2),
          ("text", 1))
    )


_CmedGatewayEncodingScheme_Type.__name__ = "Integer32"
_CmedGatewayEncodingScheme_Object = MibTableColumn
cmedGatewayEncodingScheme = _CmedGatewayEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 6),
    _CmedGatewayEncodingScheme_Type()
)
cmedGatewayEncodingScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayEncodingScheme.setStatus("current")


class _CmedGatewayProtocol_Type(Integer32):
    """Custom type cmedGatewayProtocol based on Integer32"""
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
        *(("dss1Ip", 3),
          ("ipdc", 4),
          ("megacov1", 5),
          ("megacov2", 6),
          ("mgcp", 7),
          ("notApplicable", 1),
          ("other", 2))
    )


_CmedGatewayProtocol_Type.__name__ = "Integer32"
_CmedGatewayProtocol_Object = MibTableColumn
cmedGatewayProtocol = _CmedGatewayProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 7),
    _CmedGatewayProtocol_Type()
)
cmedGatewayProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayProtocol.setStatus("current")


class _CmedGatewaySigTptProtocol_Type(Integer32):
    """Custom type cmedGatewaySigTptProtocol based on Integer32"""
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
        *(("other", 4),
          ("sctp", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_CmedGatewaySigTptProtocol_Type.__name__ = "Integer32"
_CmedGatewaySigTptProtocol_Object = MibTableColumn
cmedGatewaySigTptProtocol = _CmedGatewaySigTptProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 8),
    _CmedGatewaySigTptProtocol_Type()
)
cmedGatewaySigTptProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewaySigTptProtocol.setStatus("current")


class _CmedGatewayAdminStatus_Type(Integer32):
    """Custom type cmedGatewayAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CmedGatewayAdminStatus_Type.__name__ = "Integer32"
_CmedGatewayAdminStatus_Object = MibTableColumn
cmedGatewayAdminStatus = _CmedGatewayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 9),
    _CmedGatewayAdminStatus_Type()
)
cmedGatewayAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayAdminStatus.setStatus("current")


class _CmedGatewayOperStatus_Type(Integer32):
    """Custom type cmedGatewayOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CmedGatewayOperStatus_Type.__name__ = "Integer32"
_CmedGatewayOperStatus_Object = MibTableColumn
cmedGatewayOperStatus = _CmedGatewayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 10),
    _CmedGatewayOperStatus_Type()
)
cmedGatewayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedGatewayOperStatus.setStatus("current")
_CmedGatewayLastStatusChange_Type = TimeStamp
_CmedGatewayLastStatusChange_Object = MibTableColumn
cmedGatewayLastStatusChange = _CmedGatewayLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 11),
    _CmedGatewayLastStatusChange_Type()
)
cmedGatewayLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedGatewayLastStatusChange.setStatus("current")


class _CmedGatewayResetStatistics_Type(Integer32):
    """Custom type cmedGatewayResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("other", 2),
          ("reset", 3))
    )


_CmedGatewayResetStatistics_Type.__name__ = "Integer32"
_CmedGatewayResetStatistics_Object = MibTableColumn
cmedGatewayResetStatistics = _CmedGatewayResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 12),
    _CmedGatewayResetStatistics_Type()
)
cmedGatewayResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayResetStatistics.setStatus("current")
_CmedGatewayRowStatus_Type = RowStatus
_CmedGatewayRowStatus_Object = MibTableColumn
cmedGatewayRowStatus = _CmedGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 2, 1, 13),
    _CmedGatewayRowStatus_Type()
)
cmedGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedGatewayRowStatus.setStatus("current")
_CmedGwyControllerTable_Object = MibTable
cmedGwyControllerTable = _CmedGwyControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cmedGwyControllerTable.setStatus("current")
_CmedGwyControllerEntry_Object = MibTableRow
cmedGwyControllerEntry = _CmedGwyControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3, 1)
)
cmedGwyControllerEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGwyControllerId"),
)
if mibBuilder.loadTexts:
    cmedGwyControllerEntry.setStatus("current")


class _CmedGwyControllerId_Type(Unsigned32):
    """Custom type cmedGwyControllerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmedGwyControllerId_Type.__name__ = "Unsigned32"
_CmedGwyControllerId_Object = MibTableColumn
cmedGwyControllerId = _CmedGwyControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3, 1, 1),
    _CmedGwyControllerId_Type()
)
cmedGwyControllerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedGwyControllerId.setStatus("current")
_CmedGwyControllerIPAddress_Type = IpAddress
_CmedGwyControllerIPAddress_Object = MibTableColumn
cmedGwyControllerIPAddress = _CmedGwyControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3, 1, 2),
    _CmedGwyControllerIPAddress_Type()
)
cmedGwyControllerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedGwyControllerIPAddress.setStatus("current")


class _CmedGwyControllerPort_Type(Integer32):
    """Custom type cmedGwyControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmedGwyControllerPort_Type.__name__ = "Integer32"
_CmedGwyControllerPort_Object = MibTableColumn
cmedGwyControllerPort = _CmedGwyControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3, 1, 3),
    _CmedGwyControllerPort_Type()
)
cmedGwyControllerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedGwyControllerPort.setStatus("current")


class _CmedGwyControllerAdminStatus_Type(Integer32):
    """Custom type cmedGwyControllerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CmedGwyControllerAdminStatus_Type.__name__ = "Integer32"
_CmedGwyControllerAdminStatus_Object = MibTableColumn
cmedGwyControllerAdminStatus = _CmedGwyControllerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3, 1, 4),
    _CmedGwyControllerAdminStatus_Type()
)
cmedGwyControllerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedGwyControllerAdminStatus.setStatus("current")


class _CmedGwyControllerOperStatus_Type(Integer32):
    """Custom type cmedGwyControllerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("standby", 3),
          ("up", 1))
    )


_CmedGwyControllerOperStatus_Type.__name__ = "Integer32"
_CmedGwyControllerOperStatus_Object = MibTableColumn
cmedGwyControllerOperStatus = _CmedGwyControllerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 1, 3, 1, 5),
    _CmedGwyControllerOperStatus_Type()
)
cmedGwyControllerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedGwyControllerOperStatus.setStatus("current")
_CmedStatistics_ObjectIdentity = ObjectIdentity
cmedStatistics = _CmedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2)
)
_CmedGatewayStatsTable_Object = MibTable
cmedGatewayStatsTable = _CmedGatewayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmedGatewayStatsTable.setStatus("current")
_CmedGatewayStatsEntry_Object = MibTableRow
cmedGatewayStatsEntry = _CmedGatewayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1)
)
cmedGatewayStatsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkId"),
)
if mibBuilder.loadTexts:
    cmedGatewayStatsEntry.setStatus("current")
_CmedNumInMessages_Type = Counter32
_CmedNumInMessages_Object = MibTableColumn
cmedNumInMessages = _CmedNumInMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 1),
    _CmedNumInMessages_Type()
)
cmedNumInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedNumInMessages.setStatus("current")
_CmedNumInOctets_Type = Counter32
_CmedNumInOctets_Object = MibTableColumn
cmedNumInOctets = _CmedNumInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 2),
    _CmedNumInOctets_Type()
)
cmedNumInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedNumInOctets.setStatus("current")
_CmedNumOutMessages_Type = Counter32
_CmedNumOutMessages_Object = MibTableColumn
cmedNumOutMessages = _CmedNumOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 3),
    _CmedNumOutMessages_Type()
)
cmedNumOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedNumOutMessages.setStatus("current")
_CmedNumOutOctets_Type = Counter32
_CmedNumOutOctets_Object = MibTableColumn
cmedNumOutOctets = _CmedNumOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 4),
    _CmedNumOutOctets_Type()
)
cmedNumOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedNumOutOctets.setStatus("current")
_CmedNumErrors_Type = Counter32
_CmedNumErrors_Object = MibTableColumn
cmedNumErrors = _CmedNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 5),
    _CmedNumErrors_Type()
)
cmedNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedNumErrors.setStatus("current")
_CmedNumTimerRecovery_Type = Counter32
_CmedNumTimerRecovery_Object = MibTableColumn
cmedNumTimerRecovery = _CmedNumTimerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 6),
    _CmedNumTimerRecovery_Type()
)
cmedNumTimerRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedNumTimerRecovery.setStatus("current")
_CmedTransportNumLosses_Type = Counter32
_CmedTransportNumLosses_Object = MibTableColumn
cmedTransportNumLosses = _CmedTransportNumLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 7),
    _CmedTransportNumLosses_Type()
)
cmedTransportNumLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedTransportNumLosses.setStatus("current")
_CmedTransportNumSwitchover_Type = Counter32
_CmedTransportNumSwitchover_Object = MibTableColumn
cmedTransportNumSwitchover = _CmedTransportNumSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 8),
    _CmedTransportNumSwitchover_Type()
)
cmedTransportNumSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedTransportNumSwitchover.setStatus("current")
_CmedTransportTotalNumAlarms_Type = Counter32
_CmedTransportTotalNumAlarms_Object = MibTableColumn
cmedTransportTotalNumAlarms = _CmedTransportTotalNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 9),
    _CmedTransportTotalNumAlarms_Type()
)
cmedTransportTotalNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedTransportTotalNumAlarms.setStatus("current")


class _CmedTransportLastEvent_Type(Integer32):
    """Custom type cmedTransportLastEvent based on Integer32"""
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
        *(("linkLoss", 4),
          ("linkShutdown", 6),
          ("linkUp", 3),
          ("notApplicable", 1),
          ("other", 2),
          ("persistentError", 5),
          ("switchOver", 7))
    )


_CmedTransportLastEvent_Type.__name__ = "Integer32"
_CmedTransportLastEvent_Object = MibTableColumn
cmedTransportLastEvent = _CmedTransportLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 10),
    _CmedTransportLastEvent_Type()
)
cmedTransportLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedTransportLastEvent.setStatus("current")
_CmedTransportLastEventTime_Type = TimeStamp
_CmedTransportLastEventTime_Object = MibTableColumn
cmedTransportLastEventTime = _CmedTransportLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 11),
    _CmedTransportLastEventTime_Type()
)
cmedTransportLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedTransportLastEventTime.setStatus("current")
_CmedLastStatisticsReset_Type = TimeStamp
_CmedLastStatisticsReset_Object = MibTableColumn
cmedLastStatisticsReset = _CmedLastStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 2, 1, 1, 12),
    _CmedLastStatisticsReset_Type()
)
cmedLastStatisticsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedLastStatisticsReset.setStatus("current")
_CmedConnections_ObjectIdentity = ObjectIdentity
cmedConnections = _CmedConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3)
)
_CmedTermIdTable_Object = MibTable
cmedTermIdTable = _CmedTermIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmedTermIdTable.setStatus("current")
_CmedTermIdEntry_Object = MibTableRow
cmedTermIdEntry = _CmedTermIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 1, 1)
)
cmedTermIdEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
)
if mibBuilder.loadTexts:
    cmedTermIdEntry.setStatus("current")
_CmedNextTerminationId_Type = TestAndIncr
_CmedNextTerminationId_Object = MibTableColumn
cmedNextTerminationId = _CmedNextTerminationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 1, 1, 1),
    _CmedNextTerminationId_Type()
)
cmedNextTerminationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmedNextTerminationId.setStatus("current")
_CmedTerminationsTable_Object = MibTable
cmedTerminationsTable = _CmedTerminationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cmedTerminationsTable.setStatus("current")
_CmedTerminationsEntry_Object = MibTableRow
cmedTerminationsEntry = _CmedTerminationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1)
)
cmedTerminationsEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedTermId"),
)
if mibBuilder.loadTexts:
    cmedTerminationsEntry.setStatus("current")
_CmedTermId_Type = CMediaGatewayTermId
_CmedTermId_Object = MibTableColumn
cmedTermId = _CmedTermId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 1),
    _CmedTermId_Type()
)
cmedTermId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedTermId.setStatus("current")


class _CmedTermName_Type(SnmpAdminString):
    """Custom type cmedTermName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmedTermName_Type.__name__ = "SnmpAdminString"
_CmedTermName_Object = MibTableColumn
cmedTermName = _CmedTermName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 2),
    _CmedTermName_Type()
)
cmedTermName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedTermName.setStatus("current")


class _CmedTermAdminStatus_Type(Integer32):
    """Custom type cmedTermAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("testing", 3))
    )


_CmedTermAdminStatus_Type.__name__ = "Integer32"
_CmedTermAdminStatus_Object = MibTableColumn
cmedTermAdminStatus = _CmedTermAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 3),
    _CmedTermAdminStatus_Type()
)
cmedTermAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedTermAdminStatus.setStatus("current")


class _CmedTermOperStatus_Type(Integer32):
    """Custom type cmedTermOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CmedTermOperStatus_Type.__name__ = "Integer32"
_CmedTermOperStatus_Object = MibTableColumn
cmedTermOperStatus = _CmedTermOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 4),
    _CmedTermOperStatus_Type()
)
cmedTermOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmedTermOperStatus.setStatus("current")
_CmedTermInterfaceIdentifier_Type = InterfaceIndex
_CmedTermInterfaceIdentifier_Object = MibTableColumn
cmedTermInterfaceIdentifier = _CmedTermInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 5),
    _CmedTermInterfaceIdentifier_Type()
)
cmedTermInterfaceIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedTermInterfaceIdentifier.setStatus("current")


class _CmedTermPropertyProfileId_Type(Unsigned32):
    """Custom type cmedTermPropertyProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmedTermPropertyProfileId_Type.__name__ = "Unsigned32"
_CmedTermPropertyProfileId_Object = MibTableColumn
cmedTermPropertyProfileId = _CmedTermPropertyProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 6),
    _CmedTermPropertyProfileId_Type()
)
cmedTermPropertyProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedTermPropertyProfileId.setStatus("current")
_CmedTermRowStatus_Type = RowStatus
_CmedTermRowStatus_Object = MibTableColumn
cmedTermRowStatus = _CmedTermRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 2, 1, 7),
    _CmedTermRowStatus_Type()
)
cmedTermRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedTermRowStatus.setStatus("current")
_CmedPropertyProfileTable_Object = MibTable
cmedPropertyProfileTable = _CmedPropertyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cmedPropertyProfileTable.setStatus("current")
_CmedPropertyProfileEntry_Object = MibTableRow
cmedPropertyProfileEntry = _CmedPropertyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 3, 1)
)
cmedPropertyProfileEntry.setIndexNames(
    (0, "CISCO-IETF-MEGACO-MIB", "cmedGatewayId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedPropertyProfileId"),
    (0, "CISCO-IETF-MEGACO-MIB", "cmedPropertyProfileIndex"),
)
if mibBuilder.loadTexts:
    cmedPropertyProfileEntry.setStatus("current")


class _CmedPropertyProfileId_Type(Unsigned32):
    """Custom type cmedPropertyProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmedPropertyProfileId_Type.__name__ = "Unsigned32"
_CmedPropertyProfileId_Object = MibTableColumn
cmedPropertyProfileId = _CmedPropertyProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 3, 1, 1),
    _CmedPropertyProfileId_Type()
)
cmedPropertyProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedPropertyProfileId.setStatus("current")


class _CmedPropertyProfileIndex_Type(Unsigned32):
    """Custom type cmedPropertyProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmedPropertyProfileIndex_Type.__name__ = "Unsigned32"
_CmedPropertyProfileIndex_Object = MibTableColumn
cmedPropertyProfileIndex = _CmedPropertyProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 3, 1, 2),
    _CmedPropertyProfileIndex_Type()
)
cmedPropertyProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmedPropertyProfileIndex.setStatus("current")
_CmedPropertyProfileProperty_Type = AutonomousType
_CmedPropertyProfileProperty_Object = MibTableColumn
cmedPropertyProfileProperty = _CmedPropertyProfileProperty_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 3, 1, 3),
    _CmedPropertyProfileProperty_Type()
)
cmedPropertyProfileProperty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedPropertyProfileProperty.setStatus("current")
_CmedPropertyProfileRowStatus_Type = RowStatus
_CmedPropertyProfileRowStatus_Object = MibTableColumn
cmedPropertyProfileRowStatus = _CmedPropertyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 3, 3, 1, 4),
    _CmedPropertyProfileRowStatus_Type()
)
cmedPropertyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmedPropertyProfileRowStatus.setStatus("current")
_CmedProperties_ObjectIdentity = ObjectIdentity
cmedProperties = _CmedProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 1, 4)
)
_CiscoIetfMegacoMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIetfMegacoMIBConformance = _CiscoIetfMegacoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3)
)
_CmedCompliances_ObjectIdentity = ObjectIdentity
cmedCompliances = _CmedCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 1)
)
_CmedConfigGroups_ObjectIdentity = ObjectIdentity
cmedConfigGroups = _CmedConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 2)
)

# Managed Objects groups

cmedConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 2, 1)
)
cmedConfig.setObjects(
      *(("CISCO-IETF-MEGACO-MIB", "cmedGatewayLinkName"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayIPAddress"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayPort"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayEncodingScheme"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayProtocol"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewaySigTptProtocol"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayAdminStatus"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayOperStatus"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayLastStatusChange"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayResetStatistics"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGatewayRowStatus"))
)
if mibBuilder.loadTexts:
    cmedConfig.setStatus("current")

cmedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 2, 2)
)
cmedStatsGroup.setObjects(
      *(("CISCO-IETF-MEGACO-MIB", "cmedNumInMessages"),
        ("CISCO-IETF-MEGACO-MIB", "cmedNumInOctets"),
        ("CISCO-IETF-MEGACO-MIB", "cmedNumOutMessages"),
        ("CISCO-IETF-MEGACO-MIB", "cmedNumOutOctets"),
        ("CISCO-IETF-MEGACO-MIB", "cmedNumErrors"),
        ("CISCO-IETF-MEGACO-MIB", "cmedNumTimerRecovery"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTransportNumLosses"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTransportNumSwitchover"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTransportTotalNumAlarms"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTransportLastEvent"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTransportLastEventTime"),
        ("CISCO-IETF-MEGACO-MIB", "cmedLastStatisticsReset"))
)
if mibBuilder.loadTexts:
    cmedStatsGroup.setStatus("current")

cmedGwyControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 2, 3)
)
cmedGwyControllerGroup.setObjects(
      *(("CISCO-IETF-MEGACO-MIB", "cmedGwyControllerIPAddress"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGwyControllerPort"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGwyControllerAdminStatus"),
        ("CISCO-IETF-MEGACO-MIB", "cmedGwyControllerOperStatus"))
)
if mibBuilder.loadTexts:
    cmedGwyControllerGroup.setStatus("current")

cmedNextIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 2, 4)
)
cmedNextIdGroup.setObjects(
      *(("CISCO-IETF-MEGACO-MIB", "cmedNextTerminationId"),
        ("CISCO-IETF-MEGACO-MIB", "cmedNextLinkId"))
)
if mibBuilder.loadTexts:
    cmedNextIdGroup.setStatus("current")

cmedTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 2, 5)
)
cmedTermGroup.setObjects(
      *(("CISCO-IETF-MEGACO-MIB", "cmedTermName"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTermAdminStatus"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTermOperStatus"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTermInterfaceIdentifier"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTermPropertyProfileId"),
        ("CISCO-IETF-MEGACO-MIB", "cmedTermRowStatus"),
        ("CISCO-IETF-MEGACO-MIB", "cmedPropertyProfileProperty"),
        ("CISCO-IETF-MEGACO-MIB", "cmedPropertyProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cmedTermGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cmedCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-MEGACO-MIB",
    **{"CMediaGatewayId": CMediaGatewayId,
       "CMediaGatewayLinkId": CMediaGatewayLinkId,
       "CMediaGatewayTermId": CMediaGatewayTermId,
       "ciscoIetfMegacoMIB": ciscoIetfMegacoMIB,
       "ciscoIetfMegacoMIBNotifs": ciscoIetfMegacoMIBNotifs,
       "ciscoIetfMegacoMIBObjects": ciscoIetfMegacoMIBObjects,
       "cmedConfiguration": cmedConfiguration,
       "cmedLinkIdTable": cmedLinkIdTable,
       "cmedLinkIdEntry": cmedLinkIdEntry,
       "cmedNextLinkId": cmedNextLinkId,
       "cmedGatewayConfigTable": cmedGatewayConfigTable,
       "cmedGatewayConfigEntry": cmedGatewayConfigEntry,
       "cmedGatewayId": cmedGatewayId,
       "cmedGatewayLinkId": cmedGatewayLinkId,
       "cmedGatewayLinkName": cmedGatewayLinkName,
       "cmedGatewayIPAddress": cmedGatewayIPAddress,
       "cmedGatewayPort": cmedGatewayPort,
       "cmedGatewayEncodingScheme": cmedGatewayEncodingScheme,
       "cmedGatewayProtocol": cmedGatewayProtocol,
       "cmedGatewaySigTptProtocol": cmedGatewaySigTptProtocol,
       "cmedGatewayAdminStatus": cmedGatewayAdminStatus,
       "cmedGatewayOperStatus": cmedGatewayOperStatus,
       "cmedGatewayLastStatusChange": cmedGatewayLastStatusChange,
       "cmedGatewayResetStatistics": cmedGatewayResetStatistics,
       "cmedGatewayRowStatus": cmedGatewayRowStatus,
       "cmedGwyControllerTable": cmedGwyControllerTable,
       "cmedGwyControllerEntry": cmedGwyControllerEntry,
       "cmedGwyControllerId": cmedGwyControllerId,
       "cmedGwyControllerIPAddress": cmedGwyControllerIPAddress,
       "cmedGwyControllerPort": cmedGwyControllerPort,
       "cmedGwyControllerAdminStatus": cmedGwyControllerAdminStatus,
       "cmedGwyControllerOperStatus": cmedGwyControllerOperStatus,
       "cmedStatistics": cmedStatistics,
       "cmedGatewayStatsTable": cmedGatewayStatsTable,
       "cmedGatewayStatsEntry": cmedGatewayStatsEntry,
       "cmedNumInMessages": cmedNumInMessages,
       "cmedNumInOctets": cmedNumInOctets,
       "cmedNumOutMessages": cmedNumOutMessages,
       "cmedNumOutOctets": cmedNumOutOctets,
       "cmedNumErrors": cmedNumErrors,
       "cmedNumTimerRecovery": cmedNumTimerRecovery,
       "cmedTransportNumLosses": cmedTransportNumLosses,
       "cmedTransportNumSwitchover": cmedTransportNumSwitchover,
       "cmedTransportTotalNumAlarms": cmedTransportTotalNumAlarms,
       "cmedTransportLastEvent": cmedTransportLastEvent,
       "cmedTransportLastEventTime": cmedTransportLastEventTime,
       "cmedLastStatisticsReset": cmedLastStatisticsReset,
       "cmedConnections": cmedConnections,
       "cmedTermIdTable": cmedTermIdTable,
       "cmedTermIdEntry": cmedTermIdEntry,
       "cmedNextTerminationId": cmedNextTerminationId,
       "cmedTerminationsTable": cmedTerminationsTable,
       "cmedTerminationsEntry": cmedTerminationsEntry,
       "cmedTermId": cmedTermId,
       "cmedTermName": cmedTermName,
       "cmedTermAdminStatus": cmedTermAdminStatus,
       "cmedTermOperStatus": cmedTermOperStatus,
       "cmedTermInterfaceIdentifier": cmedTermInterfaceIdentifier,
       "cmedTermPropertyProfileId": cmedTermPropertyProfileId,
       "cmedTermRowStatus": cmedTermRowStatus,
       "cmedPropertyProfileTable": cmedPropertyProfileTable,
       "cmedPropertyProfileEntry": cmedPropertyProfileEntry,
       "cmedPropertyProfileId": cmedPropertyProfileId,
       "cmedPropertyProfileIndex": cmedPropertyProfileIndex,
       "cmedPropertyProfileProperty": cmedPropertyProfileProperty,
       "cmedPropertyProfileRowStatus": cmedPropertyProfileRowStatus,
       "cmedProperties": cmedProperties,
       "ciscoIetfMegacoMIBConformance": ciscoIetfMegacoMIBConformance,
       "cmedCompliances": cmedCompliances,
       "cmedCompliance": cmedCompliance,
       "cmedConfigGroups": cmedConfigGroups,
       "cmedConfig": cmedConfig,
       "cmedStatsGroup": cmedStatsGroup,
       "cmedGwyControllerGroup": cmedGwyControllerGroup,
       "cmedNextIdGroup": cmedNextIdGroup,
       "cmedTermGroup": cmedTermGroup}
)
