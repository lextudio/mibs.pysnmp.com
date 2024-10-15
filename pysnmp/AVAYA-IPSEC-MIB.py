# SNMP MIB module (AVAYA-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:31 2024
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

(avGatewayMibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "avGatewayMibs")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

avayaIpsecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1)
)
avayaIpsecMib.setRevisions(
        ("2007-01-08 16:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DiffHellmanGrp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14,
              15,
              16,
              17,
              18,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dhGroup1", 1),
          ("dhGroup14", 14),
          ("dhGroup15", 15),
          ("dhGroup16", 16),
          ("dhGroup17", 17),
          ("dhGroup18", 18),
          ("dhGroup2", 2),
          ("dhGroup5", 5),
          ("none", 255))
    )



class IkeEncryptAlgo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aes", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("des", 2),
          ("des3", 3),
          ("none", 255))
    )



class IkeHashAlgo(Integer32, TextualConvention):
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
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )



class EspHashTransform(Integer32, TextualConvention):
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
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )



class EspEncrTransform(Integer32, TextualConvention):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("aes", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("des", 2),
          ("des3", 3),
          ("none", 255),
          ("null", 1))
    )



class IsakmpIdentityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              256,
              257,
              270)
        )
    )
    namedValues = NamedValues(
        *(("fqdn", 2),
          ("ifName", 270),
          ("ipv4Address", 1),
          ("none", 256),
          ("peerGroup", 257),
          ("userFqdn", 3))
    )



class IsakmpIdentityValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 110),
    )



class IsakmpDpdKeepaliveMetric(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("onDemand", 2),
          ("periodic", 3))
    )



class IpsecEncapMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AvipsMIBObjects_ObjectIdentity = ObjectIdentity
avipsMIBObjects = _AvipsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1)
)
_AvipsGlobals_ObjectIdentity = ObjectIdentity
avipsGlobals = _AvipsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 1)
)
_AvipsGlobalsInvalidSpiRecovery_Type = TruthValue
_AvipsGlobalsInvalidSpiRecovery_Object = MibScalar
avipsGlobalsInvalidSpiRecovery = _AvipsGlobalsInvalidSpiRecovery_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 1, 1),
    _AvipsGlobalsInvalidSpiRecovery_Type()
)
avipsGlobalsInvalidSpiRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsGlobalsInvalidSpiRecovery.setStatus("current")
_AvipsNatTEnabled_Type = TruthValue
_AvipsNatTEnabled_Object = MibScalar
avipsNatTEnabled = _AvipsNatTEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 1, 2),
    _AvipsNatTEnabled_Type()
)
avipsNatTEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsNatTEnabled.setStatus("current")
_AvipsNatTKeepaliveInterval_Type = Integer32
_AvipsNatTKeepaliveInterval_Object = MibScalar
avipsNatTKeepaliveInterval = _AvipsNatTKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 1, 3),
    _AvipsNatTKeepaliveInterval_Type()
)
avipsNatTKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsNatTKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    avipsNatTKeepaliveInterval.setUnits("seconds")
_AvipsCryptoEngineAccelEnabled_Type = TruthValue
_AvipsCryptoEngineAccelEnabled_Object = MibScalar
avipsCryptoEngineAccelEnabled = _AvipsCryptoEngineAccelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 1, 4),
    _AvipsCryptoEngineAccelEnabled_Type()
)
avipsCryptoEngineAccelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoEngineAccelEnabled.setStatus("current")
_AvipsIsakmpGroup_ObjectIdentity = ObjectIdentity
avipsIsakmpGroup = _AvipsIsakmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2)
)
_AvipsIsakmpPeerTable_Object = MibTable
avipsIsakmpPeerTable = _AvipsIsakmpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    avipsIsakmpPeerTable.setStatus("current")
_AvipsIsakmpPeerEntry_Object = MibTableRow
avipsIsakmpPeerEntry = _AvipsIsakmpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1)
)
avipsIsakmpPeerEntry.setIndexNames(
    (0, "AVAYA-IPSEC-MIB", "avipsIsakmpPeerIdType"),
    (1, "AVAYA-IPSEC-MIB", "avipsIsakmpPeerId"),
)
if mibBuilder.loadTexts:
    avipsIsakmpPeerEntry.setStatus("current")


class _AvipsIsakmpPeerIdType_Type(IsakmpIdentityType):
    """Custom type avipsIsakmpPeerIdType based on IsakmpIdentityType"""
    subtypeSpec = IsakmpIdentityType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_AvipsIsakmpPeerIdType_Type.__name__ = "IsakmpIdentityType"
_AvipsIsakmpPeerIdType_Object = MibTableColumn
avipsIsakmpPeerIdType = _AvipsIsakmpPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 1),
    _AvipsIsakmpPeerIdType_Type()
)
avipsIsakmpPeerIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsIsakmpPeerIdType.setStatus("current")
_AvipsIsakmpPeerId_Type = IsakmpIdentityValue
_AvipsIsakmpPeerId_Object = MibTableColumn
avipsIsakmpPeerId = _AvipsIsakmpPeerId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 2),
    _AvipsIsakmpPeerId_Type()
)
avipsIsakmpPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsIsakmpPeerId.setStatus("current")


class _AvipsIsakmpPeerDescription_Type(DisplayString):
    """Custom type avipsIsakmpPeerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AvipsIsakmpPeerDescription_Type.__name__ = "DisplayString"
_AvipsIsakmpPeerDescription_Object = MibTableColumn
avipsIsakmpPeerDescription = _AvipsIsakmpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 3),
    _AvipsIsakmpPeerDescription_Type()
)
avipsIsakmpPeerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerDescription.setStatus("current")


class _AvipsIsakmpPeerIsaPlcyId1_Type(Integer32):
    """Custom type avipsIsakmpPeerIsaPlcyId1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AvipsIsakmpPeerIsaPlcyId1_Type.__name__ = "Integer32"
_AvipsIsakmpPeerIsaPlcyId1_Object = MibTableColumn
avipsIsakmpPeerIsaPlcyId1 = _AvipsIsakmpPeerIsaPlcyId1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 4),
    _AvipsIsakmpPeerIsaPlcyId1_Type()
)
avipsIsakmpPeerIsaPlcyId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerIsaPlcyId1.setStatus("current")


class _AvipsIsakmpPeerInitiateMode_Type(Integer32):
    """Custom type avipsIsakmpPeerInitiateMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 3),
          ("main", 2),
          ("none", 1))
    )


_AvipsIsakmpPeerInitiateMode_Type.__name__ = "Integer32"
_AvipsIsakmpPeerInitiateMode_Object = MibTableColumn
avipsIsakmpPeerInitiateMode = _AvipsIsakmpPeerInitiateMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 5),
    _AvipsIsakmpPeerInitiateMode_Type()
)
avipsIsakmpPeerInitiateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerInitiateMode.setStatus("current")


class _AvipsIsakmpPeerSelfIdType_Type(IsakmpIdentityType):
    """Custom type avipsIsakmpPeerSelfIdType based on IsakmpIdentityType"""


_AvipsIsakmpPeerSelfIdType_Object = MibTableColumn
avipsIsakmpPeerSelfIdType = _AvipsIsakmpPeerSelfIdType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 6),
    _AvipsIsakmpPeerSelfIdType_Type()
)
avipsIsakmpPeerSelfIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerSelfIdType.setStatus("current")


class _AvipsIsakmpPeerSelfId_Type(IsakmpIdentityValue):
    """Custom type avipsIsakmpPeerSelfId based on IsakmpIdentityValue"""
    defaultHexValue = ""


_AvipsIsakmpPeerSelfId_Object = MibTableColumn
avipsIsakmpPeerSelfId = _AvipsIsakmpPeerSelfId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 7),
    _AvipsIsakmpPeerSelfId_Type()
)
avipsIsakmpPeerSelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerSelfId.setStatus("current")


class _AvipsIsakmpPeerKeepaliveMetric_Type(IsakmpDpdKeepaliveMetric):
    """Custom type avipsIsakmpPeerKeepaliveMetric based on IsakmpDpdKeepaliveMetric"""


_AvipsIsakmpPeerKeepaliveMetric_Object = MibTableColumn
avipsIsakmpPeerKeepaliveMetric = _AvipsIsakmpPeerKeepaliveMetric_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 8),
    _AvipsIsakmpPeerKeepaliveMetric_Type()
)
avipsIsakmpPeerKeepaliveMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerKeepaliveMetric.setStatus("current")


class _AvipsIsakmpPeerKeepaliveInterval_Type(Integer32):
    """Custom type avipsIsakmpPeerKeepaliveInterval based on Integer32"""
    defaultValue = 10


_AvipsIsakmpPeerKeepaliveInterval_Object = MibTableColumn
avipsIsakmpPeerKeepaliveInterval = _AvipsIsakmpPeerKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 9),
    _AvipsIsakmpPeerKeepaliveInterval_Type()
)
avipsIsakmpPeerKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    avipsIsakmpPeerKeepaliveInterval.setUnits("seconds")


class _AvipsIsakmpPeerKeepaliveRetryInterval_Type(Integer32):
    """Custom type avipsIsakmpPeerKeepaliveRetryInterval based on Integer32"""
    defaultValue = 2


_AvipsIsakmpPeerKeepaliveRetryInterval_Object = MibTableColumn
avipsIsakmpPeerKeepaliveRetryInterval = _AvipsIsakmpPeerKeepaliveRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 10),
    _AvipsIsakmpPeerKeepaliveRetryInterval_Type()
)
avipsIsakmpPeerKeepaliveRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerKeepaliveRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    avipsIsakmpPeerKeepaliveRetryInterval.setUnits("seconds")


class _AvipsIsakmpPeerKeepaliveTrackId_Type(Integer32):
    """Custom type avipsIsakmpPeerKeepaliveTrackId based on Integer32"""
    defaultValue = 0


_AvipsIsakmpPeerKeepaliveTrackId_Object = MibTableColumn
avipsIsakmpPeerKeepaliveTrackId = _AvipsIsakmpPeerKeepaliveTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 11),
    _AvipsIsakmpPeerKeepaliveTrackId_Type()
)
avipsIsakmpPeerKeepaliveTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerKeepaliveTrackId.setStatus("current")


class _AvipsIsakmpPeerContChannel_Type(TruthValue):
    """Custom type avipsIsakmpPeerContChannel based on TruthValue"""


_AvipsIsakmpPeerContChannel_Object = MibTableColumn
avipsIsakmpPeerContChannel = _AvipsIsakmpPeerContChannel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 12),
    _AvipsIsakmpPeerContChannel_Type()
)
avipsIsakmpPeerContChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerContChannel.setStatus("current")
_AvipsIsakmpPeerRowStatus_Type = RowStatus
_AvipsIsakmpPeerRowStatus_Object = MibTableColumn
avipsIsakmpPeerRowStatus = _AvipsIsakmpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 13),
    _AvipsIsakmpPeerRowStatus_Type()
)
avipsIsakmpPeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerRowStatus.setStatus("current")


class _AvipsIsakmpPeerGroupFailbacktoPrimaryInterval_Type(Integer32):
    """Custom type avipsIsakmpPeerGroupFailbacktoPrimaryInterval based on Integer32"""
    defaultValue = 86400


_AvipsIsakmpPeerGroupFailbacktoPrimaryInterval_Object = MibTableColumn
avipsIsakmpPeerGroupFailbacktoPrimaryInterval = _AvipsIsakmpPeerGroupFailbacktoPrimaryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 1, 1, 14),
    _AvipsIsakmpPeerGroupFailbacktoPrimaryInterval_Type()
)
avipsIsakmpPeerGroupFailbacktoPrimaryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPeerGroupFailbacktoPrimaryInterval.setStatus("current")
if mibBuilder.loadTexts:
    avipsIsakmpPeerGroupFailbacktoPrimaryInterval.setUnits("seconds")
_AvipsPeerGroupPeersTable_Object = MibTable
avipsPeerGroupPeersTable = _AvipsPeerGroupPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    avipsPeerGroupPeersTable.setStatus("current")
_AvipsPeerGroupPeersEntry_Object = MibTableRow
avipsPeerGroupPeersEntry = _AvipsPeerGroupPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2, 1)
)
avipsPeerGroupPeersEntry.setIndexNames(
    (0, "AVAYA-IPSEC-MIB", "avipsPeerGroupPeersPGrpName"),
    (0, "AVAYA-IPSEC-MIB", "avipsPeerGroupPeersPeerIndex"),
)
if mibBuilder.loadTexts:
    avipsPeerGroupPeersEntry.setStatus("current")
_AvipsPeerGroupPeersPGrpName_Type = DisplayString
_AvipsPeerGroupPeersPGrpName_Object = MibTableColumn
avipsPeerGroupPeersPGrpName = _AvipsPeerGroupPeersPGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2, 1, 1),
    _AvipsPeerGroupPeersPGrpName_Type()
)
avipsPeerGroupPeersPGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsPeerGroupPeersPGrpName.setStatus("current")


class _AvipsPeerGroupPeersPeerIndex_Type(Integer32):
    """Custom type avipsPeerGroupPeersPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AvipsPeerGroupPeersPeerIndex_Type.__name__ = "Integer32"
