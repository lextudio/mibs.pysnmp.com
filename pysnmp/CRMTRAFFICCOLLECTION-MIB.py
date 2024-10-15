# SNMP MIB module (CRMTRAFFICCOLLECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CRMTRAFFICCOLLECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Ntt_ObjectIdentity = ObjectIdentity
ntt = _Ntt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2)
)
_Ba3000_ObjectIdentity = ObjectIdentity
ba3000 = _Ba3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8)
)
_CrmCommon_ObjectIdentity = ObjectIdentity
crmCommon = _CrmCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1)
)
_CrmTraffic_ObjectIdentity = ObjectIdentity
crmTraffic = _CrmTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4)
)
_CrmTrCollectIntervalTable_Object = MibTable
crmTrCollectIntervalTable = _CrmTrCollectIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    crmTrCollectIntervalTable.setStatus("mandatory")
_CrmTrCollectIntervalEntry_Object = MibTableRow
crmTrCollectIntervalEntry = _CrmTrCollectIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1)
)
crmTrCollectIntervalEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectIntervalType"),
)
if mibBuilder.loadTexts:
    crmTrCollectIntervalEntry.setStatus("mandatory")


class _CrmTrCollectIntervalType_Type(Integer32):
    """Custom type crmTrCollectIntervalType based on Integer32"""
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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectIntervalType_Type.__name__ = "Integer32"
_CrmTrCollectIntervalType_Object = MibTableColumn
crmTrCollectIntervalType = _CrmTrCollectIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 1),
    _CrmTrCollectIntervalType_Type()
)
crmTrCollectIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectIntervalType.setStatus("mandatory")


class _CrmTrCollectIntervalTime_Type(Integer32):
    """Custom type crmTrCollectIntervalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalTime_Type.__name__ = "Integer32"
_CrmTrCollectIntervalTime_Object = MibTableColumn
crmTrCollectIntervalTime = _CrmTrCollectIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 2),
    _CrmTrCollectIntervalTime_Type()
)
crmTrCollectIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectIntervalTime.setStatus("mandatory")


class _CrmTrCollectIntervalIfPoints_Type(Integer32):
    """Custom type crmTrCollectIntervalIfPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalIfPoints_Type.__name__ = "Integer32"
_CrmTrCollectIntervalIfPoints_Object = MibTableColumn
crmTrCollectIntervalIfPoints = _CrmTrCollectIntervalIfPoints_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 3),
    _CrmTrCollectIntervalIfPoints_Type()
)
crmTrCollectIntervalIfPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIntervalIfPoints.setStatus("mandatory")


class _CrmTrCollectIntervalVpcPoints_Type(Integer32):
    """Custom type crmTrCollectIntervalVpcPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalVpcPoints_Type.__name__ = "Integer32"
_CrmTrCollectIntervalVpcPoints_Object = MibTableColumn
crmTrCollectIntervalVpcPoints = _CrmTrCollectIntervalVpcPoints_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 4),
    _CrmTrCollectIntervalVpcPoints_Type()
)
crmTrCollectIntervalVpcPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIntervalVpcPoints.setStatus("mandatory")


class _CrmTrCollectIntervalVccPoints_Type(Integer32):
    """Custom type crmTrCollectIntervalVccPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalVccPoints_Type.__name__ = "Integer32"
_CrmTrCollectIntervalVccPoints_Object = MibTableColumn
crmTrCollectIntervalVccPoints = _CrmTrCollectIntervalVccPoints_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 5),
    _CrmTrCollectIntervalVccPoints_Type()
)
crmTrCollectIntervalVccPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIntervalVccPoints.setStatus("mandatory")


class _CrmTrCollectIntervalPriPoints_Type(Integer32):
    """Custom type crmTrCollectIntervalPriPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalPriPoints_Type.__name__ = "Integer32"
_CrmTrCollectIntervalPriPoints_Object = MibTableColumn
crmTrCollectIntervalPriPoints = _CrmTrCollectIntervalPriPoints_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 6),
    _CrmTrCollectIntervalPriPoints_Type()
)
crmTrCollectIntervalPriPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIntervalPriPoints.setStatus("mandatory")


class _CrmTrCollectIntervalFrIfPoints_Type(Integer32):
    """Custom type crmTrCollectIntervalFrIfPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalFrIfPoints_Type.__name__ = "Integer32"
_CrmTrCollectIntervalFrIfPoints_Object = MibTableColumn
crmTrCollectIntervalFrIfPoints = _CrmTrCollectIntervalFrIfPoints_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 7),
    _CrmTrCollectIntervalFrIfPoints_Type()
)
crmTrCollectIntervalFrIfPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIntervalFrIfPoints.setStatus("mandatory")


class _CrmTrCollectIntervalFrDlciPoints_Type(Integer32):
    """Custom type crmTrCollectIntervalFrDlciPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIntervalFrDlciPoints_Type.__name__ = "Integer32"
_CrmTrCollectIntervalFrDlciPoints_Object = MibTableColumn
crmTrCollectIntervalFrDlciPoints = _CrmTrCollectIntervalFrDlciPoints_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 1, 1, 8),
    _CrmTrCollectIntervalFrDlciPoints_Type()
)
crmTrCollectIntervalFrDlciPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIntervalFrDlciPoints.setStatus("mandatory")
_CrmTrCollectIfTable_Object = MibTable
crmTrCollectIfTable = _CrmTrCollectIfTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    crmTrCollectIfTable.setStatus("mandatory")
_CrmTrCollectIfEntry_Object = MibTableRow
crmTrCollectIfEntry = _CrmTrCollectIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1)
)
crmTrCollectIfEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectIfIfIndex"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectIfDirect"),
)
if mibBuilder.loadTexts:
    crmTrCollectIfEntry.setStatus("mandatory")


class _CrmTrCollectIfIfIndex_Type(Integer32):
    """Custom type crmTrCollectIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIfIfIndex_Type.__name__ = "Integer32"
_CrmTrCollectIfIfIndex_Object = MibTableColumn
crmTrCollectIfIfIndex = _CrmTrCollectIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 1),
    _CrmTrCollectIfIfIndex_Type()
)
crmTrCollectIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectIfIfIndex.setStatus("mandatory")


class _CrmTrCollectIfDirect_Type(Integer32):
    """Custom type crmTrCollectIfDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 1),
          ("sw2ifp", 2))
    )


_CrmTrCollectIfDirect_Type.__name__ = "Integer32"
_CrmTrCollectIfDirect_Object = MibTableColumn
crmTrCollectIfDirect = _CrmTrCollectIfDirect_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 2),
    _CrmTrCollectIfDirect_Type()
)
crmTrCollectIfDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectIfDirect.setStatus("mandatory")


class _CrmTrCollectIfInterval_Type(Integer32):
    """Custom type crmTrCollectIfInterval based on Integer32"""
    defaultValue = 1

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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectIfInterval_Type.__name__ = "Integer32"
_CrmTrCollectIfInterval_Object = MibTableColumn
crmTrCollectIfInterval = _CrmTrCollectIfInterval_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 3),
    _CrmTrCollectIfInterval_Type()
)
crmTrCollectIfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectIfInterval.setStatus("mandatory")
_CrmTrCollectIfThroughCells_Type = Counter32
_CrmTrCollectIfThroughCells_Object = MibTableColumn
crmTrCollectIfThroughCells = _CrmTrCollectIfThroughCells_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 4),
    _CrmTrCollectIfThroughCells_Type()
)
crmTrCollectIfThroughCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfThroughCells.setStatus("mandatory")


class _CrmTrCollectIfDisRes1_Type(Integer32):
    """Custom type crmTrCollectIfDisRes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes1_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes1_Object = MibTableColumn
crmTrCollectIfDisRes1 = _CrmTrCollectIfDisRes1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 5),
    _CrmTrCollectIfDisRes1_Type()
)
crmTrCollectIfDisRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes1.setStatus("mandatory")
_CrmTrCollectIfDisCells1_Type = Counter32
_CrmTrCollectIfDisCells1_Object = MibTableColumn
crmTrCollectIfDisCells1 = _CrmTrCollectIfDisCells1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 6),
    _CrmTrCollectIfDisCells1_Type()
)
crmTrCollectIfDisCells1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells1.setStatus("mandatory")


class _CrmTrCollectIfDisRes2_Type(Integer32):
    """Custom type crmTrCollectIfDisRes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes2_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes2_Object = MibTableColumn
crmTrCollectIfDisRes2 = _CrmTrCollectIfDisRes2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 7),
    _CrmTrCollectIfDisRes2_Type()
)
crmTrCollectIfDisRes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes2.setStatus("mandatory")
_CrmTrCollectIfDisCells2_Type = Counter32
_CrmTrCollectIfDisCells2_Object = MibTableColumn
crmTrCollectIfDisCells2 = _CrmTrCollectIfDisCells2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 8),
    _CrmTrCollectIfDisCells2_Type()
)
crmTrCollectIfDisCells2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells2.setStatus("mandatory")


class _CrmTrCollectIfDisRes3_Type(Integer32):
    """Custom type crmTrCollectIfDisRes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes3_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes3_Object = MibTableColumn
crmTrCollectIfDisRes3 = _CrmTrCollectIfDisRes3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 9),
    _CrmTrCollectIfDisRes3_Type()
)
crmTrCollectIfDisRes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes3.setStatus("mandatory")
_CrmTrCollectIfDisCells3_Type = Counter32
_CrmTrCollectIfDisCells3_Object = MibTableColumn
crmTrCollectIfDisCells3 = _CrmTrCollectIfDisCells3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 10),
    _CrmTrCollectIfDisCells3_Type()
)
crmTrCollectIfDisCells3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells3.setStatus("mandatory")


