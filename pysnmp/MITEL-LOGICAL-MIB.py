# SNMP MIB module (MITEL-LOGICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-LOGICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:23 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelRouterLogicalGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4)
)
mitelRouterLogicalGroup.setRevisions(
        ("2003-03-24 09:47",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
_MitelIdCsIpera1000_ObjectIdentity = ObjectIdentity
mitelIdCsIpera1000 = _MitelIdCsIpera1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelLogGrpLogicalTable_Object = MibTable
mitelLogGrpLogicalTable = _MitelLogGrpLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mitelLogGrpLogicalTable.setStatus("current")
_MitelLogGrpLogicalEntry_Object = MibTableRow
mitelLogGrpLogicalEntry = _MitelLogGrpLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 1, 1)
)
mitelLogGrpLogicalEntry.setIndexNames(
    (0, "MITEL-LOGICAL-MIB", "mitelLogicalTblIndex"),
)
if mibBuilder.loadTexts:
    mitelLogGrpLogicalEntry.setStatus("current")
_MitelLogicalTblIndex_Type = Integer32
_MitelLogicalTblIndex_Object = MibTableColumn
mitelLogicalTblIndex = _MitelLogicalTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 1, 1, 1),
    _MitelLogicalTblIndex_Type()
)
mitelLogicalTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelLogicalTblIndex.setStatus("current")


class _MitelLogicalTblDestName_Type(DisplayString):
    """Custom type mitelLogicalTblDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MitelLogicalTblDestName_Type.__name__ = "DisplayString"
_MitelLogicalTblDestName_Object = MibTableColumn
mitelLogicalTblDestName = _MitelLogicalTblDestName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 1, 1, 2),
    _MitelLogicalTblDestName_Type()
)
mitelLogicalTblDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogicalTblDestName.setStatus("current")


class _MitelLogicalTblType_Type(Integer32):
    """Custom type mitelLogicalTblType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_MitelLogicalTblType_Type.__name__ = "Integer32"
_MitelLogicalTblType_Object = MibTableColumn
mitelLogicalTblType = _MitelLogicalTblType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 1, 1, 3),
    _MitelLogicalTblType_Type()
)
mitelLogicalTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelLogicalTblType.setStatus("current")


class _MitelLogicalTblAdminStatus_Type(Integer32):
    """Custom type mitelLogicalTblAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MitelLogicalTblAdminStatus_Type.__name__ = "Integer32"
_MitelLogicalTblAdminStatus_Object = MibTableColumn
mitelLogicalTblAdminStatus = _MitelLogicalTblAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 1, 1, 4),
    _MitelLogicalTblAdminStatus_Type()
)
mitelLogicalTblAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogicalTblAdminStatus.setStatus("current")
_MitelLogGrpLogicalWanTable_Object = MibTable
mitelLogGrpLogicalWanTable = _MitelLogGrpLogicalWanTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mitelLogGrpLogicalWanTable.setStatus("current")
_MitelLogGrpLogicalWanEntry_Object = MibTableRow
mitelLogGrpLogicalWanEntry = _MitelLogGrpLogicalWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1)
)
mitelLogGrpLogicalWanEntry.setIndexNames(
    (0, "MITEL-LOGICAL-MIB", "mitelLogicalTblIndex"),
)
if mibBuilder.loadTexts:
    mitelLogGrpLogicalWanEntry.setStatus("current")


class _MitelLogWanTblCmprsn_Type(Integer32):
    """Custom type mitelLogWanTblCmprsn based on Integer32"""
    defaultValue = 1

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
        *(("any", 2),
          ("gandalf", 3),
          ("none", 1),
          ("stac", 4))
    )


_MitelLogWanTblCmprsn_Type.__name__ = "Integer32"
_MitelLogWanTblCmprsn_Object = MibTableColumn
mitelLogWanTblCmprsn = _MitelLogWanTblCmprsn_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 1),
    _MitelLogWanTblCmprsn_Type()
)
mitelLogWanTblCmprsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblCmprsn.setStatus("current")


class _MitelLogWanTblCmprsnStatus_Type(Integer32):
    """Custom type mitelLogWanTblCmprsnStatus based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("concryption", 4),
          ("encryption", 5),
          ("fza", 2),
          ("fzap", 3),
          ("none", 1),
          ("stacAscendLCBMode", 11),
          ("stacCRCCheckMode", 8),
          ("stacExtendedMode", 10),
          ("stacLCBCheckMode", 7),
          ("stacNoCheckMode", 6),
          ("stacSeqNumbers", 9))
    )


_MitelLogWanTblCmprsnStatus_Type.__name__ = "Integer32"
_MitelLogWanTblCmprsnStatus_Object = MibTableColumn
mitelLogWanTblCmprsnStatus = _MitelLogWanTblCmprsnStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 2),
    _MitelLogWanTblCmprsnStatus_Type()
)
mitelLogWanTblCmprsnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelLogWanTblCmprsnStatus.setStatus("current")


