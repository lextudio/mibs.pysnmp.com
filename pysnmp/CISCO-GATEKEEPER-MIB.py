# SNMP MIB module (CISCO-GATEKEEPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GATEKEEPER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:46 2024
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

(CgkGatekeeperID,
 CgkNAddress,
 CgkNAddressTag,
 CgkTAddressTag) = mibBuilder.importSymbols(
    "CISCO-H323-TC-MIB",
    "CgkGatekeeperID",
    "CgkNAddress",
    "CgkNAddressTag",
    "CgkTAddressTag")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 RowStatus,
 TAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoGatekeeperMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40)
)
ciscoGatekeeperMIB.setRevisions(
        ("2007-08-29 00:00",
         "2007-08-28 00:00",
         "2003-03-13 00:00",
         "2002-03-12 00:00",
         "2001-09-20 00:00",
         "2001-04-09 00:00",
         "2000-06-26 00:00",
         "2000-03-10 00:00",
         "1998-10-09 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGatekeeperMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGatekeeperMIBObjects = _CiscoGatekeeperMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1)
)
_CgkZone_ObjectIdentity = ObjectIdentity
cgkZone = _CgkZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1)
)
_CgkZoneTable_Object = MibTable
cgkZoneTable = _CgkZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cgkZoneTable.setStatus("current")
_CgkZoneEntry_Object = MibTableRow
cgkZoneEntry = _CgkZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1)
)
cgkZoneEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkZoneEntry.setStatus("current")


class _CgkZoneIndex_Type(Unsigned32):
    """Custom type cgkZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgkZoneIndex_Type.__name__ = "Unsigned32"
_CgkZoneIndex_Object = MibTableColumn
cgkZoneIndex = _CgkZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 1),
    _CgkZoneIndex_Type()
)
cgkZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgkZoneIndex.setStatus("current")
_CgkZoneZoneName_Type = CgkGatekeeperID
_CgkZoneZoneName_Object = MibTableColumn
cgkZoneZoneName = _CgkZoneZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 2),
    _CgkZoneZoneName_Type()
)
cgkZoneZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneZoneName.setStatus("current")


class _CgkZoneDomain_Type(SnmpAdminString):
    """Custom type cgkZoneDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CgkZoneDomain_Type.__name__ = "SnmpAdminString"
_CgkZoneDomain_Object = MibTableColumn
cgkZoneDomain = _CgkZoneDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 3),
    _CgkZoneDomain_Type()
)
cgkZoneDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneDomain.setStatus("current")


class _CgkZoneRasAddressTag_Type(CgkTAddressTag):
    """Custom type cgkZoneRasAddressTag based on CgkTAddressTag"""


_CgkZoneRasAddressTag_Object = MibTableColumn
cgkZoneRasAddressTag = _CgkZoneRasAddressTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 4),
    _CgkZoneRasAddressTag_Type()
)
cgkZoneRasAddressTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneRasAddressTag.setStatus("current")


class _CgkZoneRasAddress_Type(TAddress):
    """Custom type cgkZoneRasAddress based on TAddress"""
    defaultHexValue = "00"


_CgkZoneRasAddress_Object = MibTableColumn
cgkZoneRasAddress = _CgkZoneRasAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 5),
    _CgkZoneRasAddress_Type()
)
cgkZoneRasAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneRasAddress.setStatus("current")


class _CgkZoneIrrFrequency_Type(Integer32):
    """Custom type cgkZoneIrrFrequency based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgkZoneIrrFrequency_Type.__name__ = "Integer32"
_CgkZoneIrrFrequency_Object = MibTableColumn
cgkZoneIrrFrequency = _CgkZoneIrrFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 6),
    _CgkZoneIrrFrequency_Type()
)
cgkZoneIrrFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneIrrFrequency.setStatus("current")


class _CgkZoneLocalZone_Type(TruthValue):
    """Custom type cgkZoneLocalZone based on TruthValue"""


_CgkZoneLocalZone_Object = MibTableColumn
cgkZoneLocalZone = _CgkZoneLocalZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 7),
    _CgkZoneLocalZone_Type()
)
cgkZoneLocalZone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneLocalZone.setStatus("current")


class _CgkZoneDefaultSubnetFlags_Type(Integer32):
    """Custom type cgkZoneDefaultSubnetFlags based on Integer32"""
    defaultValue = 1

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


_CgkZoneDefaultSubnetFlags_Type.__name__ = "Integer32"
_CgkZoneDefaultSubnetFlags_Object = MibTableColumn
cgkZoneDefaultSubnetFlags = _CgkZoneDefaultSubnetFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 8),
    _CgkZoneDefaultSubnetFlags_Type()
)
cgkZoneDefaultSubnetFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneDefaultSubnetFlags.setStatus("current")
_CgkZoneAddressLookupFailures_Type = Counter32
_CgkZoneAddressLookupFailures_Object = MibTableColumn
cgkZoneAddressLookupFailures = _CgkZoneAddressLookupFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 9),
    _CgkZoneAddressLookupFailures_Type()
)
cgkZoneAddressLookupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkZoneAddressLookupFailures.setStatus("current")
_CgkZoneEndpointTimeouts_Type = Counter32
_CgkZoneEndpointTimeouts_Object = MibTableColumn
cgkZoneEndpointTimeouts = _CgkZoneEndpointTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 10),
    _CgkZoneEndpointTimeouts_Type()
)
cgkZoneEndpointTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkZoneEndpointTimeouts.setStatus("current")
_CgkZoneOtherFailures_Type = Counter32
_CgkZoneOtherFailures_Object = MibTableColumn
cgkZoneOtherFailures = _CgkZoneOtherFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 11),
    _CgkZoneOtherFailures_Type()
)
cgkZoneOtherFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkZoneOtherFailures.setStatus("current")
_CgkZoneLRQs_Type = Counter32
_CgkZoneLRQs_Object = MibTableColumn
cgkZoneLRQs = _CgkZoneLRQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 12),
    _CgkZoneLRQs_Type()
)
cgkZoneLRQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkZoneLRQs.setStatus("current")
_CgkZoneRowStatus_Type = RowStatus
_CgkZoneRowStatus_Object = MibTableColumn
cgkZoneRowStatus = _CgkZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 1, 1, 13),
    _CgkZoneRowStatus_Type()
)
cgkZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneRowStatus.setStatus("current")
_CgkZoneSubnetTable_Object = MibTable
cgkZoneSubnetTable = _CgkZoneSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cgkZoneSubnetTable.setStatus("current")
_CgkZoneSubnetEntry_Object = MibTableRow
cgkZoneSubnetEntry = _CgkZoneSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2, 1)
)
cgkZoneSubnetEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneSubnetTag"),
    (1, "CISCO-GATEKEEPER-MIB", "cgkZoneSubnetAddress"),
)
if mibBuilder.loadTexts:
    cgkZoneSubnetEntry.setStatus("current")
_CgkZoneSubnetTag_Type = CgkNAddressTag
_CgkZoneSubnetTag_Object = MibTableColumn
cgkZoneSubnetTag = _CgkZoneSubnetTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2, 1, 1),
    _CgkZoneSubnetTag_Type()
)
cgkZoneSubnetTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgkZoneSubnetTag.setStatus("current")
_CgkZoneSubnetAddress_Type = CgkNAddress
_CgkZoneSubnetAddress_Object = MibTableColumn
cgkZoneSubnetAddress = _CgkZoneSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2, 1, 2),
    _CgkZoneSubnetAddress_Type()
)
cgkZoneSubnetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgkZoneSubnetAddress.setStatus("current")
_CgkZoneSubnetMask_Type = CgkNAddress
_CgkZoneSubnetMask_Object = MibTableColumn
cgkZoneSubnetMask = _CgkZoneSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2, 1, 3),
    _CgkZoneSubnetMask_Type()
)
cgkZoneSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneSubnetMask.setStatus("current")


class _CgkZoneSubnetFlags_Type(Integer32):
    """Custom type cgkZoneSubnetFlags based on Integer32"""
    defaultValue = 1

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


_CgkZoneSubnetFlags_Type.__name__ = "Integer32"
_CgkZoneSubnetFlags_Object = MibTableColumn
cgkZoneSubnetFlags = _CgkZoneSubnetFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2, 1, 4),
    _CgkZoneSubnetFlags_Type()
)
cgkZoneSubnetFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneSubnetFlags.setStatus("current")
_CgkZoneSubnetRowStatus_Type = RowStatus
_CgkZoneSubnetRowStatus_Object = MibTableColumn
cgkZoneSubnetRowStatus = _CgkZoneSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 2, 1, 5),
    _CgkZoneSubnetRowStatus_Type()
)
cgkZoneSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgkZoneSubnetRowStatus.setStatus("current")
_CgkLocalZoneTable_Object = MibTable
cgkLocalZoneTable = _CgkLocalZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cgkLocalZoneTable.setStatus("current")
_CgkLocalZoneEntry_Object = MibTableRow
cgkLocalZoneEntry = _CgkLocalZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1)
)
cgkLocalZoneEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkLocalZoneEntry.setStatus("current")
_CgkLZoneACFs_Type = Counter32
_CgkLZoneACFs_Object = MibTableColumn
cgkLZoneACFs = _CgkLZoneACFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 1),
    _CgkLZoneACFs_Type()
)
cgkLZoneACFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneACFs.setStatus("current")
_CgkLZoneARJs_Type = Counter32
_CgkLZoneARJs_Object = MibTableColumn
cgkLZoneARJs = _CgkLZoneARJs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 2),
    _CgkLZoneARJs_Type()
)
cgkLZoneARJs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneARJs.setStatus("current")


class _CgkLZoneTotalBandwidth_Type(Integer32):
    """Custom type cgkLZoneTotalBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_CgkLZoneTotalBandwidth_Type.__name__ = "Integer32"