_AvipsPeerGroupPeersPeerIndex_Object = MibTableColumn
avipsPeerGroupPeersPeerIndex = _AvipsPeerGroupPeersPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2, 1, 2),
    _AvipsPeerGroupPeersPeerIndex_Type()
)
avipsPeerGroupPeersPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsPeerGroupPeersPeerIndex.setStatus("current")


class _AvipsPeerGroupPeersPIdType_Type(IsakmpIdentityType):
    """Custom type avipsPeerGroupPeersPIdType based on IsakmpIdentityType"""
    subtypeSpec = IsakmpIdentityType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AvipsPeerGroupPeersPIdType_Type.__name__ = "IsakmpIdentityType"
_AvipsPeerGroupPeersPIdType_Object = MibTableColumn
avipsPeerGroupPeersPIdType = _AvipsPeerGroupPeersPIdType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2, 1, 3),
    _AvipsPeerGroupPeersPIdType_Type()
)
avipsPeerGroupPeersPIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsPeerGroupPeersPIdType.setStatus("current")
_AvipsPeerGroupPeersPIdValue_Type = IsakmpIdentityValue
_AvipsPeerGroupPeersPIdValue_Object = MibTableColumn
avipsPeerGroupPeersPIdValue = _AvipsPeerGroupPeersPIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2, 1, 4),
    _AvipsPeerGroupPeersPIdValue_Type()
)
avipsPeerGroupPeersPIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsPeerGroupPeersPIdValue.setStatus("current")
_AvipsPeerGroupPeersRowStatus_Type = RowStatus
_AvipsPeerGroupPeersRowStatus_Object = MibTableColumn
avipsPeerGroupPeersRowStatus = _AvipsPeerGroupPeersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 2, 1, 5),
    _AvipsPeerGroupPeersRowStatus_Type()
)
avipsPeerGroupPeersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsPeerGroupPeersRowStatus.setStatus("current")
_AvipsIsakmpPlcyTable_Object = MibTable
avipsIsakmpPlcyTable = _AvipsIsakmpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    avipsIsakmpPlcyTable.setStatus("current")
_AvipsIsakmpPlcyEntry_Object = MibTableRow
avipsIsakmpPlcyEntry = _AvipsIsakmpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1)
)
avipsIsakmpPlcyEntry.setIndexNames(
    (0, "AVAYA-IPSEC-MIB", "avipsIsakmpPlcyId"),
)
if mibBuilder.loadTexts:
    avipsIsakmpPlcyEntry.setStatus("current")


class _AvipsIsakmpPlcyId_Type(Integer32):
    """Custom type avipsIsakmpPlcyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AvipsIsakmpPlcyId_Type.__name__ = "Integer32"
_AvipsIsakmpPlcyId_Object = MibTableColumn
avipsIsakmpPlcyId = _AvipsIsakmpPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 1),
    _AvipsIsakmpPlcyId_Type()
)
avipsIsakmpPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyId.setStatus("current")


class _AvipsIsakmpPlcyDescription_Type(DisplayString):
    """Custom type avipsIsakmpPlcyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AvipsIsakmpPlcyDescription_Type.__name__ = "DisplayString"
_AvipsIsakmpPlcyDescription_Object = MibTableColumn
avipsIsakmpPlcyDescription = _AvipsIsakmpPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 2),
    _AvipsIsakmpPlcyDescription_Type()
)
avipsIsakmpPlcyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyDescription.setStatus("current")


class _AvipsIsakmpPlcyDhGroup_Type(DiffHellmanGrp):
    """Custom type avipsIsakmpPlcyDhGroup based on DiffHellmanGrp"""


_AvipsIsakmpPlcyDhGroup_Object = MibTableColumn
avipsIsakmpPlcyDhGroup = _AvipsIsakmpPlcyDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 3),
    _AvipsIsakmpPlcyDhGroup_Type()
)
avipsIsakmpPlcyDhGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyDhGroup.setStatus("current")


class _AvipsIsakmpPlcyEncrAlgo_Type(IkeEncryptAlgo):
    """Custom type avipsIsakmpPlcyEncrAlgo based on IkeEncryptAlgo"""


_AvipsIsakmpPlcyEncrAlgo_Object = MibTableColumn
avipsIsakmpPlcyEncrAlgo = _AvipsIsakmpPlcyEncrAlgo_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 4),
    _AvipsIsakmpPlcyEncrAlgo_Type()
)
avipsIsakmpPlcyEncrAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyEncrAlgo.setStatus("current")


class _AvipsIsakmpPlcyHashAlgo_Type(IkeHashAlgo):
    """Custom type avipsIsakmpPlcyHashAlgo based on IkeHashAlgo"""


_AvipsIsakmpPlcyHashAlgo_Object = MibTableColumn
avipsIsakmpPlcyHashAlgo = _AvipsIsakmpPlcyHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 5),
    _AvipsIsakmpPlcyHashAlgo_Type()
)
avipsIsakmpPlcyHashAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyHashAlgo.setStatus("current")


class _AvipsIsakmpPlcyLifetime_Type(Integer32):
    """Custom type avipsIsakmpPlcyLifetime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AvipsIsakmpPlcyLifetime_Type.__name__ = "Integer32"
_AvipsIsakmpPlcyLifetime_Object = MibTableColumn
avipsIsakmpPlcyLifetime = _AvipsIsakmpPlcyLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 6),
    _AvipsIsakmpPlcyLifetime_Type()
)
avipsIsakmpPlcyLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyLifetime.setUnits("seconds")


class _AvipsIsakmpPlcyAuth_Type(Integer32):
    """Custom type avipsIsakmpPlcyAuth based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("preSharedKey", 2))
    )


_AvipsIsakmpPlcyAuth_Type.__name__ = "Integer32"
_AvipsIsakmpPlcyAuth_Object = MibTableColumn
avipsIsakmpPlcyAuth = _AvipsIsakmpPlcyAuth_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 7),
    _AvipsIsakmpPlcyAuth_Type()
)
avipsIsakmpPlcyAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyAuth.setStatus("current")
_AvipsIsakmpPlcyRowStatus_Type = RowStatus
_AvipsIsakmpPlcyRowStatus_Object = MibTableColumn
avipsIsakmpPlcyRowStatus = _AvipsIsakmpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 2, 3, 1, 8),
    _AvipsIsakmpPlcyRowStatus_Type()
)
avipsIsakmpPlcyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsIsakmpPlcyRowStatus.setStatus("current")
_AvipsIpsecGroup_ObjectIdentity = ObjectIdentity
avipsIpsecGroup = _AvipsIpsecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3)
)
_AvipsCryptoMapTable_Object = MibTable
avipsCryptoMapTable = _AvipsCryptoMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    avipsCryptoMapTable.setStatus("current")
_AvipsCryptoMapEntry_Object = MibTableRow
avipsCryptoMapEntry = _AvipsCryptoMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1)
)
avipsCryptoMapEntry.setIndexNames(
    (0, "AVAYA-IPSEC-MIB", "avipsCryptoMapId"),
)
if mibBuilder.loadTexts:
    avipsCryptoMapEntry.setStatus("current")


