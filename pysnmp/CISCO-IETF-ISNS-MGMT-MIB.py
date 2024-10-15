# SNMP MIB module (CISCO-IETF-ISNS-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-ISNS-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:39 2024
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

(FcAddressId,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId",
    "FcNameIdOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

ciscoIetfIsnsMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116)
)
ciscoIetfIsnsMgmtMIB.setRevisions(
        ("2004-08-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIsnsDiscoveryDomainSetId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CIsnsDdsStatusId(Bits, TextualConvention):
    status = "current"


class CIsnsDiscoveryDomainId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CIsnsDdFeatureBitmapId(Bits, TextualConvention):
    status = "current"


class CIsnsDdDdsModificationBitmap(Bits, TextualConvention):
    status = "current"


class CIsnsEntityIndexId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CIsnsEntityProtocolId(Integer32, TextualConvention):
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
        *(("iFCP", 3),
          ("iSCSI", 2),
          ("noProtocol", 1))
    )



class CIsnsPortalGroupIndexId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CIsnsPortalIndexId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CIsnsPortalPortId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CIsnsPortalPortTypeId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )



class CIsnsPortalGroupTagIdOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CIsnsPortalSecurityBitmapId(Bits, TextualConvention):
    status = "current"


class CIsnsNodeIndexId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CIsnsNodeIndexIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CIsnsNodeTypeId(Bits, TextualConvention):
    status = "current"


class CIsnsCosBitmapId(Bits, TextualConvention):
    status = "current"


class CIsnsScnBitmapId(Bits, TextualConvention):
    status = "current"


class CIsnsSrvrDscvryMthdId(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CIsnsObj_ObjectIdentity = ObjectIdentity
cIsnsObj = _CIsnsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1)
)
_CIsnsSrvrInfo_ObjectIdentity = ObjectIdentity
cIsnsSrvrInfo = _CIsnsSrvrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1)
)
_CIsnsSrvrInstTable_Object = MibTable
cIsnsSrvrInstTable = _CIsnsSrvrInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cIsnsSrvrInstTable.setStatus("current")
_CIsnsSrvrInstEntry_Object = MibTableRow
cIsnsSrvrInstEntry = _CIsnsSrvrInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1)
)
cIsnsSrvrInstEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
)
if mibBuilder.loadTexts:
    cIsnsSrvrInstEntry.setStatus("current")


class _CIsnsSrvrInstIndex_Type(Unsigned32):
    """Custom type cIsnsSrvrInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIsnsSrvrInstIndex_Type.__name__ = "Unsigned32"
_CIsnsSrvrInstIndex_Object = MibTableColumn
cIsnsSrvrInstIndex = _CIsnsSrvrInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 1),
    _CIsnsSrvrInstIndex_Type()
)
cIsnsSrvrInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsSrvrInstIndex.setStatus("current")


class _CIsnsSrvrInstName_Type(SnmpAdminString):
    """Custom type cIsnsSrvrInstName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsSrvrInstName_Type.__name__ = "SnmpAdminString"
_CIsnsSrvrInstName_Object = MibTableColumn
cIsnsSrvrInstName = _CIsnsSrvrInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 2),
    _CIsnsSrvrInstName_Type()
)
cIsnsSrvrInstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstName.setStatus("current")


class _CIsnsSrvrInstIsnsVersion_Type(Integer32):
    """Custom type cIsnsSrvrInstIsnsVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsSrvrInstIsnsVersion_Type.__name__ = "Integer32"
_CIsnsSrvrInstIsnsVersion_Object = MibTableColumn
cIsnsSrvrInstIsnsVersion = _CIsnsSrvrInstIsnsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 3),
    _CIsnsSrvrInstIsnsVersion_Type()
)
cIsnsSrvrInstIsnsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsSrvrInstIsnsVersion.setStatus("current")


class _CIsnsSrvrInstDescription_Type(SnmpAdminString):
    """Custom type cIsnsSrvrInstDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsSrvrInstDescription_Type.__name__ = "SnmpAdminString"
_CIsnsSrvrInstDescription_Object = MibTableColumn
cIsnsSrvrInstDescription = _CIsnsSrvrInstDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 4),
    _CIsnsSrvrInstDescription_Type()
)
cIsnsSrvrInstDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsSrvrInstDescription.setStatus("current")
_CIsnsSrvrInstAddressType_Type = InetAddressType
_CIsnsSrvrInstAddressType_Object = MibTableColumn
cIsnsSrvrInstAddressType = _CIsnsSrvrInstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 5),
    _CIsnsSrvrInstAddressType_Type()
)
cIsnsSrvrInstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstAddressType.setStatus("current")
_CIsnsSrvrInstAddress_Type = InetAddress
_CIsnsSrvrInstAddress_Object = MibTableColumn
cIsnsSrvrInstAddress = _CIsnsSrvrInstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 6),
    _CIsnsSrvrInstAddress_Type()
)
cIsnsSrvrInstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstAddress.setStatus("current")


class _CIsnsSrvrInstTcpPort_Type(Integer32):
    """Custom type cIsnsSrvrInstTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsSrvrInstTcpPort_Type.__name__ = "Integer32"
_CIsnsSrvrInstTcpPort_Object = MibTableColumn
cIsnsSrvrInstTcpPort = _CIsnsSrvrInstTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 7),
    _CIsnsSrvrInstTcpPort_Type()
)
cIsnsSrvrInstTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstTcpPort.setStatus("current")


class _CIsnsSrvrInstUdpPort_Type(Integer32):
    """Custom type cIsnsSrvrInstUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsSrvrInstUdpPort_Type.__name__ = "Integer32"
_CIsnsSrvrInstUdpPort_Object = MibTableColumn
cIsnsSrvrInstUdpPort = _CIsnsSrvrInstUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 8),
    _CIsnsSrvrInstUdpPort_Type()
)
cIsnsSrvrInstUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstUdpPort.setStatus("current")
_CIsnsSrvrInstUptime_Type = TimeTicks
_CIsnsSrvrInstUptime_Object = MibTableColumn
cIsnsSrvrInstUptime = _CIsnsSrvrInstUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 9),
    _CIsnsSrvrInstUptime_Type()
)
cIsnsSrvrInstUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsSrvrInstUptime.setStatus("current")


class _CIsnsSrvrInstRole_Type(Integer32):
    """Custom type cIsnsSrvrInstRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("server", 1),
          ("serverNotPrimary", 2))
    )


_CIsnsSrvrInstRole_Type.__name__ = "Integer32"
_CIsnsSrvrInstRole_Object = MibTableColumn
cIsnsSrvrInstRole = _CIsnsSrvrInstRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 10),
    _CIsnsSrvrInstRole_Type()
)
cIsnsSrvrInstRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsSrvrInstRole.setStatus("current")
_CIsnsSrvrInstDiscMthdsEnbld_Type = CIsnsSrvrDscvryMthdId
_CIsnsSrvrInstDiscMthdsEnbld_Object = MibTableColumn
cIsnsSrvrInstDiscMthdsEnbld = _CIsnsSrvrInstDiscMthdsEnbld_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 11),
    _CIsnsSrvrInstDiscMthdsEnbld_Type()
)
cIsnsSrvrInstDiscMthdsEnbld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstDiscMthdsEnbld.setStatus("current")
_CIsnsSrvrInstDiscMcGrpType_Type = InetAddressType
_CIsnsSrvrInstDiscMcGrpType_Object = MibTableColumn
cIsnsSrvrInstDiscMcGrpType = _CIsnsSrvrInstDiscMcGrpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 12),
    _CIsnsSrvrInstDiscMcGrpType_Type()
)
cIsnsSrvrInstDiscMcGrpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstDiscMcGrpType.setStatus("current")
_CIsnsSrvrInstDiscMcGrp_Type = InetAddress
_CIsnsSrvrInstDiscMcGrp_Object = MibTableColumn
cIsnsSrvrInstDiscMcGrp = _CIsnsSrvrInstDiscMcGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 13),
    _CIsnsSrvrInstDiscMcGrp_Type()
)
cIsnsSrvrInstDiscMcGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstDiscMcGrp.setStatus("current")


class _CIsnsSrvrInstEsiNonRespThrshld_Type(Integer32):
    """Custom type cIsnsSrvrInstEsiNonRespThrshld based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsSrvrInstEsiNonRespThrshld_Type.__name__ = "Integer32"
_CIsnsSrvrInstEsiNonRespThrshld_Object = MibTableColumn
cIsnsSrvrInstEsiNonRespThrshld = _CIsnsSrvrInstEsiNonRespThrshld_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 14),
    _CIsnsSrvrInstEsiNonRespThrshld_Type()
)
cIsnsSrvrInstEsiNonRespThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstEsiNonRespThrshld.setStatus("current")


class _CIsnsSrvrInstCntrlNodeAuth_Type(Integer32):
    """Custom type cIsnsSrvrInstCntrlNodeAuth based on Integer32"""
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
        *(("anyNode", 1),
          ("modifyNodes", 3),
          ("noSnmpAccess", 4),
          ("viewNodes", 2))
    )


_CIsnsSrvrInstCntrlNodeAuth_Type.__name__ = "Integer32"
_CIsnsSrvrInstCntrlNodeAuth_Object = MibTableColumn
cIsnsSrvrInstCntrlNodeAuth = _CIsnsSrvrInstCntrlNodeAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 15),
    _CIsnsSrvrInstCntrlNodeAuth_Type()
)
cIsnsSrvrInstCntrlNodeAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsSrvrInstCntrlNodeAuth.setStatus("current")


class _CIsnsSrvrInstEnblCntrlNdeMgtScn_Type(TruthValue):
    """Custom type cIsnsSrvrInstEnblCntrlNdeMgtScn based on TruthValue"""


_CIsnsSrvrInstEnblCntrlNdeMgtScn_Object = MibTableColumn
cIsnsSrvrInstEnblCntrlNdeMgtScn = _CIsnsSrvrInstEnblCntrlNdeMgtScn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 16),
    _CIsnsSrvrInstEnblCntrlNdeMgtScn_Type()
)
cIsnsSrvrInstEnblCntrlNdeMgtScn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstEnblCntrlNdeMgtScn.setStatus("current")


class _CIsnsSrvrInstDfltDdDdsStatus_Type(Integer32):
    """Custom type cIsnsSrvrInstDfltDdDdsStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inDefaultDdAndDds", 2),
          ("inNoDomain", 1))
    )


_CIsnsSrvrInstDfltDdDdsStatus_Type.__name__ = "Integer32"
_CIsnsSrvrInstDfltDdDdsStatus_Object = MibTableColumn
cIsnsSrvrInstDfltDdDdsStatus = _CIsnsSrvrInstDfltDdDdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 17),
    _CIsnsSrvrInstDfltDdDdsStatus_Type()
)
cIsnsSrvrInstDfltDdDdsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstDfltDdDdsStatus.setStatus("current")
_CIsnsSrvrInstUpdateDdDdsSpprtd_Type = CIsnsDdDdsModificationBitmap
_CIsnsSrvrInstUpdateDdDdsSpprtd_Object = MibTableColumn
cIsnsSrvrInstUpdateDdDdsSpprtd = _CIsnsSrvrInstUpdateDdDdsSpprtd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 18),
    _CIsnsSrvrInstUpdateDdDdsSpprtd_Type()
)
cIsnsSrvrInstUpdateDdDdsSpprtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsSrvrInstUpdateDdDdsSpprtd.setStatus("current")
_CIsnsSrvrInstUpdateDdDdsEnbld_Type = CIsnsDdDdsModificationBitmap
_CIsnsSrvrInstUpdateDdDdsEnbld_Object = MibTableColumn
cIsnsSrvrInstUpdateDdDdsEnbld = _CIsnsSrvrInstUpdateDdDdsEnbld_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 1, 1, 19),
    _CIsnsSrvrInstUpdateDdDdsEnbld_Type()
)
cIsnsSrvrInstUpdateDdDdsEnbld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsSrvrInstUpdateDdDdsEnbld.setStatus("current")
_CIsnsNumObjTable_Object = MibTable
cIsnsNumObjTable = _CIsnsNumObjTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cIsnsNumObjTable.setStatus("current")
_CIsnsNumObjEntry_Object = MibTableRow
cIsnsNumObjEntry = _CIsnsNumObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIsnsNumObjEntry.setStatus("current")


class _CIsnsNumDds_Type(Unsigned32):
    """Custom type cIsnsNumDds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumDds_Type.__name__ = "Unsigned32"
_CIsnsNumDds_Object = MibTableColumn
cIsnsNumDds = _CIsnsNumDds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 1),
    _CIsnsNumDds_Type()
)
cIsnsNumDds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumDds.setStatus("current")


class _CIsnsNumDd_Type(Unsigned32):
    """Custom type cIsnsNumDd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumDd_Type.__name__ = "Unsigned32"
_CIsnsNumDd_Object = MibTableColumn
cIsnsNumDd = _CIsnsNumDd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 2),
    _CIsnsNumDd_Type()
)
cIsnsNumDd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumDd.setStatus("current")


class _CIsnsNumEntities_Type(Unsigned32):
    """Custom type cIsnsNumEntities based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumEntities_Type.__name__ = "Unsigned32"
_CIsnsNumEntities_Object = MibTableColumn
cIsnsNumEntities = _CIsnsNumEntities_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 3),
    _CIsnsNumEntities_Type()
)
cIsnsNumEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumEntities.setStatus("current")


class _CIsnsNumPortals_Type(Unsigned32):
    """Custom type cIsnsNumPortals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumPortals_Type.__name__ = "Unsigned32"
_CIsnsNumPortals_Object = MibTableColumn
cIsnsNumPortals = _CIsnsNumPortals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 4),
    _CIsnsNumPortals_Type()
)
cIsnsNumPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumPortals.setStatus("current")


class _CIsnsNumPortalGroups_Type(Unsigned32):
    """Custom type cIsnsNumPortalGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumPortalGroups_Type.__name__ = "Unsigned32"
_CIsnsNumPortalGroups_Object = MibTableColumn
cIsnsNumPortalGroups = _CIsnsNumPortalGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 5),
    _CIsnsNumPortalGroups_Type()
)
cIsnsNumPortalGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumPortalGroups.setStatus("current")


class _CIsnsNumIscsiNodes_Type(Unsigned32):
    """Custom type cIsnsNumIscsiNodes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumIscsiNodes_Type.__name__ = "Unsigned32"
_CIsnsNumIscsiNodes_Object = MibTableColumn
cIsnsNumIscsiNodes = _CIsnsNumIscsiNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 6),
    _CIsnsNumIscsiNodes_Type()
)
cIsnsNumIscsiNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumIscsiNodes.setStatus("current")


class _CIsnsNumFcPorts_Type(Unsigned32):
    """Custom type cIsnsNumFcPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumFcPorts_Type.__name__ = "Unsigned32"
_CIsnsNumFcPorts_Object = MibTableColumn
cIsnsNumFcPorts = _CIsnsNumFcPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 7),
    _CIsnsNumFcPorts_Type()
)
cIsnsNumFcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumFcPorts.setStatus("current")