_CgkLZoneTotalBandwidth_Object = MibTableColumn
cgkLZoneTotalBandwidth = _CgkLZoneTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 3),
    _CgkLZoneTotalBandwidth_Type()
)
cgkLZoneTotalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkLZoneTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkLZoneTotalBandwidth.setUnits("100 bps")


class _CgkLZoneAllocTotalBandwidth_Type(Gauge32):
    """Custom type cgkLZoneAllocTotalBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CgkLZoneAllocTotalBandwidth_Type.__name__ = "Gauge32"
_CgkLZoneAllocTotalBandwidth_Object = MibTableColumn
cgkLZoneAllocTotalBandwidth = _CgkLZoneAllocTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 4),
    _CgkLZoneAllocTotalBandwidth_Type()
)
cgkLZoneAllocTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneAllocTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkLZoneAllocTotalBandwidth.setUnits("100 bps")


class _CgkLZoneInterzoneBandwidth_Type(Integer32):
    """Custom type cgkLZoneInterzoneBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_CgkLZoneInterzoneBandwidth_Type.__name__ = "Integer32"
_CgkLZoneInterzoneBandwidth_Object = MibTableColumn
cgkLZoneInterzoneBandwidth = _CgkLZoneInterzoneBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 5),
    _CgkLZoneInterzoneBandwidth_Type()
)
cgkLZoneInterzoneBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkLZoneInterzoneBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkLZoneInterzoneBandwidth.setUnits("100 bps")


class _CgkLZoneAllocInterzoneBandwidth_Type(Gauge32):
    """Custom type cgkLZoneAllocInterzoneBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CgkLZoneAllocInterzoneBandwidth_Type.__name__ = "Gauge32"
_CgkLZoneAllocInterzoneBandwidth_Object = MibTableColumn
cgkLZoneAllocInterzoneBandwidth = _CgkLZoneAllocInterzoneBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 6),
    _CgkLZoneAllocInterzoneBandwidth_Type()
)
cgkLZoneAllocInterzoneBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneAllocInterzoneBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkLZoneAllocInterzoneBandwidth.setUnits("100 bps")


class _CgkLZoneSessionBandwidth_Type(Integer32):
    """Custom type cgkLZoneSessionBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_CgkLZoneSessionBandwidth_Type.__name__ = "Integer32"
_CgkLZoneSessionBandwidth_Object = MibTableColumn
cgkLZoneSessionBandwidth = _CgkLZoneSessionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 7),
    _CgkLZoneSessionBandwidth_Type()
)
cgkLZoneSessionBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkLZoneSessionBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkLZoneSessionBandwidth.setUnits("100 bps")


class _CgkLZoneProxiedCall_Type(Integer32):
    """Custom type cgkLZoneProxiedCall based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CgkLZoneProxiedCall_Type.__name__ = "Integer32"
_CgkLZoneProxiedCall_Object = MibTableColumn
cgkLZoneProxiedCall = _CgkLZoneProxiedCall_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 8),
    _CgkLZoneProxiedCall_Type()
)
cgkLZoneProxiedCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkLZoneProxiedCall.setStatus("deprecated")


class _CgkLZoneProxiedCallBits_Type(Bits):
    """Custom type cgkLZoneProxiedCallBits based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("inboundToGateway", 1),
          ("inboundToMcu", 4),
          ("inboundToTerminal", 0),
          ("outboundFromGateway", 3),
          ("outboundFromMcu", 5),
          ("outboundFromTerminal", 2))
    )