class _AvipsCryptoMapId_Type(Integer32):
    """Custom type avipsCryptoMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AvipsCryptoMapId_Type.__name__ = "Integer32"
_AvipsCryptoMapId_Object = MibTableColumn
avipsCryptoMapId = _AvipsCryptoMapId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 1),
    _AvipsCryptoMapId_Type()
)
avipsCryptoMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsCryptoMapId.setStatus("current")


class _AvipsCryptoMapDescription_Type(DisplayString):
    """Custom type avipsCryptoMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AvipsCryptoMapDescription_Type.__name__ = "DisplayString"
_AvipsCryptoMapDescription_Object = MibTableColumn
avipsCryptoMapDescription = _AvipsCryptoMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 2),
    _AvipsCryptoMapDescription_Type()
)
avipsCryptoMapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapDescription.setStatus("current")


class _AvipsCryptoMapPeerIdType_Type(IsakmpIdentityType):
    """Custom type avipsCryptoMapPeerIdType based on IsakmpIdentityType"""
    subtypeSpec = IsakmpIdentityType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_AvipsCryptoMapPeerIdType_Type.__name__ = "IsakmpIdentityType"
_AvipsCryptoMapPeerIdType_Object = MibTableColumn
avipsCryptoMapPeerIdType = _AvipsCryptoMapPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 3),
    _AvipsCryptoMapPeerIdType_Type()
)
avipsCryptoMapPeerIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapPeerIdType.setStatus("current")
_AvipsCryptoMapPeerIdValue_Type = IsakmpIdentityValue
_AvipsCryptoMapPeerIdValue_Object = MibTableColumn
avipsCryptoMapPeerIdValue = _AvipsCryptoMapPeerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 4),
    _AvipsCryptoMapPeerIdValue_Type()
)
avipsCryptoMapPeerIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapPeerIdValue.setStatus("current")


class _AvipsCryptoMapTranSetName1_Type(DisplayString):
    """Custom type avipsCryptoMapTranSetName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AvipsCryptoMapTranSetName1_Type.__name__ = "DisplayString"
_AvipsCryptoMapTranSetName1_Object = MibTableColumn
avipsCryptoMapTranSetName1 = _AvipsCryptoMapTranSetName1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 5),
    _AvipsCryptoMapTranSetName1_Type()
)
avipsCryptoMapTranSetName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapTranSetName1.setStatus("current")


class _AvipsCryptoMapIsReady_Type(TruthValue):
    """Custom type avipsCryptoMapIsReady based on TruthValue"""


_AvipsCryptoMapIsReady_Object = MibTableColumn
avipsCryptoMapIsReady = _AvipsCryptoMapIsReady_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 6),
    _AvipsCryptoMapIsReady_Type()
)
avipsCryptoMapIsReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsCryptoMapIsReady.setStatus("current")


class _AvipsCryptoMapTunnelDscp_Type(Integer32):
    """Custom type avipsCryptoMapTunnelDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_AvipsCryptoMapTunnelDscp_Type.__name__ = "Integer32"
_AvipsCryptoMapTunnelDscp_Object = MibTableColumn
avipsCryptoMapTunnelDscp = _AvipsCryptoMapTunnelDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 7),
    _AvipsCryptoMapTunnelDscp_Type()
)
avipsCryptoMapTunnelDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapTunnelDscp.setStatus("current")


class _AvipsCryptoMapContChannel_Type(TruthValue):
    """Custom type avipsCryptoMapContChannel based on TruthValue"""


_AvipsCryptoMapContChannel_Object = MibTableColumn
avipsCryptoMapContChannel = _AvipsCryptoMapContChannel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 8),
    _AvipsCryptoMapContChannel_Type()
)
avipsCryptoMapContChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapContChannel.setStatus("current")
_AvipsCryptoMapRowStatus_Type = RowStatus
_AvipsCryptoMapRowStatus_Object = MibTableColumn
avipsCryptoMapRowStatus = _AvipsCryptoMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 1, 1, 9),
    _AvipsCryptoMapRowStatus_Type()
)
avipsCryptoMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsCryptoMapRowStatus.setStatus("current")
_AvipsTranSetTable_Object = MibTable
avipsTranSetTable = _AvipsTranSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    avipsTranSetTable.setStatus("current")
_AvipsTranSetEntry_Object = MibTableRow
avipsTranSetEntry = _AvipsTranSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1)
)
avipsTranSetEntry.setIndexNames(
    (1, "AVAYA-IPSEC-MIB", "avipsTranSetName"),
)
if mibBuilder.loadTexts:
    avipsTranSetEntry.setStatus("current")


class _AvipsTranSetName_Type(DisplayString):
    """Custom type avipsTranSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AvipsTranSetName_Type.__name__ = "DisplayString"
_AvipsTranSetName_Object = MibTableColumn
avipsTranSetName = _AvipsTranSetName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 1),
    _AvipsTranSetName_Type()
)
avipsTranSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsTranSetName.setStatus("current")


class _AvipsTranSetEspEncrTran_Type(EspEncrTransform):
    """Custom type avipsTranSetEspEncrTran based on EspEncrTransform"""


_AvipsTranSetEspEncrTran_Object = MibTableColumn
avipsTranSetEspEncrTran = _AvipsTranSetEspEncrTran_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 2),
    _AvipsTranSetEspEncrTran_Type()
)
avipsTranSetEspEncrTran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetEspEncrTran.setStatus("current")


class _AvipsTranSetEspHashTran_Type(EspHashTransform):
    """Custom type avipsTranSetEspHashTran based on EspHashTransform"""


_AvipsTranSetEspHashTran_Object = MibTableColumn
avipsTranSetEspHashTran = _AvipsTranSetEspHashTran_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 3),
    _AvipsTranSetEspHashTran_Type()
)
avipsTranSetEspHashTran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetEspHashTran.setStatus("current")


class _AvipsTranSetLifetime_Type(Integer32):
    """Custom type avipsTranSetLifetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 86400),
    )


_AvipsTranSetLifetime_Type.__name__ = "Integer32"
_AvipsTranSetLifetime_Object = MibTableColumn
avipsTranSetLifetime = _AvipsTranSetLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 4),
    _AvipsTranSetLifetime_Type()
)
avipsTranSetLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetLifetime.setStatus("current")
if mibBuilder.loadTexts:
    avipsTranSetLifetime.setUnits("seconds")


class _AvipsTranSetLifesize_Type(Integer32):
    """Custom type avipsTranSetLifesize based on Integer32"""
    defaultValue = 4608000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2560, 536870912),
    )


_AvipsTranSetLifesize_Type.__name__ = "Integer32"
_AvipsTranSetLifesize_Object = MibTableColumn
avipsTranSetLifesize = _AvipsTranSetLifesize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 5),
    _AvipsTranSetLifesize_Type()
)
avipsTranSetLifesize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetLifesize.setStatus("current")
if mibBuilder.loadTexts:
    avipsTranSetLifesize.setUnits("KBytes")


class _AvipsTranSetPfsGroup_Type(DiffHellmanGrp):
    """Custom type avipsTranSetPfsGroup based on DiffHellmanGrp"""


_AvipsTranSetPfsGroup_Object = MibTableColumn
avipsTranSetPfsGroup = _AvipsTranSetPfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 6),
    _AvipsTranSetPfsGroup_Type()
)
avipsTranSetPfsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetPfsGroup.setStatus("current")


class _AvipsTranSetEncapMode_Type(IpsecEncapMode):
    """Custom type avipsTranSetEncapMode based on IpsecEncapMode"""


_AvipsTranSetEncapMode_Object = MibTableColumn
avipsTranSetEncapMode = _AvipsTranSetEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 7),
    _AvipsTranSetEncapMode_Type()
)
avipsTranSetEncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetEncapMode.setStatus("current")


class _AvipsTranSetEspCompTran_Type(Integer32):
    """Custom type avipsTranSetEspCompTran based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ippcpLzs", 2),
          ("none", 1))
    )


_AvipsTranSetEspCompTran_Type.__name__ = "Integer32"
_AvipsTranSetEspCompTran_Object = MibTableColumn
avipsTranSetEspCompTran = _AvipsTranSetEspCompTran_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 8),
    _AvipsTranSetEspCompTran_Type()
)
avipsTranSetEspCompTran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranSetEspCompTran.setStatus("current")
_AvipsTranRowStatus_Type = RowStatus
_AvipsTranRowStatus_Object = MibTableColumn
avipsTranRowStatus = _AvipsTranRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 3, 2, 1, 9),
    _AvipsTranRowStatus_Type()
)
avipsTranRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsTranRowStatus.setStatus("current")
_AvipsMonitoringGroup_ObjectIdentity = ObjectIdentity
avipsMonitoringGroup = _AvipsMonitoringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4)
)
_AvipsMonitoringTables_ObjectIdentity = ObjectIdentity
avipsMonitoringTables = _AvipsMonitoringTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1)
)
_AvipsMonitoringTablesGlobals_ObjectIdentity = ObjectIdentity
avipsMonitoringTablesGlobals = _AvipsMonitoringTablesGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 1)
)


class _AvipsMonitorRstCntrs_Type(Integer32):
    """Custom type avipsMonitorRstCntrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("running", 1))
    )