class _CIsnsNumFcNodes_Type(Unsigned32):
    """Custom type cIsnsNumFcNodes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsNumFcNodes_Type.__name__ = "Unsigned32"
_CIsnsNumFcNodes_Object = MibTableColumn
cIsnsNumFcNodes = _CIsnsNumFcNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 2, 1, 8),
    _CIsnsNumFcNodes_Type()
)
cIsnsNumFcNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNumFcNodes.setStatus("current")
_CIsnsNextIdxTable_Object = MibTable
cIsnsNextIdxTable = _CIsnsNextIdxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cIsnsNextIdxTable.setStatus("current")
_CIsnsNextIdxEntry_Object = MibTableRow
cIsnsNextIdxEntry = _CIsnsNextIdxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cIsnsNextIdxEntry.setStatus("current")
_CIsnsNextIdxDds_Type = CIsnsDiscoveryDomainSetId
_CIsnsNextIdxDds_Object = MibTableColumn
cIsnsNextIdxDds = _CIsnsNextIdxDds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 3, 1, 1),
    _CIsnsNextIdxDds_Type()
)
cIsnsNextIdxDds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNextIdxDds.setStatus("current")
_CIsnsNextIdxDd_Type = CIsnsDiscoveryDomainId
_CIsnsNextIdxDd_Object = MibTableColumn
cIsnsNextIdxDd = _CIsnsNextIdxDd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 3, 1, 2),
    _CIsnsNextIdxDd_Type()
)
cIsnsNextIdxDd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNextIdxDd.setStatus("current")
_CIsnsNextIdxUnregIscsiNodeInDd_Type = CIsnsNodeIndexIdOrZero
_CIsnsNextIdxUnregIscsiNodeInDd_Object = MibTableColumn
cIsnsNextIdxUnregIscsiNodeInDd = _CIsnsNextIdxUnregIscsiNodeInDd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 3, 1, 3),
    _CIsnsNextIdxUnregIscsiNodeInDd_Type()
)
cIsnsNextIdxUnregIscsiNodeInDd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNextIdxUnregIscsiNodeInDd.setStatus("current")
_CIsnsNextIdxUnregPortalInDd_Type = CIsnsPortalIndexId
_CIsnsNextIdxUnregPortalInDd_Object = MibTableColumn
cIsnsNextIdxUnregPortalInDd = _CIsnsNextIdxUnregPortalInDd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 3, 1, 4),
    _CIsnsNextIdxUnregPortalInDd_Type()
)
cIsnsNextIdxUnregPortalInDd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsNextIdxUnregPortalInDd.setStatus("current")
_CIsnsCntlNodeInfo_ObjectIdentity = ObjectIdentity
cIsnsCntlNodeInfo = _CIsnsCntlNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4)
)
_CIsnsCntlNodeIscsiTable_Object = MibTable
cIsnsCntlNodeIscsiTable = _CIsnsCntlNodeIscsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cIsnsCntlNodeIscsiTable.setStatus("current")
_CIsnsCntlNodeIscsiEntry_Object = MibTableRow
cIsnsCntlNodeIscsiEntry = _CIsnsCntlNodeIscsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 1, 1)
)
cIsnsCntlNodeIscsiEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsCntlNodeIscsiNodeIdx"),
)
if mibBuilder.loadTexts:
    cIsnsCntlNodeIscsiEntry.setStatus("current")
_CIsnsCntlNodeIscsiNodeIdx_Type = CIsnsNodeIndexId
_CIsnsCntlNodeIscsiNodeIdx_Object = MibTableColumn
cIsnsCntlNodeIscsiNodeIdx = _CIsnsCntlNodeIscsiNodeIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 1, 1, 1),
    _CIsnsCntlNodeIscsiNodeIdx_Type()
)
cIsnsCntlNodeIscsiNodeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsCntlNodeIscsiNodeIdx.setStatus("current")


class _CIsnsCntlNodeIscsiNodeName_Type(SnmpAdminString):
    """Custom type cIsnsCntlNodeIscsiNodeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_CIsnsCntlNodeIscsiNodeName_Type.__name__ = "SnmpAdminString"
_CIsnsCntlNodeIscsiNodeName_Object = MibTableColumn
cIsnsCntlNodeIscsiNodeName = _CIsnsCntlNodeIscsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 1, 1, 2),
    _CIsnsCntlNodeIscsiNodeName_Type()
)
cIsnsCntlNodeIscsiNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsCntlNodeIscsiNodeName.setStatus("current")
_CIsnsCntlNodeIscsiRowStatus_Type = RowStatus
_CIsnsCntlNodeIscsiRowStatus_Object = MibTableColumn
cIsnsCntlNodeIscsiRowStatus = _CIsnsCntlNodeIscsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 1, 1, 3),
    _CIsnsCntlNodeIscsiRowStatus_Type()
)
cIsnsCntlNodeIscsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsCntlNodeIscsiRowStatus.setStatus("current")
_CIsnsCntlNodeFcPortTable_Object = MibTable
cIsnsCntlNodeFcPortTable = _CIsnsCntlNodeFcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cIsnsCntlNodeFcPortTable.setStatus("current")
_CIsnsCntlNodeFcPortEntry_Object = MibTableRow
cIsnsCntlNodeFcPortEntry = _CIsnsCntlNodeFcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 2, 1)
)
cIsnsCntlNodeFcPortEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsCntlNodeFcPortName"),
)
if mibBuilder.loadTexts:
    cIsnsCntlNodeFcPortEntry.setStatus("current")
_CIsnsCntlNodeFcPortName_Type = FcNameIdOrZero
_CIsnsCntlNodeFcPortName_Object = MibTableColumn
cIsnsCntlNodeFcPortName = _CIsnsCntlNodeFcPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 2, 1, 1),
    _CIsnsCntlNodeFcPortName_Type()
)
cIsnsCntlNodeFcPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsCntlNodeFcPortName.setStatus("current")
_CIsnsCntlNodeFcPortRowStatus_Type = RowStatus
_CIsnsCntlNodeFcPortRowStatus_Object = MibTableColumn
cIsnsCntlNodeFcPortRowStatus = _CIsnsCntlNodeFcPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 4, 2, 1, 2),
    _CIsnsCntlNodeFcPortRowStatus_Type()
)
cIsnsCntlNodeFcPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsCntlNodeFcPortRowStatus.setStatus("current")
_CIsnsDdsInfo_ObjectIdentity = ObjectIdentity
cIsnsDdsInfo = _CIsnsDdsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5)
)
_CIsnsDdsTable_Object = MibTable
cIsnsDdsTable = _CIsnsDdsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cIsnsDdsTable.setStatus("current")
_CIsnsDdsEntry_Object = MibTableRow
cIsnsDdsEntry = _CIsnsDdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 1, 1)
)
cIsnsDdsEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsId"),
)
if mibBuilder.loadTexts:
    cIsnsDdsEntry.setStatus("current")
_CIsnsDdsId_Type = CIsnsDiscoveryDomainSetId
_CIsnsDdsId_Object = MibTableColumn
cIsnsDdsId = _CIsnsDdsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 1, 1, 1),
    _CIsnsDdsId_Type()
)
cIsnsDdsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsDdsId.setStatus("current")


class _CIsnsDdsSymbolicName_Type(SnmpAdminString):
    """Custom type cIsnsDdsSymbolicName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsDdsSymbolicName_Type.__name__ = "SnmpAdminString"
_CIsnsDdsSymbolicName_Object = MibTableColumn
cIsnsDdsSymbolicName = _CIsnsDdsSymbolicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 1, 1, 2),
    _CIsnsDdsSymbolicName_Type()
)
cIsnsDdsSymbolicName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdsSymbolicName.setStatus("current")


class _CIsnsDdsStatus_Type(CIsnsDdsStatusId):
    """Custom type cIsnsDdsStatus based on CIsnsDdsStatusId"""
    defaultBinValue = "1"


_CIsnsDdsStatus_Object = MibTableColumn
cIsnsDdsStatus = _CIsnsDdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 1, 1, 3),
    _CIsnsDdsStatus_Type()
)
cIsnsDdsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdsStatus.setStatus("current")
_CIsnsDdsRowStatus_Type = RowStatus
_CIsnsDdsRowStatus_Object = MibTableColumn
cIsnsDdsRowStatus = _CIsnsDdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 1, 1, 4),
    _CIsnsDdsRowStatus_Type()
)
cIsnsDdsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdsRowStatus.setStatus("current")
_CIsnsDdsMemberTable_Object = MibTable
cIsnsDdsMemberTable = _CIsnsDdsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cIsnsDdsMemberTable.setStatus("current")
_CIsnsDdsMemberEntry_Object = MibTableRow
cIsnsDdsMemberEntry = _CIsnsDdsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 2, 1)
)
cIsnsDdsMemberEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsId"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdId"),
)
if mibBuilder.loadTexts:
    cIsnsDdsMemberEntry.setStatus("current")
_CIsnsDdsMemberRowStatus_Type = RowStatus
_CIsnsDdsMemberRowStatus_Object = MibTableColumn
cIsnsDdsMemberRowStatus = _CIsnsDdsMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 5, 2, 1, 1),
    _CIsnsDdsMemberRowStatus_Type()
)
cIsnsDdsMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdsMemberRowStatus.setStatus("current")
_CIsnsDdInfo_ObjectIdentity = ObjectIdentity
cIsnsDdInfo = _CIsnsDdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6)
)
_CIsnsDdTable_Object = MibTable
cIsnsDdTable = _CIsnsDdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cIsnsDdTable.setStatus("current")
_CIsnsDdEntry_Object = MibTableRow
cIsnsDdEntry = _CIsnsDdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 1, 1)
)
cIsnsDdEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdId"),
)
if mibBuilder.loadTexts:
    cIsnsDdEntry.setStatus("current")
_CIsnsDdId_Type = CIsnsDiscoveryDomainId
_CIsnsDdId_Object = MibTableColumn
cIsnsDdId = _CIsnsDdId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 1, 1, 1),
    _CIsnsDdId_Type()
)
cIsnsDdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsDdId.setStatus("current")


class _CIsnsDdSymbolicName_Type(SnmpAdminString):
    """Custom type cIsnsDdSymbolicName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsDdSymbolicName_Type.__name__ = "SnmpAdminString"
_CIsnsDdSymbolicName_Object = MibTableColumn
cIsnsDdSymbolicName = _CIsnsDdSymbolicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 1, 1, 2),
    _CIsnsDdSymbolicName_Type()
)
cIsnsDdSymbolicName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdSymbolicName.setStatus("current")
_CIsnsDdFeatures_Type = CIsnsDdFeatureBitmapId
_CIsnsDdFeatures_Object = MibTableColumn
cIsnsDdFeatures = _CIsnsDdFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 1, 1, 3),
    _CIsnsDdFeatures_Type()
)
cIsnsDdFeatures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdFeatures.setStatus("current")
_CIsnsDdRowStatus_Type = RowStatus
_CIsnsDdRowStatus_Object = MibTableColumn
cIsnsDdRowStatus = _CIsnsDdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 1, 1, 4),
    _CIsnsDdRowStatus_Type()
)
cIsnsDdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdRowStatus.setStatus("current")
_CIsnsDdIscsiMemberTable_Object = MibTable
cIsnsDdIscsiMemberTable = _CIsnsDdIscsiMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cIsnsDdIscsiMemberTable.setStatus("current")
_CIsnsDdIscsiMemberEntry_Object = MibTableRow
cIsnsDdIscsiMemberEntry = _CIsnsDdIscsiMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 2, 1)
)
cIsnsDdIscsiMemberEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdId"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberIscsiIdx"),
)
if mibBuilder.loadTexts:
    cIsnsDdIscsiMemberEntry.setStatus("current")
_CIsnsDdMemberIscsiIdx_Type = CIsnsNodeIndexId
_CIsnsDdMemberIscsiIdx_Object = MibTableColumn
cIsnsDdMemberIscsiIdx = _CIsnsDdMemberIscsiIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 2, 1, 1),
    _CIsnsDdMemberIscsiIdx_Type()
)
cIsnsDdMemberIscsiIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsDdMemberIscsiIdx.setStatus("current")