_CgkLZoneProxiedCallBits_Type.__name__ = "Bits"
_CgkLZoneProxiedCallBits_Object = MibTableColumn
cgkLZoneProxiedCallBits = _CgkLZoneProxiedCallBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 9),
    _CgkLZoneProxiedCallBits_Type()
)
cgkLZoneProxiedCallBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkLZoneProxiedCallBits.setStatus("current")
_CgkLZoneTotalConcurrentCalls_Type = Gauge32
_CgkLZoneTotalConcurrentCalls_Object = MibTableColumn
cgkLZoneTotalConcurrentCalls = _CgkLZoneTotalConcurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 3, 1, 10),
    _CgkLZoneTotalConcurrentCalls_Type()
)
cgkLZoneTotalConcurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneTotalConcurrentCalls.setStatus("current")
_CgkZoneStats_ObjectIdentity = ObjectIdentity
cgkZoneStats = _CgkZoneStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4)
)
_CgkLocalZoneStatsAdmissionTable_Object = MibTable
cgkLocalZoneStatsAdmissionTable = _CgkLocalZoneStatsAdmissionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsAdmissionTable.setStatus("current")
_CgkLocalZoneStatsAdmissionTableEntry_Object = MibTableRow
cgkLocalZoneStatsAdmissionTableEntry = _CgkLocalZoneStatsAdmissionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1, 1)
)
cgkLocalZoneStatsAdmissionTableEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsAdmissionTableEntry.setStatus("current")
_CgkLZoneStatsAdmissionRequests_Type = Counter32
_CgkLZoneStatsAdmissionRequests_Object = MibTableColumn
cgkLZoneStatsAdmissionRequests = _CgkLZoneStatsAdmissionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1, 1, 1),
    _CgkLZoneStatsAdmissionRequests_Type()
)
cgkLZoneStatsAdmissionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsAdmissionRequests.setStatus("current")
_CgkLZoneStatsOriginAdmissionRequests_Type = Counter32
_CgkLZoneStatsOriginAdmissionRequests_Object = MibTableColumn
cgkLZoneStatsOriginAdmissionRequests = _CgkLZoneStatsOriginAdmissionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1, 1, 2),
    _CgkLZoneStatsOriginAdmissionRequests_Type()
)
cgkLZoneStatsOriginAdmissionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsOriginAdmissionRequests.setStatus("current")
_CgkLZoneStatsOriginAdmissionConfirms_Type = Counter32
_CgkLZoneStatsOriginAdmissionConfirms_Object = MibTableColumn
cgkLZoneStatsOriginAdmissionConfirms = _CgkLZoneStatsOriginAdmissionConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1, 1, 3),
    _CgkLZoneStatsOriginAdmissionConfirms_Type()
)
cgkLZoneStatsOriginAdmissionConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsOriginAdmissionConfirms.setStatus("current")
_CgkLZoneStatsOriginAdmissionRejects_Type = Counter32
_CgkLZoneStatsOriginAdmissionRejects_Object = MibTableColumn
cgkLZoneStatsOriginAdmissionRejects = _CgkLZoneStatsOriginAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1, 1, 4),
    _CgkLZoneStatsOriginAdmissionRejects_Type()
)
cgkLZoneStatsOriginAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsOriginAdmissionRejects.setStatus("current")
_CgkLZoneStatsOriginTotalConcurrentCalls_Type = Gauge32
_CgkLZoneStatsOriginTotalConcurrentCalls_Object = MibTableColumn
cgkLZoneStatsOriginTotalConcurrentCalls = _CgkLZoneStatsOriginTotalConcurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 1, 1, 5),
    _CgkLZoneStatsOriginTotalConcurrentCalls_Type()
)
cgkLZoneStatsOriginTotalConcurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsOriginTotalConcurrentCalls.setStatus("current")
_CgkLocalZoneStatsLocationTable_Object = MibTable
cgkLocalZoneStatsLocationTable = _CgkLocalZoneStatsLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsLocationTable.setStatus("current")
_CgkLocalZoneStatsLocationTableEntry_Object = MibTableRow
cgkLocalZoneStatsLocationTableEntry = _CgkLocalZoneStatsLocationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2, 1)
)
cgkLocalZoneStatsLocationTableEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsLocationTableEntry.setStatus("current")
_CgkLZoneStatsSentLocationRequests_Type = Counter32
_CgkLZoneStatsSentLocationRequests_Object = MibTableColumn
cgkLZoneStatsSentLocationRequests = _CgkLZoneStatsSentLocationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2, 1, 1),
    _CgkLZoneStatsSentLocationRequests_Type()
)
cgkLZoneStatsSentLocationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentLocationRequests.setStatus("current")
_CgkLZoneStatsRcvdLocationConfirms_Type = Counter32
_CgkLZoneStatsRcvdLocationConfirms_Object = MibTableColumn
cgkLZoneStatsRcvdLocationConfirms = _CgkLZoneStatsRcvdLocationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2, 1, 2),
    _CgkLZoneStatsRcvdLocationConfirms_Type()
)
cgkLZoneStatsRcvdLocationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdLocationConfirms.setStatus("current")
_CgkLZoneStatsSentLocationConfirms_Type = Counter32
_CgkLZoneStatsSentLocationConfirms_Object = MibTableColumn
cgkLZoneStatsSentLocationConfirms = _CgkLZoneStatsSentLocationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2, 1, 3),
    _CgkLZoneStatsSentLocationConfirms_Type()
)
cgkLZoneStatsSentLocationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentLocationConfirms.setStatus("current")
_CgkLZoneStatsRcvdLocationRejects_Type = Counter32
_CgkLZoneStatsRcvdLocationRejects_Object = MibTableColumn
cgkLZoneStatsRcvdLocationRejects = _CgkLZoneStatsRcvdLocationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2, 1, 4),
    _CgkLZoneStatsRcvdLocationRejects_Type()
)
cgkLZoneStatsRcvdLocationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdLocationRejects.setStatus("current")
_CgkLZoneStatsSentLocationRejects_Type = Counter32
_CgkLZoneStatsSentLocationRejects_Object = MibTableColumn
cgkLZoneStatsSentLocationRejects = _CgkLZoneStatsSentLocationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 2, 1, 5),
    _CgkLZoneStatsSentLocationRejects_Type()
)
cgkLZoneStatsSentLocationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentLocationRejects.setStatus("current")
_CgkLocalZoneStatsRegistrationTable_Object = MibTable
cgkLocalZoneStatsRegistrationTable = _CgkLocalZoneStatsRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsRegistrationTable.setStatus("current")
_CgkLocalZoneStatsRegistrationTableEntry_Object = MibTableRow
cgkLocalZoneStatsRegistrationTableEntry = _CgkLocalZoneStatsRegistrationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3, 1)
)
cgkLocalZoneStatsRegistrationTableEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsRegistrationTableEntry.setStatus("current")
_CgkLZoneStatsFullRegistrationRequests_Type = Counter32
_CgkLZoneStatsFullRegistrationRequests_Object = MibTableColumn
cgkLZoneStatsFullRegistrationRequests = _CgkLZoneStatsFullRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3, 1, 1),
    _CgkLZoneStatsFullRegistrationRequests_Type()
)
cgkLZoneStatsFullRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsFullRegistrationRequests.setStatus("current")
_CgkLZoneStatsLightRegistrationRequests_Type = Counter32
_CgkLZoneStatsLightRegistrationRequests_Object = MibTableColumn
cgkLZoneStatsLightRegistrationRequests = _CgkLZoneStatsLightRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3, 1, 2),
    _CgkLZoneStatsLightRegistrationRequests_Type()
)
cgkLZoneStatsLightRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsLightRegistrationRequests.setStatus("current")
_CgkLZoneStatsRegistrationConfirms_Type = Counter32
_CgkLZoneStatsRegistrationConfirms_Object = MibTableColumn
cgkLZoneStatsRegistrationConfirms = _CgkLZoneStatsRegistrationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3, 1, 3),
    _CgkLZoneStatsRegistrationConfirms_Type()
)
cgkLZoneStatsRegistrationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRegistrationConfirms.setStatus("current")
_CgkLZoneStatsRegistrationRejects_Type = Counter32
_CgkLZoneStatsRegistrationRejects_Object = MibTableColumn
cgkLZoneStatsRegistrationRejects = _CgkLZoneStatsRegistrationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3, 1, 4),
    _CgkLZoneStatsRegistrationRejects_Type()
)
cgkLZoneStatsRegistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRegistrationRejects.setStatus("current")
_CgkLZoneStatsRegisteredEndpoints_Type = Counter32
_CgkLZoneStatsRegisteredEndpoints_Object = MibTableColumn
cgkLZoneStatsRegisteredEndpoints = _CgkLZoneStatsRegisteredEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 3, 1, 5),
    _CgkLZoneStatsRegisteredEndpoints_Type()
)
cgkLZoneStatsRegisteredEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRegisteredEndpoints.setStatus("current")
_CgkLocalZoneStatsUnRegistrationTable_Object = MibTable
cgkLocalZoneStatsUnRegistrationTable = _CgkLocalZoneStatsUnRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsUnRegistrationTable.setStatus("current")
_CgkLocalZoneStatsUnRegistrationTableEntry_Object = MibTableRow
cgkLocalZoneStatsUnRegistrationTableEntry = _CgkLocalZoneStatsUnRegistrationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1)
)
cgkLocalZoneStatsUnRegistrationTableEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsUnRegistrationTableEntry.setStatus("current")
_CgkLZoneStatsRcvdUnregistrationRequests_Type = Counter32
_CgkLZoneStatsRcvdUnregistrationRequests_Object = MibTableColumn
cgkLZoneStatsRcvdUnregistrationRequests = _CgkLZoneStatsRcvdUnregistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 1),
    _CgkLZoneStatsRcvdUnregistrationRequests_Type()
)
cgkLZoneStatsRcvdUnregistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdUnregistrationRequests.setStatus("current")
_CgkLZoneStatsSentUnregistrationRequests_Type = Counter32
_CgkLZoneStatsSentUnregistrationRequests_Object = MibTableColumn
cgkLZoneStatsSentUnregistrationRequests = _CgkLZoneStatsSentUnregistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 2),
    _CgkLZoneStatsSentUnregistrationRequests_Type()
)
cgkLZoneStatsSentUnregistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentUnregistrationRequests.setStatus("current")
_CgkLZoneStatsTimeoutSentUnregistrationRequests_Type = Counter32
_CgkLZoneStatsTimeoutSentUnregistrationRequests_Object = MibTableColumn
cgkLZoneStatsTimeoutSentUnregistrationRequests = _CgkLZoneStatsTimeoutSentUnregistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 3),
    _CgkLZoneStatsTimeoutSentUnregistrationRequests_Type()
)
cgkLZoneStatsTimeoutSentUnregistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsTimeoutSentUnregistrationRequests.setStatus("current")
_CgkLZoneStatsRcvdUnregistrationConfirms_Type = Counter32
_CgkLZoneStatsRcvdUnregistrationConfirms_Object = MibTableColumn
cgkLZoneStatsRcvdUnregistrationConfirms = _CgkLZoneStatsRcvdUnregistrationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 4),
    _CgkLZoneStatsRcvdUnregistrationConfirms_Type()
)
cgkLZoneStatsRcvdUnregistrationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdUnregistrationConfirms.setStatus("current")
_CgkLZoneStatsSentUnregistrationConfirms_Type = Counter32
_CgkLZoneStatsSentUnregistrationConfirms_Object = MibTableColumn
cgkLZoneStatsSentUnregistrationConfirms = _CgkLZoneStatsSentUnregistrationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 5),
    _CgkLZoneStatsSentUnregistrationConfirms_Type()
)
cgkLZoneStatsSentUnregistrationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentUnregistrationConfirms.setStatus("current")
_CgkLZoneStatsRcvdUnregistrationRejects_Type = Counter32
_CgkLZoneStatsRcvdUnregistrationRejects_Object = MibTableColumn
cgkLZoneStatsRcvdUnregistrationRejects = _CgkLZoneStatsRcvdUnregistrationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 6),
    _CgkLZoneStatsRcvdUnregistrationRejects_Type()
)
cgkLZoneStatsRcvdUnregistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdUnregistrationRejects.setStatus("current")
_CgkLZoneStatsSentUnregistrationRejects_Type = Counter32
_CgkLZoneStatsSentUnregistrationRejects_Object = MibTableColumn
cgkLZoneStatsSentUnregistrationRejects = _CgkLZoneStatsSentUnregistrationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 4, 1, 7),
    _CgkLZoneStatsSentUnregistrationRejects_Type()
)
cgkLZoneStatsSentUnregistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentUnregistrationRejects.setStatus("current")
_CgkLocalZoneStatsDisengageTable_Object = MibTable
cgkLocalZoneStatsDisengageTable = _CgkLocalZoneStatsDisengageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsDisengageTable.setStatus("current")
_CgkLocalZoneStatsDisengageTableEntry_Object = MibTableRow
cgkLocalZoneStatsDisengageTableEntry = _CgkLocalZoneStatsDisengageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1)
)
cgkLocalZoneStatsDisengageTableEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkZoneIndex"),
)
if mibBuilder.loadTexts:
    cgkLocalZoneStatsDisengageTableEntry.setStatus("current")