_AvipsMonitorRstCntrs_Type.__name__ = "Integer32"
_AvipsMonitorRstCntrs_Object = MibScalar
avipsMonitorRstCntrs = _AvipsMonitorRstCntrs_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 1, 1),
    _AvipsMonitorRstCntrs_Type()
)
avipsMonitorRstCntrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avipsMonitorRstCntrs.setStatus("current")
_AvipsMonitorRstCntrsLastChange_Type = TimeStamp
_AvipsMonitorRstCntrsLastChange_Object = MibScalar
avipsMonitorRstCntrsLastChange = _AvipsMonitorRstCntrsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 1, 2),
    _AvipsMonitorRstCntrsLastChange_Type()
)
avipsMonitorRstCntrsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsMonitorRstCntrsLastChange.setStatus("current")
_AvipsPeerTable_Object = MibTable
avipsPeerTable = _AvipsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    avipsPeerTable.setStatus("current")
_AvipsPeerEntry_Object = MibTableRow
avipsPeerEntry = _AvipsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1)
)
avipsPeerEntry.setIndexNames(
    (0, "AVAYA-IPSEC-MIB", "avipsPeerLocalId"),
    (0, "AVAYA-IPSEC-MIB", "avipsPeerRemoteId"),
)
if mibBuilder.loadTexts:
    avipsPeerEntry.setStatus("current")
_AvipsPeerLocalId_Type = Unsigned32
_AvipsPeerLocalId_Object = MibTableColumn
avipsPeerLocalId = _AvipsPeerLocalId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 1),
    _AvipsPeerLocalId_Type()
)
avipsPeerLocalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsPeerLocalId.setStatus("current")
_AvipsPeerRemoteId_Type = Unsigned32
_AvipsPeerRemoteId_Object = MibTableColumn
avipsPeerRemoteId = _AvipsPeerRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 2),
    _AvipsPeerRemoteId_Type()
)
avipsPeerRemoteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsPeerRemoteId.setStatus("current")
_AvipsPeerLocalType_Type = IsakmpIdentityType
_AvipsPeerLocalType_Object = MibTableColumn
avipsPeerLocalType = _AvipsPeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 3),
    _AvipsPeerLocalType_Type()
)
avipsPeerLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerLocalType.setStatus("current")
_AvipsPeerLocalValue_Type = IsakmpIdentityValue
_AvipsPeerLocalValue_Object = MibTableColumn
avipsPeerLocalValue = _AvipsPeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 4),
    _AvipsPeerLocalValue_Type()
)
avipsPeerLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerLocalValue.setStatus("current")
_AvipsPeerRemoteType_Type = IsakmpIdentityType
_AvipsPeerRemoteType_Object = MibTableColumn
avipsPeerRemoteType = _AvipsPeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 5),
    _AvipsPeerRemoteType_Type()
)
avipsPeerRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemoteType.setStatus("current")
_AvipsPeerRemoteValue_Type = IsakmpIdentityValue
_AvipsPeerRemoteValue_Object = MibTableColumn
avipsPeerRemoteValue = _AvipsPeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 6),
    _AvipsPeerRemoteValue_Type()
)
avipsPeerRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemoteValue.setStatus("current")
_AvipsPeerRemoteDescription_Type = DisplayString
_AvipsPeerRemoteDescription_Object = MibTableColumn
avipsPeerRemoteDescription = _AvipsPeerRemoteDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 7),
    _AvipsPeerRemoteDescription_Type()
)
avipsPeerRemoteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemoteDescription.setStatus("current")
_AvipsPeerLocalAddress_Type = IpAddress
_AvipsPeerLocalAddress_Object = MibTableColumn
avipsPeerLocalAddress = _AvipsPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 8),
    _AvipsPeerLocalAddress_Type()
)
avipsPeerLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerLocalAddress.setStatus("current")
_AvipsPeerRemoteAddress_Type = IpAddress
_AvipsPeerRemoteAddress_Object = MibTableColumn
avipsPeerRemoteAddress = _AvipsPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 9),
    _AvipsPeerRemoteAddress_Type()
)
avipsPeerRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemoteAddress.setStatus("current")
_AvipsPeerRemotePeerGrpActiveIndex_Type = Integer32
_AvipsPeerRemotePeerGrpActiveIndex_Object = MibTableColumn
avipsPeerRemotePeerGrpActiveIndex = _AvipsPeerRemotePeerGrpActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 10),
    _AvipsPeerRemotePeerGrpActiveIndex_Type()
)
avipsPeerRemotePeerGrpActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemotePeerGrpActiveIndex.setStatus("current")
_AvipsPeerRemotePeerGrpActiveIdType_Type = IsakmpIdentityType
_AvipsPeerRemotePeerGrpActiveIdType_Object = MibTableColumn
avipsPeerRemotePeerGrpActiveIdType = _AvipsPeerRemotePeerGrpActiveIdType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 11),
    _AvipsPeerRemotePeerGrpActiveIdType_Type()
)
avipsPeerRemotePeerGrpActiveIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemotePeerGrpActiveIdType.setStatus("current")
_AvipsPeerRemotePeerGrpActiveIdValue_Type = IsakmpIdentityValue
_AvipsPeerRemotePeerGrpActiveIdValue_Object = MibTableColumn
avipsPeerRemotePeerGrpActiveIdValue = _AvipsPeerRemotePeerGrpActiveIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 12),
    _AvipsPeerRemotePeerGrpActiveIdValue_Type()
)
avipsPeerRemotePeerGrpActiveIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerRemotePeerGrpActiveIdValue.setStatus("current")


class _AvipsPeerIsakmpState_Type(Integer32):
    """Custom type avipsPeerIsakmpState based on Integer32"""
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
        *(("closed", 1),
          ("established", 3),
          ("failed", 4),
          ("inProgress", 2))
    )


_AvipsPeerIsakmpState_Type.__name__ = "Integer32"
_AvipsPeerIsakmpState_Object = MibTableColumn
avipsPeerIsakmpState = _AvipsPeerIsakmpState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 13),
    _AvipsPeerIsakmpState_Type()
)
avipsPeerIsakmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerIsakmpState.setStatus("current")
_AvipsPeerIsakmpStateLastChange_Type = TimeStamp
_AvipsPeerIsakmpStateLastChange_Object = MibTableColumn
avipsPeerIsakmpStateLastChange = _AvipsPeerIsakmpStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 14),
    _AvipsPeerIsakmpStateLastChange_Type()
)
avipsPeerIsakmpStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerIsakmpStateLastChange.setStatus("current")
_AvipsPeerTunnelsClosed_Type = Gauge32
_AvipsPeerTunnelsClosed_Object = MibTableColumn
avipsPeerTunnelsClosed = _AvipsPeerTunnelsClosed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 15),
    _AvipsPeerTunnelsClosed_Type()
)
avipsPeerTunnelsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerTunnelsClosed.setStatus("current")
_AvipsPeerTunnelsInProgress_Type = Gauge32
_AvipsPeerTunnelsInProgress_Object = MibTableColumn
avipsPeerTunnelsInProgress = _AvipsPeerTunnelsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 16),
    _AvipsPeerTunnelsInProgress_Type()
)
avipsPeerTunnelsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerTunnelsInProgress.setStatus("current")
_AvipsPeerTunnelsEstablished_Type = Gauge32
_AvipsPeerTunnelsEstablished_Object = MibTableColumn
avipsPeerTunnelsEstablished = _AvipsPeerTunnelsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 17),
    _AvipsPeerTunnelsEstablished_Type()
)
avipsPeerTunnelsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerTunnelsEstablished.setStatus("current")
_AvipsPeerTunnelsFailed_Type = Gauge32
_AvipsPeerTunnelsFailed_Object = MibTableColumn
avipsPeerTunnelsFailed = _AvipsPeerTunnelsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 18),
    _AvipsPeerTunnelsFailed_Type()
)
avipsPeerTunnelsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerTunnelsFailed.setStatus("current")
_AvipsPeerInOctets_Type = Counter32
_AvipsPeerInOctets_Object = MibTableColumn
avipsPeerInOctets = _AvipsPeerInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 19),
    _AvipsPeerInOctets_Type()
)
avipsPeerInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInOctets.setStatus("current")
_AvipsPeerInOctetsWraps_Type = Counter32
_AvipsPeerInOctetsWraps_Object = MibTableColumn
avipsPeerInOctetsWraps = _AvipsPeerInOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 20),
    _AvipsPeerInOctetsWraps_Type()
)
avipsPeerInOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInOctetsWraps.setStatus("current")
_AvipsPeerInDecompOctets_Type = Counter32
_AvipsPeerInDecompOctets_Object = MibTableColumn
avipsPeerInDecompOctets = _AvipsPeerInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 21),
    _AvipsPeerInDecompOctets_Type()
)
avipsPeerInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInDecompOctets.setStatus("current")
_AvipsPeerInDecompOctetsWraps_Type = Counter32
_AvipsPeerInDecompOctetsWraps_Object = MibTableColumn
avipsPeerInDecompOctetsWraps = _AvipsPeerInDecompOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 22),
    _AvipsPeerInDecompOctetsWraps_Type()
)
avipsPeerInDecompOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInDecompOctetsWraps.setStatus("current")
_AvipsPeerInDecompRatio_Type = Gauge32
_AvipsPeerInDecompRatio_Object = MibTableColumn
avipsPeerInDecompRatio = _AvipsPeerInDecompRatio_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 23),
    _AvipsPeerInDecompRatio_Type()
)
avipsPeerInDecompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInDecompRatio.setStatus("current")
if mibBuilder.loadTexts:
    avipsPeerInDecompRatio.setUnits("Ratio * 100")