class _CIsnsDdMemberIscsiName_Type(SnmpAdminString):
    """Custom type cIsnsDdMemberIscsiName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_CIsnsDdMemberIscsiName_Type.__name__ = "SnmpAdminString"
_CIsnsDdMemberIscsiName_Object = MibTableColumn
cIsnsDdMemberIscsiName = _CIsnsDdMemberIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 2, 1, 2),
    _CIsnsDdMemberIscsiName_Type()
)
cIsnsDdMemberIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberIscsiName.setStatus("current")
_CIsnsDdMemberIsRegistered_Type = TruthValue
_CIsnsDdMemberIsRegistered_Object = MibTableColumn
cIsnsDdMemberIsRegistered = _CIsnsDdMemberIsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 2, 1, 3),
    _CIsnsDdMemberIsRegistered_Type()
)
cIsnsDdMemberIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsDdMemberIsRegistered.setStatus("current")
_CIsnsDdMemberRowStatus_Type = RowStatus
_CIsnsDdMemberRowStatus_Object = MibTableColumn
cIsnsDdMemberRowStatus = _CIsnsDdMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 2, 1, 4),
    _CIsnsDdMemberRowStatus_Type()
)
cIsnsDdMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberRowStatus.setStatus("current")
_CIsnsDdPortalMemberTable_Object = MibTable
cIsnsDdPortalMemberTable = _CIsnsDdPortalMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cIsnsDdPortalMemberTable.setStatus("current")
_CIsnsDdPortalMemberEntry_Object = MibTableRow
cIsnsDdPortalMemberEntry = _CIsnsDdPortalMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1)
)
cIsnsDdPortalMemberEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdId"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalIdx"),
)
if mibBuilder.loadTexts:
    cIsnsDdPortalMemberEntry.setStatus("current")
_CIsnsDdMemberPortalIdx_Type = CIsnsPortalIndexId
_CIsnsDdMemberPortalIdx_Object = MibTableColumn
cIsnsDdMemberPortalIdx = _CIsnsDdMemberPortalIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 1),
    _CIsnsDdMemberPortalIdx_Type()
)
cIsnsDdMemberPortalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalIdx.setStatus("current")
_CIsnsDdMemberPortalAddrType_Type = InetAddressType
_CIsnsDdMemberPortalAddrType_Object = MibTableColumn
cIsnsDdMemberPortalAddrType = _CIsnsDdMemberPortalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 2),
    _CIsnsDdMemberPortalAddrType_Type()
)
cIsnsDdMemberPortalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalAddrType.setStatus("current")
_CIsnsDdMemberPortalAddr_Type = InetAddress
_CIsnsDdMemberPortalAddr_Object = MibTableColumn
cIsnsDdMemberPortalAddr = _CIsnsDdMemberPortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 3),
    _CIsnsDdMemberPortalAddr_Type()
)
cIsnsDdMemberPortalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalAddr.setStatus("current")
_CIsnsDdMemberPortalPortType_Type = CIsnsPortalPortTypeId
_CIsnsDdMemberPortalPortType_Object = MibTableColumn
cIsnsDdMemberPortalPortType = _CIsnsDdMemberPortalPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 4),
    _CIsnsDdMemberPortalPortType_Type()
)
cIsnsDdMemberPortalPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalPortType.setStatus("current")
_CIsnsDdMemberPortalPort_Type = CIsnsPortalPortId
_CIsnsDdMemberPortalPort_Object = MibTableColumn
cIsnsDdMemberPortalPort = _CIsnsDdMemberPortalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 5),
    _CIsnsDdMemberPortalPort_Type()
)
cIsnsDdMemberPortalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalPort.setStatus("current")
_CIsnsDdMemberPortalIsRegistered_Type = TruthValue
_CIsnsDdMemberPortalIsRegistered_Object = MibTableColumn
cIsnsDdMemberPortalIsRegistered = _CIsnsDdMemberPortalIsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 6),
    _CIsnsDdMemberPortalIsRegistered_Type()
)
cIsnsDdMemberPortalIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalIsRegistered.setStatus("current")
_CIsnsDdMemberPortalRowStatus_Type = RowStatus
_CIsnsDdMemberPortalRowStatus_Object = MibTableColumn
cIsnsDdMemberPortalRowStatus = _CIsnsDdMemberPortalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 3, 1, 7),
    _CIsnsDdMemberPortalRowStatus_Type()
)
cIsnsDdMemberPortalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberPortalRowStatus.setStatus("current")
_CIsnsDdFcPortMemberTable_Object = MibTable
cIsnsDdFcPortMemberTable = _CIsnsDdFcPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cIsnsDdFcPortMemberTable.setStatus("current")
_CIsnsDdFcPortMemberEntry_Object = MibTableRow
cIsnsDdFcPortMemberEntry = _CIsnsDdFcPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 4, 1)
)
cIsnsDdFcPortMemberEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdId"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberFcPortName"),
)
if mibBuilder.loadTexts:
    cIsnsDdFcPortMemberEntry.setStatus("current")
_CIsnsDdMemberFcPortName_Type = FcNameIdOrZero
_CIsnsDdMemberFcPortName_Object = MibTableColumn
cIsnsDdMemberFcPortName = _CIsnsDdMemberFcPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 4, 1, 1),
    _CIsnsDdMemberFcPortName_Type()
)
cIsnsDdMemberFcPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsDdMemberFcPortName.setStatus("current")
_CIsnsDdMemberFcIsRegistered_Type = TruthValue
_CIsnsDdMemberFcIsRegistered_Object = MibTableColumn
cIsnsDdMemberFcIsRegistered = _CIsnsDdMemberFcIsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 4, 1, 2),
    _CIsnsDdMemberFcIsRegistered_Type()
)
cIsnsDdMemberFcIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsDdMemberFcIsRegistered.setStatus("current")
_CIsnsDdMemberFcRowStatus_Type = RowStatus
_CIsnsDdMemberFcRowStatus_Object = MibTableColumn
cIsnsDdMemberFcRowStatus = _CIsnsDdMemberFcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 6, 4, 1, 3),
    _CIsnsDdMemberFcRowStatus_Type()
)
cIsnsDdMemberFcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsDdMemberFcRowStatus.setStatus("current")
_CIsnsReg_ObjectIdentity = ObjectIdentity
cIsnsReg = _CIsnsReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7)
)
_CIsnsRegEntityInfo_ObjectIdentity = ObjectIdentity
cIsnsRegEntityInfo = _CIsnsRegEntityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1)
)
_CIsnsRegEntityTable_Object = MibTable
cIsnsRegEntityTable = _CIsnsRegEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegEntityTable.setStatus("current")
_CIsnsRegEntityEntry_Object = MibTableRow
cIsnsRegEntityEntry = _CIsnsRegEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1)
)
cIsnsRegEntityEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityIdx"),
)
if mibBuilder.loadTexts:
    cIsnsRegEntityEntry.setStatus("current")
_CIsnsRegEntityIdx_Type = CIsnsEntityIndexId
_CIsnsRegEntityIdx_Object = MibTableColumn
cIsnsRegEntityIdx = _CIsnsRegEntityIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 1),
    _CIsnsRegEntityIdx_Type()
)
cIsnsRegEntityIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsRegEntityIdx.setStatus("current")


class _CIsnsRegEntityEID_Type(SnmpAdminString):
    """Custom type cIsnsRegEntityEID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegEntityEID_Type.__name__ = "SnmpAdminString"
_CIsnsRegEntityEID_Object = MibTableColumn
cIsnsRegEntityEID = _CIsnsRegEntityEID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 2),
    _CIsnsRegEntityEID_Type()
)
cIsnsRegEntityEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityEID.setStatus("current")
_CIsnsRegEntityProtocol_Type = CIsnsEntityProtocolId
_CIsnsRegEntityProtocol_Object = MibTableColumn
cIsnsRegEntityProtocol = _CIsnsRegEntityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 3),
    _CIsnsRegEntityProtocol_Type()
)
cIsnsRegEntityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityProtocol.setStatus("current")
_CIsnsRegEntityMgtAddrType_Type = InetAddressType
_CIsnsRegEntityMgtAddrType_Object = MibTableColumn
cIsnsRegEntityMgtAddrType = _CIsnsRegEntityMgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 4),
    _CIsnsRegEntityMgtAddrType_Type()
)
cIsnsRegEntityMgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityMgtAddrType.setStatus("current")
_CIsnsRegEntityMgtAddr_Type = InetAddress
_CIsnsRegEntityMgtAddr_Object = MibTableColumn
cIsnsRegEntityMgtAddr = _CIsnsRegEntityMgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 5),
    _CIsnsRegEntityMgtAddr_Type()
)
cIsnsRegEntityMgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityMgtAddr.setStatus("current")
_CIsnsRegEntityTimestamp_Type = DateAndTime
_CIsnsRegEntityTimestamp_Object = MibTableColumn
cIsnsRegEntityTimestamp = _CIsnsRegEntityTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 6),
    _CIsnsRegEntityTimestamp_Type()
)
cIsnsRegEntityTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityTimestamp.setStatus("current")


class _CIsnsRegEntityVersionMin_Type(Integer32):
    """Custom type cIsnsRegEntityVersionMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsRegEntityVersionMin_Type.__name__ = "Integer32"
_CIsnsRegEntityVersionMin_Object = MibTableColumn
cIsnsRegEntityVersionMin = _CIsnsRegEntityVersionMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 7),
    _CIsnsRegEntityVersionMin_Type()
)
cIsnsRegEntityVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityVersionMin.setStatus("current")


class _CIsnsRegEntityVersionMax_Type(Integer32):
    """Custom type cIsnsRegEntityVersionMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsRegEntityVersionMax_Type.__name__ = "Integer32"
_CIsnsRegEntityVersionMax_Object = MibTableColumn
cIsnsRegEntityVersionMax = _CIsnsRegEntityVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 8),
    _CIsnsRegEntityVersionMax_Type()
)
cIsnsRegEntityVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityVersionMax.setStatus("current")


class _CIsnsRegEntityRegPeriod_Type(Unsigned32):
    """Custom type cIsnsRegEntityRegPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegEntityRegPeriod_Type.__name__ = "Unsigned32"
_CIsnsRegEntityRegPeriod_Object = MibTableColumn
cIsnsRegEntityRegPeriod = _CIsnsRegEntityRegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 1, 1, 9),
    _CIsnsRegEntityRegPeriod_Type()
)
cIsnsRegEntityRegPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityRegPeriod.setStatus("current")
_CIsnsRegEntityNumObjTable_Object = MibTable
cIsnsRegEntityNumObjTable = _CIsnsRegEntityNumObjTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    cIsnsRegEntityNumObjTable.setStatus("current")
_CIsnsRegEntityNumObjEntry_Object = MibTableRow
cIsnsRegEntityNumObjEntry = _CIsnsRegEntityNumObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegEntityNumObjEntry.setStatus("current")


class _CIsnsRegEntityInfoNumPortals_Type(Unsigned32):
    """Custom type cIsnsRegEntityInfoNumPortals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegEntityInfoNumPortals_Type.__name__ = "Unsigned32"
_CIsnsRegEntityInfoNumPortals_Object = MibTableColumn
cIsnsRegEntityInfoNumPortals = _CIsnsRegEntityInfoNumPortals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2, 1, 1),
    _CIsnsRegEntityInfoNumPortals_Type()
)
cIsnsRegEntityInfoNumPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityInfoNumPortals.setStatus("current")


class _CIsnsRegEntityInfoNumPortalGroup_Type(Unsigned32):
    """Custom type cIsnsRegEntityInfoNumPortalGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegEntityInfoNumPortalGroup_Type.__name__ = "Unsigned32"
_CIsnsRegEntityInfoNumPortalGroup_Object = MibTableColumn
cIsnsRegEntityInfoNumPortalGroup = _CIsnsRegEntityInfoNumPortalGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2, 1, 2),
    _CIsnsRegEntityInfoNumPortalGroup_Type()
)
cIsnsRegEntityInfoNumPortalGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityInfoNumPortalGroup.setStatus("current")


class _CIsnsRegEntityInfoNumIscsiNodes_Type(Unsigned32):
    """Custom type cIsnsRegEntityInfoNumIscsiNodes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegEntityInfoNumIscsiNodes_Type.__name__ = "Unsigned32"
_CIsnsRegEntityInfoNumIscsiNodes_Object = MibTableColumn
cIsnsRegEntityInfoNumIscsiNodes = _CIsnsRegEntityInfoNumIscsiNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2, 1, 3),
    _CIsnsRegEntityInfoNumIscsiNodes_Type()
)
cIsnsRegEntityInfoNumIscsiNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityInfoNumIscsiNodes.setStatus("current")


class _CIsnsRegEntityInfoNumFcPorts_Type(Unsigned32):
    """Custom type cIsnsRegEntityInfoNumFcPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegEntityInfoNumFcPorts_Type.__name__ = "Unsigned32"
_CIsnsRegEntityInfoNumFcPorts_Object = MibTableColumn
cIsnsRegEntityInfoNumFcPorts = _CIsnsRegEntityInfoNumFcPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2, 1, 4),
    _CIsnsRegEntityInfoNumFcPorts_Type()
)
cIsnsRegEntityInfoNumFcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityInfoNumFcPorts.setStatus("current")


class _CIsnsRegEntityInfoNumFcNodes_Type(Unsigned32):
    """Custom type cIsnsRegEntityInfoNumFcNodes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegEntityInfoNumFcNodes_Type.__name__ = "Unsigned32"
_CIsnsRegEntityInfoNumFcNodes_Object = MibTableColumn
cIsnsRegEntityInfoNumFcNodes = _CIsnsRegEntityInfoNumFcNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 1, 2, 1, 5),
    _CIsnsRegEntityInfoNumFcNodes_Type()
)
cIsnsRegEntityInfoNumFcNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegEntityInfoNumFcNodes.setStatus("current")
_CIsnsRegPortalInfo_ObjectIdentity = ObjectIdentity
cIsnsRegPortalInfo = _CIsnsRegPortalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2)
)
_CIsnsRegPortalTable_Object = MibTable
cIsnsRegPortalTable = _CIsnsRegPortalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegPortalTable.setStatus("current")
_CIsnsRegPortalEntry_Object = MibTableRow
cIsnsRegPortalEntry = _CIsnsRegPortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1)
)
cIsnsRegPortalEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityIdx"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalPrtlIdx"),
)
if mibBuilder.loadTexts:
    cIsnsRegPortalEntry.setStatus("current")
_CIsnsRegPortalPrtlIdx_Type = CIsnsPortalIndexId
_CIsnsRegPortalPrtlIdx_Object = MibTableColumn
cIsnsRegPortalPrtlIdx = _CIsnsRegPortalPrtlIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 1),
    _CIsnsRegPortalPrtlIdx_Type()
)
cIsnsRegPortalPrtlIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsRegPortalPrtlIdx.setStatus("current")
_CIsnsRegPortalAddrType_Type = InetAddressType
_CIsnsRegPortalAddrType_Object = MibTableColumn
cIsnsRegPortalAddrType = _CIsnsRegPortalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 2),
    _CIsnsRegPortalAddrType_Type()
)
cIsnsRegPortalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalAddrType.setStatus("current")
_CIsnsRegPortalAddr_Type = InetAddress
_CIsnsRegPortalAddr_Object = MibTableColumn
cIsnsRegPortalAddr = _CIsnsRegPortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 3),
    _CIsnsRegPortalAddr_Type()
)
cIsnsRegPortalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalAddr.setStatus("current")
_CIsnsRegPortalPortType_Type = CIsnsPortalPortTypeId
_CIsnsRegPortalPortType_Object = MibTableColumn
cIsnsRegPortalPortType = _CIsnsRegPortalPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 4),
    _CIsnsRegPortalPortType_Type()
)
cIsnsRegPortalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalPortType.setStatus("current")
_CIsnsRegPortalPort_Type = CIsnsPortalPortId
_CIsnsRegPortalPort_Object = MibTableColumn
cIsnsRegPortalPort = _CIsnsRegPortalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 5),
    _CIsnsRegPortalPort_Type()
)
cIsnsRegPortalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalPort.setStatus("current")


class _CIsnsRegPortalSymName_Type(SnmpAdminString):
    """Custom type cIsnsRegPortalSymName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegPortalSymName_Type.__name__ = "SnmpAdminString"
_CIsnsRegPortalSymName_Object = MibTableColumn
cIsnsRegPortalSymName = _CIsnsRegPortalSymName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 6),
    _CIsnsRegPortalSymName_Type()
)
cIsnsRegPortalSymName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalSymName.setStatus("current")


class _CIsnsRegPortalEsiInterval_Type(Unsigned32):
    """Custom type cIsnsRegPortalEsiInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegPortalEsiInterval_Type.__name__ = "Unsigned32"