class _MitelLogWanTblEncryptn_Type(Integer32):
    """Custom type mitelLogWanTblEncryptn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MitelLogWanTblEncryptn_Type.__name__ = "Integer32"
_MitelLogWanTblEncryptn_Object = MibTableColumn
mitelLogWanTblEncryptn = _MitelLogWanTblEncryptn_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 3),
    _MitelLogWanTblEncryptn_Type()
)
mitelLogWanTblEncryptn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblEncryptn.setStatus("current")


class _MitelLogWanTblBackupOvrflow_Type(Integer32):
    """Custom type mitelLogWanTblBackupOvrflow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("disabled", 1),
          ("overflow", 3))
    )


_MitelLogWanTblBackupOvrflow_Type.__name__ = "Integer32"
_MitelLogWanTblBackupOvrflow_Object = MibTableColumn
mitelLogWanTblBackupOvrflow = _MitelLogWanTblBackupOvrflow_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 4),
    _MitelLogWanTblBackupOvrflow_Type()
)
mitelLogWanTblBackupOvrflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblBackupOvrflow.setStatus("current")


class _MitelLogWanTblThshld_Type(Integer32):
    """Custom type mitelLogWanTblThshld based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MitelLogWanTblThshld_Type.__name__ = "Integer32"
_MitelLogWanTblThshld_Object = MibTableColumn
mitelLogWanTblThshld = _MitelLogWanTblThshld_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 5),
    _MitelLogWanTblThshld_Type()
)
mitelLogWanTblThshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblThshld.setStatus("current")


class _MitelLogWanTblConnTimer_Type(Integer32):
    """Custom type mitelLogWanTblConnTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MitelLogWanTblConnTimer_Type.__name__ = "Integer32"
_MitelLogWanTblConnTimer_Object = MibTableColumn
mitelLogWanTblConnTimer = _MitelLogWanTblConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 6),
    _MitelLogWanTblConnTimer_Type()
)
mitelLogWanTblConnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblConnTimer.setStatus("current")


class _MitelLogWanTblDiscTimer_Type(Integer32):
    """Custom type mitelLogWanTblDiscTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MitelLogWanTblDiscTimer_Type.__name__ = "Integer32"
_MitelLogWanTblDiscTimer_Object = MibTableColumn
mitelLogWanTblDiscTimer = _MitelLogWanTblDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 7),
    _MitelLogWanTblDiscTimer_Type()
)
mitelLogWanTblDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblDiscTimer.setStatus("current")


class _MitelLogWanTblProtocolType_Type(Integer32):
    """Custom type mitelLogWanTblProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("framerelay", 2),
          ("ppp", 1),
          ("x25", 3))
    )


_MitelLogWanTblProtocolType_Type.__name__ = "Integer32"
_MitelLogWanTblProtocolType_Object = MibTableColumn
mitelLogWanTblProtocolType = _MitelLogWanTblProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 2, 1, 8),
    _MitelLogWanTblProtocolType_Type()
)
mitelLogWanTblProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanTblProtocolType.setStatus("current")
_MitelLogGrpLogicalWanPortTable_Object = MibTable
mitelLogGrpLogicalWanPortTable = _MitelLogGrpLogicalWanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mitelLogGrpLogicalWanPortTable.setStatus("current")
_MitelLogGrpLogicalWanPortEntry_Object = MibTableRow
mitelLogGrpLogicalWanPortEntry = _MitelLogGrpLogicalWanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1)
)
mitelLogGrpLogicalWanPortEntry.setIndexNames(
    (0, "MITEL-LOGICAL-MIB", "mitelLogicalTblIndex"),
    (0, "MITEL-LOGICAL-MIB", "mitelLogWanPortTblIndex"),
)
if mibBuilder.loadTexts:
    mitelLogGrpLogicalWanPortEntry.setStatus("current")
_MitelLogWanPortTblIndex_Type = Integer32
_MitelLogWanPortTblIndex_Object = MibTableColumn
mitelLogWanPortTblIndex = _MitelLogWanPortTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 1),
    _MitelLogWanPortTblIndex_Type()
)
mitelLogWanPortTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelLogWanPortTblIndex.setStatus("current")


class _MitelLogWanPortTblWanType_Type(Integer32):
    """Custom type mitelLogWanPortTblWanType based on Integer32"""
    defaultValue = 2

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
        *(("incomming", 3),
          ("ondemand", 2),
          ("outgoing", 4),
          ("permanent", 1))
    )