_CgkLZoneStatsRcvdDisengageRequests_Type = Counter32
_CgkLZoneStatsRcvdDisengageRequests_Object = MibTableColumn
cgkLZoneStatsRcvdDisengageRequests = _CgkLZoneStatsRcvdDisengageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1, 1),
    _CgkLZoneStatsRcvdDisengageRequests_Type()
)
cgkLZoneStatsRcvdDisengageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdDisengageRequests.setStatus("current")
_CgkLZoneStatsSentDisengageRequests_Type = Counter32
_CgkLZoneStatsSentDisengageRequests_Object = MibTableColumn
cgkLZoneStatsSentDisengageRequests = _CgkLZoneStatsSentDisengageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1, 2),
    _CgkLZoneStatsSentDisengageRequests_Type()
)
cgkLZoneStatsSentDisengageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentDisengageRequests.setStatus("current")
_CgkLZoneStatsRcvdDisengageConfirms_Type = Counter32
_CgkLZoneStatsRcvdDisengageConfirms_Object = MibTableColumn
cgkLZoneStatsRcvdDisengageConfirms = _CgkLZoneStatsRcvdDisengageConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1, 3),
    _CgkLZoneStatsRcvdDisengageConfirms_Type()
)
cgkLZoneStatsRcvdDisengageConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdDisengageConfirms.setStatus("current")
_CgkLZoneStatsSentDisengageConfirms_Type = Counter32
_CgkLZoneStatsSentDisengageConfirms_Object = MibTableColumn
cgkLZoneStatsSentDisengageConfirms = _CgkLZoneStatsSentDisengageConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1, 4),
    _CgkLZoneStatsSentDisengageConfirms_Type()
)
cgkLZoneStatsSentDisengageConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentDisengageConfirms.setStatus("current")
_CgkLZoneStatsRcvdDisengageRejects_Type = Counter32
_CgkLZoneStatsRcvdDisengageRejects_Object = MibTableColumn
cgkLZoneStatsRcvdDisengageRejects = _CgkLZoneStatsRcvdDisengageRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1, 5),
    _CgkLZoneStatsRcvdDisengageRejects_Type()
)
cgkLZoneStatsRcvdDisengageRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsRcvdDisengageRejects.setStatus("current")
_CgkLZoneStatsSentDisengageRejects_Type = Counter32
_CgkLZoneStatsSentDisengageRejects_Object = MibTableColumn
cgkLZoneStatsSentDisengageRejects = _CgkLZoneStatsSentDisengageRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 4, 5, 1, 6),
    _CgkLZoneStatsSentDisengageRejects_Type()
)
cgkLZoneStatsSentDisengageRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkLZoneStatsSentDisengageRejects.setStatus("current")
_CgkRemoteZone_ObjectIdentity = ObjectIdentity
cgkRemoteZone = _CgkRemoteZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 5)
)


class _CgkRZoneTotalBandwidth_Type(Integer32):
    """Custom type cgkRZoneTotalBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_CgkRZoneTotalBandwidth_Type.__name__ = "Integer32"
_CgkRZoneTotalBandwidth_Object = MibScalar
cgkRZoneTotalBandwidth = _CgkRZoneTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 5, 1),
    _CgkRZoneTotalBandwidth_Type()
)
cgkRZoneTotalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkRZoneTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkRZoneTotalBandwidth.setUnits("100 bps")


class _CgkRZoneAllocTotalBandwidth_Type(Gauge32):
    """Custom type cgkRZoneAllocTotalBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CgkRZoneAllocTotalBandwidth_Type.__name__ = "Gauge32"
_CgkRZoneAllocTotalBandwidth_Object = MibScalar
cgkRZoneAllocTotalBandwidth = _CgkRZoneAllocTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 1, 5, 2),
    _CgkRZoneAllocTotalBandwidth_Type()
)
cgkRZoneAllocTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkRZoneAllocTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkRZoneAllocTotalBandwidth.setUnits("100 bps")
_CgkHistory_ObjectIdentity = ObjectIdentity
cgkHistory = _CgkHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2)
)


class _CgkHistoryMaxEventEntries_Type(Integer32):
    """Custom type cgkHistoryMaxEventEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CgkHistoryMaxEventEntries_Type.__name__ = "Integer32"
_CgkHistoryMaxEventEntries_Object = MibScalar
cgkHistoryMaxEventEntries = _CgkHistoryMaxEventEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 1),
    _CgkHistoryMaxEventEntries_Type()
)
cgkHistoryMaxEventEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkHistoryMaxEventEntries.setStatus("current")
_CgkHistoryEventTable_Object = MibTable
cgkHistoryEventTable = _CgkHistoryEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cgkHistoryEventTable.setStatus("current")
_CgkHistoryEventEntry_Object = MibTableRow
cgkHistoryEventEntry = _CgkHistoryEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1)
)
cgkHistoryEventEntry.setIndexNames(
    (0, "CISCO-GATEKEEPER-MIB", "cgkHistoryEventIndex"),
)
if mibBuilder.loadTexts:
    cgkHistoryEventEntry.setStatus("current")


class _CgkHistoryEventIndex_Type(Integer32):
    """Custom type cgkHistoryEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CgkHistoryEventIndex_Type.__name__ = "Integer32"
_CgkHistoryEventIndex_Object = MibTableColumn
cgkHistoryEventIndex = _CgkHistoryEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 1),
    _CgkHistoryEventIndex_Type()
)
cgkHistoryEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgkHistoryEventIndex.setStatus("current")