_CIsnsRegPortalEsiInterval_Object = MibTableColumn
cIsnsRegPortalEsiInterval = _CIsnsRegPortalEsiInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 7),
    _CIsnsRegPortalEsiInterval_Type()
)
cIsnsRegPortalEsiInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalEsiInterval.setStatus("current")
_CIsnsRegPortalEsiPortType_Type = CIsnsPortalPortTypeId
_CIsnsRegPortalEsiPortType_Object = MibTableColumn
cIsnsRegPortalEsiPortType = _CIsnsRegPortalEsiPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 8),
    _CIsnsRegPortalEsiPortType_Type()
)
cIsnsRegPortalEsiPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalEsiPortType.setStatus("current")
_CIsnsRegPortalEsiPort_Type = CIsnsPortalPortId
_CIsnsRegPortalEsiPort_Object = MibTableColumn
cIsnsRegPortalEsiPort = _CIsnsRegPortalEsiPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 9),
    _CIsnsRegPortalEsiPort_Type()
)
cIsnsRegPortalEsiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalEsiPort.setStatus("current")
_CIsnsRegPortalScnPortType_Type = CIsnsPortalPortTypeId
_CIsnsRegPortalScnPortType_Object = MibTableColumn
cIsnsRegPortalScnPortType = _CIsnsRegPortalScnPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 10),
    _CIsnsRegPortalScnPortType_Type()
)
cIsnsRegPortalScnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalScnPortType.setStatus("current")
_CIsnsRegPortalScnPort_Type = CIsnsPortalPortId
_CIsnsRegPortalScnPort_Object = MibTableColumn
cIsnsRegPortalScnPort = _CIsnsRegPortalScnPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 11),
    _CIsnsRegPortalScnPort_Type()
)
cIsnsRegPortalScnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalScnPort.setStatus("current")
_CIsnsRegPortalSecurityInfo_Type = CIsnsPortalSecurityBitmapId
_CIsnsRegPortalSecurityInfo_Object = MibTableColumn
cIsnsRegPortalSecurityInfo = _CIsnsRegPortalSecurityInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 2, 1, 1, 12),
    _CIsnsRegPortalSecurityInfo_Type()
)
cIsnsRegPortalSecurityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPortalSecurityInfo.setStatus("current")
_CIsnsRegPortalGroupInfo_ObjectIdentity = ObjectIdentity
cIsnsRegPortalGroupInfo = _CIsnsRegPortalGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3)
)
_CIsnsRegPgTable_Object = MibTable
cIsnsRegPgTable = _CIsnsRegPgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegPgTable.setStatus("current")
_CIsnsRegPgEntry_Object = MibTableRow
cIsnsRegPgEntry = _CIsnsRegPgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1)
)
cIsnsRegPgEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityIdx"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgIdx"),
)
if mibBuilder.loadTexts:
    cIsnsRegPgEntry.setStatus("current")
_CIsnsRegPgIdx_Type = CIsnsPortalGroupIndexId
_CIsnsRegPgIdx_Object = MibTableColumn
cIsnsRegPgIdx = _CIsnsRegPgIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 1),
    _CIsnsRegPgIdx_Type()
)
cIsnsRegPgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsRegPgIdx.setStatus("current")
_CIsnsRegPgIscsiNodeIdx_Type = CIsnsNodeIndexId
_CIsnsRegPgIscsiNodeIdx_Object = MibTableColumn
cIsnsRegPgIscsiNodeIdx = _CIsnsRegPgIscsiNodeIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 2),
    _CIsnsRegPgIscsiNodeIdx_Type()
)
cIsnsRegPgIscsiNodeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgIscsiNodeIdx.setStatus("current")


class _CIsnsRegPgIscsiName_Type(SnmpAdminString):
    """Custom type cIsnsRegPgIscsiName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_CIsnsRegPgIscsiName_Type.__name__ = "SnmpAdminString"
_CIsnsRegPgIscsiName_Object = MibTableColumn
cIsnsRegPgIscsiName = _CIsnsRegPgIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 3),
    _CIsnsRegPgIscsiName_Type()
)
cIsnsRegPgIscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgIscsiName.setStatus("current")
_CIsnsRegPgPortalPrtlIdx_Type = CIsnsPortalIndexId
_CIsnsRegPgPortalPrtlIdx_Object = MibTableColumn
cIsnsRegPgPortalPrtlIdx = _CIsnsRegPgPortalPrtlIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 4),
    _CIsnsRegPgPortalPrtlIdx_Type()
)
cIsnsRegPgPortalPrtlIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgPortalPrtlIdx.setStatus("current")
_CIsnsRegPgPortalAddrType_Type = InetAddressType
_CIsnsRegPgPortalAddrType_Object = MibTableColumn
cIsnsRegPgPortalAddrType = _CIsnsRegPgPortalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 5),
    _CIsnsRegPgPortalAddrType_Type()
)
cIsnsRegPgPortalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgPortalAddrType.setStatus("current")
_CIsnsRegPgPortalAddr_Type = InetAddress
_CIsnsRegPgPortalAddr_Object = MibTableColumn
cIsnsRegPgPortalAddr = _CIsnsRegPgPortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 6),
    _CIsnsRegPgPortalAddr_Type()
)
cIsnsRegPgPortalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgPortalAddr.setStatus("current")
_CIsnsRegPgPortalPortType_Type = CIsnsPortalPortTypeId
_CIsnsRegPgPortalPortType_Object = MibTableColumn
cIsnsRegPgPortalPortType = _CIsnsRegPgPortalPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 7),
    _CIsnsRegPgPortalPortType_Type()
)
cIsnsRegPgPortalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgPortalPortType.setStatus("current")
_CIsnsRegPgPortalPort_Type = CIsnsPortalPortId
_CIsnsRegPgPortalPort_Object = MibTableColumn
cIsnsRegPgPortalPort = _CIsnsRegPgPortalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 8),
    _CIsnsRegPgPortalPort_Type()
)
cIsnsRegPgPortalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgPortalPort.setStatus("current")
_CIsnsRegPgPGT_Type = CIsnsPortalGroupTagIdOrZero
_CIsnsRegPgPGT_Object = MibTableColumn
cIsnsRegPgPGT = _CIsnsRegPgPGT_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 3, 1, 1, 9),
    _CIsnsRegPgPGT_Type()
)
cIsnsRegPgPGT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegPgPGT.setStatus("current")
_CIsnsRegIscsiNodeInfo_ObjectIdentity = ObjectIdentity
cIsnsRegIscsiNodeInfo = _CIsnsRegIscsiNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4)
)
_CIsnsRegIscsiNodeTable_Object = MibTable
cIsnsRegIscsiNodeTable = _CIsnsRegIscsiNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeTable.setStatus("current")
_CIsnsRegIscsiNodeEntry_Object = MibTableRow
cIsnsRegIscsiNodeEntry = _CIsnsRegIscsiNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1)
)
cIsnsRegIscsiNodeEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityIdx"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeIdx"),
)
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeEntry.setStatus("current")
_CIsnsRegIscsiNodeIdx_Type = CIsnsNodeIndexId
_CIsnsRegIscsiNodeIdx_Object = MibTableColumn
cIsnsRegIscsiNodeIdx = _CIsnsRegIscsiNodeIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 1),
    _CIsnsRegIscsiNodeIdx_Type()
)
cIsnsRegIscsiNodeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeIdx.setStatus("current")


class _CIsnsRegIscsiNodeName_Type(SnmpAdminString):
    """Custom type cIsnsRegIscsiNodeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_CIsnsRegIscsiNodeName_Type.__name__ = "SnmpAdminString"
_CIsnsRegIscsiNodeName_Object = MibTableColumn
cIsnsRegIscsiNodeName = _CIsnsRegIscsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 2),
    _CIsnsRegIscsiNodeName_Type()
)
cIsnsRegIscsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeName.setStatus("current")
_CIsnsRegIscsiNodeType_Type = CIsnsNodeTypeId
_CIsnsRegIscsiNodeType_Object = MibTableColumn
cIsnsRegIscsiNodeType = _CIsnsRegIscsiNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 3),
    _CIsnsRegIscsiNodeType_Type()
)
cIsnsRegIscsiNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeType.setStatus("current")


class _CIsnsRegIscsiNodeAlias_Type(SnmpAdminString):
    """Custom type cIsnsRegIscsiNodeAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegIscsiNodeAlias_Type.__name__ = "SnmpAdminString"
_CIsnsRegIscsiNodeAlias_Object = MibTableColumn
cIsnsRegIscsiNodeAlias = _CIsnsRegIscsiNodeAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 4),
    _CIsnsRegIscsiNodeAlias_Type()
)
cIsnsRegIscsiNodeAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeAlias.setStatus("current")
_CIsnsRegIscsiNodeScnBitmap_Type = CIsnsScnBitmapId
_CIsnsRegIscsiNodeScnBitmap_Object = MibTableColumn
cIsnsRegIscsiNodeScnBitmap = _CIsnsRegIscsiNodeScnBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 5),
    _CIsnsRegIscsiNodeScnBitmap_Type()
)
cIsnsRegIscsiNodeScnBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeScnBitmap.setStatus("current")
_CIsnsRegIscsiNodeWwnToken_Type = FcNameIdOrZero
_CIsnsRegIscsiNodeWwnToken_Object = MibTableColumn
cIsnsRegIscsiNodeWwnToken = _CIsnsRegIscsiNodeWwnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 6),
    _CIsnsRegIscsiNodeWwnToken_Type()
)
cIsnsRegIscsiNodeWwnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeWwnToken.setStatus("current")


class _CIsnsRegIscsiNodeAuthMethod_Type(SnmpAdminString):
    """Custom type cIsnsRegIscsiNodeAuthMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegIscsiNodeAuthMethod_Type.__name__ = "SnmpAdminString"
_CIsnsRegIscsiNodeAuthMethod_Object = MibTableColumn
cIsnsRegIscsiNodeAuthMethod = _CIsnsRegIscsiNodeAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 4, 1, 1, 7),
    _CIsnsRegIscsiNodeAuthMethod_Type()
)
cIsnsRegIscsiNodeAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegIscsiNodeAuthMethod.setStatus("current")
_CIsnsRegFcPortInfo_ObjectIdentity = ObjectIdentity
cIsnsRegFcPortInfo = _CIsnsRegFcPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5)
)
_CIsnsRegFcPortTable_Object = MibTable
cIsnsRegFcPortTable = _CIsnsRegFcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegFcPortTable.setStatus("current")
_CIsnsRegFcPortEntry_Object = MibTableRow
cIsnsRegFcPortEntry = _CIsnsRegFcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1)
)
cIsnsRegFcPortEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityIdx"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortWwpn"),
)
if mibBuilder.loadTexts:
    cIsnsRegFcPortEntry.setStatus("current")
_CIsnsRegFcPortWwpn_Type = FcNameIdOrZero
_CIsnsRegFcPortWwpn_Object = MibTableColumn
cIsnsRegFcPortWwpn = _CIsnsRegFcPortWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 1),
    _CIsnsRegFcPortWwpn_Type()
)
cIsnsRegFcPortWwpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsRegFcPortWwpn.setStatus("current")
_CIsnsRegFcPortID_Type = FcAddressId
_CIsnsRegFcPortID_Object = MibTableColumn
cIsnsRegFcPortID = _CIsnsRegFcPortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 2),
    _CIsnsRegFcPortID_Type()
)
cIsnsRegFcPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortID.setStatus("current")


class _CIsnsRegFcPortType_Type(Integer32):
    """Custom type cIsnsRegFcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsRegFcPortType_Type.__name__ = "Integer32"
_CIsnsRegFcPortType_Object = MibTableColumn
cIsnsRegFcPortType = _CIsnsRegFcPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 3),
    _CIsnsRegFcPortType_Type()
)
cIsnsRegFcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortType.setStatus("current")


class _CIsnsRegFcPortSymName_Type(SnmpAdminString):
    """Custom type cIsnsRegFcPortSymName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegFcPortSymName_Type.__name__ = "SnmpAdminString"
_CIsnsRegFcPortSymName_Object = MibTableColumn
cIsnsRegFcPortSymName = _CIsnsRegFcPortSymName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 4),
    _CIsnsRegFcPortSymName_Type()
)
cIsnsRegFcPortSymName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortSymName.setStatus("current")
_CIsnsRegFcPortFabricPortWwn_Type = FcNameIdOrZero
_CIsnsRegFcPortFabricPortWwn_Object = MibTableColumn
cIsnsRegFcPortFabricPortWwn = _CIsnsRegFcPortFabricPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 5),
    _CIsnsRegFcPortFabricPortWwn_Type()
)
cIsnsRegFcPortFabricPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortFabricPortWwn.setStatus("current")
_CIsnsRegFcPortHA_Type = FcAddressId
_CIsnsRegFcPortHA_Object = MibTableColumn
cIsnsRegFcPortHA = _CIsnsRegFcPortHA_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 6),
    _CIsnsRegFcPortHA_Type()
)
cIsnsRegFcPortHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortHA.setStatus("current")
_CIsnsRegFcPortAddrType_Type = InetAddressType
_CIsnsRegFcPortAddrType_Object = MibTableColumn
cIsnsRegFcPortAddrType = _CIsnsRegFcPortAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 7),
    _CIsnsRegFcPortAddrType_Type()
)
cIsnsRegFcPortAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortAddrType.setStatus("current")
_CIsnsRegFcPortAddr_Type = InetAddress
_CIsnsRegFcPortAddr_Object = MibTableColumn
cIsnsRegFcPortAddr = _CIsnsRegFcPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 8),
    _CIsnsRegFcPortAddr_Type()
)
cIsnsRegFcPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortAddr.setStatus("current")
_CIsnsRegFcPortFcCos_Type = CIsnsCosBitmapId
_CIsnsRegFcPortFcCos_Object = MibTableColumn
cIsnsRegFcPortFcCos = _CIsnsRegFcPortFcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 9),
    _CIsnsRegFcPortFcCos_Type()
)
cIsnsRegFcPortFcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortFcCos.setStatus("current")


class _CIsnsRegFcPortFc4Types_Type(OctetString):
    """Custom type cIsnsRegFcPortFc4Types based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CIsnsRegFcPortFc4Types_Type.__name__ = "OctetString"
_CIsnsRegFcPortFc4Types_Object = MibTableColumn
cIsnsRegFcPortFc4Types = _CIsnsRegFcPortFc4Types_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 10),
    _CIsnsRegFcPortFc4Types_Type()
)
cIsnsRegFcPortFc4Types.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortFc4Types.setStatus("current")


class _CIsnsRegFcPortFc4Descr_Type(OctetString):
    """Custom type cIsnsRegFcPortFc4Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegFcPortFc4Descr_Type.__name__ = "OctetString"
_CIsnsRegFcPortFc4Descr_Object = MibTableColumn
cIsnsRegFcPortFc4Descr = _CIsnsRegFcPortFc4Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 11),
    _CIsnsRegFcPortFc4Descr_Type()
)
cIsnsRegFcPortFc4Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortFc4Descr.setStatus("current")