_AvipsPeerInPkts_Type = Counter32
_AvipsPeerInPkts_Object = MibTableColumn
avipsPeerInPkts = _AvipsPeerInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 24),
    _AvipsPeerInPkts_Type()
)
avipsPeerInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInPkts.setStatus("current")
_AvipsPeerInDropPkts_Type = Counter32
_AvipsPeerInDropPkts_Object = MibTableColumn
avipsPeerInDropPkts = _AvipsPeerInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 25),
    _AvipsPeerInDropPkts_Type()
)
avipsPeerInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerInDropPkts.setStatus("current")
_AvipsPeerOutOctets_Type = Counter32
_AvipsPeerOutOctets_Object = MibTableColumn
avipsPeerOutOctets = _AvipsPeerOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 26),
    _AvipsPeerOutOctets_Type()
)
avipsPeerOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutOctets.setStatus("current")
_AvipsPeerOutOctetsWraps_Type = Counter32
_AvipsPeerOutOctetsWraps_Object = MibTableColumn
avipsPeerOutOctetsWraps = _AvipsPeerOutOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 27),
    _AvipsPeerOutOctetsWraps_Type()
)
avipsPeerOutOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutOctetsWraps.setStatus("current")
_AvipsPeerOutUncompOctets_Type = Counter32
_AvipsPeerOutUncompOctets_Object = MibTableColumn
avipsPeerOutUncompOctets = _AvipsPeerOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 28),
    _AvipsPeerOutUncompOctets_Type()
)
avipsPeerOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutUncompOctets.setStatus("current")
_AvipsPeerOutUncompOctetsWraps_Type = Counter32
_AvipsPeerOutUncompOctetsWraps_Object = MibTableColumn
avipsPeerOutUncompOctetsWraps = _AvipsPeerOutUncompOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 29),
    _AvipsPeerOutUncompOctetsWraps_Type()
)
avipsPeerOutUncompOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutUncompOctetsWraps.setStatus("current")
_AvipsPeerOutCompRatio_Type = Gauge32
_AvipsPeerOutCompRatio_Object = MibTableColumn
avipsPeerOutCompRatio = _AvipsPeerOutCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 30),
    _AvipsPeerOutCompRatio_Type()
)
avipsPeerOutCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutCompRatio.setStatus("current")
if mibBuilder.loadTexts:
    avipsPeerOutCompRatio.setUnits("Ratio * 100")
_AvipsPeerOutPkts_Type = Counter32
_AvipsPeerOutPkts_Object = MibTableColumn
avipsPeerOutPkts = _AvipsPeerOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 31),
    _AvipsPeerOutPkts_Type()
)
avipsPeerOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutPkts.setStatus("current")
_AvipsPeerOutDropPkts_Type = Counter32
_AvipsPeerOutDropPkts_Object = MibTableColumn
avipsPeerOutDropPkts = _AvipsPeerOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 2, 1, 32),
    _AvipsPeerOutDropPkts_Type()
)
avipsPeerOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsPeerOutDropPkts.setStatus("current")
_AvipsTunnelTable_Object = MibTable
avipsTunnelTable = _AvipsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    avipsTunnelTable.setStatus("current")
_AvipsTunnelEntry_Object = MibTableRow
avipsTunnelEntry = _AvipsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1)
)
avipsTunnelEntry.setIndexNames(
    (0, "AVAYA-IPSEC-MIB", "avipsTunnelIndex"),
    (0, "AVAYA-IPSEC-MIB", "avipsTunnelSubIndex"),
    (0, "AVAYA-IPSEC-MIB", "avipsTunnelPeerLocalId"),
    (0, "AVAYA-IPSEC-MIB", "avipsTunnelPeerRemoteId"),
)
if mibBuilder.loadTexts:
    avipsTunnelEntry.setStatus("current")
_AvipsTunnelPeerLocalId_Type = Unsigned32
_AvipsTunnelPeerLocalId_Object = MibTableColumn
avipsTunnelPeerLocalId = _AvipsTunnelPeerLocalId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 1),
    _AvipsTunnelPeerLocalId_Type()
)
avipsTunnelPeerLocalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsTunnelPeerLocalId.setStatus("current")
_AvipsTunnelPeerRemoteId_Type = Unsigned32
_AvipsTunnelPeerRemoteId_Object = MibTableColumn
avipsTunnelPeerRemoteId = _AvipsTunnelPeerRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 2),
    _AvipsTunnelPeerRemoteId_Type()
)
avipsTunnelPeerRemoteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsTunnelPeerRemoteId.setStatus("current")


class _AvipsTunnelIndex_Type(Integer32):
    """Custom type avipsTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AvipsTunnelIndex_Type.__name__ = "Integer32"
_AvipsTunnelIndex_Object = MibTableColumn
avipsTunnelIndex = _AvipsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 3),
    _AvipsTunnelIndex_Type()
)
avipsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsTunnelIndex.setStatus("current")


class _AvipsTunnelSubIndex_Type(Integer32):
    """Custom type avipsTunnelSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AvipsTunnelSubIndex_Type.__name__ = "Integer32"
_AvipsTunnelSubIndex_Object = MibTableColumn
avipsTunnelSubIndex = _AvipsTunnelSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 4),
    _AvipsTunnelSubIndex_Type()
)
avipsTunnelSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avipsTunnelSubIndex.setStatus("current")
_AvipsTunnelPeerLocalType_Type = IsakmpIdentityType
_AvipsTunnelPeerLocalType_Object = MibTableColumn
avipsTunnelPeerLocalType = _AvipsTunnelPeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 5),
    _AvipsTunnelPeerLocalType_Type()
)
avipsTunnelPeerLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelPeerLocalType.setStatus("current")
_AvipsTunnelPeerLocalValue_Type = IsakmpIdentityValue
_AvipsTunnelPeerLocalValue_Object = MibTableColumn
avipsTunnelPeerLocalValue = _AvipsTunnelPeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 6),
    _AvipsTunnelPeerLocalValue_Type()
)
avipsTunnelPeerLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelPeerLocalValue.setStatus("current")
_AvipsTunnelPeerRemoteType_Type = IsakmpIdentityType
_AvipsTunnelPeerRemoteType_Object = MibTableColumn
avipsTunnelPeerRemoteType = _AvipsTunnelPeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 7),
    _AvipsTunnelPeerRemoteType_Type()
)
avipsTunnelPeerRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelPeerRemoteType.setStatus("current")
_AvipsTunnelPeerRemoteValue_Type = IsakmpIdentityValue
_AvipsTunnelPeerRemoteValue_Object = MibTableColumn
avipsTunnelPeerRemoteValue = _AvipsTunnelPeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 8),
    _AvipsTunnelPeerRemoteValue_Type()
)
avipsTunnelPeerRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelPeerRemoteValue.setStatus("current")
_AvipsTunnelDescription_Type = DisplayString
_AvipsTunnelDescription_Object = MibTableColumn
avipsTunnelDescription = _AvipsTunnelDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 9),
    _AvipsTunnelDescription_Type()
)
avipsTunnelDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelDescription.setStatus("current")
_AvipsTunnelLocalAddress_Type = IpAddress
_AvipsTunnelLocalAddress_Object = MibTableColumn
avipsTunnelLocalAddress = _AvipsTunnelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 10),
    _AvipsTunnelLocalAddress_Type()
)
avipsTunnelLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelLocalAddress.setStatus("current")
_AvipsTunnelRemoteAddress_Type = IpAddress
_AvipsTunnelRemoteAddress_Object = MibTableColumn
avipsTunnelRemoteAddress = _AvipsTunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 11),
    _AvipsTunnelRemoteAddress_Type()
)
avipsTunnelRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelRemoteAddress.setStatus("current")
_AvipsTunnelProxyLocalSubnet_Type = IpAddress
_AvipsTunnelProxyLocalSubnet_Object = MibTableColumn
avipsTunnelProxyLocalSubnet = _AvipsTunnelProxyLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 12),
    _AvipsTunnelProxyLocalSubnet_Type()
)
avipsTunnelProxyLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelProxyLocalSubnet.setStatus("current")
_AvipsTunnelProxyLocalMask_Type = IpAddress
_AvipsTunnelProxyLocalMask_Object = MibTableColumn
avipsTunnelProxyLocalMask = _AvipsTunnelProxyLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 13),
    _AvipsTunnelProxyLocalMask_Type()
)
avipsTunnelProxyLocalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelProxyLocalMask.setStatus("current")
_AvipsTunnelProxyRemoteSubnet_Type = IpAddress
_AvipsTunnelProxyRemoteSubnet_Object = MibTableColumn
avipsTunnelProxyRemoteSubnet = _AvipsTunnelProxyRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 14),
    _AvipsTunnelProxyRemoteSubnet_Type()
)
avipsTunnelProxyRemoteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelProxyRemoteSubnet.setStatus("current")
_AvipsTunnelProxyRemoteMask_Type = IpAddress
_AvipsTunnelProxyRemoteMask_Object = MibTableColumn
avipsTunnelProxyRemoteMask = _AvipsTunnelProxyRemoteMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 15),
    _AvipsTunnelProxyRemoteMask_Type()
)
avipsTunnelProxyRemoteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelProxyRemoteMask.setStatus("current")


class _AvipsTunnelState_Type(Integer32):
    """Custom type avipsTunnelState based on Integer32"""
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
        *(("closed", 1),
          ("established", 3),
          ("failed", 4),
          ("inProgress", 2))
    )