class _CrmTrCollectIfDisRes4_Type(Integer32):
    """Custom type crmTrCollectIfDisRes4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes4_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes4_Object = MibTableColumn
crmTrCollectIfDisRes4 = _CrmTrCollectIfDisRes4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 11),
    _CrmTrCollectIfDisRes4_Type()
)
crmTrCollectIfDisRes4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes4.setStatus("mandatory")
_CrmTrCollectIfDisCells4_Type = Counter32
_CrmTrCollectIfDisCells4_Object = MibTableColumn
crmTrCollectIfDisCells4 = _CrmTrCollectIfDisCells4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 12),
    _CrmTrCollectIfDisCells4_Type()
)
crmTrCollectIfDisCells4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells4.setStatus("mandatory")


class _CrmTrCollectIfDisRes5_Type(Integer32):
    """Custom type crmTrCollectIfDisRes5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes5_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes5_Object = MibTableColumn
crmTrCollectIfDisRes5 = _CrmTrCollectIfDisRes5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 13),
    _CrmTrCollectIfDisRes5_Type()
)
crmTrCollectIfDisRes5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes5.setStatus("mandatory")
_CrmTrCollectIfDisCells5_Type = Counter32
_CrmTrCollectIfDisCells5_Object = MibTableColumn
crmTrCollectIfDisCells5 = _CrmTrCollectIfDisCells5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 14),
    _CrmTrCollectIfDisCells5_Type()
)
crmTrCollectIfDisCells5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells5.setStatus("mandatory")


class _CrmTrCollectIfDisRes6_Type(Integer32):
    """Custom type crmTrCollectIfDisRes6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes6_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes6_Object = MibTableColumn
crmTrCollectIfDisRes6 = _CrmTrCollectIfDisRes6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 15),
    _CrmTrCollectIfDisRes6_Type()
)
crmTrCollectIfDisRes6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes6.setStatus("mandatory")
_CrmTrCollectIfDisCells6_Type = Counter32
_CrmTrCollectIfDisCells6_Object = MibTableColumn
crmTrCollectIfDisCells6 = _CrmTrCollectIfDisCells6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 16),
    _CrmTrCollectIfDisCells6_Type()
)
crmTrCollectIfDisCells6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells6.setStatus("mandatory")


class _CrmTrCollectIfDisRes7_Type(Integer32):
    """Custom type crmTrCollectIfDisRes7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes7_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes7_Object = MibTableColumn
crmTrCollectIfDisRes7 = _CrmTrCollectIfDisRes7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 17),
    _CrmTrCollectIfDisRes7_Type()
)
crmTrCollectIfDisRes7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes7.setStatus("mandatory")
_CrmTrCollectIfDisCells7_Type = Counter32
_CrmTrCollectIfDisCells7_Object = MibTableColumn
crmTrCollectIfDisCells7 = _CrmTrCollectIfDisCells7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 18),
    _CrmTrCollectIfDisCells7_Type()
)
crmTrCollectIfDisCells7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells7.setStatus("mandatory")


class _CrmTrCollectIfDisRes8_Type(Integer32):
    """Custom type crmTrCollectIfDisRes8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectIfDisRes8_Type.__name__ = "Integer32"
_CrmTrCollectIfDisRes8_Object = MibTableColumn
crmTrCollectIfDisRes8 = _CrmTrCollectIfDisRes8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 19),
    _CrmTrCollectIfDisRes8_Type()
)
crmTrCollectIfDisRes8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisRes8.setStatus("mandatory")
_CrmTrCollectIfDisCells8_Type = Counter32
_CrmTrCollectIfDisCells8_Object = MibTableColumn
crmTrCollectIfDisCells8 = _CrmTrCollectIfDisCells8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 20),
    _CrmTrCollectIfDisCells8_Type()
)
crmTrCollectIfDisCells8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectIfDisCells8.setStatus("mandatory")
_CrmTrCollectIfStartTime_Type = DateAndTime
_CrmTrCollectIfStartTime_Object = MibTableColumn
crmTrCollectIfStartTime = _CrmTrCollectIfStartTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 21),
    _CrmTrCollectIfStartTime_Type()
)
crmTrCollectIfStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectIfStartTime.setStatus("mandatory")
_CrmTrCollectIfEndTime_Type = DateAndTime
_CrmTrCollectIfEndTime_Object = MibTableColumn
crmTrCollectIfEndTime = _CrmTrCollectIfEndTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 22),
    _CrmTrCollectIfEndTime_Type()
)
crmTrCollectIfEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectIfEndTime.setStatus("mandatory")


class _CrmTrCollectIfRowStatus_Type(Integer32):
    """Custom type crmTrCollectIfRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectIfRowStatus_Type.__name__ = "Integer32"
_CrmTrCollectIfRowStatus_Object = MibTableColumn
crmTrCollectIfRowStatus = _CrmTrCollectIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 2, 1, 23),
    _CrmTrCollectIfRowStatus_Type()
)
crmTrCollectIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectIfRowStatus.setStatus("mandatory")
_CrmTrCollectVpcTable_Object = MibTable
crmTrCollectVpcTable = _CrmTrCollectVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3)
)
if mibBuilder.loadTexts:
    crmTrCollectVpcTable.setStatus("mandatory")
_CrmTrCollectVpcEntry_Object = MibTableRow
crmTrCollectVpcEntry = _CrmTrCollectVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1)
)
crmTrCollectVpcEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVpcIfIndex"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVpcVpi"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVpcDirect"),
)
if mibBuilder.loadTexts:
    crmTrCollectVpcEntry.setStatus("mandatory")


class _CrmTrCollectVpcIfIndex_Type(Integer32):
    """Custom type crmTrCollectVpcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVpcIfIndex_Type.__name__ = "Integer32"
_CrmTrCollectVpcIfIndex_Object = MibTableColumn
crmTrCollectVpcIfIndex = _CrmTrCollectVpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 1),
    _CrmTrCollectVpcIfIndex_Type()
)
crmTrCollectVpcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVpcIfIndex.setStatus("mandatory")


class _CrmTrCollectVpcVpi_Type(Integer32):
    """Custom type crmTrCollectVpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVpcVpi_Type.__name__ = "Integer32"
_CrmTrCollectVpcVpi_Object = MibTableColumn
crmTrCollectVpcVpi = _CrmTrCollectVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 2),
    _CrmTrCollectVpcVpi_Type()
)
crmTrCollectVpcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVpcVpi.setStatus("mandatory")


class _CrmTrCollectVpcDirect_Type(Integer32):
    """Custom type crmTrCollectVpcDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 1),
          ("sw2ifp", 2))
    )


_CrmTrCollectVpcDirect_Type.__name__ = "Integer32"
_CrmTrCollectVpcDirect_Object = MibTableColumn
crmTrCollectVpcDirect = _CrmTrCollectVpcDirect_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 3),
    _CrmTrCollectVpcDirect_Type()
)
crmTrCollectVpcDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVpcDirect.setStatus("mandatory")


class _CrmTrCollectVpcInterval_Type(Integer32):
    """Custom type crmTrCollectVpcInterval based on Integer32"""
    defaultValue = 1

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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectVpcInterval_Type.__name__ = "Integer32"
_CrmTrCollectVpcInterval_Object = MibTableColumn
crmTrCollectVpcInterval = _CrmTrCollectVpcInterval_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 4),
    _CrmTrCollectVpcInterval_Type()
)
crmTrCollectVpcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVpcInterval.setStatus("mandatory")
_CrmTrCollectVpcThroughCells_Type = Counter32
_CrmTrCollectVpcThroughCells_Object = MibTableColumn
crmTrCollectVpcThroughCells = _CrmTrCollectVpcThroughCells_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 5),
    _CrmTrCollectVpcThroughCells_Type()
)
crmTrCollectVpcThroughCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcThroughCells.setStatus("mandatory")


class _CrmTrCollectVpcDisRes1_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes1_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes1_Object = MibTableColumn
crmTrCollectVpcDisRes1 = _CrmTrCollectVpcDisRes1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 6),
    _CrmTrCollectVpcDisRes1_Type()
)
crmTrCollectVpcDisRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes1.setStatus("mandatory")
_CrmTrCollectVpcDisCells1_Type = Counter32
_CrmTrCollectVpcDisCells1_Object = MibTableColumn
crmTrCollectVpcDisCells1 = _CrmTrCollectVpcDisCells1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 7),
    _CrmTrCollectVpcDisCells1_Type()
)
crmTrCollectVpcDisCells1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells1.setStatus("mandatory")


class _CrmTrCollectVpcDisRes2_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes2_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes2_Object = MibTableColumn
crmTrCollectVpcDisRes2 = _CrmTrCollectVpcDisRes2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 8),
    _CrmTrCollectVpcDisRes2_Type()
)
crmTrCollectVpcDisRes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes2.setStatus("mandatory")
_CrmTrCollectVpcDisCells2_Type = Counter32
_CrmTrCollectVpcDisCells2_Object = MibTableColumn
crmTrCollectVpcDisCells2 = _CrmTrCollectVpcDisCells2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 9),
    _CrmTrCollectVpcDisCells2_Type()
)
crmTrCollectVpcDisCells2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells2.setStatus("mandatory")


class _CrmTrCollectVpcDisRes3_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes3_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes3_Object = MibTableColumn
crmTrCollectVpcDisRes3 = _CrmTrCollectVpcDisRes3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 10),
    _CrmTrCollectVpcDisRes3_Type()
)
crmTrCollectVpcDisRes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes3.setStatus("mandatory")
_CrmTrCollectVpcDisCells3_Type = Counter32
_CrmTrCollectVpcDisCells3_Object = MibTableColumn
crmTrCollectVpcDisCells3 = _CrmTrCollectVpcDisCells3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 11),
    _CrmTrCollectVpcDisCells3_Type()
)
crmTrCollectVpcDisCells3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells3.setStatus("mandatory")


class _CrmTrCollectVpcDisRes4_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes4_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes4_Object = MibTableColumn
crmTrCollectVpcDisRes4 = _CrmTrCollectVpcDisRes4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 12),
    _CrmTrCollectVpcDisRes4_Type()
)
crmTrCollectVpcDisRes4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes4.setStatus("mandatory")
_CrmTrCollectVpcDisCells4_Type = Counter32
_CrmTrCollectVpcDisCells4_Object = MibTableColumn
crmTrCollectVpcDisCells4 = _CrmTrCollectVpcDisCells4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 13),
    _CrmTrCollectVpcDisCells4_Type()
)
crmTrCollectVpcDisCells4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells4.setStatus("mandatory")


class _CrmTrCollectVpcDisRes5_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes5_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes5_Object = MibTableColumn
crmTrCollectVpcDisRes5 = _CrmTrCollectVpcDisRes5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 14),
    _CrmTrCollectVpcDisRes5_Type()
)
crmTrCollectVpcDisRes5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes5.setStatus("mandatory")
_CrmTrCollectVpcDisCells5_Type = Counter32
_CrmTrCollectVpcDisCells5_Object = MibTableColumn
crmTrCollectVpcDisCells5 = _CrmTrCollectVpcDisCells5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 15),
    _CrmTrCollectVpcDisCells5_Type()
)
crmTrCollectVpcDisCells5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells5.setStatus("mandatory")


class _CrmTrCollectVpcDisRes6_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes6_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes6_Object = MibTableColumn
crmTrCollectVpcDisRes6 = _CrmTrCollectVpcDisRes6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 16),
    _CrmTrCollectVpcDisRes6_Type()
)
crmTrCollectVpcDisRes6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes6.setStatus("mandatory")
_CrmTrCollectVpcDisCells6_Type = Counter32
_CrmTrCollectVpcDisCells6_Object = MibTableColumn
crmTrCollectVpcDisCells6 = _CrmTrCollectVpcDisCells6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 17),
    _CrmTrCollectVpcDisCells6_Type()
)
crmTrCollectVpcDisCells6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells6.setStatus("mandatory")


class _CrmTrCollectVpcDisRes7_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes7_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes7_Object = MibTableColumn
crmTrCollectVpcDisRes7 = _CrmTrCollectVpcDisRes7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 18),
    _CrmTrCollectVpcDisRes7_Type()
)
crmTrCollectVpcDisRes7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes7.setStatus("mandatory")
_CrmTrCollectVpcDisCells7_Type = Counter32
_CrmTrCollectVpcDisCells7_Object = MibTableColumn
crmTrCollectVpcDisCells7 = _CrmTrCollectVpcDisCells7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 19),
    _CrmTrCollectVpcDisCells7_Type()
)
crmTrCollectVpcDisCells7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells7.setStatus("mandatory")


class _CrmTrCollectVpcDisRes8_Type(Integer32):
    """Custom type crmTrCollectVpcDisRes8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVpcDisRes8_Type.__name__ = "Integer32"