class _CIsnsRegFcPortFc4Features_Type(OctetString):
    """Custom type cIsnsRegFcPortFc4Features based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CIsnsRegFcPortFc4Features_Type.__name__ = "OctetString"
_CIsnsRegFcPortFc4Features_Object = MibTableColumn
cIsnsRegFcPortFc4Features = _CIsnsRegFcPortFc4Features_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 12),
    _CIsnsRegFcPortFc4Features_Type()
)
cIsnsRegFcPortFc4Features.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortFc4Features.setStatus("current")
_CIsnsRegFcPortScnBitmap_Type = CIsnsScnBitmapId
_CIsnsRegFcPortScnBitmap_Object = MibTableColumn
cIsnsRegFcPortScnBitmap = _CIsnsRegFcPortScnBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 13),
    _CIsnsRegFcPortScnBitmap_Type()
)
cIsnsRegFcPortScnBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortScnBitmap.setStatus("current")
_CIsnsRegFcPortRole_Type = CIsnsNodeTypeId
_CIsnsRegFcPortRole_Object = MibTableColumn
cIsnsRegFcPortRole = _CIsnsRegFcPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 14),
    _CIsnsRegFcPortRole_Type()
)
cIsnsRegFcPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortRole.setStatus("current")
_CIsnsRegFcPortFcNodeWwn_Type = FcNameIdOrZero
_CIsnsRegFcPortFcNodeWwn_Object = MibTableColumn
cIsnsRegFcPortFcNodeWwn = _CIsnsRegFcPortFcNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 15),
    _CIsnsRegFcPortFcNodeWwn_Type()
)
cIsnsRegFcPortFcNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortFcNodeWwn.setStatus("current")
_CIsnsRegFcPortPpnWwn_Type = FcNameIdOrZero
_CIsnsRegFcPortPpnWwn_Object = MibTableColumn
cIsnsRegFcPortPpnWwn = _CIsnsRegFcPortPpnWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 5, 1, 1, 16),
    _CIsnsRegFcPortPpnWwn_Type()
)
cIsnsRegFcPortPpnWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcPortPpnWwn.setStatus("current")
_CIsnsRegFcNodeInfo_ObjectIdentity = ObjectIdentity
cIsnsRegFcNodeInfo = _CIsnsRegFcNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6)
)
_CIsnsRegFcNodeTable_Object = MibTable
cIsnsRegFcNodeTable = _CIsnsRegFcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegFcNodeTable.setStatus("current")
_CIsnsRegFcNodeEntry_Object = MibTableRow
cIsnsRegFcNodeEntry = _CIsnsRegFcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1)
)
cIsnsRegFcNodeEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeWwn"),
)
if mibBuilder.loadTexts:
    cIsnsRegFcNodeEntry.setStatus("current")
_CIsnsRegFcNodeWwn_Type = FcNameIdOrZero
_CIsnsRegFcNodeWwn_Object = MibTableColumn
cIsnsRegFcNodeWwn = _CIsnsRegFcNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1, 1),
    _CIsnsRegFcNodeWwn_Type()
)
cIsnsRegFcNodeWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeWwn.setStatus("current")


class _CIsnsRegFcNodeSymName_Type(SnmpAdminString):
    """Custom type cIsnsRegFcNodeSymName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsRegFcNodeSymName_Type.__name__ = "SnmpAdminString"
_CIsnsRegFcNodeSymName_Object = MibTableColumn
cIsnsRegFcNodeSymName = _CIsnsRegFcNodeSymName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1, 2),
    _CIsnsRegFcNodeSymName_Type()
)
cIsnsRegFcNodeSymName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeSymName.setStatus("current")
_CIsnsRegFcNodeAddrType_Type = InetAddressType
_CIsnsRegFcNodeAddrType_Object = MibTableColumn
cIsnsRegFcNodeAddrType = _CIsnsRegFcNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1, 3),
    _CIsnsRegFcNodeAddrType_Type()
)
cIsnsRegFcNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeAddrType.setStatus("current")
_CIsnsRegFcNodeAddr_Type = InetAddress
_CIsnsRegFcNodeAddr_Object = MibTableColumn
cIsnsRegFcNodeAddr = _CIsnsRegFcNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1, 4),
    _CIsnsRegFcNodeAddr_Type()
)
cIsnsRegFcNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeAddr.setStatus("current")


class _CIsnsRegFcNodeIPA_Type(OctetString):
    """Custom type cIsnsRegFcNodeIPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CIsnsRegFcNodeIPA_Type.__name__ = "OctetString"
_CIsnsRegFcNodeIPA_Object = MibTableColumn
cIsnsRegFcNodeIPA = _CIsnsRegFcNodeIPA_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1, 5),
    _CIsnsRegFcNodeIPA_Type()
)
cIsnsRegFcNodeIPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeIPA.setStatus("current")


class _CIsnsRegFcNodeProxyIscsiName_Type(SnmpAdminString):
    """Custom type cIsnsRegFcNodeProxyIscsiName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_CIsnsRegFcNodeProxyIscsiName_Type.__name__ = "SnmpAdminString"
_CIsnsRegFcNodeProxyIscsiName_Object = MibTableColumn
cIsnsRegFcNodeProxyIscsiName = _CIsnsRegFcNodeProxyIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 1, 1, 6),
    _CIsnsRegFcNodeProxyIscsiName_Type()
)
cIsnsRegFcNodeProxyIscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeProxyIscsiName.setStatus("current")
_CIsnsRegFcNodeInfoTable_Object = MibTable
cIsnsRegFcNodeInfoTable = _CIsnsRegFcNodeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 2)
)
if mibBuilder.loadTexts:
    cIsnsRegFcNodeInfoTable.setStatus("current")
_CIsnsRegFcNodeInfoEntry_Object = MibTableRow
cIsnsRegFcNodeInfoEntry = _CIsnsRegFcNodeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cIsnsRegFcNodeInfoEntry.setStatus("current")


class _CIsnsRegFcNodeInfoNumFcPorts_Type(Unsigned32):
    """Custom type cIsnsRegFcNodeInfoNumFcPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIsnsRegFcNodeInfoNumFcPorts_Type.__name__ = "Unsigned32"
_CIsnsRegFcNodeInfoNumFcPorts_Object = MibTableColumn
cIsnsRegFcNodeInfoNumFcPorts = _CIsnsRegFcNodeInfoNumFcPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 2, 1, 1),
    _CIsnsRegFcNodeInfoNumFcPorts_Type()
)
cIsnsRegFcNodeInfoNumFcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeInfoNumFcPorts.setStatus("current")
_CIsnsRegFcNodeFcPortTable_Object = MibTable
cIsnsRegFcNodeFcPortTable = _CIsnsRegFcNodeFcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 3)
)
if mibBuilder.loadTexts:
    cIsnsRegFcNodeFcPortTable.setStatus("current")
_CIsnsRegFcNodeFcPortEntry_Object = MibTableRow
cIsnsRegFcNodeFcPortEntry = _CIsnsRegFcNodeFcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 3, 1)
)
cIsnsRegFcNodeFcPortEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeWwn"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortWwpn"),
)
if mibBuilder.loadTexts:
    cIsnsRegFcNodeFcPortEntry.setStatus("current")
_CIsnsRegFcNodeFcPortEntityEIdx_Type = CIsnsEntityIndexId
_CIsnsRegFcNodeFcPortEntityEIdx_Object = MibTableColumn
cIsnsRegFcNodeFcPortEntityEIdx = _CIsnsRegFcNodeFcPortEntityEIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 1, 7, 6, 3, 1, 1),
    _CIsnsRegFcNodeFcPortEntityEIdx_Type()
)
cIsnsRegFcNodeFcPortEntityEIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsRegFcNodeFcPortEntityEIdx.setStatus("current")
_CIsnsClntInfo_ObjectIdentity = ObjectIdentity
cIsnsClntInfo = _CIsnsClntInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2)
)
_CIsnsClntInstTable_Object = MibTable
cIsnsClntInstTable = _CIsnsClntInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIsnsClntInstTable.setStatus("current")
_CIsnsClntInstEntry_Object = MibTableRow
cIsnsClntInstEntry = _CIsnsClntInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1)
)
cIsnsClntInstEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstIndex"),
)
if mibBuilder.loadTexts:
    cIsnsClntInstEntry.setStatus("current")


class _CIsnsClntInstIndex_Type(Unsigned32):
    """Custom type cIsnsClntInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIsnsClntInstIndex_Type.__name__ = "Unsigned32"
_CIsnsClntInstIndex_Object = MibTableColumn
cIsnsClntInstIndex = _CIsnsClntInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 1),
    _CIsnsClntInstIndex_Type()
)
cIsnsClntInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsClntInstIndex.setStatus("current")


class _CIsnsClntInstName_Type(SnmpAdminString):
    """Custom type cIsnsClntInstName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsClntInstName_Type.__name__ = "SnmpAdminString"
_CIsnsClntInstName_Object = MibTableColumn
cIsnsClntInstName = _CIsnsClntInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 2),
    _CIsnsClntInstName_Type()
)
cIsnsClntInstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstName.setStatus("current")


class _CIsnsClntInstIsnspVersion_Type(Integer32):
    """Custom type cIsnsClntInstIsnspVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntInstIsnspVersion_Type.__name__ = "Integer32"
_CIsnsClntInstIsnspVersion_Object = MibTableColumn
cIsnsClntInstIsnspVersion = _CIsnsClntInstIsnspVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 3),
    _CIsnsClntInstIsnspVersion_Type()
)
cIsnsClntInstIsnspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntInstIsnspVersion.setStatus("current")


class _CIsnsClntInstDescription_Type(SnmpAdminString):
    """Custom type cIsnsClntInstDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsClntInstDescription_Type.__name__ = "SnmpAdminString"
_CIsnsClntInstDescription_Object = MibTableColumn
cIsnsClntInstDescription = _CIsnsClntInstDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 4),
    _CIsnsClntInstDescription_Type()
)
cIsnsClntInstDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntInstDescription.setStatus("current")
_CIsnsClntInstAddressType_Type = InetAddressType
_CIsnsClntInstAddressType_Object = MibTableColumn
cIsnsClntInstAddressType = _CIsnsClntInstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 5),
    _CIsnsClntInstAddressType_Type()
)
cIsnsClntInstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstAddressType.setStatus("current")
_CIsnsClntInstAddress_Type = InetAddress
_CIsnsClntInstAddress_Object = MibTableColumn
cIsnsClntInstAddress = _CIsnsClntInstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 6),
    _CIsnsClntInstAddress_Type()
)
cIsnsClntInstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstAddress.setStatus("current")


class _CIsnsClntInstTcpPort_Type(Integer32):
    """Custom type cIsnsClntInstTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntInstTcpPort_Type.__name__ = "Integer32"
_CIsnsClntInstTcpPort_Object = MibTableColumn
cIsnsClntInstTcpPort = _CIsnsClntInstTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 7),
    _CIsnsClntInstTcpPort_Type()
)
cIsnsClntInstTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstTcpPort.setStatus("current")


class _CIsnsClntInstUdpPort_Type(Integer32):
    """Custom type cIsnsClntInstUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntInstUdpPort_Type.__name__ = "Integer32"
_CIsnsClntInstUdpPort_Object = MibTableColumn
cIsnsClntInstUdpPort = _CIsnsClntInstUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 8),
    _CIsnsClntInstUdpPort_Type()
)
cIsnsClntInstUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstUdpPort.setStatus("current")
_CIsnsClntInstUptime_Type = TimeTicks
_CIsnsClntInstUptime_Object = MibTableColumn
cIsnsClntInstUptime = _CIsnsClntInstUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 9),
    _CIsnsClntInstUptime_Type()
)
cIsnsClntInstUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntInstUptime.setStatus("current")
_CIsnsClntInstAvailDiscMthd_Type = CIsnsSrvrDscvryMthdId
_CIsnsClntInstAvailDiscMthd_Object = MibTableColumn
cIsnsClntInstAvailDiscMthd = _CIsnsClntInstAvailDiscMthd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 10),
    _CIsnsClntInstAvailDiscMthd_Type()
)
cIsnsClntInstAvailDiscMthd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntInstAvailDiscMthd.setStatus("current")
_CIsnsClntInstPrmryDiscMthd_Type = CIsnsSrvrDscvryMthdId
_CIsnsClntInstPrmryDiscMthd_Object = MibTableColumn
cIsnsClntInstPrmryDiscMthd = _CIsnsClntInstPrmryDiscMthd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 11),
    _CIsnsClntInstPrmryDiscMthd_Type()
)
cIsnsClntInstPrmryDiscMthd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstPrmryDiscMthd.setStatus("current")
_CIsnsClntInstScndryDiscMthd_Type = CIsnsSrvrDscvryMthdId
_CIsnsClntInstScndryDiscMthd_Object = MibTableColumn
cIsnsClntInstScndryDiscMthd = _CIsnsClntInstScndryDiscMthd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 12),
    _CIsnsClntInstScndryDiscMthd_Type()
)
cIsnsClntInstScndryDiscMthd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstScndryDiscMthd.setStatus("current")
_CIsnsClntInstDiscMcGrpType_Type = InetAddressType
_CIsnsClntInstDiscMcGrpType_Object = MibTableColumn
cIsnsClntInstDiscMcGrpType = _CIsnsClntInstDiscMcGrpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 13),
    _CIsnsClntInstDiscMcGrpType_Type()
)
cIsnsClntInstDiscMcGrpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstDiscMcGrpType.setStatus("current")
_CIsnsClntInstDiscMcGrp_Type = InetAddress
_CIsnsClntInstDiscMcGrp_Object = MibTableColumn
cIsnsClntInstDiscMcGrp = _CIsnsClntInstDiscMcGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 1, 1, 14),
    _CIsnsClntInstDiscMcGrp_Type()
)
cIsnsClntInstDiscMcGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIsnsClntInstDiscMcGrp.setStatus("current")
_CIsnsClntCfgSrvrTable_Object = MibTable
cIsnsClntCfgSrvrTable = _CIsnsClntCfgSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrTable.setStatus("current")
_CIsnsClntCfgSrvrEntry_Object = MibTableRow
cIsnsClntCfgSrvrEntry = _CIsnsClntCfgSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1)
)
cIsnsClntCfgSrvrEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrIndex"),
)
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrEntry.setStatus("current")


class _CIsnsClntCfgSrvrIndex_Type(Unsigned32):
    """Custom type cIsnsClntCfgSrvrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CIsnsClntCfgSrvrIndex_Type.__name__ = "Unsigned32"
_CIsnsClntCfgSrvrIndex_Object = MibTableColumn
cIsnsClntCfgSrvrIndex = _CIsnsClntCfgSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 1),
    _CIsnsClntCfgSrvrIndex_Type()
)
cIsnsClntCfgSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrIndex.setStatus("current")
_CIsnsClntCfgSrvrAddrType_Type = InetAddressType
_CIsnsClntCfgSrvrAddrType_Object = MibTableColumn
cIsnsClntCfgSrvrAddrType = _CIsnsClntCfgSrvrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 2),
    _CIsnsClntCfgSrvrAddrType_Type()
)
cIsnsClntCfgSrvrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrAddrType.setStatus("current")
_CIsnsClntCfgSrvrAddr_Type = InetAddress
_CIsnsClntCfgSrvrAddr_Object = MibTableColumn
cIsnsClntCfgSrvrAddr = _CIsnsClntCfgSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 3),
    _CIsnsClntCfgSrvrAddr_Type()
)
cIsnsClntCfgSrvrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrAddr.setStatus("current")


class _CIsnsClntCfgSrvrTcpPort_Type(Integer32):
    """Custom type cIsnsClntCfgSrvrTcpPort based on Integer32"""
    defaultValue = 3205

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntCfgSrvrTcpPort_Type.__name__ = "Integer32"
_CIsnsClntCfgSrvrTcpPort_Object = MibTableColumn
cIsnsClntCfgSrvrTcpPort = _CIsnsClntCfgSrvrTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 4),
    _CIsnsClntCfgSrvrTcpPort_Type()
)
cIsnsClntCfgSrvrTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrTcpPort.setStatus("current")