_AvipsTunnelState_Type.__name__ = "Integer32"
_AvipsTunnelState_Object = MibTableColumn
avipsTunnelState = _AvipsTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 16),
    _AvipsTunnelState_Type()
)
avipsTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelState.setStatus("current")
_AvipsTunnelStateLastChange_Type = TimeStamp
_AvipsTunnelStateLastChange_Object = MibTableColumn
avipsTunnelStateLastChange = _AvipsTunnelStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 17),
    _AvipsTunnelStateLastChange_Type()
)
avipsTunnelStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelStateLastChange.setStatus("current")
_AvipsTunnelLastCntrsReset_Type = TimeStamp
_AvipsTunnelLastCntrsReset_Object = MibTableColumn
avipsTunnelLastCntrsReset = _AvipsTunnelLastCntrsReset_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 18),
    _AvipsTunnelLastCntrsReset_Type()
)
avipsTunnelLastCntrsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelLastCntrsReset.setStatus("current")
_AvipsTunnelInOctets_Type = Counter32
_AvipsTunnelInOctets_Object = MibTableColumn
avipsTunnelInOctets = _AvipsTunnelInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 19),
    _AvipsTunnelInOctets_Type()
)
avipsTunnelInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInOctets.setStatus("current")
_AvipsTunnelInOctetsWraps_Type = Counter32
_AvipsTunnelInOctetsWraps_Object = MibTableColumn
avipsTunnelInOctetsWraps = _AvipsTunnelInOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 20),
    _AvipsTunnelInOctetsWraps_Type()
)
avipsTunnelInOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInOctetsWraps.setStatus("current")
_AvipsTunnelInDecompOctets_Type = Counter32
_AvipsTunnelInDecompOctets_Object = MibTableColumn
avipsTunnelInDecompOctets = _AvipsTunnelInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 21),
    _AvipsTunnelInDecompOctets_Type()
)
avipsTunnelInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDecompOctets.setStatus("current")
_AvipsTunnelInDecompOctetsWraps_Type = Counter32
_AvipsTunnelInDecompOctetsWraps_Object = MibTableColumn
avipsTunnelInDecompOctetsWraps = _AvipsTunnelInDecompOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 22),
    _AvipsTunnelInDecompOctetsWraps_Type()
)
avipsTunnelInDecompOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDecompOctetsWraps.setStatus("current")
_AvipsTunnelInDecompRatio_Type = Gauge32
_AvipsTunnelInDecompRatio_Object = MibTableColumn
avipsTunnelInDecompRatio = _AvipsTunnelInDecompRatio_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 23),
    _AvipsTunnelInDecompRatio_Type()
)
avipsTunnelInDecompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDecompRatio.setStatus("current")
if mibBuilder.loadTexts:
    avipsTunnelInDecompRatio.setUnits("Ratio * 100")
_AvipsTunnelInPkts_Type = Counter32
_AvipsTunnelInPkts_Object = MibTableColumn
avipsTunnelInPkts = _AvipsTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 24),
    _AvipsTunnelInPkts_Type()
)
avipsTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInPkts.setStatus("current")
_AvipsTunnelInDropTotalPkts_Type = Counter32
_AvipsTunnelInDropTotalPkts_Object = MibTableColumn
avipsTunnelInDropTotalPkts = _AvipsTunnelInDropTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 25),
    _AvipsTunnelInDropTotalPkts_Type()
)
avipsTunnelInDropTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropTotalPkts.setStatus("current")
_AvipsTunnelInDropAntiReplayPkts_Type = Counter32
_AvipsTunnelInDropAntiReplayPkts_Object = MibTableColumn
avipsTunnelInDropAntiReplayPkts = _AvipsTunnelInDropAntiReplayPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 26),
    _AvipsTunnelInDropAntiReplayPkts_Type()
)
avipsTunnelInDropAntiReplayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropAntiReplayPkts.setStatus("current")
_AvipsTunnelInDropHmacFailPkts_Type = Counter32
_AvipsTunnelInDropHmacFailPkts_Object = MibTableColumn
avipsTunnelInDropHmacFailPkts = _AvipsTunnelInDropHmacFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 27),
    _AvipsTunnelInDropHmacFailPkts_Type()
)
avipsTunnelInDropHmacFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropHmacFailPkts.setStatus("current")
_AvipsTunnelInDropBadTrailerPkts_Type = Counter32
_AvipsTunnelInDropBadTrailerPkts_Object = MibTableColumn
avipsTunnelInDropBadTrailerPkts = _AvipsTunnelInDropBadTrailerPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 28),
    _AvipsTunnelInDropBadTrailerPkts_Type()
)
avipsTunnelInDropBadTrailerPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropBadTrailerPkts.setStatus("current")
_AvipsTunnelInDropInvalidIdPkts_Type = Counter32
_AvipsTunnelInDropInvalidIdPkts_Object = MibTableColumn
avipsTunnelInDropInvalidIdPkts = _AvipsTunnelInDropInvalidIdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 29),
    _AvipsTunnelInDropInvalidIdPkts_Type()
)
avipsTunnelInDropInvalidIdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropInvalidIdPkts.setStatus("current")
_AvipsTunnelInDropUnprotectPkts_Type = Counter32
_AvipsTunnelInDropUnprotectPkts_Object = MibTableColumn
avipsTunnelInDropUnprotectPkts = _AvipsTunnelInDropUnprotectPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 30),
    _AvipsTunnelInDropUnprotectPkts_Type()
)
avipsTunnelInDropUnprotectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropUnprotectPkts.setStatus("current")
_AvipsTunnelInDropInvalidLenPkts_Type = Counter32
_AvipsTunnelInDropInvalidLenPkts_Object = MibTableColumn
avipsTunnelInDropInvalidLenPkts = _AvipsTunnelInDropInvalidLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 31),
    _AvipsTunnelInDropInvalidLenPkts_Type()
)
avipsTunnelInDropInvalidLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropInvalidLenPkts.setStatus("current")
_AvipsTunnelInDropSaExpiredPkts_Type = Counter32
_AvipsTunnelInDropSaExpiredPkts_Object = MibTableColumn
avipsTunnelInDropSaExpiredPkts = _AvipsTunnelInDropSaExpiredPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 32),
    _AvipsTunnelInDropSaExpiredPkts_Type()
)
avipsTunnelInDropSaExpiredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelInDropSaExpiredPkts.setStatus("current")
_AvipsTunnelOutOctets_Type = Counter32
_AvipsTunnelOutOctets_Object = MibTableColumn
avipsTunnelOutOctets = _AvipsTunnelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 33),
    _AvipsTunnelOutOctets_Type()
)
avipsTunnelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutOctets.setStatus("current")
_AvipsTunnelOutOctetsWraps_Type = Counter32
_AvipsTunnelOutOctetsWraps_Object = MibTableColumn
avipsTunnelOutOctetsWraps = _AvipsTunnelOutOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 34),
    _AvipsTunnelOutOctetsWraps_Type()
)
avipsTunnelOutOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutOctetsWraps.setStatus("current")
_AvipsTunnelOutUncompOctets_Type = Counter32
_AvipsTunnelOutUncompOctets_Object = MibTableColumn
avipsTunnelOutUncompOctets = _AvipsTunnelOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 35),
    _AvipsTunnelOutUncompOctets_Type()
)
avipsTunnelOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutUncompOctets.setStatus("current")
_AvipsTunnelOutUncompOctetsWraps_Type = Counter32
_AvipsTunnelOutUncompOctetsWraps_Object = MibTableColumn
avipsTunnelOutUncompOctetsWraps = _AvipsTunnelOutUncompOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 36),
    _AvipsTunnelOutUncompOctetsWraps_Type()
)
avipsTunnelOutUncompOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutUncompOctetsWraps.setStatus("current")
_AvipsTunnelOutCompRatio_Type = Gauge32
_AvipsTunnelOutCompRatio_Object = MibTableColumn
avipsTunnelOutCompRatio = _AvipsTunnelOutCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 37),
    _AvipsTunnelOutCompRatio_Type()
)
avipsTunnelOutCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutCompRatio.setStatus("current")
if mibBuilder.loadTexts:
    avipsTunnelOutCompRatio.setUnits("Ratio * 100")
_AvipsTunnelOutPkts_Type = Counter32
_AvipsTunnelOutPkts_Object = MibTableColumn
avipsTunnelOutPkts = _AvipsTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 38),
    _AvipsTunnelOutPkts_Type()
)
avipsTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutPkts.setStatus("current")
_AvipsTunnelOutDropTotalPkts_Type = Counter32
_AvipsTunnelOutDropTotalPkts_Object = MibTableColumn
avipsTunnelOutDropTotalPkts = _AvipsTunnelOutDropTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 39),
    _AvipsTunnelOutDropTotalPkts_Type()
)
avipsTunnelOutDropTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutDropTotalPkts.setStatus("current")
_AvipsTunnelOutDropNoSaPkts_Type = Counter32
_AvipsTunnelOutDropNoSaPkts_Object = MibTableColumn
avipsTunnelOutDropNoSaPkts = _AvipsTunnelOutDropNoSaPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 40),
    _AvipsTunnelOutDropNoSaPkts_Type()
)
avipsTunnelOutDropNoSaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutDropNoSaPkts.setStatus("current")
_AvipsTunnelOutDropSeqRolPkts_Type = Counter32
_AvipsTunnelOutDropSeqRolPkts_Object = MibTableColumn
avipsTunnelOutDropSeqRolPkts = _AvipsTunnelOutDropSeqRolPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 41),
    _AvipsTunnelOutDropSeqRolPkts_Type()
)
avipsTunnelOutDropSeqRolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutDropSeqRolPkts.setStatus("current")
_AvipsTunnelOutDropSaExpiredPkts_Type = Counter32
_AvipsTunnelOutDropSaExpiredPkts_Object = MibTableColumn
avipsTunnelOutDropSaExpiredPkts = _AvipsTunnelOutDropSaExpiredPkts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 1, 4, 1, 3, 1, 42),
    _AvipsTunnelOutDropSaExpiredPkts_Type()
)
avipsTunnelOutDropSaExpiredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avipsTunnelOutDropSaExpiredPkts.setStatus("current")
_AvipsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
avipsMIBNotificationPrefix = _AvipsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2)
)
_AvipsMIBNotifications_ObjectIdentity = ObjectIdentity
avipsMIBNotifications = _AvipsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0)
)
_AvipsMIBConformance_ObjectIdentity = ObjectIdentity
avipsMIBConformance = _AvipsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 3)
)
_AvipsMIBGroups_ObjectIdentity = ObjectIdentity
avipsMIBGroups = _AvipsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 3, 1)
)
_AvipsMIBCompliances_ObjectIdentity = ObjectIdentity
avipsMIBCompliances = _AvipsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 3, 2)
)