_CrmTrCollectVpcDisRes8_Object = MibTableColumn
crmTrCollectVpcDisRes8 = _CrmTrCollectVpcDisRes8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 20),
    _CrmTrCollectVpcDisRes8_Type()
)
crmTrCollectVpcDisRes8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisRes8.setStatus("mandatory")
_CrmTrCollectVpcDisCells8_Type = Counter32
_CrmTrCollectVpcDisCells8_Object = MibTableColumn
crmTrCollectVpcDisCells8 = _CrmTrCollectVpcDisCells8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 21),
    _CrmTrCollectVpcDisCells8_Type()
)
crmTrCollectVpcDisCells8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVpcDisCells8.setStatus("mandatory")
_CrmTrCollectVpcStartTime_Type = DateAndTime
_CrmTrCollectVpcStartTime_Object = MibTableColumn
crmTrCollectVpcStartTime = _CrmTrCollectVpcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 22),
    _CrmTrCollectVpcStartTime_Type()
)
crmTrCollectVpcStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVpcStartTime.setStatus("mandatory")
_CrmTrCollectVpcEndTime_Type = DateAndTime
_CrmTrCollectVpcEndTime_Object = MibTableColumn
crmTrCollectVpcEndTime = _CrmTrCollectVpcEndTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 23),
    _CrmTrCollectVpcEndTime_Type()
)
crmTrCollectVpcEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVpcEndTime.setStatus("mandatory")


class _CrmTrCollectVpcRowStatus_Type(Integer32):
    """Custom type crmTrCollectVpcRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVpcRowStatus_Type.__name__ = "Integer32"
_CrmTrCollectVpcRowStatus_Object = MibTableColumn
crmTrCollectVpcRowStatus = _CrmTrCollectVpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 3, 1, 24),
    _CrmTrCollectVpcRowStatus_Type()
)
crmTrCollectVpcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVpcRowStatus.setStatus("mandatory")
_CrmTrCollectVccTable_Object = MibTable
crmTrCollectVccTable = _CrmTrCollectVccTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4)
)
if mibBuilder.loadTexts:
    crmTrCollectVccTable.setStatus("mandatory")
_CrmTrCollectVccEntry_Object = MibTableRow
crmTrCollectVccEntry = _CrmTrCollectVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1)
)
crmTrCollectVccEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVccIfIndex"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVccVpi"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVccVci"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectVccDirect"),
)
if mibBuilder.loadTexts:
    crmTrCollectVccEntry.setStatus("mandatory")


class _CrmTrCollectVccIfIndex_Type(Integer32):
    """Custom type crmTrCollectVccIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVccIfIndex_Type.__name__ = "Integer32"
_CrmTrCollectVccIfIndex_Object = MibTableColumn
crmTrCollectVccIfIndex = _CrmTrCollectVccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 1),
    _CrmTrCollectVccIfIndex_Type()
)
crmTrCollectVccIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVccIfIndex.setStatus("mandatory")


class _CrmTrCollectVccVpi_Type(Integer32):
    """Custom type crmTrCollectVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVccVpi_Type.__name__ = "Integer32"
_CrmTrCollectVccVpi_Object = MibTableColumn
crmTrCollectVccVpi = _CrmTrCollectVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 2),
    _CrmTrCollectVccVpi_Type()
)
crmTrCollectVccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVccVpi.setStatus("mandatory")


class _CrmTrCollectVccVci_Type(Integer32):
    """Custom type crmTrCollectVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVccVci_Type.__name__ = "Integer32"
_CrmTrCollectVccVci_Object = MibTableColumn
crmTrCollectVccVci = _CrmTrCollectVccVci_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 3),
    _CrmTrCollectVccVci_Type()
)
crmTrCollectVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVccVci.setStatus("mandatory")


class _CrmTrCollectVccDirect_Type(Integer32):
    """Custom type crmTrCollectVccDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 2),
          ("sw2ifp", 1))
    )


_CrmTrCollectVccDirect_Type.__name__ = "Integer32"
_CrmTrCollectVccDirect_Object = MibTableColumn
crmTrCollectVccDirect = _CrmTrCollectVccDirect_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 4),
    _CrmTrCollectVccDirect_Type()
)
crmTrCollectVccDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectVccDirect.setStatus("mandatory")


class _CrmTrCollectVccInterval_Type(Integer32):
    """Custom type crmTrCollectVccInterval based on Integer32"""
    defaultValue = 1

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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectVccInterval_Type.__name__ = "Integer32"
_CrmTrCollectVccInterval_Object = MibTableColumn
crmTrCollectVccInterval = _CrmTrCollectVccInterval_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 5),
    _CrmTrCollectVccInterval_Type()
)
crmTrCollectVccInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVccInterval.setStatus("mandatory")
_CrmTrCollectVccThroughCells_Type = Counter32
_CrmTrCollectVccThroughCells_Object = MibTableColumn
crmTrCollectVccThroughCells = _CrmTrCollectVccThroughCells_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 6),
    _CrmTrCollectVccThroughCells_Type()
)
crmTrCollectVccThroughCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccThroughCells.setStatus("mandatory")


class _CrmTrCollectVccDisRes1_Type(Integer32):
    """Custom type crmTrCollectVccDisRes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes1_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes1_Object = MibTableColumn
crmTrCollectVccDisRes1 = _CrmTrCollectVccDisRes1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 7),
    _CrmTrCollectVccDisRes1_Type()
)
crmTrCollectVccDisRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes1.setStatus("mandatory")
_CrmTrCollectVccDisCells1_Type = Counter32
_CrmTrCollectVccDisCells1_Object = MibTableColumn
crmTrCollectVccDisCells1 = _CrmTrCollectVccDisCells1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 8),
    _CrmTrCollectVccDisCells1_Type()
)
crmTrCollectVccDisCells1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells1.setStatus("mandatory")


class _CrmTrCollectVccDisRes2_Type(Integer32):
    """Custom type crmTrCollectVccDisRes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes2_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes2_Object = MibTableColumn
crmTrCollectVccDisRes2 = _CrmTrCollectVccDisRes2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 9),
    _CrmTrCollectVccDisRes2_Type()
)
crmTrCollectVccDisRes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes2.setStatus("mandatory")
_CrmTrCollectVccDisCells2_Type = Counter32
_CrmTrCollectVccDisCells2_Object = MibTableColumn
crmTrCollectVccDisCells2 = _CrmTrCollectVccDisCells2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 10),
    _CrmTrCollectVccDisCells2_Type()
)
crmTrCollectVccDisCells2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells2.setStatus("mandatory")


class _CrmTrCollectVccDisRes3_Type(Integer32):
    """Custom type crmTrCollectVccDisRes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes3_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes3_Object = MibTableColumn
crmTrCollectVccDisRes3 = _CrmTrCollectVccDisRes3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 11),
    _CrmTrCollectVccDisRes3_Type()
)
crmTrCollectVccDisRes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes3.setStatus("mandatory")
_CrmTrCollectVccDisCells3_Type = Counter32
_CrmTrCollectVccDisCells3_Object = MibTableColumn
crmTrCollectVccDisCells3 = _CrmTrCollectVccDisCells3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 12),
    _CrmTrCollectVccDisCells3_Type()
)
crmTrCollectVccDisCells3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells3.setStatus("mandatory")