_MitelLogWanPortTblWanType_Type.__name__ = "Integer32"
_MitelLogWanPortTblWanType_Object = MibTableColumn
mitelLogWanPortTblWanType = _MitelLogWanPortTblWanType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 2),
    _MitelLogWanPortTblWanType_Type()
)
mitelLogWanPortTblWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblWanType.setStatus("current")


class _MitelLogWanPortTblTransType_Type(Integer32):
    """Custom type mitelLogWanPortTblTransType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 3),
          ("hdlc", 1),
          ("modem", 2))
    )


_MitelLogWanPortTblTransType_Type.__name__ = "Integer32"
_MitelLogWanPortTblTransType_Object = MibTableColumn
mitelLogWanPortTblTransType = _MitelLogWanPortTblTransType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 3),
    _MitelLogWanPortTblTransType_Type()
)
mitelLogWanPortTblTransType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblTransType.setStatus("current")


class _MitelLogWanPortTblRetry_Type(Integer32):
    """Custom type mitelLogWanPortTblRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MitelLogWanPortTblRetry_Type.__name__ = "Integer32"
_MitelLogWanPortTblRetry_Object = MibTableColumn
mitelLogWanPortTblRetry = _MitelLogWanPortTblRetry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 4),
    _MitelLogWanPortTblRetry_Type()
)
mitelLogWanPortTblRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblRetry.setStatus("current")


class _MitelLogWanPortTblRetryPeriod_Type(Integer32):
    """Custom type mitelLogWanPortTblRetryPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MitelLogWanPortTblRetryPeriod_Type.__name__ = "Integer32"
_MitelLogWanPortTblRetryPeriod_Object = MibTableColumn
mitelLogWanPortTblRetryPeriod = _MitelLogWanPortTblRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 5),
    _MitelLogWanPortTblRetryPeriod_Type()
)
mitelLogWanPortTblRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblRetryPeriod.setStatus("current")


class _MitelLogWanPortTblPrepend_Type(OctetString):
    """Custom type mitelLogWanPortTblPrepend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_MitelLogWanPortTblPrepend_Type.__name__ = "OctetString"
_MitelLogWanPortTblPrepend_Object = MibTableColumn
mitelLogWanPortTblPrepend = _MitelLogWanPortTblPrepend_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 6),
    _MitelLogWanPortTblPrepend_Type()
)
mitelLogWanPortTblPrepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblPrepend.setStatus("current")


class _MitelLogWanPortTblDestAddr_Type(DisplayString):
    """Custom type mitelLogWanPortTblDestAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MitelLogWanPortTblDestAddr_Type.__name__ = "DisplayString"
_MitelLogWanPortTblDestAddr_Object = MibTableColumn
mitelLogWanPortTblDestAddr = _MitelLogWanPortTblDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 7),
    _MitelLogWanPortTblDestAddr_Type()
)
mitelLogWanPortTblDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblDestAddr.setStatus("current")


class _MitelLogWanPortTblNextDestAddr_Type(DisplayString):
    """Custom type mitelLogWanPortTblNextDestAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MitelLogWanPortTblNextDestAddr_Type.__name__ = "DisplayString"
_MitelLogWanPortTblNextDestAddr_Object = MibTableColumn
mitelLogWanPortTblNextDestAddr = _MitelLogWanPortTblNextDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 8),
    _MitelLogWanPortTblNextDestAddr_Type()
)
mitelLogWanPortTblNextDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblNextDestAddr.setStatus("current")


class _MitelLogWanPortTblChId_Type(Integer32):
    """Custom type mitelLogWanPortTblChId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelLogWanPortTblChId_Type.__name__ = "Integer32"
_MitelLogWanPortTblChId_Object = MibTableColumn
mitelLogWanPortTblChId = _MitelLogWanPortTblChId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 9),
    _MitelLogWanPortTblChId_Type()
)
mitelLogWanPortTblChId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblChId.setStatus("current")


class _MitelLogWanPortTblDialback_Type(Integer32):
    """Custom type mitelLogWanPortTblDialback based on Integer32"""
    defaultValue = 2

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


_MitelLogWanPortTblDialback_Type.__name__ = "Integer32"
_MitelLogWanPortTblDialback_Object = MibTableColumn
mitelLogWanPortTblDialback = _MitelLogWanPortTblDialback_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 10),
    _MitelLogWanPortTblDialback_Type()
)
mitelLogWanPortTblDialback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblDialback.setStatus("current")


class _MitelLogWanPortTblAdminStatus_Type(Integer32):
    """Custom type mitelLogWanPortTblAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MitelLogWanPortTblAdminStatus_Type.__name__ = "Integer32"
_MitelLogWanPortTblAdminStatus_Object = MibTableColumn
mitelLogWanPortTblAdminStatus = _MitelLogWanPortTblAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 11),
    _MitelLogWanPortTblAdminStatus_Type()
)
mitelLogWanPortTblAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogWanPortTblAdminStatus.setStatus("current")