class _CgkHistoryEventType_Type(Integer32):
    """Custom type cgkHistoryEventType based on Integer32"""
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
        *(("other", 1),
          ("overload", 5),
          ("register", 2),
          ("unregister", 3),
          ("unregisterForced", 4))
    )


_CgkHistoryEventType_Type.__name__ = "Integer32"
_CgkHistoryEventType_Object = MibTableColumn
cgkHistoryEventType = _CgkHistoryEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 2),
    _CgkHistoryEventType_Type()
)
cgkHistoryEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventType.setStatus("current")
_CgkHistoryEventTime_Type = TimeStamp
_CgkHistoryEventTime_Object = MibTableColumn
cgkHistoryEventTime = _CgkHistoryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 3),
    _CgkHistoryEventTime_Type()
)
cgkHistoryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventTime.setStatus("current")
_CgkHistoryEventText_Type = DisplayString
_CgkHistoryEventText_Object = MibTableColumn
cgkHistoryEventText = _CgkHistoryEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 4),
    _CgkHistoryEventText_Type()
)
cgkHistoryEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventText.setStatus("current")


class _CgkHistoryEventEndpointType_Type(Integer32):
    """Custom type cgkHistoryEventEndpointType based on Integer32"""
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
        *(("gatekeeper", 3),
          ("gateway", 4),
          ("mcu", 5),
          ("none", 1),
          ("other", 2),
          ("proxy", 7),
          ("terminal", 6))
    )


_CgkHistoryEventEndpointType_Type.__name__ = "Integer32"
_CgkHistoryEventEndpointType_Object = MibTableColumn
cgkHistoryEventEndpointType = _CgkHistoryEventEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 5),
    _CgkHistoryEventEndpointType_Type()
)
cgkHistoryEventEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventEndpointType.setStatus("current")
_CgkHistoryEventEndpointAddrTag_Type = CgkNAddressTag
_CgkHistoryEventEndpointAddrTag_Object = MibTableColumn
cgkHistoryEventEndpointAddrTag = _CgkHistoryEventEndpointAddrTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 6),
    _CgkHistoryEventEndpointAddrTag_Type()
)
cgkHistoryEventEndpointAddrTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventEndpointAddrTag.setStatus("current")
_CgkHistoryEventEndpointAddress_Type = CgkNAddress
_CgkHistoryEventEndpointAddress_Object = MibTableColumn
cgkHistoryEventEndpointAddress = _CgkHistoryEventEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 7),
    _CgkHistoryEventEndpointAddress_Type()
)
cgkHistoryEventEndpointAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventEndpointAddress.setStatus("current")
_CgkHistoryEventEndpointH323id_Type = SnmpAdminString
_CgkHistoryEventEndpointH323id_Object = MibTableColumn
cgkHistoryEventEndpointH323id = _CgkHistoryEventEndpointH323id_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 2, 2, 1, 8),
    _CgkHistoryEventEndpointH323id_Type()
)
cgkHistoryEventEndpointH323id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkHistoryEventEndpointH323id.setStatus("current")
_CgkGeneralConfig_ObjectIdentity = ObjectIdentity
cgkGeneralConfig = _CgkGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 3)
)


class _CgkMIBEnableEventNotification_Type(TruthValue):
    """Custom type cgkMIBEnableEventNotification based on TruthValue"""


_CgkMIBEnableEventNotification_Object = MibScalar
cgkMIBEnableEventNotification = _CgkMIBEnableEventNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 3, 1),
    _CgkMIBEnableEventNotification_Type()
)
cgkMIBEnableEventNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkMIBEnableEventNotification.setStatus("current")


class _CgkMIBDefaultTotalBandwidth_Type(Integer32):
    """Custom type cgkMIBDefaultTotalBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_CgkMIBDefaultTotalBandwidth_Type.__name__ = "Integer32"
_CgkMIBDefaultTotalBandwidth_Object = MibScalar
cgkMIBDefaultTotalBandwidth = _CgkMIBDefaultTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 3, 2),
    _CgkMIBDefaultTotalBandwidth_Type()
)
cgkMIBDefaultTotalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkMIBDefaultTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkMIBDefaultTotalBandwidth.setUnits("100 bps")


class _CgkMIBDefaultInterzoneBandwidth_Type(Integer32):
    """Custom type cgkMIBDefaultInterzoneBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_CgkMIBDefaultInterzoneBandwidth_Type.__name__ = "Integer32"
_CgkMIBDefaultInterzoneBandwidth_Object = MibScalar
cgkMIBDefaultInterzoneBandwidth = _CgkMIBDefaultInterzoneBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 3, 3),
    _CgkMIBDefaultInterzoneBandwidth_Type()
)
cgkMIBDefaultInterzoneBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkMIBDefaultInterzoneBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkMIBDefaultInterzoneBandwidth.setUnits("100 bps")