class _CrmTrCollectVccDisRes4_Type(Integer32):
    """Custom type crmTrCollectVccDisRes4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes4_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes4_Object = MibTableColumn
crmTrCollectVccDisRes4 = _CrmTrCollectVccDisRes4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 13),
    _CrmTrCollectVccDisRes4_Type()
)
crmTrCollectVccDisRes4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes4.setStatus("mandatory")
_CrmTrCollectVccDisCells4_Type = Counter32
_CrmTrCollectVccDisCells4_Object = MibTableColumn
crmTrCollectVccDisCells4 = _CrmTrCollectVccDisCells4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 14),
    _CrmTrCollectVccDisCells4_Type()
)
crmTrCollectVccDisCells4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells4.setStatus("mandatory")


class _CrmTrCollectVccDisRes5_Type(Integer32):
    """Custom type crmTrCollectVccDisRes5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes5_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes5_Object = MibTableColumn
crmTrCollectVccDisRes5 = _CrmTrCollectVccDisRes5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 15),
    _CrmTrCollectVccDisRes5_Type()
)
crmTrCollectVccDisRes5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes5.setStatus("mandatory")
_CrmTrCollectVccDisCells5_Type = Counter32
_CrmTrCollectVccDisCells5_Object = MibTableColumn
crmTrCollectVccDisCells5 = _CrmTrCollectVccDisCells5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 16),
    _CrmTrCollectVccDisCells5_Type()
)
crmTrCollectVccDisCells5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells5.setStatus("mandatory")


class _CrmTrCollectVccDisRes6_Type(Integer32):
    """Custom type crmTrCollectVccDisRes6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes6_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes6_Object = MibTableColumn
crmTrCollectVccDisRes6 = _CrmTrCollectVccDisRes6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 17),
    _CrmTrCollectVccDisRes6_Type()
)
crmTrCollectVccDisRes6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes6.setStatus("mandatory")
_CrmTrCollectVccDisCells6_Type = Counter32
_CrmTrCollectVccDisCells6_Object = MibTableColumn
crmTrCollectVccDisCells6 = _CrmTrCollectVccDisCells6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 18),
    _CrmTrCollectVccDisCells6_Type()
)
crmTrCollectVccDisCells6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells6.setStatus("mandatory")


class _CrmTrCollectVccDisRes7_Type(Integer32):
    """Custom type crmTrCollectVccDisRes7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes7_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes7_Object = MibTableColumn
crmTrCollectVccDisRes7 = _CrmTrCollectVccDisRes7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 19),
    _CrmTrCollectVccDisRes7_Type()
)
crmTrCollectVccDisRes7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes7.setStatus("mandatory")
_CrmTrCollectVccDisCells7_Type = Counter32
_CrmTrCollectVccDisCells7_Object = MibTableColumn
crmTrCollectVccDisCells7 = _CrmTrCollectVccDisCells7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 20),
    _CrmTrCollectVccDisCells7_Type()
)
crmTrCollectVccDisCells7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells7.setStatus("mandatory")


class _CrmTrCollectVccDisRes8_Type(Integer32):
    """Custom type crmTrCollectVccDisRes8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectVccDisRes8_Type.__name__ = "Integer32"
_CrmTrCollectVccDisRes8_Object = MibTableColumn
crmTrCollectVccDisRes8 = _CrmTrCollectVccDisRes8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 21),
    _CrmTrCollectVccDisRes8_Type()
)
crmTrCollectVccDisRes8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisRes8.setStatus("mandatory")
_CrmTrCollectVccDisCells8_Type = Counter32
_CrmTrCollectVccDisCells8_Object = MibTableColumn
crmTrCollectVccDisCells8 = _CrmTrCollectVccDisCells8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 22),
    _CrmTrCollectVccDisCells8_Type()
)
crmTrCollectVccDisCells8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectVccDisCells8.setStatus("mandatory")
_CrmTrCollectVccStartTime_Type = DateAndTime
_CrmTrCollectVccStartTime_Object = MibTableColumn
crmTrCollectVccStartTime = _CrmTrCollectVccStartTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 23),
    _CrmTrCollectVccStartTime_Type()
)
crmTrCollectVccStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVccStartTime.setStatus("mandatory")
_CrmTrCollectVccEndTime_Type = DateAndTime
_CrmTrCollectVccEndTime_Object = MibTableColumn
crmTrCollectVccEndTime = _CrmTrCollectVccEndTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 24),
    _CrmTrCollectVccEndTime_Type()
)
crmTrCollectVccEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVccEndTime.setStatus("mandatory")


class _CrmTrCollectVccRowStatus_Type(Integer32):
    """Custom type crmTrCollectVccRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectVccRowStatus_Type.__name__ = "Integer32"
_CrmTrCollectVccRowStatus_Object = MibTableColumn
crmTrCollectVccRowStatus = _CrmTrCollectVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 4, 1, 25),
    _CrmTrCollectVccRowStatus_Type()
)
crmTrCollectVccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectVccRowStatus.setStatus("mandatory")
_CrmTrCollectPriTable_Object = MibTable
crmTrCollectPriTable = _CrmTrCollectPriTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5)
)
if mibBuilder.loadTexts:
    crmTrCollectPriTable.setStatus("mandatory")
_CrmTrCollectPriEntry_Object = MibTableRow
crmTrCollectPriEntry = _CrmTrCollectPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1)
)
crmTrCollectPriEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectPriIfIndex"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectPriClass"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectPriDirect"),
)
if mibBuilder.loadTexts:
    crmTrCollectPriEntry.setStatus("mandatory")


class _CrmTrCollectPriIfIndex_Type(Integer32):
    """Custom type crmTrCollectPriIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectPriIfIndex_Type.__name__ = "Integer32"
_CrmTrCollectPriIfIndex_Object = MibTableColumn
crmTrCollectPriIfIndex = _CrmTrCollectPriIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 1),
    _CrmTrCollectPriIfIndex_Type()
)
crmTrCollectPriIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectPriIfIndex.setStatus("mandatory")
_CrmTrCollectPriClass_Type = Integer32
_CrmTrCollectPriClass_Object = MibTableColumn
crmTrCollectPriClass = _CrmTrCollectPriClass_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 2),
    _CrmTrCollectPriClass_Type()
)
crmTrCollectPriClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectPriClass.setStatus("mandatory")


class _CrmTrCollectPriDirect_Type(Integer32):
    """Custom type crmTrCollectPriDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 2),
          ("sw2ifp", 1))
    )


_CrmTrCollectPriDirect_Type.__name__ = "Integer32"
_CrmTrCollectPriDirect_Object = MibTableColumn
crmTrCollectPriDirect = _CrmTrCollectPriDirect_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 3),
    _CrmTrCollectPriDirect_Type()
)
crmTrCollectPriDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectPriDirect.setStatus("mandatory")


class _CrmTrCollectPriInterval_Type(Integer32):
    """Custom type crmTrCollectPriInterval based on Integer32"""
    defaultValue = 1

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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectPriInterval_Type.__name__ = "Integer32"
_CrmTrCollectPriInterval_Object = MibTableColumn
crmTrCollectPriInterval = _CrmTrCollectPriInterval_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 4),
    _CrmTrCollectPriInterval_Type()
)
crmTrCollectPriInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectPriInterval.setStatus("mandatory")
_CrmTrCollectPriThroughCells_Type = Counter32
_CrmTrCollectPriThroughCells_Object = MibTableColumn
crmTrCollectPriThroughCells = _CrmTrCollectPriThroughCells_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 5),
    _CrmTrCollectPriThroughCells_Type()
)
crmTrCollectPriThroughCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriThroughCells.setStatus("mandatory")


class _CrmTrCollectPriDisRes1_Type(Integer32):
    """Custom type crmTrCollectPriDisRes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes1_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes1_Object = MibTableColumn
crmTrCollectPriDisRes1 = _CrmTrCollectPriDisRes1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 6),
    _CrmTrCollectPriDisRes1_Type()
)
crmTrCollectPriDisRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes1.setStatus("mandatory")
_CrmTrCollectPriDisCells1_Type = Counter32
_CrmTrCollectPriDisCells1_Object = MibTableColumn
crmTrCollectPriDisCells1 = _CrmTrCollectPriDisCells1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 7),
    _CrmTrCollectPriDisCells1_Type()
)
crmTrCollectPriDisCells1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells1.setStatus("mandatory")


class _CrmTrCollectPriDisRes2_Type(Integer32):
    """Custom type crmTrCollectPriDisRes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes2_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes2_Object = MibTableColumn
crmTrCollectPriDisRes2 = _CrmTrCollectPriDisRes2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 8),
    _CrmTrCollectPriDisRes2_Type()
)
crmTrCollectPriDisRes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes2.setStatus("mandatory")
_CrmTrCollectPriDisCells2_Type = Counter32
_CrmTrCollectPriDisCells2_Object = MibTableColumn
crmTrCollectPriDisCells2 = _CrmTrCollectPriDisCells2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 9),
    _CrmTrCollectPriDisCells2_Type()
)
crmTrCollectPriDisCells2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells2.setStatus("mandatory")