class _MitelLogWanPortTblOperStatus_Type(Integer32):
    """Custom type mitelLogWanPortTblOperStatus based on Integer32"""
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
        *(("connected", 2),
          ("connecting", 1),
          ("disconnected", 4),
          ("disconnecting", 3),
          ("retryExhausted", 5))
    )


_MitelLogWanPortTblOperStatus_Type.__name__ = "Integer32"
_MitelLogWanPortTblOperStatus_Object = MibTableColumn
mitelLogWanPortTblOperStatus = _MitelLogWanPortTblOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 12),
    _MitelLogWanPortTblOperStatus_Type()
)
mitelLogWanPortTblOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelLogWanPortTblOperStatus.setStatus("current")
_MitelLogWanPortTblStatus_Type = RowStatus
_MitelLogWanPortTblStatus_Object = MibTableColumn
mitelLogWanPortTblStatus = _MitelLogWanPortTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4, 3, 1, 13),
    _MitelLogWanPortTblStatus_Type()
)
mitelLogWanPortTblStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelLogWanPortTblStatus.setStatus("current")

# Managed Objects groups


# Notification objects

mitelWanRetryThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 403)
)
mitelWanRetryThreshold.setObjects(
    ("MITEL-LOGICAL-MIB", "mitelLogWanPortTblStatus")
)
if mibBuilder.loadTexts:
    mitelWanRetryThreshold.setStatus(
        "current"
    )


# Notifications groups

mitelIpera1000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)
)
mitelIpera1000Notifications.setObjects(
    ("MITEL-LOGICAL-MIB", "mitelWanRetryThreshold")
)
if mibBuilder.loadTexts:
    mitelIpera1000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-LOGICAL-MIB",
    **{"mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsIpera1000": mitelIdCsIpera1000,
       "mitelIpera1000Notifications": mitelIpera1000Notifications,
       "mitelWanRetryThreshold": mitelWanRetryThreshold,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterLogicalGroup": mitelRouterLogicalGroup,
       "mitelLogGrpLogicalTable": mitelLogGrpLogicalTable,
       "mitelLogGrpLogicalEntry": mitelLogGrpLogicalEntry,
       "mitelLogicalTblIndex": mitelLogicalTblIndex,
       "mitelLogicalTblDestName": mitelLogicalTblDestName,
       "mitelLogicalTblType": mitelLogicalTblType,
       "mitelLogicalTblAdminStatus": mitelLogicalTblAdminStatus,
       "mitelLogGrpLogicalWanTable": mitelLogGrpLogicalWanTable,
       "mitelLogGrpLogicalWanEntry": mitelLogGrpLogicalWanEntry,
       "mitelLogWanTblCmprsn": mitelLogWanTblCmprsn,
       "mitelLogWanTblCmprsnStatus": mitelLogWanTblCmprsnStatus,
       "mitelLogWanTblEncryptn": mitelLogWanTblEncryptn,
       "mitelLogWanTblBackupOvrflow": mitelLogWanTblBackupOvrflow,
       "mitelLogWanTblThshld": mitelLogWanTblThshld,
       "mitelLogWanTblConnTimer": mitelLogWanTblConnTimer,
       "mitelLogWanTblDiscTimer": mitelLogWanTblDiscTimer,
       "mitelLogWanTblProtocolType": mitelLogWanTblProtocolType,
       "mitelLogGrpLogicalWanPortTable": mitelLogGrpLogicalWanPortTable,
       "mitelLogGrpLogicalWanPortEntry": mitelLogGrpLogicalWanPortEntry,
       "mitelLogWanPortTblIndex": mitelLogWanPortTblIndex,
       "mitelLogWanPortTblWanType": mitelLogWanPortTblWanType,
       "mitelLogWanPortTblTransType": mitelLogWanPortTblTransType,
       "mitelLogWanPortTblRetry": mitelLogWanPortTblRetry,
       "mitelLogWanPortTblRetryPeriod": mitelLogWanPortTblRetryPeriod,
       "mitelLogWanPortTblPrepend": mitelLogWanPortTblPrepend,
       "mitelLogWanPortTblDestAddr": mitelLogWanPortTblDestAddr,
       "mitelLogWanPortTblNextDestAddr": mitelLogWanPortTblNextDestAddr,
       "mitelLogWanPortTblChId": mitelLogWanPortTblChId,
       "mitelLogWanPortTblDialback": mitelLogWanPortTblDialback,
       "mitelLogWanPortTblAdminStatus": mitelLogWanPortTblAdminStatus,
       "mitelLogWanPortTblOperStatus": mitelLogWanPortTblOperStatus,
       "mitelLogWanPortTblStatus": mitelLogWanPortTblStatus}
)