class _CIsnsClntCfgSrvrUdpPort_Type(Integer32):
    """Custom type cIsnsClntCfgSrvrUdpPort based on Integer32"""
    defaultValue = 3205

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntCfgSrvrUdpPort_Type.__name__ = "Integer32"
_CIsnsClntCfgSrvrUdpPort_Object = MibTableColumn
cIsnsClntCfgSrvrUdpPort = _CIsnsClntCfgSrvrUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 5),
    _CIsnsClntCfgSrvrUdpPort_Type()
)
cIsnsClntCfgSrvrUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrUdpPort.setStatus("current")


class _CIsnsClntCfgSrvrPriority_Type(Integer32):
    """Custom type cIsnsClntCfgSrvrPriority based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CIsnsClntCfgSrvrPriority_Type.__name__ = "Integer32"
_CIsnsClntCfgSrvrPriority_Object = MibTableColumn
cIsnsClntCfgSrvrPriority = _CIsnsClntCfgSrvrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 6),
    _CIsnsClntCfgSrvrPriority_Type()
)
cIsnsClntCfgSrvrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrPriority.setStatus("current")


class _CIsnsClntCfgSrvrTimeout_Type(Integer32):
    """Custom type cIsnsClntCfgSrvrTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CIsnsClntCfgSrvrTimeout_Type.__name__ = "Integer32"
_CIsnsClntCfgSrvrTimeout_Object = MibTableColumn
cIsnsClntCfgSrvrTimeout = _CIsnsClntCfgSrvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 7),
    _CIsnsClntCfgSrvrTimeout_Type()
)
cIsnsClntCfgSrvrTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrTimeout.setStatus("current")


class _CIsnsClntCfgSrvrRetries_Type(Integer32):
    """Custom type cIsnsClntCfgSrvrRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CIsnsClntCfgSrvrRetries_Type.__name__ = "Integer32"
_CIsnsClntCfgSrvrRetries_Object = MibTableColumn
cIsnsClntCfgSrvrRetries = _CIsnsClntCfgSrvrRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 8),
    _CIsnsClntCfgSrvrRetries_Type()
)
cIsnsClntCfgSrvrRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrRetries.setStatus("current")
_CIsnsClntCfgSrvrRowStatus_Type = RowStatus
_CIsnsClntCfgSrvrRowStatus_Object = MibTableColumn
cIsnsClntCfgSrvrRowStatus = _CIsnsClntCfgSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 2, 1, 9),
    _CIsnsClntCfgSrvrRowStatus_Type()
)
cIsnsClntCfgSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntCfgSrvrRowStatus.setStatus("current")
_CIsnsClntDscvrdSrvrTable_Object = MibTable
cIsnsClntDscvrdSrvrTable = _CIsnsClntDscvrdSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrTable.setStatus("current")
_CIsnsClntDscvrdSrvrEntry_Object = MibTableRow
cIsnsClntDscvrdSrvrEntry = _CIsnsClntDscvrdSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1)
)
cIsnsClntDscvrdSrvrEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrIndex"),
)
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrEntry.setStatus("current")


class _CIsnsClntDscvrdSrvrIndex_Type(Unsigned32):
    """Custom type cIsnsClntDscvrdSrvrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIsnsClntDscvrdSrvrIndex_Type.__name__ = "Unsigned32"
_CIsnsClntDscvrdSrvrIndex_Object = MibTableColumn
cIsnsClntDscvrdSrvrIndex = _CIsnsClntDscvrdSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 1),
    _CIsnsClntDscvrdSrvrIndex_Type()
)
cIsnsClntDscvrdSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrIndex.setStatus("current")
_CIsnsClntDscvrdSrvrAddrType_Type = InetAddressType
_CIsnsClntDscvrdSrvrAddrType_Object = MibTableColumn
cIsnsClntDscvrdSrvrAddrType = _CIsnsClntDscvrdSrvrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 2),
    _CIsnsClntDscvrdSrvrAddrType_Type()
)
cIsnsClntDscvrdSrvrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrAddrType.setStatus("current")
_CIsnsClntDscvrdSrvrAddr_Type = InetAddress
_CIsnsClntDscvrdSrvrAddr_Object = MibTableColumn
cIsnsClntDscvrdSrvrAddr = _CIsnsClntDscvrdSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 3),
    _CIsnsClntDscvrdSrvrAddr_Type()
)
cIsnsClntDscvrdSrvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrAddr.setStatus("current")


class _CIsnsClntDscvrdSrvrTcpPort_Type(Integer32):
    """Custom type cIsnsClntDscvrdSrvrTcpPort based on Integer32"""
    defaultValue = 3205

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntDscvrdSrvrTcpPort_Type.__name__ = "Integer32"
_CIsnsClntDscvrdSrvrTcpPort_Object = MibTableColumn
cIsnsClntDscvrdSrvrTcpPort = _CIsnsClntDscvrdSrvrTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 4),
    _CIsnsClntDscvrdSrvrTcpPort_Type()
)
cIsnsClntDscvrdSrvrTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrTcpPort.setStatus("current")


class _CIsnsClntDscvrdSrvrUdpPort_Type(Integer32):
    """Custom type cIsnsClntDscvrdSrvrUdpPort based on Integer32"""
    defaultValue = 3205

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsClntDscvrdSrvrUdpPort_Type.__name__ = "Integer32"
_CIsnsClntDscvrdSrvrUdpPort_Object = MibTableColumn
cIsnsClntDscvrdSrvrUdpPort = _CIsnsClntDscvrdSrvrUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 5),
    _CIsnsClntDscvrdSrvrUdpPort_Type()
)
cIsnsClntDscvrdSrvrUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrUdpPort.setStatus("current")


class _CIsnsClntDscvrdSrvrIsnsVersion_Type(Integer32):
    """Custom type cIsnsClntDscvrdSrvrIsnsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CIsnsClntDscvrdSrvrIsnsVersion_Type.__name__ = "Integer32"
_CIsnsClntDscvrdSrvrIsnsVersion_Object = MibTableColumn
cIsnsClntDscvrdSrvrIsnsVersion = _CIsnsClntDscvrdSrvrIsnsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 6),
    _CIsnsClntDscvrdSrvrIsnsVersion_Type()
)
cIsnsClntDscvrdSrvrIsnsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrIsnsVersion.setStatus("current")
_CIsnsClntDscvrdSrvrDiscMthd_Type = CIsnsSrvrDscvryMthdId
_CIsnsClntDscvrdSrvrDiscMthd_Object = MibTableColumn
cIsnsClntDscvrdSrvrDiscMthd = _CIsnsClntDscvrdSrvrDiscMthd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 3, 1, 7),
    _CIsnsClntDscvrdSrvrDiscMthd_Type()
)
cIsnsClntDscvrdSrvrDiscMthd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntDscvrdSrvrDiscMthd.setStatus("current")
_CIsnsClntRegEntityTable_Object = MibTable
cIsnsClntRegEntityTable = _CIsnsClntRegEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cIsnsClntRegEntityTable.setStatus("current")
_CIsnsClntRegEntityEntry_Object = MibTableRow
cIsnsClntRegEntityEntry = _CIsnsClntRegEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 4, 1)
)
cIsnsClntRegEntityEntry.setIndexNames(
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrIndex"),
    (0, "CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntRegEntityIdx"),
)
if mibBuilder.loadTexts:
    cIsnsClntRegEntityEntry.setStatus("current")
_CIsnsClntRegEntityIdx_Type = CIsnsEntityIndexId
_CIsnsClntRegEntityIdx_Object = MibTableColumn
cIsnsClntRegEntityIdx = _CIsnsClntRegEntityIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 4, 1, 1),
    _CIsnsClntRegEntityIdx_Type()
)
cIsnsClntRegEntityIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsClntRegEntityIdx.setStatus("current")


class _CIsnsClntRegEntityEID_Type(SnmpAdminString):
    """Custom type cIsnsClntRegEntityEID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CIsnsClntRegEntityEID_Type.__name__ = "SnmpAdminString"
_CIsnsClntRegEntityEID_Object = MibTableColumn
cIsnsClntRegEntityEID = _CIsnsClntRegEntityEID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 4, 1, 2),
    _CIsnsClntRegEntityEID_Type()
)
cIsnsClntRegEntityEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntRegEntityEID.setStatus("current")
_CIsnsClntRegEntityProtocol_Type = CIsnsEntityProtocolId
_CIsnsClntRegEntityProtocol_Object = MibTableColumn
cIsnsClntRegEntityProtocol = _CIsnsClntRegEntityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 2, 4, 1, 3),
    _CIsnsClntRegEntityProtocol_Type()
)
cIsnsClntRegEntityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIsnsClntRegEntityProtocol.setStatus("current")
_CIsnsNotification_ObjectIdentity = ObjectIdentity
cIsnsNotification = _CIsnsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3)
)
_CIsnsNotificationPrefix_ObjectIdentity = ObjectIdentity
cIsnsNotificationPrefix = _CIsnsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0)
)
_CIsnsNotificationInfo_ObjectIdentity = ObjectIdentity
cIsnsNotificationInfo = _CIsnsNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 1)
)


class _CIsnsInstInfo_Type(SnmpAdminString):
    """Custom type cIsnsInstInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CIsnsInstInfo_Type.__name__ = "SnmpAdminString"
_CIsnsInstInfo_Object = MibScalar
cIsnsInstInfo = _CIsnsInstInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 1, 1),
    _CIsnsInstInfo_Type()
)
cIsnsInstInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIsnsInstInfo.setStatus("current")
_CIsnsAddrTypeNotifctn_Type = InetAddressType
_CIsnsAddrTypeNotifctn_Object = MibScalar
cIsnsAddrTypeNotifctn = _CIsnsAddrTypeNotifctn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 1, 2),
    _CIsnsAddrTypeNotifctn_Type()
)
cIsnsAddrTypeNotifctn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIsnsAddrTypeNotifctn.setStatus("current")
_CIsnsAddrNotifctn_Type = InetAddress
_CIsnsAddrNotifctn_Object = MibScalar
cIsnsAddrNotifctn = _CIsnsAddrNotifctn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 1, 3),
    _CIsnsAddrNotifctn_Type()
)
cIsnsAddrNotifctn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIsnsAddrNotifctn.setStatus("current")


class _CIsnsTcpPortNotifctn_Type(Integer32):
    """Custom type cIsnsTcpPortNotifctn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsTcpPortNotifctn_Type.__name__ = "Integer32"
_CIsnsTcpPortNotifctn_Object = MibScalar
cIsnsTcpPortNotifctn = _CIsnsTcpPortNotifctn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 1, 4),
    _CIsnsTcpPortNotifctn_Type()
)
cIsnsTcpPortNotifctn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIsnsTcpPortNotifctn.setStatus("current")