# Managed Objects groups

avipsConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 3, 1, 1)
)
avipsConfigurationGroup.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsGlobalsInvalidSpiRecovery"),
        ("AVAYA-IPSEC-MIB", "avipsNatTEnabled"),
        ("AVAYA-IPSEC-MIB", "avipsNatTKeepaliveInterval"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerDescription"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerIsaPlcyId1"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerSelfIdType"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerSelfId"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerKeepaliveMetric"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerKeepaliveInterval"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerKeepaliveRetryInterval"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerKeepaliveTrackId"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerContChannel"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerRowStatus"),
        ("AVAYA-IPSEC-MIB", "avipsPeerGroupPeersPIdType"),
        ("AVAYA-IPSEC-MIB", "avipsPeerGroupPeersPIdValue"),
        ("AVAYA-IPSEC-MIB", "avipsPeerGroupPeersRowStatus"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyDescription"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyDhGroup"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyEncrAlgo"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyHashAlgo"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyLifetime"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyAuth"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPlcyRowStatus"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapDescription"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapPeerIdType"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapPeerIdValue"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapTranSetName1"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapIsReady"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapTunnelDscp"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapContChannel"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoMapRowStatus"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetEspEncrTran"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetEspHashTran"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetLifetime"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetLifesize"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetPfsGroup"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetEncapMode"),
        ("AVAYA-IPSEC-MIB", "avipsTranSetEspCompTran"),
        ("AVAYA-IPSEC-MIB", "avipsTranRowStatus"),
        ("AVAYA-IPSEC-MIB", "avipsCryptoEngineAccelEnabled"),
        ("AVAYA-IPSEC-MIB", "avipsIsakmpPeerInitiateMode"))
)
if mibBuilder.loadTexts:
    avipsConfigurationGroup.setStatus("current")

avipsMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 3, 1, 2)
)
avipsMonitorGroup.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsMonitorRstCntrs"),
        ("AVAYA-IPSEC-MIB", "avipsMonitorRstCntrsLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteDescription"),
        ("AVAYA-IPSEC-MIB", "avipsPeerLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerIsakmpState"),
        ("AVAYA-IPSEC-MIB", "avipsPeerIsakmpStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInOctets"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInPkts"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInDropPkts"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutOctets"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutPkts"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutDropPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelDescription"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelState"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInOctets"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropAntiReplayPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropHmacFailPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropBadTrailerPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropInvalidIdPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropUnprotectPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropInvalidLenPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropSaExpiredPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutOctets"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutDropNoSaPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutDropSeqRolPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutDropSaExpiredPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelLastCntrsReset"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemotePeerGrpActiveIdValue"),
        ("AVAYA-IPSEC-MIB", "avipsPeerTunnelsClosed"),
        ("AVAYA-IPSEC-MIB", "avipsPeerTunnelsInProgress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerTunnelsEstablished"),
        ("AVAYA-IPSEC-MIB", "avipsPeerTunnelsFailed"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDecompOctets"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDecompOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutUncompOctets"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutUncompOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInDecompOctets"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInDecompOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutUncompOctetsWraps"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutUncompOctets"),
        ("AVAYA-IPSEC-MIB", "avipsPeerInDecompRatio"),
        ("AVAYA-IPSEC-MIB", "avipsPeerOutCompRatio"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDecompRatio"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutCompRatio"),
        ("AVAYA-IPSEC-MIB", "avipsPeerLocalType"),
        ("AVAYA-IPSEC-MIB", "avipsPeerLocalValue"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteType"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteValue"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelPeerLocalType"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelPeerLocalValue"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelPeerRemoteType"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelPeerRemoteValue"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemotePeerGrpActiveIdType"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemotePeerGrpActiveIndex"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelInDropTotalPkts"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelOutDropTotalPkts"))
)
if mibBuilder.loadTexts:
    avipsMonitorGroup.setStatus("current")


# Notification objects

avipsIskampEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0, 1)
)
avipsIskampEstablished.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsPeerLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerIsakmpStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteDescription"))
)
if mibBuilder.loadTexts:
    avipsIskampEstablished.setStatus(
        "current"
    )

avipsIskampClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0, 2)
)
avipsIskampClosed.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsPeerLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerIsakmpStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteDescription"))
)
if mibBuilder.loadTexts:
    avipsIskampClosed.setStatus(
        "current"
    )

avipsIskampFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0, 3)
)
avipsIskampFailed.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsPeerLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsPeerIsakmpStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsPeerRemoteDescription"))
)
if mibBuilder.loadTexts:
    avipsIskampFailed.setStatus(
        "current"
    )

avipsIpsecTunnelEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0, 4)
)
avipsIpsecTunnelEstablished.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsTunnelLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelDescription"))
)
if mibBuilder.loadTexts:
    avipsIpsecTunnelEstablished.setStatus(
        "current"
    )

avipsIpsecTunnelClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0, 5)
)
avipsIpsecTunnelClosed.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsTunnelLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelDescription"))
)
if mibBuilder.loadTexts:
    avipsIpsecTunnelClosed.setStatus(
        "current"
    )

avipsIpsecTunnelFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 2, 0, 6)
)
avipsIpsecTunnelFailed.setObjects(
      *(("AVAYA-IPSEC-MIB", "avipsTunnelLocalAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelRemoteAddress"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyLocalMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteSubnet"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelProxyRemoteMask"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelStateLastChange"),
        ("AVAYA-IPSEC-MIB", "avipsTunnelDescription"))
)
if mibBuilder.loadTexts:
    avipsIpsecTunnelFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

avipsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    avipsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-IPSEC-MIB",
    **{"DiffHellmanGrp": DiffHellmanGrp,
       "IkeEncryptAlgo": IkeEncryptAlgo,
       "IkeHashAlgo": IkeHashAlgo,
       "EspHashTransform": EspHashTransform,
       "EspEncrTransform": EspEncrTransform,
       "IsakmpIdentityType": IsakmpIdentityType,
       "IsakmpIdentityValue": IsakmpIdentityValue,
       "IsakmpDpdKeepaliveMetric": IsakmpDpdKeepaliveMetric,
       "IpsecEncapMode": IpsecEncapMode,
       "avayaIpsecMib": avayaIpsecMib,
       "avipsMIBObjects": avipsMIBObjects,
       "avipsGlobals": avipsGlobals,
       "avipsGlobalsInvalidSpiRecovery": avipsGlobalsInvalidSpiRecovery,
       "avipsNatTEnabled": avipsNatTEnabled,
       "avipsNatTKeepaliveInterval": avipsNatTKeepaliveInterval,
       "avipsCryptoEngineAccelEnabled": avipsCryptoEngineAccelEnabled,
       "avipsIsakmpGroup": avipsIsakmpGroup,
       "avipsIsakmpPeerTable": avipsIsakmpPeerTable,
       "avipsIsakmpPeerEntry": avipsIsakmpPeerEntry,
       "avipsIsakmpPeerIdType": avipsIsakmpPeerIdType,
       "avipsIsakmpPeerId": avipsIsakmpPeerId,
       "avipsIsakmpPeerDescription": avipsIsakmpPeerDescription,
       "avipsIsakmpPeerIsaPlcyId1": avipsIsakmpPeerIsaPlcyId1,
       "avipsIsakmpPeerInitiateMode": avipsIsakmpPeerInitiateMode,
       "avipsIsakmpPeerSelfIdType": avipsIsakmpPeerSelfIdType,
       "avipsIsakmpPeerSelfId": avipsIsakmpPeerSelfId,
       "avipsIsakmpPeerKeepaliveMetric": avipsIsakmpPeerKeepaliveMetric,
       "avipsIsakmpPeerKeepaliveInterval": avipsIsakmpPeerKeepaliveInterval,
       "avipsIsakmpPeerKeepaliveRetryInterval": avipsIsakmpPeerKeepaliveRetryInterval,
       "avipsIsakmpPeerKeepaliveTrackId": avipsIsakmpPeerKeepaliveTrackId,
       "avipsIsakmpPeerContChannel": avipsIsakmpPeerContChannel,
       "avipsIsakmpPeerRowStatus": avipsIsakmpPeerRowStatus,
       "avipsIsakmpPeerGroupFailbacktoPrimaryInterval": avipsIsakmpPeerGroupFailbacktoPrimaryInterval,
       "avipsPeerGroupPeersTable": avipsPeerGroupPeersTable,
       "avipsPeerGroupPeersEntry": avipsPeerGroupPeersEntry,
       "avipsPeerGroupPeersPGrpName": avipsPeerGroupPeersPGrpName,
       "avipsPeerGroupPeersPeerIndex": avipsPeerGroupPeersPeerIndex,
       "avipsPeerGroupPeersPIdType": avipsPeerGroupPeersPIdType,
       "avipsPeerGroupPeersPIdValue": avipsPeerGroupPeersPIdValue,
       "avipsPeerGroupPeersRowStatus": avipsPeerGroupPeersRowStatus,
       "avipsIsakmpPlcyTable": avipsIsakmpPlcyTable,
       "avipsIsakmpPlcyEntry": avipsIsakmpPlcyEntry,
       "avipsIsakmpPlcyId": avipsIsakmpPlcyId,
       "avipsIsakmpPlcyDescription": avipsIsakmpPlcyDescription,
       "avipsIsakmpPlcyDhGroup": avipsIsakmpPlcyDhGroup,
       "avipsIsakmpPlcyEncrAlgo": avipsIsakmpPlcyEncrAlgo,
       "avipsIsakmpPlcyHashAlgo": avipsIsakmpPlcyHashAlgo,
       "avipsIsakmpPlcyLifetime": avipsIsakmpPlcyLifetime,
       "avipsIsakmpPlcyAuth": avipsIsakmpPlcyAuth,
       "avipsIsakmpPlcyRowStatus": avipsIsakmpPlcyRowStatus,
       "avipsIpsecGroup": avipsIpsecGroup,
       "avipsCryptoMapTable": avipsCryptoMapTable,
       "avipsCryptoMapEntry": avipsCryptoMapEntry,
       "avipsCryptoMapId": avipsCryptoMapId,
       "avipsCryptoMapDescription": avipsCryptoMapDescription,
       "avipsCryptoMapPeerIdType": avipsCryptoMapPeerIdType,
       "avipsCryptoMapPeerIdValue": avipsCryptoMapPeerIdValue,
       "avipsCryptoMapTranSetName1": avipsCryptoMapTranSetName1,
       "avipsCryptoMapIsReady": avipsCryptoMapIsReady,
       "avipsCryptoMapTunnelDscp": avipsCryptoMapTunnelDscp,
       "avipsCryptoMapContChannel": avipsCryptoMapContChannel,
       "avipsCryptoMapRowStatus": avipsCryptoMapRowStatus,
       "avipsTranSetTable": avipsTranSetTable,
       "avipsTranSetEntry": avipsTranSetEntry,
       "avipsTranSetName": avipsTranSetName,
       "avipsTranSetEspEncrTran": avipsTranSetEspEncrTran,
       "avipsTranSetEspHashTran": avipsTranSetEspHashTran,
       "avipsTranSetLifetime": avipsTranSetLifetime,
       "avipsTranSetLifesize": avipsTranSetLifesize,
       "avipsTranSetPfsGroup": avipsTranSetPfsGroup,
       "avipsTranSetEncapMode": avipsTranSetEncapMode,
       "avipsTranSetEspCompTran": avipsTranSetEspCompTran,
       "avipsTranRowStatus": avipsTranRowStatus,
       "avipsMonitoringGroup": avipsMonitoringGroup,
       "avipsMonitoringTables": avipsMonitoringTables,
       "avipsMonitoringTablesGlobals": avipsMonitoringTablesGlobals,
       "avipsMonitorRstCntrs": avipsMonitorRstCntrs,
       "avipsMonitorRstCntrsLastChange": avipsMonitorRstCntrsLastChange,
       "avipsPeerTable": avipsPeerTable,
       "avipsPeerEntry": avipsPeerEntry,
       "avipsPeerLocalId": avipsPeerLocalId,
       "avipsPeerRemoteId": avipsPeerRemoteId,
       "avipsPeerLocalType": avipsPeerLocalType,
       "avipsPeerLocalValue": avipsPeerLocalValue,
       "avipsPeerRemoteType": avipsPeerRemoteType,
       "avipsPeerRemoteValue": avipsPeerRemoteValue,
       "avipsPeerRemoteDescription": avipsPeerRemoteDescription,
       "avipsPeerLocalAddress": avipsPeerLocalAddress,
       "avipsPeerRemoteAddress": avipsPeerRemoteAddress,
       "avipsPeerRemotePeerGrpActiveIndex": avipsPeerRemotePeerGrpActiveIndex,
       "avipsPeerRemotePeerGrpActiveIdType": avipsPeerRemotePeerGrpActiveIdType,
       "avipsPeerRemotePeerGrpActiveIdValue": avipsPeerRemotePeerGrpActiveIdValue,
       "avipsPeerIsakmpState": avipsPeerIsakmpState,
       "avipsPeerIsakmpStateLastChange": avipsPeerIsakmpStateLastChange,
       "avipsPeerTunnelsClosed": avipsPeerTunnelsClosed,
       "avipsPeerTunnelsInProgress": avipsPeerTunnelsInProgress,
       "avipsPeerTunnelsEstablished": avipsPeerTunnelsEstablished,
       "avipsPeerTunnelsFailed": avipsPeerTunnelsFailed,
       "avipsPeerInOctets": avipsPeerInOctets,
       "avipsPeerInOctetsWraps": avipsPeerInOctetsWraps,
       "avipsPeerInDecompOctets": avipsPeerInDecompOctets,
       "avipsPeerInDecompOctetsWraps": avipsPeerInDecompOctetsWraps,
       "avipsPeerInDecompRatio": avipsPeerInDecompRatio,
       "avipsPeerInPkts": avipsPeerInPkts,
       "avipsPeerInDropPkts": avipsPeerInDropPkts,
       "avipsPeerOutOctets": avipsPeerOutOctets,
       "avipsPeerOutOctetsWraps": avipsPeerOutOctetsWraps,
       "avipsPeerOutUncompOctets": avipsPeerOutUncompOctets,
       "avipsPeerOutUncompOctetsWraps": avipsPeerOutUncompOctetsWraps,
       "avipsPeerOutCompRatio": avipsPeerOutCompRatio,
       "avipsPeerOutPkts": avipsPeerOutPkts,
       "avipsPeerOutDropPkts": avipsPeerOutDropPkts,
       "avipsTunnelTable": avipsTunnelTable,
       "avipsTunnelEntry": avipsTunnelEntry,
       "avipsTunnelPeerLocalId": avipsTunnelPeerLocalId,
       "avipsTunnelPeerRemoteId": avipsTunnelPeerRemoteId,
       "avipsTunnelIndex": avipsTunnelIndex,
       "avipsTunnelSubIndex": avipsTunnelSubIndex,
       "avipsTunnelPeerLocalType": avipsTunnelPeerLocalType,
       "avipsTunnelPeerLocalValue": avipsTunnelPeerLocalValue,
       "avipsTunnelPeerRemoteType": avipsTunnelPeerRemoteType,
       "avipsTunnelPeerRemoteValue": avipsTunnelPeerRemoteValue,
       "avipsTunnelDescription": avipsTunnelDescription,
       "avipsTunnelLocalAddress": avipsTunnelLocalAddress,
       "avipsTunnelRemoteAddress": avipsTunnelRemoteAddress,
       "avipsTunnelProxyLocalSubnet": avipsTunnelProxyLocalSubnet,
       "avipsTunnelProxyLocalMask": avipsTunnelProxyLocalMask,
       "avipsTunnelProxyRemoteSubnet": avipsTunnelProxyRemoteSubnet,
       "avipsTunnelProxyRemoteMask": avipsTunnelProxyRemoteMask,
       "avipsTunnelState": avipsTunnelState,
       "avipsTunnelStateLastChange": avipsTunnelStateLastChange,
       "avipsTunnelLastCntrsReset": avipsTunnelLastCntrsReset,
       "avipsTunnelInOctets": avipsTunnelInOctets,
       "avipsTunnelInOctetsWraps": avipsTunnelInOctetsWraps,
       "avipsTunnelInDecompOctets": avipsTunnelInDecompOctets,
       "avipsTunnelInDecompOctetsWraps": avipsTunnelInDecompOctetsWraps,
       "avipsTunnelInDecompRatio": avipsTunnelInDecompRatio,
       "avipsTunnelInPkts": avipsTunnelInPkts,
       "avipsTunnelInDropTotalPkts": avipsTunnelInDropTotalPkts,
       "avipsTunnelInDropAntiReplayPkts": avipsTunnelInDropAntiReplayPkts,
       "avipsTunnelInDropHmacFailPkts": avipsTunnelInDropHmacFailPkts,
       "avipsTunnelInDropBadTrailerPkts": avipsTunnelInDropBadTrailerPkts,
       "avipsTunnelInDropInvalidIdPkts": avipsTunnelInDropInvalidIdPkts,
       "avipsTunnelInDropUnprotectPkts": avipsTunnelInDropUnprotectPkts,
       "avipsTunnelInDropInvalidLenPkts": avipsTunnelInDropInvalidLenPkts,
       "avipsTunnelInDropSaExpiredPkts": avipsTunnelInDropSaExpiredPkts,
       "avipsTunnelOutOctets": avipsTunnelOutOctets,
       "avipsTunnelOutOctetsWraps": avipsTunnelOutOctetsWraps,
       "avipsTunnelOutUncompOctets": avipsTunnelOutUncompOctets,
       "avipsTunnelOutUncompOctetsWraps": avipsTunnelOutUncompOctetsWraps,
       "avipsTunnelOutCompRatio": avipsTunnelOutCompRatio,
       "avipsTunnelOutPkts": avipsTunnelOutPkts,
       "avipsTunnelOutDropTotalPkts": avipsTunnelOutDropTotalPkts,
       "avipsTunnelOutDropNoSaPkts": avipsTunnelOutDropNoSaPkts,
       "avipsTunnelOutDropSeqRolPkts": avipsTunnelOutDropSeqRolPkts,
       "avipsTunnelOutDropSaExpiredPkts": avipsTunnelOutDropSaExpiredPkts,
       "avipsMIBNotificationPrefix": avipsMIBNotificationPrefix,
       "avipsMIBNotifications": avipsMIBNotifications,
       "avipsIskampEstablished": avipsIskampEstablished,
       "avipsIskampClosed": avipsIskampClosed,
       "avipsIskampFailed": avipsIskampFailed,
       "avipsIpsecTunnelEstablished": avipsIpsecTunnelEstablished,
       "avipsIpsecTunnelClosed": avipsIpsecTunnelClosed,
       "avipsIpsecTunnelFailed": avipsIpsecTunnelFailed,
       "avipsMIBConformance": avipsMIBConformance,
       "avipsMIBGroups": avipsMIBGroups,
       "avipsConfigurationGroup": avipsConfigurationGroup,
       "avipsMonitorGroup": avipsMonitorGroup,
       "avipsMIBCompliances": avipsMIBCompliances,
       "avipsMIBCompliance": avipsMIBCompliance}
)