class _CgkMIBDefaultSessionBandwidth_Type(Integer32):
    """Custom type cgkMIBDefaultSessionBandwidth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_CgkMIBDefaultSessionBandwidth_Type.__name__ = "Integer32"
_CgkMIBDefaultSessionBandwidth_Object = MibScalar
cgkMIBDefaultSessionBandwidth = _CgkMIBDefaultSessionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 3, 4),
    _CgkMIBDefaultSessionBandwidth_Type()
)
cgkMIBDefaultSessionBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgkMIBDefaultSessionBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cgkMIBDefaultSessionBandwidth.setUnits("100 bps")
_CgkGeneralStats_ObjectIdentity = ObjectIdentity
cgkGeneralStats = _CgkGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4)
)
_CgkStatsAdmissionRequests_Type = Counter32
_CgkStatsAdmissionRequests_Object = MibScalar
cgkStatsAdmissionRequests = _CgkStatsAdmissionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 1),
    _CgkStatsAdmissionRequests_Type()
)
cgkStatsAdmissionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsAdmissionRequests.setStatus("current")
_CgkStatsOriginAdmissionRequests_Type = Counter32
_CgkStatsOriginAdmissionRequests_Object = MibScalar
cgkStatsOriginAdmissionRequests = _CgkStatsOriginAdmissionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 2),
    _CgkStatsOriginAdmissionRequests_Type()
)
cgkStatsOriginAdmissionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsOriginAdmissionRequests.setStatus("current")
_CgkStatsAdmissionConfirms_Type = Counter32
_CgkStatsAdmissionConfirms_Object = MibScalar
cgkStatsAdmissionConfirms = _CgkStatsAdmissionConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 3),
    _CgkStatsAdmissionConfirms_Type()
)
cgkStatsAdmissionConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsAdmissionConfirms.setStatus("current")
_CgkStatsOriginAdmissionConfirms_Type = Counter32
_CgkStatsOriginAdmissionConfirms_Object = MibScalar
cgkStatsOriginAdmissionConfirms = _CgkStatsOriginAdmissionConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 4),
    _CgkStatsOriginAdmissionConfirms_Type()
)
cgkStatsOriginAdmissionConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsOriginAdmissionConfirms.setStatus("current")
_CgkStatsAdmissionRejects_Type = Counter32
_CgkStatsAdmissionRejects_Object = MibScalar
cgkStatsAdmissionRejects = _CgkStatsAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 5),
    _CgkStatsAdmissionRejects_Type()
)
cgkStatsAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsAdmissionRejects.setStatus("current")
_CgkStatsOriginAdmissionRejects_Type = Counter32
_CgkStatsOriginAdmissionRejects_Object = MibScalar
cgkStatsOriginAdmissionRejects = _CgkStatsOriginAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 6),
    _CgkStatsOriginAdmissionRejects_Type()
)
cgkStatsOriginAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsOriginAdmissionRejects.setStatus("current")
_CgkStatsTotalConcurrentCalls_Type = Gauge32
_CgkStatsTotalConcurrentCalls_Object = MibScalar
cgkStatsTotalConcurrentCalls = _CgkStatsTotalConcurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 7),
    _CgkStatsTotalConcurrentCalls_Type()
)
cgkStatsTotalConcurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsTotalConcurrentCalls.setStatus("current")
_CgkStatsOriginTotalConcurrentCalls_Type = Gauge32
_CgkStatsOriginTotalConcurrentCalls_Object = MibScalar
cgkStatsOriginTotalConcurrentCalls = _CgkStatsOriginTotalConcurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 8),
    _CgkStatsOriginTotalConcurrentCalls_Type()
)
cgkStatsOriginTotalConcurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsOriginTotalConcurrentCalls.setStatus("current")
_CgkStatsRcvdLocationRequests_Type = Counter32
_CgkStatsRcvdLocationRequests_Object = MibScalar
cgkStatsRcvdLocationRequests = _CgkStatsRcvdLocationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 9),
    _CgkStatsRcvdLocationRequests_Type()
)
cgkStatsRcvdLocationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRcvdLocationRequests.setStatus("current")
_CgkStatsSentLocationRequests_Type = Counter32
_CgkStatsSentLocationRequests_Object = MibScalar
cgkStatsSentLocationRequests = _CgkStatsSentLocationRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 10),
    _CgkStatsSentLocationRequests_Type()
)
cgkStatsSentLocationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsSentLocationRequests.setStatus("current")
_CgkStatsRcvdLocationConfirms_Type = Counter32
_CgkStatsRcvdLocationConfirms_Object = MibScalar
cgkStatsRcvdLocationConfirms = _CgkStatsRcvdLocationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 11),
    _CgkStatsRcvdLocationConfirms_Type()
)
cgkStatsRcvdLocationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRcvdLocationConfirms.setStatus("current")
_CgkStatsSentLocationConfirms_Type = Counter32
_CgkStatsSentLocationConfirms_Object = MibScalar
cgkStatsSentLocationConfirms = _CgkStatsSentLocationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 12),
    _CgkStatsSentLocationConfirms_Type()
)
cgkStatsSentLocationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsSentLocationConfirms.setStatus("current")
_CgkStatsRcvdLocationRejects_Type = Counter32
_CgkStatsRcvdLocationRejects_Object = MibScalar
cgkStatsRcvdLocationRejects = _CgkStatsRcvdLocationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 13),
    _CgkStatsRcvdLocationRejects_Type()
)
cgkStatsRcvdLocationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRcvdLocationRejects.setStatus("current")
_CgkStatsSentLocationRejects_Type = Counter32
_CgkStatsSentLocationRejects_Object = MibScalar
cgkStatsSentLocationRejects = _CgkStatsSentLocationRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 14),
    _CgkStatsSentLocationRejects_Type()
)
cgkStatsSentLocationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsSentLocationRejects.setStatus("current")
_CgkStatsRegisteredEndpoints_Type = Counter32
_CgkStatsRegisteredEndpoints_Object = MibScalar
cgkStatsRegisteredEndpoints = _CgkStatsRegisteredEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 15),
    _CgkStatsRegisteredEndpoints_Type()
)
cgkStatsRegisteredEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRegisteredEndpoints.setStatus("current")
_CgkStatsRcvdDisengageRequests_Type = Counter32
_CgkStatsRcvdDisengageRequests_Object = MibScalar
cgkStatsRcvdDisengageRequests = _CgkStatsRcvdDisengageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 16),
    _CgkStatsRcvdDisengageRequests_Type()
)
cgkStatsRcvdDisengageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRcvdDisengageRequests.setStatus("current")
_CgkStatsSentDisengageRequests_Type = Counter32
_CgkStatsSentDisengageRequests_Object = MibScalar
cgkStatsSentDisengageRequests = _CgkStatsSentDisengageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 17),
    _CgkStatsSentDisengageRequests_Type()
)
cgkStatsSentDisengageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsSentDisengageRequests.setStatus("current")
_CgkStatsRcvdDisengageConfirms_Type = Counter32
_CgkStatsRcvdDisengageConfirms_Object = MibScalar
cgkStatsRcvdDisengageConfirms = _CgkStatsRcvdDisengageConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 18),
    _CgkStatsRcvdDisengageConfirms_Type()
)
cgkStatsRcvdDisengageConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRcvdDisengageConfirms.setStatus("current")
_CgkStatsSentDisengageConfirms_Type = Counter32
_CgkStatsSentDisengageConfirms_Object = MibScalar
cgkStatsSentDisengageConfirms = _CgkStatsSentDisengageConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 19),
    _CgkStatsSentDisengageConfirms_Type()
)
cgkStatsSentDisengageConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsSentDisengageConfirms.setStatus("current")
_CgkStatsRcvdDisengageRejects_Type = Counter32
_CgkStatsRcvdDisengageRejects_Object = MibScalar
cgkStatsRcvdDisengageRejects = _CgkStatsRcvdDisengageRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 20),
    _CgkStatsRcvdDisengageRejects_Type()
)
cgkStatsRcvdDisengageRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsRcvdDisengageRejects.setStatus("current")
_CgkStatsSentDisengageRejects_Type = Counter32
_CgkStatsSentDisengageRejects_Object = MibScalar
cgkStatsSentDisengageRejects = _CgkStatsSentDisengageRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 1, 4, 21),
    _CgkStatsSentDisengageRejects_Type()
)
cgkStatsSentDisengageRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgkStatsSentDisengageRejects.setStatus("current")
_CiscoGatekeeperMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoGatekeeperMIBNotificationPrefix = _CiscoGatekeeperMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 2)
)
_CiscoGatekeeperMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoGatekeeperMIBNotifications = _CiscoGatekeeperMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 2, 0)
)
_CiscoGatekeeperMIBConformance_ObjectIdentity = ObjectIdentity
ciscoGatekeeperMIBConformance = _CiscoGatekeeperMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3)
)
_CiscoGatekeeperMIBCompliance_ObjectIdentity = ObjectIdentity
ciscoGatekeeperMIBCompliance = _CiscoGatekeeperMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 1)
)
_CiscoGatekeeperMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGatekeeperMIBGroups = _CiscoGatekeeperMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2)
)

# Managed Objects groups

cgkZoneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 1)
)
cgkZoneGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkZoneZoneName"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneDomain"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneRasAddressTag"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneRasAddress"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneIrrFrequency"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneLocalZone"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneDefaultSubnetFlags"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneAddressLookupFailures"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneEndpointTimeouts"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneOtherFailures"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneLRQs"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneRowStatus"))
)
if mibBuilder.loadTexts:
    cgkZoneGroup.setStatus("current")

cgkZoneSubnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 2)
)
cgkZoneSubnetGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkZoneSubnetMask"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneSubnetFlags"),
        ("CISCO-GATEKEEPER-MIB", "cgkZoneSubnetRowStatus"))
)
if mibBuilder.loadTexts:
    cgkZoneSubnetGroup.setStatus("current")

cgkLocalZoneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 3)
)
cgkLocalZoneGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkLZoneACFs"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneARJs"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneAllocTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneAllocInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneSessionBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneProxiedCall"))
)
if mibBuilder.loadTexts:
    cgkLocalZoneGroup.setStatus("deprecated")

cgkHistoryEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 4)
)
cgkHistoryEventGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkHistoryMaxEventEntries"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventType"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventTime"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventText"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointType"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointAddress"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointAddrTag"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointH323id"),
        ("CISCO-GATEKEEPER-MIB", "cgkMIBEnableEventNotification"))
)
if mibBuilder.loadTexts:
    cgkHistoryEventGroup.setStatus("current")

cgkGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 5)
)
cgkGeneralGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkMIBDefaultTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkMIBDefaultInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkMIBDefaultSessionBandwidth"))
)
if mibBuilder.loadTexts:
    cgkGeneralGroup.setStatus("current")

cgkLocalZoneGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 7)
)
cgkLocalZoneGroupRev1.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkLZoneACFs"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneARJs"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneAllocTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneAllocInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneSessionBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneProxiedCall"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneProxiedCallBits"))
)
if mibBuilder.loadTexts:
    cgkLocalZoneGroupRev1.setStatus("deprecated")

cgkLocalZoneGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 8)
)
cgkLocalZoneGroupRev2.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkLZoneACFs"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneARJs"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneAllocTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneAllocInterzoneBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneSessionBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneProxiedCallBits"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneTotalConcurrentCalls"))
)
if mibBuilder.loadTexts:
    cgkLocalZoneGroupRev2.setStatus("current")

cgkZoneMgmtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 9)
)
cgkZoneMgmtStatsGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsAdmissionRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsOriginAdmissionRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsOriginAdmissionConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsOriginAdmissionRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsOriginTotalConcurrentCalls"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentLocationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdLocationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentLocationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdLocationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentLocationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsFullRegistrationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsLightRegistrationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRegistrationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRegistrationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRegisteredEndpoints"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdUnregistrationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentUnregistrationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsTimeoutSentUnregistrationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdUnregistrationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentUnregistrationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdUnregistrationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentUnregistrationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdDisengageRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentDisengageRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdDisengageConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentDisengageConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsRcvdDisengageRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkLZoneStatsSentDisengageRejects"))
)
if mibBuilder.loadTexts:
    cgkZoneMgmtStatsGroup.setStatus("current")

cgkGeneralMgmtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 10)
)
cgkGeneralMgmtStatsGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkStatsAdmissionRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsOriginAdmissionRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsAdmissionConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsOriginAdmissionConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsAdmissionRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsOriginAdmissionRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsTotalConcurrentCalls"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsOriginTotalConcurrentCalls"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRcvdLocationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsSentLocationRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRcvdLocationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsSentLocationConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRcvdLocationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsSentLocationRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRegisteredEndpoints"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRcvdDisengageRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsSentDisengageRequests"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRcvdDisengageConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsSentDisengageConfirms"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsRcvdDisengageRejects"),
        ("CISCO-GATEKEEPER-MIB", "cgkStatsSentDisengageRejects"))
)
if mibBuilder.loadTexts:
    cgkGeneralMgmtStatsGroup.setStatus("current")

cgkRemoteZoneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 11)
)
cgkRemoteZoneGroup.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkRZoneTotalBandwidth"),
        ("CISCO-GATEKEEPER-MIB", "cgkRZoneAllocTotalBandwidth"))
)
if mibBuilder.loadTexts:
    cgkRemoteZoneGroup.setStatus("current")


# Notification objects

ciscoGatekeeperEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 2, 0, 1)
)
ciscoGatekeeperEvent.setObjects(
      *(("CISCO-GATEKEEPER-MIB", "cgkHistoryEventType"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointType"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointAddrTag"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointAddress"),
        ("CISCO-GATEKEEPER-MIB", "cgkHistoryEventEndpointH323id"))
)
if mibBuilder.loadTexts:
    ciscoGatekeeperEvent.setStatus(
        "current"
    )


# Notifications groups

cgkNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 2, 6)
)
cgkNotificationsGroup.setObjects(
    ("CISCO-GATEKEEPER-MIB", "ciscoGatekeeperEvent")
)
if mibBuilder.loadTexts:
    cgkNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cgkGatekeeperCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cgkGatekeeperCompliance.setStatus(
        "deprecated"
    )

cgkGatekeeperComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cgkGatekeeperComplianceRev1.setStatus(
        "deprecated"
    )

cgkGatekeeperComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cgkGatekeeperComplianceRev2.setStatus(
        "deprecated"
    )

cgkGatekeeperComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cgkGatekeeperComplianceRev3.setStatus(
        "deprecated"
    )

cgkGatekeeperComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 40, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cgkGatekeeperComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GATEKEEPER-MIB",
    **{"ciscoGatekeeperMIB": ciscoGatekeeperMIB,
       "ciscoGatekeeperMIBObjects": ciscoGatekeeperMIBObjects,
       "cgkZone": cgkZone,
       "cgkZoneTable": cgkZoneTable,
       "cgkZoneEntry": cgkZoneEntry,
       "cgkZoneIndex": cgkZoneIndex,
       "cgkZoneZoneName": cgkZoneZoneName,
       "cgkZoneDomain": cgkZoneDomain,
       "cgkZoneRasAddressTag": cgkZoneRasAddressTag,
       "cgkZoneRasAddress": cgkZoneRasAddress,
       "cgkZoneIrrFrequency": cgkZoneIrrFrequency,
       "cgkZoneLocalZone": cgkZoneLocalZone,
       "cgkZoneDefaultSubnetFlags": cgkZoneDefaultSubnetFlags,
       "cgkZoneAddressLookupFailures": cgkZoneAddressLookupFailures,
       "cgkZoneEndpointTimeouts": cgkZoneEndpointTimeouts,
       "cgkZoneOtherFailures": cgkZoneOtherFailures,
       "cgkZoneLRQs": cgkZoneLRQs,
       "cgkZoneRowStatus": cgkZoneRowStatus,
       "cgkZoneSubnetTable": cgkZoneSubnetTable,
       "cgkZoneSubnetEntry": cgkZoneSubnetEntry,
       "cgkZoneSubnetTag": cgkZoneSubnetTag,
       "cgkZoneSubnetAddress": cgkZoneSubnetAddress,
       "cgkZoneSubnetMask": cgkZoneSubnetMask,
       "cgkZoneSubnetFlags": cgkZoneSubnetFlags,
       "cgkZoneSubnetRowStatus": cgkZoneSubnetRowStatus,
       "cgkLocalZoneTable": cgkLocalZoneTable,
       "cgkLocalZoneEntry": cgkLocalZoneEntry,
       "cgkLZoneACFs": cgkLZoneACFs,
       "cgkLZoneARJs": cgkLZoneARJs,
       "cgkLZoneTotalBandwidth": cgkLZoneTotalBandwidth,
       "cgkLZoneAllocTotalBandwidth": cgkLZoneAllocTotalBandwidth,
       "cgkLZoneInterzoneBandwidth": cgkLZoneInterzoneBandwidth,
       "cgkLZoneAllocInterzoneBandwidth": cgkLZoneAllocInterzoneBandwidth,
       "cgkLZoneSessionBandwidth": cgkLZoneSessionBandwidth,
       "cgkLZoneProxiedCall": cgkLZoneProxiedCall,
       "cgkLZoneProxiedCallBits": cgkLZoneProxiedCallBits,
       "cgkLZoneTotalConcurrentCalls": cgkLZoneTotalConcurrentCalls,
       "cgkZoneStats": cgkZoneStats,
       "cgkLocalZoneStatsAdmissionTable": cgkLocalZoneStatsAdmissionTable,
       "cgkLocalZoneStatsAdmissionTableEntry": cgkLocalZoneStatsAdmissionTableEntry,
       "cgkLZoneStatsAdmissionRequests": cgkLZoneStatsAdmissionRequests,
       "cgkLZoneStatsOriginAdmissionRequests": cgkLZoneStatsOriginAdmissionRequests,
       "cgkLZoneStatsOriginAdmissionConfirms": cgkLZoneStatsOriginAdmissionConfirms,
       "cgkLZoneStatsOriginAdmissionRejects": cgkLZoneStatsOriginAdmissionRejects,
       "cgkLZoneStatsOriginTotalConcurrentCalls": cgkLZoneStatsOriginTotalConcurrentCalls,
       "cgkLocalZoneStatsLocationTable": cgkLocalZoneStatsLocationTable,
       "cgkLocalZoneStatsLocationTableEntry": cgkLocalZoneStatsLocationTableEntry,
       "cgkLZoneStatsSentLocationRequests": cgkLZoneStatsSentLocationRequests,
       "cgkLZoneStatsRcvdLocationConfirms": cgkLZoneStatsRcvdLocationConfirms,
       "cgkLZoneStatsSentLocationConfirms": cgkLZoneStatsSentLocationConfirms,
       "cgkLZoneStatsRcvdLocationRejects": cgkLZoneStatsRcvdLocationRejects,
       "cgkLZoneStatsSentLocationRejects": cgkLZoneStatsSentLocationRejects,
       "cgkLocalZoneStatsRegistrationTable": cgkLocalZoneStatsRegistrationTable,
       "cgkLocalZoneStatsRegistrationTableEntry": cgkLocalZoneStatsRegistrationTableEntry,
       "cgkLZoneStatsFullRegistrationRequests": cgkLZoneStatsFullRegistrationRequests,
       "cgkLZoneStatsLightRegistrationRequests": cgkLZoneStatsLightRegistrationRequests,
       "cgkLZoneStatsRegistrationConfirms": cgkLZoneStatsRegistrationConfirms,
       "cgkLZoneStatsRegistrationRejects": cgkLZoneStatsRegistrationRejects,
       "cgkLZoneStatsRegisteredEndpoints": cgkLZoneStatsRegisteredEndpoints,
       "cgkLocalZoneStatsUnRegistrationTable": cgkLocalZoneStatsUnRegistrationTable,
       "cgkLocalZoneStatsUnRegistrationTableEntry": cgkLocalZoneStatsUnRegistrationTableEntry,
       "cgkLZoneStatsRcvdUnregistrationRequests": cgkLZoneStatsRcvdUnregistrationRequests,
       "cgkLZoneStatsSentUnregistrationRequests": cgkLZoneStatsSentUnregistrationRequests,
       "cgkLZoneStatsTimeoutSentUnregistrationRequests": cgkLZoneStatsTimeoutSentUnregistrationRequests,
       "cgkLZoneStatsRcvdUnregistrationConfirms": cgkLZoneStatsRcvdUnregistrationConfirms,
       "cgkLZoneStatsSentUnregistrationConfirms": cgkLZoneStatsSentUnregistrationConfirms,
       "cgkLZoneStatsRcvdUnregistrationRejects": cgkLZoneStatsRcvdUnregistrationRejects,
       "cgkLZoneStatsSentUnregistrationRejects": cgkLZoneStatsSentUnregistrationRejects,
       "cgkLocalZoneStatsDisengageTable": cgkLocalZoneStatsDisengageTable,
       "cgkLocalZoneStatsDisengageTableEntry": cgkLocalZoneStatsDisengageTableEntry,
       "cgkLZoneStatsRcvdDisengageRequests": cgkLZoneStatsRcvdDisengageRequests,
       "cgkLZoneStatsSentDisengageRequests": cgkLZoneStatsSentDisengageRequests,
       "cgkLZoneStatsRcvdDisengageConfirms": cgkLZoneStatsRcvdDisengageConfirms,
       "cgkLZoneStatsSentDisengageConfirms": cgkLZoneStatsSentDisengageConfirms,
       "cgkLZoneStatsRcvdDisengageRejects": cgkLZoneStatsRcvdDisengageRejects,
       "cgkLZoneStatsSentDisengageRejects": cgkLZoneStatsSentDisengageRejects,
       "cgkRemoteZone": cgkRemoteZone,
       "cgkRZoneTotalBandwidth": cgkRZoneTotalBandwidth,
       "cgkRZoneAllocTotalBandwidth": cgkRZoneAllocTotalBandwidth,
       "cgkHistory": cgkHistory,
       "cgkHistoryMaxEventEntries": cgkHistoryMaxEventEntries,
       "cgkHistoryEventTable": cgkHistoryEventTable,
       "cgkHistoryEventEntry": cgkHistoryEventEntry,
       "cgkHistoryEventIndex": cgkHistoryEventIndex,
       "cgkHistoryEventType": cgkHistoryEventType,
       "cgkHistoryEventTime": cgkHistoryEventTime,
       "cgkHistoryEventText": cgkHistoryEventText,
       "cgkHistoryEventEndpointType": cgkHistoryEventEndpointType,
       "cgkHistoryEventEndpointAddrTag": cgkHistoryEventEndpointAddrTag,
       "cgkHistoryEventEndpointAddress": cgkHistoryEventEndpointAddress,
       "cgkHistoryEventEndpointH323id": cgkHistoryEventEndpointH323id,
       "cgkGeneralConfig": cgkGeneralConfig,
       "cgkMIBEnableEventNotification": cgkMIBEnableEventNotification,
       "cgkMIBDefaultTotalBandwidth": cgkMIBDefaultTotalBandwidth,
       "cgkMIBDefaultInterzoneBandwidth": cgkMIBDefaultInterzoneBandwidth,
       "cgkMIBDefaultSessionBandwidth": cgkMIBDefaultSessionBandwidth,
       "cgkGeneralStats": cgkGeneralStats,
       "cgkStatsAdmissionRequests": cgkStatsAdmissionRequests,
       "cgkStatsOriginAdmissionRequests": cgkStatsOriginAdmissionRequests,
       "cgkStatsAdmissionConfirms": cgkStatsAdmissionConfirms,
       "cgkStatsOriginAdmissionConfirms": cgkStatsOriginAdmissionConfirms,
       "cgkStatsAdmissionRejects": cgkStatsAdmissionRejects,
       "cgkStatsOriginAdmissionRejects": cgkStatsOriginAdmissionRejects,
       "cgkStatsTotalConcurrentCalls": cgkStatsTotalConcurrentCalls,
       "cgkStatsOriginTotalConcurrentCalls": cgkStatsOriginTotalConcurrentCalls,
       "cgkStatsRcvdLocationRequests": cgkStatsRcvdLocationRequests,
       "cgkStatsSentLocationRequests": cgkStatsSentLocationRequests,
       "cgkStatsRcvdLocationConfirms": cgkStatsRcvdLocationConfirms,
       "cgkStatsSentLocationConfirms": cgkStatsSentLocationConfirms,
       "cgkStatsRcvdLocationRejects": cgkStatsRcvdLocationRejects,
       "cgkStatsSentLocationRejects": cgkStatsSentLocationRejects,
       "cgkStatsRegisteredEndpoints": cgkStatsRegisteredEndpoints,
       "cgkStatsRcvdDisengageRequests": cgkStatsRcvdDisengageRequests,
       "cgkStatsSentDisengageRequests": cgkStatsSentDisengageRequests,
       "cgkStatsRcvdDisengageConfirms": cgkStatsRcvdDisengageConfirms,
       "cgkStatsSentDisengageConfirms": cgkStatsSentDisengageConfirms,
       "cgkStatsRcvdDisengageRejects": cgkStatsRcvdDisengageRejects,
       "cgkStatsSentDisengageRejects": cgkStatsSentDisengageRejects,
       "ciscoGatekeeperMIBNotificationPrefix": ciscoGatekeeperMIBNotificationPrefix,
       "ciscoGatekeeperMIBNotifications": ciscoGatekeeperMIBNotifications,
       "ciscoGatekeeperEvent": ciscoGatekeeperEvent,
       "ciscoGatekeeperMIBConformance": ciscoGatekeeperMIBConformance,
       "ciscoGatekeeperMIBCompliance": ciscoGatekeeperMIBCompliance,
       "cgkGatekeeperCompliance": cgkGatekeeperCompliance,
       "cgkGatekeeperComplianceRev1": cgkGatekeeperComplianceRev1,
       "cgkGatekeeperComplianceRev2": cgkGatekeeperComplianceRev2,
       "cgkGatekeeperComplianceRev3": cgkGatekeeperComplianceRev3,
       "cgkGatekeeperComplianceRev4": cgkGatekeeperComplianceRev4,
       "ciscoGatekeeperMIBGroups": ciscoGatekeeperMIBGroups,
       "cgkZoneGroup": cgkZoneGroup,
       "cgkZoneSubnetGroup": cgkZoneSubnetGroup,
       "cgkLocalZoneGroup": cgkLocalZoneGroup,
       "cgkHistoryEventGroup": cgkHistoryEventGroup,
       "cgkGeneralGroup": cgkGeneralGroup,
       "cgkNotificationsGroup": cgkNotificationsGroup,
       "cgkLocalZoneGroupRev1": cgkLocalZoneGroupRev1,
       "cgkLocalZoneGroupRev2": cgkLocalZoneGroupRev2,
       "cgkZoneMgmtStatsGroup": cgkZoneMgmtStatsGroup,
       "cgkGeneralMgmtStatsGroup": cgkGeneralMgmtStatsGroup,
       "cgkRemoteZoneGroup": cgkRemoteZoneGroup}
)