class _CrmTrCollectPriDisRes3_Type(Integer32):
    """Custom type crmTrCollectPriDisRes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes3_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes3_Object = MibTableColumn
crmTrCollectPriDisRes3 = _CrmTrCollectPriDisRes3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 10),
    _CrmTrCollectPriDisRes3_Type()
)
crmTrCollectPriDisRes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes3.setStatus("mandatory")
_CrmTrCollectPriDisCells3_Type = Counter32
_CrmTrCollectPriDisCells3_Object = MibTableColumn
crmTrCollectPriDisCells3 = _CrmTrCollectPriDisCells3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 11),
    _CrmTrCollectPriDisCells3_Type()
)
crmTrCollectPriDisCells3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells3.setStatus("mandatory")


class _CrmTrCollectPriDisRes4_Type(Integer32):
    """Custom type crmTrCollectPriDisRes4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes4_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes4_Object = MibTableColumn
crmTrCollectPriDisRes4 = _CrmTrCollectPriDisRes4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 12),
    _CrmTrCollectPriDisRes4_Type()
)
crmTrCollectPriDisRes4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes4.setStatus("mandatory")
_CrmTrCollectPriDisCells4_Type = Counter32
_CrmTrCollectPriDisCells4_Object = MibTableColumn
crmTrCollectPriDisCells4 = _CrmTrCollectPriDisCells4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 13),
    _CrmTrCollectPriDisCells4_Type()
)
crmTrCollectPriDisCells4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells4.setStatus("mandatory")


class _CrmTrCollectPriDisRes5_Type(Integer32):
    """Custom type crmTrCollectPriDisRes5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes5_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes5_Object = MibTableColumn
crmTrCollectPriDisRes5 = _CrmTrCollectPriDisRes5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 14),
    _CrmTrCollectPriDisRes5_Type()
)
crmTrCollectPriDisRes5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes5.setStatus("mandatory")
_CrmTrCollectPriDisCells5_Type = Counter32
_CrmTrCollectPriDisCells5_Object = MibTableColumn
crmTrCollectPriDisCells5 = _CrmTrCollectPriDisCells5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 15),
    _CrmTrCollectPriDisCells5_Type()
)
crmTrCollectPriDisCells5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells5.setStatus("mandatory")


class _CrmTrCollectPriDisRes6_Type(Integer32):
    """Custom type crmTrCollectPriDisRes6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes6_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes6_Object = MibTableColumn
crmTrCollectPriDisRes6 = _CrmTrCollectPriDisRes6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 16),
    _CrmTrCollectPriDisRes6_Type()
)
crmTrCollectPriDisRes6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes6.setStatus("mandatory")
_CrmTrCollectPriDisCells6_Type = Counter32
_CrmTrCollectPriDisCells6_Object = MibTableColumn
crmTrCollectPriDisCells6 = _CrmTrCollectPriDisCells6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 17),
    _CrmTrCollectPriDisCells6_Type()
)
crmTrCollectPriDisCells6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells6.setStatus("mandatory")


class _CrmTrCollectPriDisRes7_Type(Integer32):
    """Custom type crmTrCollectPriDisRes7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes7_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes7_Object = MibTableColumn
crmTrCollectPriDisRes7 = _CrmTrCollectPriDisRes7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 18),
    _CrmTrCollectPriDisRes7_Type()
)
crmTrCollectPriDisRes7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes7.setStatus("mandatory")
_CrmTrCollectPriDisCells7_Type = Counter32
_CrmTrCollectPriDisCells7_Object = MibTableColumn
crmTrCollectPriDisCells7 = _CrmTrCollectPriDisCells7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 19),
    _CrmTrCollectPriDisCells7_Type()
)
crmTrCollectPriDisCells7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells7.setStatus("mandatory")


class _CrmTrCollectPriDisRes8_Type(Integer32):
    """Custom type crmTrCollectPriDisRes8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectPriDisRes8_Type.__name__ = "Integer32"
_CrmTrCollectPriDisRes8_Object = MibTableColumn
crmTrCollectPriDisRes8 = _CrmTrCollectPriDisRes8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 20),
    _CrmTrCollectPriDisRes8_Type()
)
crmTrCollectPriDisRes8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisRes8.setStatus("mandatory")
_CrmTrCollectPriDisCells8_Type = Counter32
_CrmTrCollectPriDisCells8_Object = MibTableColumn
crmTrCollectPriDisCells8 = _CrmTrCollectPriDisCells8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 21),
    _CrmTrCollectPriDisCells8_Type()
)
crmTrCollectPriDisCells8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectPriDisCells8.setStatus("mandatory")
_CrmTrCollectPriStartTime_Type = DateAndTime
_CrmTrCollectPriStartTime_Object = MibTableColumn
crmTrCollectPriStartTime = _CrmTrCollectPriStartTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 22),
    _CrmTrCollectPriStartTime_Type()
)
crmTrCollectPriStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectPriStartTime.setStatus("mandatory")
_CrmTrCollectPriEndTime_Type = DateAndTime
_CrmTrCollectPriEndTime_Object = MibTableColumn
crmTrCollectPriEndTime = _CrmTrCollectPriEndTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 23),
    _CrmTrCollectPriEndTime_Type()
)
crmTrCollectPriEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectPriEndTime.setStatus("mandatory")


class _CrmTrCollectPriRowStatus_Type(Integer32):
    """Custom type crmTrCollectPriRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectPriRowStatus_Type.__name__ = "Integer32"
_CrmTrCollectPriRowStatus_Object = MibTableColumn
crmTrCollectPriRowStatus = _CrmTrCollectPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 5, 1, 24),
    _CrmTrCollectPriRowStatus_Type()
)
crmTrCollectPriRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectPriRowStatus.setStatus("mandatory")
_CrmTrCollectFrIfTable_Object = MibTable
crmTrCollectFrIfTable = _CrmTrCollectFrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6)
)
if mibBuilder.loadTexts:
    crmTrCollectFrIfTable.setStatus("mandatory")
_CrmTrCollectFrIfEntry_Object = MibTableRow
crmTrCollectFrIfEntry = _CrmTrCollectFrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1)
)
crmTrCollectFrIfEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectFrIfIfIndex"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectFrIfDirect"),
)
if mibBuilder.loadTexts:
    crmTrCollectFrIfEntry.setStatus("mandatory")


class _CrmTrCollectFrIfIfIndex_Type(Integer32):
    """Custom type crmTrCollectFrIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectFrIfIfIndex_Type.__name__ = "Integer32"
_CrmTrCollectFrIfIfIndex_Object = MibTableColumn
crmTrCollectFrIfIfIndex = _CrmTrCollectFrIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 1),
    _CrmTrCollectFrIfIfIndex_Type()
)
crmTrCollectFrIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectFrIfIfIndex.setStatus("mandatory")


class _CrmTrCollectFrIfDirect_Type(Integer32):
    """Custom type crmTrCollectFrIfDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 2),
          ("sw2ifp", 1))
    )


_CrmTrCollectFrIfDirect_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDirect_Object = MibTableColumn
crmTrCollectFrIfDirect = _CrmTrCollectFrIfDirect_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 2),
    _CrmTrCollectFrIfDirect_Type()
)
crmTrCollectFrIfDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDirect.setStatus("mandatory")


class _CrmTrCollectFrIfInterval_Type(Integer32):
    """Custom type crmTrCollectFrIfInterval based on Integer32"""
    defaultValue = 1

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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectFrIfInterval_Type.__name__ = "Integer32"
_CrmTrCollectFrIfInterval_Object = MibTableColumn
crmTrCollectFrIfInterval = _CrmTrCollectFrIfInterval_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 3),
    _CrmTrCollectFrIfInterval_Type()
)
crmTrCollectFrIfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrIfInterval.setStatus("mandatory")
_CrmTrCollectFrIfThroughCells_Type = Counter32
_CrmTrCollectFrIfThroughCells_Object = MibTableColumn
crmTrCollectFrIfThroughCells = _CrmTrCollectFrIfThroughCells_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 4),
    _CrmTrCollectFrIfThroughCells_Type()
)
crmTrCollectFrIfThroughCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfThroughCells.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes1_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes1_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes1_Object = MibTableColumn
crmTrCollectFrIfDisRes1 = _CrmTrCollectFrIfDisRes1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 5),
    _CrmTrCollectFrIfDisRes1_Type()
)
crmTrCollectFrIfDisRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes1.setStatus("mandatory")
_CrmTrCollectFrIfDisCells1_Type = Counter32
_CrmTrCollectFrIfDisCells1_Object = MibTableColumn
crmTrCollectFrIfDisCells1 = _CrmTrCollectFrIfDisCells1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 6),
    _CrmTrCollectFrIfDisCells1_Type()
)
crmTrCollectFrIfDisCells1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells1.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes2_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes2_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes2_Object = MibTableColumn
crmTrCollectFrIfDisRes2 = _CrmTrCollectFrIfDisRes2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 7),
    _CrmTrCollectFrIfDisRes2_Type()
)
crmTrCollectFrIfDisRes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes2.setStatus("mandatory")
_CrmTrCollectFrIfDisCells2_Type = Counter32
_CrmTrCollectFrIfDisCells2_Object = MibTableColumn
crmTrCollectFrIfDisCells2 = _CrmTrCollectFrIfDisCells2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 8),
    _CrmTrCollectFrIfDisCells2_Type()
)
crmTrCollectFrIfDisCells2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells2.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes3_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes3_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes3_Object = MibTableColumn
crmTrCollectFrIfDisRes3 = _CrmTrCollectFrIfDisRes3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 9),
    _CrmTrCollectFrIfDisRes3_Type()
)
crmTrCollectFrIfDisRes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes3.setStatus("mandatory")
_CrmTrCollectFrIfDisCells3_Type = Counter32
_CrmTrCollectFrIfDisCells3_Object = MibTableColumn
crmTrCollectFrIfDisCells3 = _CrmTrCollectFrIfDisCells3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 10),
    _CrmTrCollectFrIfDisCells3_Type()
)
crmTrCollectFrIfDisCells3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells3.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes4_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes4_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes4_Object = MibTableColumn
crmTrCollectFrIfDisRes4 = _CrmTrCollectFrIfDisRes4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 11),
    _CrmTrCollectFrIfDisRes4_Type()
)
crmTrCollectFrIfDisRes4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes4.setStatus("mandatory")
_CrmTrCollectFrIfDisCells4_Type = Counter32
_CrmTrCollectFrIfDisCells4_Object = MibTableColumn
crmTrCollectFrIfDisCells4 = _CrmTrCollectFrIfDisCells4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 12),
    _CrmTrCollectFrIfDisCells4_Type()
)
crmTrCollectFrIfDisCells4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells4.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes5_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes5_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes5_Object = MibTableColumn
crmTrCollectFrIfDisRes5 = _CrmTrCollectFrIfDisRes5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 13),
    _CrmTrCollectFrIfDisRes5_Type()
)
crmTrCollectFrIfDisRes5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes5.setStatus("mandatory")
_CrmTrCollectFrIfDisCells5_Type = Counter32
_CrmTrCollectFrIfDisCells5_Object = MibTableColumn
crmTrCollectFrIfDisCells5 = _CrmTrCollectFrIfDisCells5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 14),
    _CrmTrCollectFrIfDisCells5_Type()
)
crmTrCollectFrIfDisCells5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells5.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes6_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes6_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes6_Object = MibTableColumn
crmTrCollectFrIfDisRes6 = _CrmTrCollectFrIfDisRes6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 15),
    _CrmTrCollectFrIfDisRes6_Type()
)
crmTrCollectFrIfDisRes6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes6.setStatus("mandatory")
_CrmTrCollectFrIfDisCells6_Type = Counter32
_CrmTrCollectFrIfDisCells6_Object = MibTableColumn
crmTrCollectFrIfDisCells6 = _CrmTrCollectFrIfDisCells6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 16),
    _CrmTrCollectFrIfDisCells6_Type()
)
crmTrCollectFrIfDisCells6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells6.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes7_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes7_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes7_Object = MibTableColumn
crmTrCollectFrIfDisRes7 = _CrmTrCollectFrIfDisRes7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 17),
    _CrmTrCollectFrIfDisRes7_Type()
)
crmTrCollectFrIfDisRes7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes7.setStatus("mandatory")
_CrmTrCollectFrIfDisCells7_Type = Counter32
_CrmTrCollectFrIfDisCells7_Object = MibTableColumn
crmTrCollectFrIfDisCells7 = _CrmTrCollectFrIfDisCells7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 18),
    _CrmTrCollectFrIfDisCells7_Type()
)
crmTrCollectFrIfDisCells7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells7.setStatus("mandatory")


class _CrmTrCollectFrIfDisRes8_Type(Integer32):
    """Custom type crmTrCollectFrIfDisRes8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrIfDisRes8_Type.__name__ = "Integer32"