class _CIsnsUdpPortNotifctn_Type(Integer32):
    """Custom type cIsnsUdpPortNotifctn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIsnsUdpPortNotifctn_Type.__name__ = "Integer32"
_CIsnsUdpPortNotifctn_Object = MibScalar
cIsnsUdpPortNotifctn = _CIsnsUdpPortNotifctn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 1, 5),
    _CIsnsUdpPortNotifctn_Type()
)
cIsnsUdpPortNotifctn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIsnsUdpPortNotifctn.setStatus("current")
_CIsnsConformance_ObjectIdentity = ObjectIdentity
cIsnsConformance = _CIsnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2)
)
_CIsnsGroups_ObjectIdentity = ObjectIdentity
cIsnsGroups = _CIsnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1)
)
_CIsnsCompliances_ObjectIdentity = ObjectIdentity
cIsnsCompliances = _CIsnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 2)
)
cIsnsSrvrInstEntry.registerAugmentions(
    ("CISCO-IETF-ISNS-MGMT-MIB",
     "cIsnsNumObjEntry")
)
cIsnsNumObjEntry.setIndexNames(*cIsnsSrvrInstEntry.getIndexNames())
cIsnsSrvrInstEntry.registerAugmentions(
    ("CISCO-IETF-ISNS-MGMT-MIB",
     "cIsnsNextIdxEntry")
)
cIsnsNextIdxEntry.setIndexNames(*cIsnsSrvrInstEntry.getIndexNames())
cIsnsRegEntityEntry.registerAugmentions(
    ("CISCO-IETF-ISNS-MGMT-MIB",
     "cIsnsRegEntityNumObjEntry")
)
cIsnsRegEntityNumObjEntry.setIndexNames(*cIsnsRegEntityEntry.getIndexNames())
cIsnsRegFcNodeEntry.registerAugmentions(
    ("CISCO-IETF-ISNS-MGMT-MIB",
     "cIsnsRegFcNodeInfoEntry")
)
cIsnsRegFcNodeInfoEntry.setIndexNames(*cIsnsRegFcNodeEntry.getIndexNames())

# Managed Objects groups

cIsnsServerAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 1)
)
cIsnsServerAttributesGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstIsnsVersion"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstDescription"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstAddressType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstAddress"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstTcpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstUdpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstUptime"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstRole"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstDiscMthdsEnbld"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstDiscMcGrpType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstDiscMcGrp"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstCntrlNodeAuth"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstEsiNonRespThrshld"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstEnblCntrlNdeMgtScn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstDfltDdDdsStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstUpdateDdDdsSpprtd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsSrvrInstUpdateDdDdsEnbld"))
)
if mibBuilder.loadTexts:
    cIsnsServerAttributesGroup.setStatus("current")

cIsnsServerNumObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 2)
)
cIsnsServerNumObjGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumDds"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumDd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumEntities"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumPortals"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumPortalGroups"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumIscsiNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumFcPorts"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNumFcNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumPortals"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumPortalGroup"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumIscsiNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumFcPorts"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumFcNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeInfoNumFcPorts"))
)
if mibBuilder.loadTexts:
    cIsnsServerNumObjGroup.setStatus("current")

cIsnsServerNextIdxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 3)
)
cIsnsServerNextIdxGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNextIdxDds"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNextIdxDd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNextIdxUnregIscsiNodeInDd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsNextIdxUnregPortalInDd"))
)
if mibBuilder.loadTexts:
    cIsnsServerNextIdxGroup.setStatus("current")

cIsnsServerIscsiCntlNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 4)
)
cIsnsServerIscsiCntlNodeGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsCntlNodeIscsiNodeName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsCntlNodeIscsiRowStatus"))
)
if mibBuilder.loadTexts:
    cIsnsServerIscsiCntlNodeGroup.setStatus("current")

cIsnsServerIfcpCntlNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 5)
)
cIsnsServerIfcpCntlNodeGroup.setObjects(
    ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsCntlNodeFcPortRowStatus")
)
if mibBuilder.loadTexts:
    cIsnsServerIfcpCntlNodeGroup.setStatus("current")

cIsnsServerIscsiDdsDdObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 6)
)
cIsnsServerIscsiDdsDdObjGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsSymbolicName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsMemberRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdSymbolicName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdFeatures"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberIscsiName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberIsRegistered"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalIsRegistered"))
)
if mibBuilder.loadTexts:
    cIsnsServerIscsiDdsDdObjGroup.setStatus("current")

cIsnsServerIfcpDdsDdObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 7)
)
cIsnsServerIfcpDdsDdObjGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsSymbolicName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdsMemberRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdSymbolicName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdFeatures"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberPortalIsRegistered"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberFcIsRegistered"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsDdMemberFcRowStatus"))
)
if mibBuilder.loadTexts:
    cIsnsServerIfcpDdsDdObjGroup.setStatus("current")

cIsnsServerRegIscsiObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 8)
)
cIsnsServerRegIscsiObjGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityEID"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityProtocol"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityMgtAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityMgtAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityTimestamp"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityVersionMin"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityVersionMax"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityRegPeriod"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumPortals"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumPortalGroup"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumIscsiNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumFcPorts"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumFcNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalSymName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalEsiInterval"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalEsiPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalEsiPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalScnPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalScnPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalSecurityInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgIscsiNodeIdx"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgIscsiName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgPortalPrtlIdx"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgPortalAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgPortalAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgPortalPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgPortalPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPgPGT"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeAlias"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeScnBitmap"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeWwnToken"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegIscsiNodeAuthMethod"))
)
if mibBuilder.loadTexts:
    cIsnsServerRegIscsiObjGroup.setStatus("current")

cIsnsServerRegIfcpObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 9)
)
cIsnsServerRegIfcpObjGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityEID"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityProtocol"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityMgtAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityMgtAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityTimestamp"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityVersionMin"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityVersionMax"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityRegPeriod"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumPortals"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumPortalGroup"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumIscsiNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumFcPorts"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegEntityInfoNumFcNodes"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalSymName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalEsiInterval"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalEsiPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalEsiPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalScnPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalScnPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegPortalSecurityInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortID"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortSymName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortFabricPortWwn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortHA"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortFcCos"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortFc4Types"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortFc4Descr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortFc4Features"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortScnBitmap"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortRole"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortFcNodeWwn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcPortPpnWwn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeSymName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeIPA"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeProxyIscsiName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsRegFcNodeFcPortEntityEIdx"))
)
if mibBuilder.loadTexts:
    cIsnsServerRegIfcpObjGroup.setStatus("current")

cIsnsClientAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 10)
)
cIsnsClientAttributesGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstName"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstIsnspVersion"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstDescription"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstAddressType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstAddress"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstTcpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstUdpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstUptime"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstAvailDiscMthd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstPrmryDiscMthd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstScndryDiscMthd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstDiscMcGrpType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntInstDiscMcGrp"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrTcpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrUdpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrPriority"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrTimeout"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrRetries"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntCfgSrvrRowStatus"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrAddrType"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrAddr"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrTcpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrUdpPort"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrIsnsVersion"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntDscvrdSrvrDiscMthd"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntRegEntityEID"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClntRegEntityProtocol"))
)
if mibBuilder.loadTexts:
    cIsnsClientAttributesGroup.setStatus("current")

cIsnsNotificationObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 11)
)
cIsnsNotificationObjGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrTypeNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsTcpPortNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsUdpPortNotifctn"))
)
if mibBuilder.loadTexts:
    cIsnsNotificationObjGroup.setStatus("current")


# Notification objects

cIsnsServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0, 1)
)
cIsnsServerStart.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrTypeNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsTcpPortNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsUdpPortNotifctn"))
)
if mibBuilder.loadTexts:
    cIsnsServerStart.setStatus(
        "current"
    )

cIsnsServerShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0, 2)
)
cIsnsServerShutdown.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrTypeNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsTcpPortNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsUdpPortNotifctn"))
)
if mibBuilder.loadTexts:
    cIsnsServerShutdown.setStatus(
        "current"
    )

cIsnsClientStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0, 3)
)
cIsnsClientStart.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrTypeNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsTcpPortNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsUdpPortNotifctn"))
)
if mibBuilder.loadTexts:
    cIsnsClientStart.setStatus(
        "current"
    )

cIsnsClientInitalRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0, 4)
)
cIsnsClientInitalRegistration.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrTypeNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsTcpPortNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsUdpPortNotifctn"))
)
if mibBuilder.loadTexts:
    cIsnsClientInitalRegistration.setStatus(
        "current"
    )

cIsnsClientLostConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0, 5)
)
cIsnsClientLostConnection.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrTypeNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsAddrNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsTcpPortNotifctn"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsUdpPortNotifctn"))
)
if mibBuilder.loadTexts:
    cIsnsClientLostConnection.setStatus(
        "current"
    )

cIsnsClientNoServerDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 1, 3, 0, 6)
)
cIsnsClientNoServerDiscovered.setObjects(
    ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsInstInfo")
)
if mibBuilder.loadTexts:
    cIsnsClientNoServerDiscovered.setStatus(
        "current"
    )


# Notifications groups

cIsnsServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 12)
)
cIsnsServerNotificationGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsServerStart"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsServerShutdown"))
)
if mibBuilder.loadTexts:
    cIsnsServerNotificationGroup.setStatus(
        "current"
    )

cIsnsClientNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 1, 13)
)
cIsnsClientNotificationGroup.setObjects(
      *(("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClientStart"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClientInitalRegistration"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClientLostConnection"),
        ("CISCO-IETF-ISNS-MGMT-MIB", "cIsnsClientNoServerDiscovered"))
)
if mibBuilder.loadTexts:
    cIsnsClientNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cIsnsIscsiServerComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cIsnsIscsiServerComplianceV1.setStatus(
        "current"
    )

cIsnsIscsiClientComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cIsnsIscsiClientComplianceV1.setStatus(
        "current"
    )

cIsnsIfcpServerComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cIsnsIfcpServerComplianceV1.setStatus(
        "current"
    )

cIsnsIfcpClientComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cIsnsIfcpClientComplianceV1.setStatus(
        "current"
    )

cIsnsServerCountStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 116, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cIsnsServerCountStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-ISNS-MGMT-MIB",
    **{"CIsnsDiscoveryDomainSetId": CIsnsDiscoveryDomainSetId,
       "CIsnsDdsStatusId": CIsnsDdsStatusId,
       "CIsnsDiscoveryDomainId": CIsnsDiscoveryDomainId,
       "CIsnsDdFeatureBitmapId": CIsnsDdFeatureBitmapId,
       "CIsnsDdDdsModificationBitmap": CIsnsDdDdsModificationBitmap,
       "CIsnsEntityIndexId": CIsnsEntityIndexId,
       "CIsnsEntityProtocolId": CIsnsEntityProtocolId,
       "CIsnsPortalGroupIndexId": CIsnsPortalGroupIndexId,
       "CIsnsPortalIndexId": CIsnsPortalIndexId,
       "CIsnsPortalPortId": CIsnsPortalPortId,
       "CIsnsPortalPortTypeId": CIsnsPortalPortTypeId,
       "CIsnsPortalGroupTagIdOrZero": CIsnsPortalGroupTagIdOrZero,
       "CIsnsPortalSecurityBitmapId": CIsnsPortalSecurityBitmapId,
       "CIsnsNodeIndexId": CIsnsNodeIndexId,
       "CIsnsNodeIndexIdOrZero": CIsnsNodeIndexIdOrZero,
       "CIsnsNodeTypeId": CIsnsNodeTypeId,
       "CIsnsCosBitmapId": CIsnsCosBitmapId,
       "CIsnsScnBitmapId": CIsnsScnBitmapId,
       "CIsnsSrvrDscvryMthdId": CIsnsSrvrDscvryMthdId,
       "ciscoIetfIsnsMgmtMIB": ciscoIetfIsnsMgmtMIB,
       "cIsnsObj": cIsnsObj,
       "cIsnsSrvrInfo": cIsnsSrvrInfo,
       "cIsnsSrvrInstTable": cIsnsSrvrInstTable,
       "cIsnsSrvrInstEntry": cIsnsSrvrInstEntry,
       "cIsnsSrvrInstIndex": cIsnsSrvrInstIndex,
       "cIsnsSrvrInstName": cIsnsSrvrInstName,
       "cIsnsSrvrInstIsnsVersion": cIsnsSrvrInstIsnsVersion,
       "cIsnsSrvrInstDescription": cIsnsSrvrInstDescription,
       "cIsnsSrvrInstAddressType": cIsnsSrvrInstAddressType,
       "cIsnsSrvrInstAddress": cIsnsSrvrInstAddress,
       "cIsnsSrvrInstTcpPort": cIsnsSrvrInstTcpPort,
       "cIsnsSrvrInstUdpPort": cIsnsSrvrInstUdpPort,
       "cIsnsSrvrInstUptime": cIsnsSrvrInstUptime,
       "cIsnsSrvrInstRole": cIsnsSrvrInstRole,
       "cIsnsSrvrInstDiscMthdsEnbld": cIsnsSrvrInstDiscMthdsEnbld,
       "cIsnsSrvrInstDiscMcGrpType": cIsnsSrvrInstDiscMcGrpType,
       "cIsnsSrvrInstDiscMcGrp": cIsnsSrvrInstDiscMcGrp,
       "cIsnsSrvrInstEsiNonRespThrshld": cIsnsSrvrInstEsiNonRespThrshld,
       "cIsnsSrvrInstCntrlNodeAuth": cIsnsSrvrInstCntrlNodeAuth,
       "cIsnsSrvrInstEnblCntrlNdeMgtScn": cIsnsSrvrInstEnblCntrlNdeMgtScn,
       "cIsnsSrvrInstDfltDdDdsStatus": cIsnsSrvrInstDfltDdDdsStatus,
       "cIsnsSrvrInstUpdateDdDdsSpprtd": cIsnsSrvrInstUpdateDdDdsSpprtd,
       "cIsnsSrvrInstUpdateDdDdsEnbld": cIsnsSrvrInstUpdateDdDdsEnbld,
       "cIsnsNumObjTable": cIsnsNumObjTable,
       "cIsnsNumObjEntry": cIsnsNumObjEntry,
       "cIsnsNumDds": cIsnsNumDds,
       "cIsnsNumDd": cIsnsNumDd,
       "cIsnsNumEntities": cIsnsNumEntities,
       "cIsnsNumPortals": cIsnsNumPortals,
       "cIsnsNumPortalGroups": cIsnsNumPortalGroups,
       "cIsnsNumIscsiNodes": cIsnsNumIscsiNodes,
       "cIsnsNumFcPorts": cIsnsNumFcPorts,
       "cIsnsNumFcNodes": cIsnsNumFcNodes,
       "cIsnsNextIdxTable": cIsnsNextIdxTable,
       "cIsnsNextIdxEntry": cIsnsNextIdxEntry,
       "cIsnsNextIdxDds": cIsnsNextIdxDds,
       "cIsnsNextIdxDd": cIsnsNextIdxDd,
       "cIsnsNextIdxUnregIscsiNodeInDd": cIsnsNextIdxUnregIscsiNodeInDd,
       "cIsnsNextIdxUnregPortalInDd": cIsnsNextIdxUnregPortalInDd,
       "cIsnsCntlNodeInfo": cIsnsCntlNodeInfo,
       "cIsnsCntlNodeIscsiTable": cIsnsCntlNodeIscsiTable,
       "cIsnsCntlNodeIscsiEntry": cIsnsCntlNodeIscsiEntry,
       "cIsnsCntlNodeIscsiNodeIdx": cIsnsCntlNodeIscsiNodeIdx,
       "cIsnsCntlNodeIscsiNodeName": cIsnsCntlNodeIscsiNodeName,
       "cIsnsCntlNodeIscsiRowStatus": cIsnsCntlNodeIscsiRowStatus,
       "cIsnsCntlNodeFcPortTable": cIsnsCntlNodeFcPortTable,
       "cIsnsCntlNodeFcPortEntry": cIsnsCntlNodeFcPortEntry,
       "cIsnsCntlNodeFcPortName": cIsnsCntlNodeFcPortName,
       "cIsnsCntlNodeFcPortRowStatus": cIsnsCntlNodeFcPortRowStatus,
       "cIsnsDdsInfo": cIsnsDdsInfo,
       "cIsnsDdsTable": cIsnsDdsTable,
       "cIsnsDdsEntry": cIsnsDdsEntry,
       "cIsnsDdsId": cIsnsDdsId,
       "cIsnsDdsSymbolicName": cIsnsDdsSymbolicName,
       "cIsnsDdsStatus": cIsnsDdsStatus,
       "cIsnsDdsRowStatus": cIsnsDdsRowStatus,
       "cIsnsDdsMemberTable": cIsnsDdsMemberTable,
       "cIsnsDdsMemberEntry": cIsnsDdsMemberEntry,
       "cIsnsDdsMemberRowStatus": cIsnsDdsMemberRowStatus,
       "cIsnsDdInfo": cIsnsDdInfo,
       "cIsnsDdTable": cIsnsDdTable,
       "cIsnsDdEntry": cIsnsDdEntry,
       "cIsnsDdId": cIsnsDdId,
       "cIsnsDdSymbolicName": cIsnsDdSymbolicName,
       "cIsnsDdFeatures": cIsnsDdFeatures,
       "cIsnsDdRowStatus": cIsnsDdRowStatus,
       "cIsnsDdIscsiMemberTable": cIsnsDdIscsiMemberTable,
       "cIsnsDdIscsiMemberEntry": cIsnsDdIscsiMemberEntry,
       "cIsnsDdMemberIscsiIdx": cIsnsDdMemberIscsiIdx,
       "cIsnsDdMemberIscsiName": cIsnsDdMemberIscsiName,
       "cIsnsDdMemberIsRegistered": cIsnsDdMemberIsRegistered,
       "cIsnsDdMemberRowStatus": cIsnsDdMemberRowStatus,
       "cIsnsDdPortalMemberTable": cIsnsDdPortalMemberTable,
       "cIsnsDdPortalMemberEntry": cIsnsDdPortalMemberEntry,
       "cIsnsDdMemberPortalIdx": cIsnsDdMemberPortalIdx,
       "cIsnsDdMemberPortalAddrType": cIsnsDdMemberPortalAddrType,
       "cIsnsDdMemberPortalAddr": cIsnsDdMemberPortalAddr,
       "cIsnsDdMemberPortalPortType": cIsnsDdMemberPortalPortType,
       "cIsnsDdMemberPortalPort": cIsnsDdMemberPortalPort,
       "cIsnsDdMemberPortalIsRegistered": cIsnsDdMemberPortalIsRegistered,
       "cIsnsDdMemberPortalRowStatus": cIsnsDdMemberPortalRowStatus,
       "cIsnsDdFcPortMemberTable": cIsnsDdFcPortMemberTable,
       "cIsnsDdFcPortMemberEntry": cIsnsDdFcPortMemberEntry,
       "cIsnsDdMemberFcPortName": cIsnsDdMemberFcPortName,
       "cIsnsDdMemberFcIsRegistered": cIsnsDdMemberFcIsRegistered,
       "cIsnsDdMemberFcRowStatus": cIsnsDdMemberFcRowStatus,
       "cIsnsReg": cIsnsReg,
       "cIsnsRegEntityInfo": cIsnsRegEntityInfo,
       "cIsnsRegEntityTable": cIsnsRegEntityTable,
       "cIsnsRegEntityEntry": cIsnsRegEntityEntry,
       "cIsnsRegEntityIdx": cIsnsRegEntityIdx,
       "cIsnsRegEntityEID": cIsnsRegEntityEID,
       "cIsnsRegEntityProtocol": cIsnsRegEntityProtocol,
       "cIsnsRegEntityMgtAddrType": cIsnsRegEntityMgtAddrType,
       "cIsnsRegEntityMgtAddr": cIsnsRegEntityMgtAddr,
       "cIsnsRegEntityTimestamp": cIsnsRegEntityTimestamp,
       "cIsnsRegEntityVersionMin": cIsnsRegEntityVersionMin,
       "cIsnsRegEntityVersionMax": cIsnsRegEntityVersionMax,
       "cIsnsRegEntityRegPeriod": cIsnsRegEntityRegPeriod,
       "cIsnsRegEntityNumObjTable": cIsnsRegEntityNumObjTable,
       "cIsnsRegEntityNumObjEntry": cIsnsRegEntityNumObjEntry,
       "cIsnsRegEntityInfoNumPortals": cIsnsRegEntityInfoNumPortals,
       "cIsnsRegEntityInfoNumPortalGroup": cIsnsRegEntityInfoNumPortalGroup,
       "cIsnsRegEntityInfoNumIscsiNodes": cIsnsRegEntityInfoNumIscsiNodes,
       "cIsnsRegEntityInfoNumFcPorts": cIsnsRegEntityInfoNumFcPorts,
       "cIsnsRegEntityInfoNumFcNodes": cIsnsRegEntityInfoNumFcNodes,
       "cIsnsRegPortalInfo": cIsnsRegPortalInfo,
       "cIsnsRegPortalTable": cIsnsRegPortalTable,
       "cIsnsRegPortalEntry": cIsnsRegPortalEntry,
       "cIsnsRegPortalPrtlIdx": cIsnsRegPortalPrtlIdx,
       "cIsnsRegPortalAddrType": cIsnsRegPortalAddrType,
       "cIsnsRegPortalAddr": cIsnsRegPortalAddr,
       "cIsnsRegPortalPortType": cIsnsRegPortalPortType,
       "cIsnsRegPortalPort": cIsnsRegPortalPort,
       "cIsnsRegPortalSymName": cIsnsRegPortalSymName,
       "cIsnsRegPortalEsiInterval": cIsnsRegPortalEsiInterval,
       "cIsnsRegPortalEsiPortType": cIsnsRegPortalEsiPortType,
       "cIsnsRegPortalEsiPort": cIsnsRegPortalEsiPort,
       "cIsnsRegPortalScnPortType": cIsnsRegPortalScnPortType,
       "cIsnsRegPortalScnPort": cIsnsRegPortalScnPort,
       "cIsnsRegPortalSecurityInfo": cIsnsRegPortalSecurityInfo,
       "cIsnsRegPortalGroupInfo": cIsnsRegPortalGroupInfo,
       "cIsnsRegPgTable": cIsnsRegPgTable,
       "cIsnsRegPgEntry": cIsnsRegPgEntry,
       "cIsnsRegPgIdx": cIsnsRegPgIdx,
       "cIsnsRegPgIscsiNodeIdx": cIsnsRegPgIscsiNodeIdx,
       "cIsnsRegPgIscsiName": cIsnsRegPgIscsiName,
       "cIsnsRegPgPortalPrtlIdx": cIsnsRegPgPortalPrtlIdx,
       "cIsnsRegPgPortalAddrType": cIsnsRegPgPortalAddrType,
       "cIsnsRegPgPortalAddr": cIsnsRegPgPortalAddr,
       "cIsnsRegPgPortalPortType": cIsnsRegPgPortalPortType,
       "cIsnsRegPgPortalPort": cIsnsRegPgPortalPort,
       "cIsnsRegPgPGT": cIsnsRegPgPGT,
       "cIsnsRegIscsiNodeInfo": cIsnsRegIscsiNodeInfo,
       "cIsnsRegIscsiNodeTable": cIsnsRegIscsiNodeTable,
       "cIsnsRegIscsiNodeEntry": cIsnsRegIscsiNodeEntry,
       "cIsnsRegIscsiNodeIdx": cIsnsRegIscsiNodeIdx,
       "cIsnsRegIscsiNodeName": cIsnsRegIscsiNodeName,
       "cIsnsRegIscsiNodeType": cIsnsRegIscsiNodeType,
       "cIsnsRegIscsiNodeAlias": cIsnsRegIscsiNodeAlias,
       "cIsnsRegIscsiNodeScnBitmap": cIsnsRegIscsiNodeScnBitmap,
       "cIsnsRegIscsiNodeWwnToken": cIsnsRegIscsiNodeWwnToken,
       "cIsnsRegIscsiNodeAuthMethod": cIsnsRegIscsiNodeAuthMethod,
       "cIsnsRegFcPortInfo": cIsnsRegFcPortInfo,
       "cIsnsRegFcPortTable": cIsnsRegFcPortTable,
       "cIsnsRegFcPortEntry": cIsnsRegFcPortEntry,
       "cIsnsRegFcPortWwpn": cIsnsRegFcPortWwpn,
       "cIsnsRegFcPortID": cIsnsRegFcPortID,
       "cIsnsRegFcPortType": cIsnsRegFcPortType,
       "cIsnsRegFcPortSymName": cIsnsRegFcPortSymName,
       "cIsnsRegFcPortFabricPortWwn": cIsnsRegFcPortFabricPortWwn,
       "cIsnsRegFcPortHA": cIsnsRegFcPortHA,
       "cIsnsRegFcPortAddrType": cIsnsRegFcPortAddrType,
       "cIsnsRegFcPortAddr": cIsnsRegFcPortAddr,
       "cIsnsRegFcPortFcCos": cIsnsRegFcPortFcCos,
       "cIsnsRegFcPortFc4Types": cIsnsRegFcPortFc4Types,
       "cIsnsRegFcPortFc4Descr": cIsnsRegFcPortFc4Descr,
       "cIsnsRegFcPortFc4Features": cIsnsRegFcPortFc4Features,
       "cIsnsRegFcPortScnBitmap": cIsnsRegFcPortScnBitmap,
       "cIsnsRegFcPortRole": cIsnsRegFcPortRole,
       "cIsnsRegFcPortFcNodeWwn": cIsnsRegFcPortFcNodeWwn,
       "cIsnsRegFcPortPpnWwn": cIsnsRegFcPortPpnWwn,
       "cIsnsRegFcNodeInfo": cIsnsRegFcNodeInfo,
       "cIsnsRegFcNodeTable": cIsnsRegFcNodeTable,
       "cIsnsRegFcNodeEntry": cIsnsRegFcNodeEntry,
       "cIsnsRegFcNodeWwn": cIsnsRegFcNodeWwn,
       "cIsnsRegFcNodeSymName": cIsnsRegFcNodeSymName,
       "cIsnsRegFcNodeAddrType": cIsnsRegFcNodeAddrType,
       "cIsnsRegFcNodeAddr": cIsnsRegFcNodeAddr,
       "cIsnsRegFcNodeIPA": cIsnsRegFcNodeIPA,
       "cIsnsRegFcNodeProxyIscsiName": cIsnsRegFcNodeProxyIscsiName,
       "cIsnsRegFcNodeInfoTable": cIsnsRegFcNodeInfoTable,
       "cIsnsRegFcNodeInfoEntry": cIsnsRegFcNodeInfoEntry,
       "cIsnsRegFcNodeInfoNumFcPorts": cIsnsRegFcNodeInfoNumFcPorts,
       "cIsnsRegFcNodeFcPortTable": cIsnsRegFcNodeFcPortTable,
       "cIsnsRegFcNodeFcPortEntry": cIsnsRegFcNodeFcPortEntry,
       "cIsnsRegFcNodeFcPortEntityEIdx": cIsnsRegFcNodeFcPortEntityEIdx,
       "cIsnsClntInfo": cIsnsClntInfo,
       "cIsnsClntInstTable": cIsnsClntInstTable,
       "cIsnsClntInstEntry": cIsnsClntInstEntry,
       "cIsnsClntInstIndex": cIsnsClntInstIndex,
       "cIsnsClntInstName": cIsnsClntInstName,
       "cIsnsClntInstIsnspVersion": cIsnsClntInstIsnspVersion,
       "cIsnsClntInstDescription": cIsnsClntInstDescription,
       "cIsnsClntInstAddressType": cIsnsClntInstAddressType,
       "cIsnsClntInstAddress": cIsnsClntInstAddress,
       "cIsnsClntInstTcpPort": cIsnsClntInstTcpPort,
       "cIsnsClntInstUdpPort": cIsnsClntInstUdpPort,
       "cIsnsClntInstUptime": cIsnsClntInstUptime,
       "cIsnsClntInstAvailDiscMthd": cIsnsClntInstAvailDiscMthd,
       "cIsnsClntInstPrmryDiscMthd": cIsnsClntInstPrmryDiscMthd,
       "cIsnsClntInstScndryDiscMthd": cIsnsClntInstScndryDiscMthd,
       "cIsnsClntInstDiscMcGrpType": cIsnsClntInstDiscMcGrpType,
       "cIsnsClntInstDiscMcGrp": cIsnsClntInstDiscMcGrp,
       "cIsnsClntCfgSrvrTable": cIsnsClntCfgSrvrTable,
       "cIsnsClntCfgSrvrEntry": cIsnsClntCfgSrvrEntry,
       "cIsnsClntCfgSrvrIndex": cIsnsClntCfgSrvrIndex,
       "cIsnsClntCfgSrvrAddrType": cIsnsClntCfgSrvrAddrType,
       "cIsnsClntCfgSrvrAddr": cIsnsClntCfgSrvrAddr,
       "cIsnsClntCfgSrvrTcpPort": cIsnsClntCfgSrvrTcpPort,
       "cIsnsClntCfgSrvrUdpPort": cIsnsClntCfgSrvrUdpPort,
       "cIsnsClntCfgSrvrPriority": cIsnsClntCfgSrvrPriority,
       "cIsnsClntCfgSrvrTimeout": cIsnsClntCfgSrvrTimeout,
       "cIsnsClntCfgSrvrRetries": cIsnsClntCfgSrvrRetries,
       "cIsnsClntCfgSrvrRowStatus": cIsnsClntCfgSrvrRowStatus,
       "cIsnsClntDscvrdSrvrTable": cIsnsClntDscvrdSrvrTable,
       "cIsnsClntDscvrdSrvrEntry": cIsnsClntDscvrdSrvrEntry,
       "cIsnsClntDscvrdSrvrIndex": cIsnsClntDscvrdSrvrIndex,
       "cIsnsClntDscvrdSrvrAddrType": cIsnsClntDscvrdSrvrAddrType,
       "cIsnsClntDscvrdSrvrAddr": cIsnsClntDscvrdSrvrAddr,
       "cIsnsClntDscvrdSrvrTcpPort": cIsnsClntDscvrdSrvrTcpPort,
       "cIsnsClntDscvrdSrvrUdpPort": cIsnsClntDscvrdSrvrUdpPort,
       "cIsnsClntDscvrdSrvrIsnsVersion": cIsnsClntDscvrdSrvrIsnsVersion,
       "cIsnsClntDscvrdSrvrDiscMthd": cIsnsClntDscvrdSrvrDiscMthd,
       "cIsnsClntRegEntityTable": cIsnsClntRegEntityTable,
       "cIsnsClntRegEntityEntry": cIsnsClntRegEntityEntry,
       "cIsnsClntRegEntityIdx": cIsnsClntRegEntityIdx,
       "cIsnsClntRegEntityEID": cIsnsClntRegEntityEID,
       "cIsnsClntRegEntityProtocol": cIsnsClntRegEntityProtocol,
       "cIsnsNotification": cIsnsNotification,
       "cIsnsNotificationPrefix": cIsnsNotificationPrefix,
       "cIsnsServerStart": cIsnsServerStart,
       "cIsnsServerShutdown": cIsnsServerShutdown,
       "cIsnsClientStart": cIsnsClientStart,
       "cIsnsClientInitalRegistration": cIsnsClientInitalRegistration,
       "cIsnsClientLostConnection": cIsnsClientLostConnection,
       "cIsnsClientNoServerDiscovered": cIsnsClientNoServerDiscovered,
       "cIsnsNotificationInfo": cIsnsNotificationInfo,
       "cIsnsInstInfo": cIsnsInstInfo,
       "cIsnsAddrTypeNotifctn": cIsnsAddrTypeNotifctn,
       "cIsnsAddrNotifctn": cIsnsAddrNotifctn,
       "cIsnsTcpPortNotifctn": cIsnsTcpPortNotifctn,
       "cIsnsUdpPortNotifctn": cIsnsUdpPortNotifctn,
       "cIsnsConformance": cIsnsConformance,
       "cIsnsGroups": cIsnsGroups,
       "cIsnsServerAttributesGroup": cIsnsServerAttributesGroup,
       "cIsnsServerNumObjGroup": cIsnsServerNumObjGroup,
       "cIsnsServerNextIdxGroup": cIsnsServerNextIdxGroup,
       "cIsnsServerIscsiCntlNodeGroup": cIsnsServerIscsiCntlNodeGroup,
       "cIsnsServerIfcpCntlNodeGroup": cIsnsServerIfcpCntlNodeGroup,
       "cIsnsServerIscsiDdsDdObjGroup": cIsnsServerIscsiDdsDdObjGroup,
       "cIsnsServerIfcpDdsDdObjGroup": cIsnsServerIfcpDdsDdObjGroup,
       "cIsnsServerRegIscsiObjGroup": cIsnsServerRegIscsiObjGroup,
       "cIsnsServerRegIfcpObjGroup": cIsnsServerRegIfcpObjGroup,
       "cIsnsClientAttributesGroup": cIsnsClientAttributesGroup,
       "cIsnsNotificationObjGroup": cIsnsNotificationObjGroup,
       "cIsnsServerNotificationGroup": cIsnsServerNotificationGroup,
       "cIsnsClientNotificationGroup": cIsnsClientNotificationGroup,
       "cIsnsCompliances": cIsnsCompliances,
       "cIsnsIscsiServerComplianceV1": cIsnsIscsiServerComplianceV1,
       "cIsnsIscsiClientComplianceV1": cIsnsIscsiClientComplianceV1,
       "cIsnsIfcpServerComplianceV1": cIsnsIfcpServerComplianceV1,
       "cIsnsIfcpClientComplianceV1": cIsnsIfcpClientComplianceV1,
       "cIsnsServerCountStatsCompliance": cIsnsServerCountStatsCompliance}
)