_CrmTrCollectFrIfDisRes8_Object = MibTableColumn
crmTrCollectFrIfDisRes8 = _CrmTrCollectFrIfDisRes8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 19),
    _CrmTrCollectFrIfDisRes8_Type()
)
crmTrCollectFrIfDisRes8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisRes8.setStatus("mandatory")
_CrmTrCollectFrIfDisCells8_Type = Counter32
_CrmTrCollectFrIfDisCells8_Object = MibTableColumn
crmTrCollectFrIfDisCells8 = _CrmTrCollectFrIfDisCells8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 20),
    _CrmTrCollectFrIfDisCells8_Type()
)
crmTrCollectFrIfDisCells8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrIfDisCells8.setStatus("mandatory")
_CrmTrCollectFrIfStartTime_Type = DateAndTime
_CrmTrCollectFrIfStartTime_Object = MibTableColumn
crmTrCollectFrIfStartTime = _CrmTrCollectFrIfStartTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 21),
    _CrmTrCollectFrIfStartTime_Type()
)
crmTrCollectFrIfStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrIfStartTime.setStatus("mandatory")
_CrmTrCollectFrIfEndTime_Type = DateAndTime
_CrmTrCollectFrIfEndTime_Object = MibTableColumn
crmTrCollectFrIfEndTime = _CrmTrCollectFrIfEndTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 22),
    _CrmTrCollectFrIfEndTime_Type()
)
crmTrCollectFrIfEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrIfEndTime.setStatus("mandatory")


class _CrmTrCollectFrIfRowStatus_Type(Integer32):
    """Custom type crmTrCollectFrIfRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectFrIfRowStatus_Type.__name__ = "Integer32"
_CrmTrCollectFrIfRowStatus_Object = MibTableColumn
crmTrCollectFrIfRowStatus = _CrmTrCollectFrIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 6, 1, 23),
    _CrmTrCollectFrIfRowStatus_Type()
)
crmTrCollectFrIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrIfRowStatus.setStatus("mandatory")
_CrmTrCollectFrDlciTable_Object = MibTable
crmTrCollectFrDlciTable = _CrmTrCollectFrDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7)
)
if mibBuilder.loadTexts:
    crmTrCollectFrDlciTable.setStatus("mandatory")
_CrmTrCollectFrDlciEntry_Object = MibTableRow
crmTrCollectFrDlciEntry = _CrmTrCollectFrDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1)
)
crmTrCollectFrDlciEntry.setIndexNames(
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectFrDlciIfIndex"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectFrDlciDlci"),
    (0, "CRMTRAFFICCOLLECTION-MIB", "crmTrCollectFrDlciDirect"),
)
if mibBuilder.loadTexts:
    crmTrCollectFrDlciEntry.setStatus("mandatory")


class _CrmTrCollectFrDlciIfIndex_Type(Integer32):
    """Custom type crmTrCollectFrDlciIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectFrDlciIfIndex_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciIfIndex_Object = MibTableColumn
crmTrCollectFrDlciIfIndex = _CrmTrCollectFrDlciIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 1),
    _CrmTrCollectFrDlciIfIndex_Type()
)
crmTrCollectFrDlciIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciIfIndex.setStatus("mandatory")


class _CrmTrCollectFrDlciDlci_Type(Integer32):
    """Custom type crmTrCollectFrDlciDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectFrDlciDlci_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDlci_Object = MibTableColumn
crmTrCollectFrDlciDlci = _CrmTrCollectFrDlciDlci_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 2),
    _CrmTrCollectFrDlciDlci_Type()
)
crmTrCollectFrDlciDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDlci.setStatus("mandatory")


class _CrmTrCollectFrDlciDirect_Type(Integer32):
    """Custom type crmTrCollectFrDlciDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 2),
          ("sw2ifp", 1))
    )


_CrmTrCollectFrDlciDirect_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDirect_Object = MibTableColumn
crmTrCollectFrDlciDirect = _CrmTrCollectFrDlciDirect_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 3),
    _CrmTrCollectFrDlciDirect_Type()
)
crmTrCollectFrDlciDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDirect.setStatus("mandatory")


class _CrmTrCollectFrDlciInterval_Type(Integer32):
    """Custom type crmTrCollectFrDlciInterval based on Integer32"""
    defaultValue = 1

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
        *(("five-seconds", 2),
          ("none", 1),
          ("one-hour", 5),
          ("one-minitutes", 3),
          ("ten-miniutes", 4))
    )


_CrmTrCollectFrDlciInterval_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciInterval_Object = MibTableColumn
crmTrCollectFrDlciInterval = _CrmTrCollectFrDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 4),
    _CrmTrCollectFrDlciInterval_Type()
)
crmTrCollectFrDlciInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciInterval.setStatus("mandatory")
_CrmTrCollectFrDlciThroughCells_Type = Counter32
_CrmTrCollectFrDlciThroughCells_Object = MibTableColumn
crmTrCollectFrDlciThroughCells = _CrmTrCollectFrDlciThroughCells_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 5),
    _CrmTrCollectFrDlciThroughCells_Type()
)
crmTrCollectFrDlciThroughCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciThroughCells.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes1_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes1_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes1_Object = MibTableColumn
crmTrCollectFrDlciDisRes1 = _CrmTrCollectFrDlciDisRes1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 6),
    _CrmTrCollectFrDlciDisRes1_Type()
)
crmTrCollectFrDlciDisRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes1.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells1_Type = Counter32
_CrmTrCollectFrDlciDisCells1_Object = MibTableColumn
crmTrCollectFrDlciDisCells1 = _CrmTrCollectFrDlciDisCells1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 7),
    _CrmTrCollectFrDlciDisCells1_Type()
)
crmTrCollectFrDlciDisCells1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells1.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes2_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes2_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes2_Object = MibTableColumn
crmTrCollectFrDlciDisRes2 = _CrmTrCollectFrDlciDisRes2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 8),
    _CrmTrCollectFrDlciDisRes2_Type()
)
crmTrCollectFrDlciDisRes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes2.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells2_Type = Counter32
_CrmTrCollectFrDlciDisCells2_Object = MibTableColumn
crmTrCollectFrDlciDisCells2 = _CrmTrCollectFrDlciDisCells2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 9),
    _CrmTrCollectFrDlciDisCells2_Type()
)
crmTrCollectFrDlciDisCells2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells2.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes3_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes3_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes3_Object = MibTableColumn
crmTrCollectFrDlciDisRes3 = _CrmTrCollectFrDlciDisRes3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 10),
    _CrmTrCollectFrDlciDisRes3_Type()
)
crmTrCollectFrDlciDisRes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes3.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells3_Type = Counter32
_CrmTrCollectFrDlciDisCells3_Object = MibTableColumn
crmTrCollectFrDlciDisCells3 = _CrmTrCollectFrDlciDisCells3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 11),
    _CrmTrCollectFrDlciDisCells3_Type()
)
crmTrCollectFrDlciDisCells3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells3.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes4_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes4_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes4_Object = MibTableColumn
crmTrCollectFrDlciDisRes4 = _CrmTrCollectFrDlciDisRes4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 12),
    _CrmTrCollectFrDlciDisRes4_Type()
)
crmTrCollectFrDlciDisRes4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes4.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells4_Type = Counter32
_CrmTrCollectFrDlciDisCells4_Object = MibTableColumn
crmTrCollectFrDlciDisCells4 = _CrmTrCollectFrDlciDisCells4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 13),
    _CrmTrCollectFrDlciDisCells4_Type()
)
crmTrCollectFrDlciDisCells4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells4.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes5_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes5_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes5_Object = MibTableColumn
crmTrCollectFrDlciDisRes5 = _CrmTrCollectFrDlciDisRes5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 14),
    _CrmTrCollectFrDlciDisRes5_Type()
)
crmTrCollectFrDlciDisRes5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes5.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells5_Type = Counter32
_CrmTrCollectFrDlciDisCells5_Object = MibTableColumn
crmTrCollectFrDlciDisCells5 = _CrmTrCollectFrDlciDisCells5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 15),
    _CrmTrCollectFrDlciDisCells5_Type()
)
crmTrCollectFrDlciDisCells5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells5.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes6_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes6_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes6_Object = MibTableColumn
crmTrCollectFrDlciDisRes6 = _CrmTrCollectFrDlciDisRes6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 16),
    _CrmTrCollectFrDlciDisRes6_Type()
)
crmTrCollectFrDlciDisRes6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes6.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells6_Type = Counter32
_CrmTrCollectFrDlciDisCells6_Object = MibTableColumn
crmTrCollectFrDlciDisCells6 = _CrmTrCollectFrDlciDisCells6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 17),
    _CrmTrCollectFrDlciDisCells6_Type()
)
crmTrCollectFrDlciDisCells6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells6.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes7_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes7_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes7_Object = MibTableColumn
crmTrCollectFrDlciDisRes7 = _CrmTrCollectFrDlciDisRes7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 18),
    _CrmTrCollectFrDlciDisRes7_Type()
)
crmTrCollectFrDlciDisRes7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes7.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells7_Type = Counter32
_CrmTrCollectFrDlciDisCells7_Object = MibTableColumn
crmTrCollectFrDlciDisCells7 = _CrmTrCollectFrDlciDisCells7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 19),
    _CrmTrCollectFrDlciDisCells7_Type()
)
crmTrCollectFrDlciDisCells7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells7.setStatus("mandatory")


class _CrmTrCollectFrDlciDisRes8_Type(Integer32):
    """Custom type crmTrCollectFrDlciDisRes8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              20,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              50,
              51,
              52,
              60,
              61,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 4),
          ("aal1SnError", 69),
          ("aal1SnOut", 68),
          ("aal2DelaySuppress", 64),
          ("aal2FaxSells", 66),
          ("aal2IllegalFrame", 60),
          ("aal2IllegalSell", 63),
          ("aal2PbSells", 67),
          ("aal2SellLoss", 61),
          ("aal2VoiceSells", 65),
          ("bufferOverflow", 1),
          ("cellHeaderError", 20),
          ("dsn-ifuMessage", 34),
          ("frAbnormal", 40),
          ("frExcess", 41),
          ("frLogical", 42),
          ("hdlcError", 33),
          ("notMeasurement", 0),
          ("other1", 50),
          ("other2", 51),
          ("other3", 52),
          ("parityError", 3),
          ("parityErrorFrame", 35),
          ("pathParityError", 31),
          ("policingViolation", 2),
          ("priBufferOverflow", 5),
          ("sarCsError", 10),
          ("sectionParityError", 30),
          ("tenMifParityError", 32),
          ("vcAis", 80),
          ("vcFerf", 81),
          ("vcLoopback", 83),
          ("vpLoopback", 82))
    )


_CrmTrCollectFrDlciDisRes8_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciDisRes8_Object = MibTableColumn
crmTrCollectFrDlciDisRes8 = _CrmTrCollectFrDlciDisRes8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 20),
    _CrmTrCollectFrDlciDisRes8_Type()
)
crmTrCollectFrDlciDisRes8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisRes8.setStatus("mandatory")
_CrmTrCollectFrDlciDisCells8_Type = Counter32
_CrmTrCollectFrDlciDisCells8_Object = MibTableColumn
crmTrCollectFrDlciDisCells8 = _CrmTrCollectFrDlciDisCells8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 21),
    _CrmTrCollectFrDlciDisCells8_Type()
)
crmTrCollectFrDlciDisCells8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciDisCells8.setStatus("mandatory")
_CrmTrCollectFrDlciStartTime_Type = DateAndTime
_CrmTrCollectFrDlciStartTime_Object = MibTableColumn
crmTrCollectFrDlciStartTime = _CrmTrCollectFrDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 22),
    _CrmTrCollectFrDlciStartTime_Type()
)
crmTrCollectFrDlciStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciStartTime.setStatus("mandatory")
_CrmTrCollectFrDlciEndTime_Type = DateAndTime
_CrmTrCollectFrDlciEndTime_Object = MibTableColumn
crmTrCollectFrDlciEndTime = _CrmTrCollectFrDlciEndTime_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 23),
    _CrmTrCollectFrDlciEndTime_Type()
)
crmTrCollectFrDlciEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciEndTime.setStatus("mandatory")


class _CrmTrCollectFrDlciRowStatus_Type(Integer32):
    """Custom type crmTrCollectFrDlciRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrCollectFrDlciRowStatus_Type.__name__ = "Integer32"
_CrmTrCollectFrDlciRowStatus_Object = MibTableColumn
crmTrCollectFrDlciRowStatus = _CrmTrCollectFrDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 4, 7, 1, 24),
    _CrmTrCollectFrDlciRowStatus_Type()
)
crmTrCollectFrDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrCollectFrDlciRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRMTRAFFICCOLLECTION-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "ntt": ntt,
       "mibDoc": mibDoc,
       "ba3000": ba3000,
       "crmCommon": crmCommon,
       "crmTraffic": crmTraffic,
       "crmTrCollectIntervalTable": crmTrCollectIntervalTable,
       "crmTrCollectIntervalEntry": crmTrCollectIntervalEntry,
       "crmTrCollectIntervalType": crmTrCollectIntervalType,
       "crmTrCollectIntervalTime": crmTrCollectIntervalTime,
       "crmTrCollectIntervalIfPoints": crmTrCollectIntervalIfPoints,
       "crmTrCollectIntervalVpcPoints": crmTrCollectIntervalVpcPoints,
       "crmTrCollectIntervalVccPoints": crmTrCollectIntervalVccPoints,
       "crmTrCollectIntervalPriPoints": crmTrCollectIntervalPriPoints,
       "crmTrCollectIntervalFrIfPoints": crmTrCollectIntervalFrIfPoints,
       "crmTrCollectIntervalFrDlciPoints": crmTrCollectIntervalFrDlciPoints,
       "crmTrCollectIfTable": crmTrCollectIfTable,
       "crmTrCollectIfEntry": crmTrCollectIfEntry,
       "crmTrCollectIfIfIndex": crmTrCollectIfIfIndex,
       "crmTrCollectIfDirect": crmTrCollectIfDirect,
       "crmTrCollectIfInterval": crmTrCollectIfInterval,
       "crmTrCollectIfThroughCells": crmTrCollectIfThroughCells,
       "crmTrCollectIfDisRes1": crmTrCollectIfDisRes1,
       "crmTrCollectIfDisCells1": crmTrCollectIfDisCells1,
       "crmTrCollectIfDisRes2": crmTrCollectIfDisRes2,
       "crmTrCollectIfDisCells2": crmTrCollectIfDisCells2,
       "crmTrCollectIfDisRes3": crmTrCollectIfDisRes3,
       "crmTrCollectIfDisCells3": crmTrCollectIfDisCells3,
       "crmTrCollectIfDisRes4": crmTrCollectIfDisRes4,
       "crmTrCollectIfDisCells4": crmTrCollectIfDisCells4,
       "crmTrCollectIfDisRes5": crmTrCollectIfDisRes5,
       "crmTrCollectIfDisCells5": crmTrCollectIfDisCells5,
       "crmTrCollectIfDisRes6": crmTrCollectIfDisRes6,
       "crmTrCollectIfDisCells6": crmTrCollectIfDisCells6,
       "crmTrCollectIfDisRes7": crmTrCollectIfDisRes7,
       "crmTrCollectIfDisCells7": crmTrCollectIfDisCells7,
       "crmTrCollectIfDisRes8": crmTrCollectIfDisRes8,
       "crmTrCollectIfDisCells8": crmTrCollectIfDisCells8,
       "crmTrCollectIfStartTime": crmTrCollectIfStartTime,
       "crmTrCollectIfEndTime": crmTrCollectIfEndTime,
       "crmTrCollectIfRowStatus": crmTrCollectIfRowStatus,
       "crmTrCollectVpcTable": crmTrCollectVpcTable,
       "crmTrCollectVpcEntry": crmTrCollectVpcEntry,
       "crmTrCollectVpcIfIndex": crmTrCollectVpcIfIndex,
       "crmTrCollectVpcVpi": crmTrCollectVpcVpi,
       "crmTrCollectVpcDirect": crmTrCollectVpcDirect,
       "crmTrCollectVpcInterval": crmTrCollectVpcInterval,
       "crmTrCollectVpcThroughCells": crmTrCollectVpcThroughCells,
       "crmTrCollectVpcDisRes1": crmTrCollectVpcDisRes1,
       "crmTrCollectVpcDisCells1": crmTrCollectVpcDisCells1,
       "crmTrCollectVpcDisRes2": crmTrCollectVpcDisRes2,
       "crmTrCollectVpcDisCells2": crmTrCollectVpcDisCells2,
       "crmTrCollectVpcDisRes3": crmTrCollectVpcDisRes3,
       "crmTrCollectVpcDisCells3": crmTrCollectVpcDisCells3,
       "crmTrCollectVpcDisRes4": crmTrCollectVpcDisRes4,
       "crmTrCollectVpcDisCells4": crmTrCollectVpcDisCells4,
       "crmTrCollectVpcDisRes5": crmTrCollectVpcDisRes5,
       "crmTrCollectVpcDisCells5": crmTrCollectVpcDisCells5,
       "crmTrCollectVpcDisRes6": crmTrCollectVpcDisRes6,
       "crmTrCollectVpcDisCells6": crmTrCollectVpcDisCells6,
       "crmTrCollectVpcDisRes7": crmTrCollectVpcDisRes7,
       "crmTrCollectVpcDisCells7": crmTrCollectVpcDisCells7,
       "crmTrCollectVpcDisRes8": crmTrCollectVpcDisRes8,
       "crmTrCollectVpcDisCells8": crmTrCollectVpcDisCells8,
       "crmTrCollectVpcStartTime": crmTrCollectVpcStartTime,
       "crmTrCollectVpcEndTime": crmTrCollectVpcEndTime,
       "crmTrCollectVpcRowStatus": crmTrCollectVpcRowStatus,
       "crmTrCollectVccTable": crmTrCollectVccTable,
       "crmTrCollectVccEntry": crmTrCollectVccEntry,
       "crmTrCollectVccIfIndex": crmTrCollectVccIfIndex,
       "crmTrCollectVccVpi": crmTrCollectVccVpi,
       "crmTrCollectVccVci": crmTrCollectVccVci,
       "crmTrCollectVccDirect": crmTrCollectVccDirect,
       "crmTrCollectVccInterval": crmTrCollectVccInterval,
       "crmTrCollectVccThroughCells": crmTrCollectVccThroughCells,
       "crmTrCollectVccDisRes1": crmTrCollectVccDisRes1,
       "crmTrCollectVccDisCells1": crmTrCollectVccDisCells1,
       "crmTrCollectVccDisRes2": crmTrCollectVccDisRes2,
       "crmTrCollectVccDisCells2": crmTrCollectVccDisCells2,
       "crmTrCollectVccDisRes3": crmTrCollectVccDisRes3,
       "crmTrCollectVccDisCells3": crmTrCollectVccDisCells3,
       "crmTrCollectVccDisRes4": crmTrCollectVccDisRes4,
       "crmTrCollectVccDisCells4": crmTrCollectVccDisCells4,
       "crmTrCollectVccDisRes5": crmTrCollectVccDisRes5,
       "crmTrCollectVccDisCells5": crmTrCollectVccDisCells5,
       "crmTrCollectVccDisRes6": crmTrCollectVccDisRes6,
       "crmTrCollectVccDisCells6": crmTrCollectVccDisCells6,
       "crmTrCollectVccDisRes7": crmTrCollectVccDisRes7,
       "crmTrCollectVccDisCells7": crmTrCollectVccDisCells7,
       "crmTrCollectVccDisRes8": crmTrCollectVccDisRes8,
       "crmTrCollectVccDisCells8": crmTrCollectVccDisCells8,
       "crmTrCollectVccStartTime": crmTrCollectVccStartTime,
       "crmTrCollectVccEndTime": crmTrCollectVccEndTime,
       "crmTrCollectVccRowStatus": crmTrCollectVccRowStatus,
       "crmTrCollectPriTable": crmTrCollectPriTable,
       "crmTrCollectPriEntry": crmTrCollectPriEntry,
       "crmTrCollectPriIfIndex": crmTrCollectPriIfIndex,
       "crmTrCollectPriClass": crmTrCollectPriClass,
       "crmTrCollectPriDirect": crmTrCollectPriDirect,
       "crmTrCollectPriInterval": crmTrCollectPriInterval,
       "crmTrCollectPriThroughCells": crmTrCollectPriThroughCells,
       "crmTrCollectPriDisRes1": crmTrCollectPriDisRes1,
       "crmTrCollectPriDisCells1": crmTrCollectPriDisCells1,
       "crmTrCollectPriDisRes2": crmTrCollectPriDisRes2,
       "crmTrCollectPriDisCells2": crmTrCollectPriDisCells2,
       "crmTrCollectPriDisRes3": crmTrCollectPriDisRes3,
       "crmTrCollectPriDisCells3": crmTrCollectPriDisCells3,
       "crmTrCollectPriDisRes4": crmTrCollectPriDisRes4,
       "crmTrCollectPriDisCells4": crmTrCollectPriDisCells4,
       "crmTrCollectPriDisRes5": crmTrCollectPriDisRes5,
       "crmTrCollectPriDisCells5": crmTrCollectPriDisCells5,
       "crmTrCollectPriDisRes6": crmTrCollectPriDisRes6,
       "crmTrCollectPriDisCells6": crmTrCollectPriDisCells6,
       "crmTrCollectPriDisRes7": crmTrCollectPriDisRes7,
       "crmTrCollectPriDisCells7": crmTrCollectPriDisCells7,
       "crmTrCollectPriDisRes8": crmTrCollectPriDisRes8,
       "crmTrCollectPriDisCells8": crmTrCollectPriDisCells8,
       "crmTrCollectPriStartTime": crmTrCollectPriStartTime,
       "crmTrCollectPriEndTime": crmTrCollectPriEndTime,
       "crmTrCollectPriRowStatus": crmTrCollectPriRowStatus,
       "crmTrCollectFrIfTable": crmTrCollectFrIfTable,
       "crmTrCollectFrIfEntry": crmTrCollectFrIfEntry,
       "crmTrCollectFrIfIfIndex": crmTrCollectFrIfIfIndex,
       "crmTrCollectFrIfDirect": crmTrCollectFrIfDirect,
       "crmTrCollectFrIfInterval": crmTrCollectFrIfInterval,
       "crmTrCollectFrIfThroughCells": crmTrCollectFrIfThroughCells,
       "crmTrCollectFrIfDisRes1": crmTrCollectFrIfDisRes1,
       "crmTrCollectFrIfDisCells1": crmTrCollectFrIfDisCells1,
       "crmTrCollectFrIfDisRes2": crmTrCollectFrIfDisRes2,
       "crmTrCollectFrIfDisCells2": crmTrCollectFrIfDisCells2,
       "crmTrCollectFrIfDisRes3": crmTrCollectFrIfDisRes3,
       "crmTrCollectFrIfDisCells3": crmTrCollectFrIfDisCells3,
       "crmTrCollectFrIfDisRes4": crmTrCollectFrIfDisRes4,
       "crmTrCollectFrIfDisCells4": crmTrCollectFrIfDisCells4,
       "crmTrCollectFrIfDisRes5": crmTrCollectFrIfDisRes5,
       "crmTrCollectFrIfDisCells5": crmTrCollectFrIfDisCells5,
       "crmTrCollectFrIfDisRes6": crmTrCollectFrIfDisRes6,
       "crmTrCollectFrIfDisCells6": crmTrCollectFrIfDisCells6,
       "crmTrCollectFrIfDisRes7": crmTrCollectFrIfDisRes7,
       "crmTrCollectFrIfDisCells7": crmTrCollectFrIfDisCells7,
       "crmTrCollectFrIfDisRes8": crmTrCollectFrIfDisRes8,
       "crmTrCollectFrIfDisCells8": crmTrCollectFrIfDisCells8,
       "crmTrCollectFrIfStartTime": crmTrCollectFrIfStartTime,
       "crmTrCollectFrIfEndTime": crmTrCollectFrIfEndTime,
       "crmTrCollectFrIfRowStatus": crmTrCollectFrIfRowStatus,
       "crmTrCollectFrDlciTable": crmTrCollectFrDlciTable,
       "crmTrCollectFrDlciEntry": crmTrCollectFrDlciEntry,
       "crmTrCollectFrDlciIfIndex": crmTrCollectFrDlciIfIndex,
       "crmTrCollectFrDlciDlci": crmTrCollectFrDlciDlci,
       "crmTrCollectFrDlciDirect": crmTrCollectFrDlciDirect,
       "crmTrCollectFrDlciInterval": crmTrCollectFrDlciInterval,
       "crmTrCollectFrDlciThroughCells": crmTrCollectFrDlciThroughCells,
       "crmTrCollectFrDlciDisRes1": crmTrCollectFrDlciDisRes1,
       "crmTrCollectFrDlciDisCells1": crmTrCollectFrDlciDisCells1,
       "crmTrCollectFrDlciDisRes2": crmTrCollectFrDlciDisRes2,
       "crmTrCollectFrDlciDisCells2": crmTrCollectFrDlciDisCells2,
       "crmTrCollectFrDlciDisRes3": crmTrCollectFrDlciDisRes3,
       "crmTrCollectFrDlciDisCells3": crmTrCollectFrDlciDisCells3,
       "crmTrCollectFrDlciDisRes4": crmTrCollectFrDlciDisRes4,
       "crmTrCollectFrDlciDisCells4": crmTrCollectFrDlciDisCells4,
       "crmTrCollectFrDlciDisRes5": crmTrCollectFrDlciDisRes5,
       "crmTrCollectFrDlciDisCells5": crmTrCollectFrDlciDisCells5,
       "crmTrCollectFrDlciDisRes6": crmTrCollectFrDlciDisRes6,
       "crmTrCollectFrDlciDisCells6": crmTrCollectFrDlciDisCells6,
       "crmTrCollectFrDlciDisRes7": crmTrCollectFrDlciDisRes7,
       "crmTrCollectFrDlciDisCells7": crmTrCollectFrDlciDisCells7,
       "crmTrCollectFrDlciDisRes8": crmTrCollectFrDlciDisRes8,
       "crmTrCollectFrDlciDisCells8": crmTrCollectFrDlciDisCells8,
       "crmTrCollectFrDlciStartTime": crmTrCollectFrDlciStartTime,
       "crmTrCollectFrDlciEndTime": crmTrCollectFrDlciEndTime,
       "crmTrCollectFrDlciRowStatus": crmTrCollectFrDlciRowStatus}
)
