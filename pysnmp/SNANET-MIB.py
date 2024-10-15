# SNMP MIB module (SNANET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNANET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:46 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Unisys_ObjectIdentity = ObjectIdentity
unisys = _Unisys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223)
)
_Dcp_ObjectIdentity = ObjectIdentity
dcp = _Dcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8)
)
_Snanet_ObjectIdentity = ObjectIdentity
snanet = _Snanet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3)
)
_ProdInfo_ObjectIdentity = ObjectIdentity
prodInfo = _ProdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 1)
)


class _ProdInfoDesc_Type(DisplayString):
    """Custom type prodInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProdInfoDesc_Type.__name__ = "DisplayString"
_ProdInfoDesc_Object = MibScalar
prodInfoDesc = _ProdInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 1, 1),
    _ProdInfoDesc_Type()
)
prodInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoDesc.setStatus("mandatory")
_ProdInfoFeatures_Type = Integer32
_ProdInfoFeatures_Object = MibScalar
prodInfoFeatures = _ProdInfoFeatures_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 1, 2),
    _ProdInfoFeatures_Type()
)
prodInfoFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoFeatures.setStatus("mandatory")
_T5node_ObjectIdentity = ObjectIdentity
t5node = _T5node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2)
)
_T5nodeTable_Object = MibTable
t5nodeTable = _T5nodeTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    t5nodeTable.setStatus("mandatory")
_T5nodeEntry_Object = MibTableRow
t5nodeEntry = _T5nodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1)
)
t5nodeEntry.setIndexNames(
    (0, "SNANET-MIB", "t5nodeIndex"),
)
if mibBuilder.loadTexts:
    t5nodeEntry.setStatus("mandatory")
_T5nodeIndex_Type = Integer32
_T5nodeIndex_Object = MibTableColumn
t5nodeIndex = _T5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 1),
    _T5nodeIndex_Type()
)
t5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeIndex.setStatus("mandatory")


class _T5nodeDomainName_Type(DisplayString):
    """Custom type t5nodeDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5nodeDomainName_Type.__name__ = "DisplayString"
_T5nodeDomainName_Object = MibTableColumn
t5nodeDomainName = _T5nodeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 2),
    _T5nodeDomainName_Type()
)
t5nodeDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeDomainName.setStatus("mandatory")


class _T5nodeOperState_Type(Integer32):
    """Custom type t5nodeOperState based on Integer32"""
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
        *(("down", 3),
          ("other", 1),
          ("standby", 4),
          ("up", 2))
    )


_T5nodeOperState_Type.__name__ = "Integer32"
_T5nodeOperState_Object = MibTableColumn
t5nodeOperState = _T5nodeOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 3),
    _T5nodeOperState_Type()
)
t5nodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeOperState.setStatus("mandatory")


class _T5nodeSubareaNumber_Type(Integer32):
    """Custom type t5nodeSubareaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_T5nodeSubareaNumber_Type.__name__ = "Integer32"
_T5nodeSubareaNumber_Object = MibTableColumn
t5nodeSubareaNumber = _T5nodeSubareaNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 4),
    _T5nodeSubareaNumber_Type()
)
t5nodeSubareaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeSubareaNumber.setStatus("mandatory")


class _T5nodeSscpName_Type(DisplayString):
    """Custom type t5nodeSscpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_T5nodeSscpName_Type.__name__ = "DisplayString"
_T5nodeSscpName_Object = MibTableColumn
t5nodeSscpName = _T5nodeSscpName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 5),
    _T5nodeSscpName_Type()
)
t5nodeSscpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeSscpName.setStatus("mandatory")


class _T5nodeNetworkName_Type(DisplayString):
    """Custom type t5nodeNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5nodeNetworkName_Type.__name__ = "DisplayString"
_T5nodeNetworkName_Object = MibTableColumn
t5nodeNetworkName = _T5nodeNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 6),
    _T5nodeNetworkName_Type()
)
t5nodeNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeNetworkName.setStatus("mandatory")


class _T5nodeSscpId_Type(Integer32):
    """Custom type t5nodeSscpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T5nodeSscpId_Type.__name__ = "Integer32"
_T5nodeSscpId_Object = MibTableColumn
t5nodeSscpId = _T5nodeSscpId_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 7),
    _T5nodeSscpId_Type()
)
t5nodeSscpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodeSscpId.setStatus("mandatory")


class _T5nodePuName_Type(DisplayString):
    """Custom type t5nodePuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5nodePuName_Type.__name__ = "DisplayString"
_T5nodePuName_Object = MibTableColumn
t5nodePuName = _T5nodePuName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 1, 1, 8),
    _T5nodePuName_Type()
)
t5nodePuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5nodePuName.setStatus("mandatory")
_T5CdrmTable_Object = MibTable
t5CdrmTable = _T5CdrmTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2)
)
if mibBuilder.loadTexts:
    t5CdrmTable.setStatus("mandatory")
_T5CdrmEntry_Object = MibTableRow
t5CdrmEntry = _T5CdrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1)
)
t5CdrmEntry.setIndexNames(
    (0, "SNANET-MIB", "t5CdrmT5nodeIndex"),
    (0, "SNANET-MIB", "t5CdrmName"),
)
if mibBuilder.loadTexts:
    t5CdrmEntry.setStatus("mandatory")
_T5CdrmT5nodeIndex_Type = Integer32
_T5CdrmT5nodeIndex_Object = MibTableColumn
t5CdrmT5nodeIndex = _T5CdrmT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 1),
    _T5CdrmT5nodeIndex_Type()
)
t5CdrmT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmT5nodeIndex.setStatus("mandatory")


class _T5CdrmName_Type(DisplayString):
    """Custom type t5CdrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CdrmName_Type.__name__ = "DisplayString"
_T5CdrmName_Object = MibTableColumn
t5CdrmName = _T5CdrmName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 2),
    _T5CdrmName_Type()
)
t5CdrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmName.setStatus("mandatory")


class _T5CdrmSnaName_Type(DisplayString):
    """Custom type t5CdrmSnaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_T5CdrmSnaName_Type.__name__ = "DisplayString"
_T5CdrmSnaName_Object = MibTableColumn
t5CdrmSnaName = _T5CdrmSnaName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 3),
    _T5CdrmSnaName_Type()
)
t5CdrmSnaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmSnaName.setStatus("mandatory")


class _T5CdrmType_Type(Integer32):
    """Custom type t5CdrmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("snanet", 2))
    )


_T5CdrmType_Type.__name__ = "Integer32"
_T5CdrmType_Object = MibTableColumn
t5CdrmType = _T5CdrmType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 4),
    _T5CdrmType_Type()
)
t5CdrmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmType.setStatus("mandatory")


class _T5CdrmAdminState_Type(Integer32):
    """Custom type t5CdrmAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_T5CdrmAdminState_Type.__name__ = "Integer32"
_T5CdrmAdminState_Object = MibTableColumn
t5CdrmAdminState = _T5CdrmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 5),
    _T5CdrmAdminState_Type()
)
t5CdrmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t5CdrmAdminState.setStatus("mandatory")


class _T5CdrmOperState_Type(Integer32):
    """Custom type t5CdrmOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("down", 2),
          ("up", 1))
    )


_T5CdrmOperState_Type.__name__ = "Integer32"
_T5CdrmOperState_Object = MibTableColumn
t5CdrmOperState = _T5CdrmOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 6),
    _T5CdrmOperState_Type()
)
t5CdrmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmOperState.setStatus("mandatory")


class _T5CdrmSubareaNumber_Type(Integer32):
    """Custom type t5CdrmSubareaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_T5CdrmSubareaNumber_Type.__name__ = "Integer32"
_T5CdrmSubareaNumber_Object = MibTableColumn
t5CdrmSubareaNumber = _T5CdrmSubareaNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 7),
    _T5CdrmSubareaNumber_Type()
)
t5CdrmSubareaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmSubareaNumber.setStatus("mandatory")


class _T5CdrmNetworkName_Type(DisplayString):
    """Custom type t5CdrmNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CdrmNetworkName_Type.__name__ = "DisplayString"
_T5CdrmNetworkName_Object = MibTableColumn
t5CdrmNetworkName = _T5CdrmNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 8),
    _T5CdrmNetworkName_Type()
)
t5CdrmNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmNetworkName.setStatus("mandatory")


class _T5CdrmElementAddress_Type(Integer32):
    """Custom type t5CdrmElementAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_T5CdrmElementAddress_Type.__name__ = "Integer32"
_T5CdrmElementAddress_Object = MibTableColumn
t5CdrmElementAddress = _T5CdrmElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 2, 1, 9),
    _T5CdrmElementAddress_Type()
)
t5CdrmElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrmElementAddress.setStatus("mandatory")
_T5CdrscTable_Object = MibTable
t5CdrscTable = _T5CdrscTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3)
)
if mibBuilder.loadTexts:
    t5CdrscTable.setStatus("mandatory")
_T5CdrscEntry_Object = MibTableRow
t5CdrscEntry = _T5CdrscEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1)
)
t5CdrscEntry.setIndexNames(
    (0, "SNANET-MIB", "t5CdrscT5nodeIndex"),
    (0, "SNANET-MIB", "t5CdrscName"),
)
if mibBuilder.loadTexts:
    t5CdrscEntry.setStatus("mandatory")
_T5CdrscT5nodeIndex_Type = Integer32
_T5CdrscT5nodeIndex_Object = MibTableColumn
t5CdrscT5nodeIndex = _T5CdrscT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 1),
    _T5CdrscT5nodeIndex_Type()
)
t5CdrscT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscT5nodeIndex.setStatus("mandatory")


class _T5CdrscName_Type(DisplayString):
    """Custom type t5CdrscName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CdrscName_Type.__name__ = "DisplayString"
_T5CdrscName_Object = MibTableColumn
t5CdrscName = _T5CdrscName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 2),
    _T5CdrscName_Type()
)
t5CdrscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscName.setStatus("mandatory")


class _T5CdrscSnaName_Type(DisplayString):
    """Custom type t5CdrscSnaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_T5CdrscSnaName_Type.__name__ = "DisplayString"
_T5CdrscSnaName_Object = MibTableColumn
t5CdrscSnaName = _T5CdrscSnaName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 3),
    _T5CdrscSnaName_Type()
)
t5CdrscSnaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscSnaName.setStatus("mandatory")


class _T5CdrscCdrmName_Type(DisplayString):
    """Custom type t5CdrscCdrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CdrscCdrmName_Type.__name__ = "DisplayString"
_T5CdrscCdrmName_Object = MibTableColumn
t5CdrscCdrmName = _T5CdrscCdrmName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 4),
    _T5CdrscCdrmName_Type()
)
t5CdrscCdrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscCdrmName.setStatus("mandatory")


class _T5CdrscAdminState_Type(Integer32):
    """Custom type t5CdrscAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_T5CdrscAdminState_Type.__name__ = "Integer32"
_T5CdrscAdminState_Object = MibTableColumn
t5CdrscAdminState = _T5CdrscAdminState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 5),
    _T5CdrscAdminState_Type()
)
t5CdrscAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t5CdrscAdminState.setStatus("mandatory")


class _T5CdrscOperState_Type(Integer32):
    """Custom type t5CdrscOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("down", 2),
          ("up", 1))
    )


_T5CdrscOperState_Type.__name__ = "Integer32"
_T5CdrscOperState_Object = MibTableColumn
t5CdrscOperState = _T5CdrscOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 6),
    _T5CdrscOperState_Type()
)
t5CdrscOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscOperState.setStatus("mandatory")
_T5CdrscSessions_Type = Counter32
_T5CdrscSessions_Object = MibTableColumn
t5CdrscSessions = _T5CdrscSessions_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 7),
    _T5CdrscSessions_Type()
)
t5CdrscSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscSessions.setStatus("mandatory")


class _T5CdrscDlmName_Type(DisplayString):
    """Custom type t5CdrscDlmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CdrscDlmName_Type.__name__ = "DisplayString"
_T5CdrscDlmName_Object = MibTableColumn
t5CdrscDlmName = _T5CdrscDlmName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 8),
    _T5CdrscDlmName_Type()
)
t5CdrscDlmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscDlmName.setStatus("mandatory")


class _T5CdrscCosName_Type(DisplayString):
    """Custom type t5CdrscCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CdrscCosName_Type.__name__ = "DisplayString"
_T5CdrscCosName_Object = MibTableColumn
t5CdrscCosName = _T5CdrscCosName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 3, 1, 9),
    _T5CdrscCosName_Type()
)
t5CdrscCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CdrscCosName.setStatus("mandatory")
_T5DlmTable_Object = MibTable
t5DlmTable = _T5DlmTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4)
)
if mibBuilder.loadTexts:
    t5DlmTable.setStatus("mandatory")
_T5DlmEntry_Object = MibTableRow
t5DlmEntry = _T5DlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1)
)
t5DlmEntry.setIndexNames(
    (0, "SNANET-MIB", "t5DlmT5nodeIndex"),
    (0, "SNANET-MIB", "t5DlmName"),
)
if mibBuilder.loadTexts:
    t5DlmEntry.setStatus("mandatory")
_T5DlmT5nodeIndex_Type = Integer32
_T5DlmT5nodeIndex_Object = MibTableColumn
t5DlmT5nodeIndex = _T5DlmT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 1),
    _T5DlmT5nodeIndex_Type()
)
t5DlmT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmT5nodeIndex.setStatus("mandatory")


class _T5DlmName_Type(DisplayString):
    """Custom type t5DlmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5DlmName_Type.__name__ = "DisplayString"
_T5DlmName_Object = MibTableColumn
t5DlmName = _T5DlmName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 2),
    _T5DlmName_Type()
)
t5DlmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmName.setStatus("mandatory")


class _T5DlmSnaName_Type(DisplayString):
    """Custom type t5DlmSnaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_T5DlmSnaName_Type.__name__ = "DisplayString"
_T5DlmSnaName_Object = MibTableColumn
t5DlmSnaName = _T5DlmSnaName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 3),
    _T5DlmSnaName_Type()
)
t5DlmSnaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmSnaName.setStatus("mandatory")


class _T5DlmFmprof_Type(OctetString):
    """Custom type t5DlmFmprof based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmFmprof_Type.__name__ = "OctetString"
_T5DlmFmprof_Object = MibTableColumn
t5DlmFmprof = _T5DlmFmprof_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 4),
    _T5DlmFmprof_Type()
)
t5DlmFmprof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmFmprof.setStatus("mandatory")


class _T5DlmTsprof_Type(OctetString):
    """Custom type t5DlmTsprof based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmTsprof_Type.__name__ = "OctetString"
_T5DlmTsprof_Object = MibTableColumn
t5DlmTsprof = _T5DlmTsprof_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 5),
    _T5DlmTsprof_Type()
)
t5DlmTsprof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmTsprof.setStatus("mandatory")


class _T5DlmPriprot_Type(OctetString):
    """Custom type t5DlmPriprot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmPriprot_Type.__name__ = "OctetString"
_T5DlmPriprot_Object = MibTableColumn
t5DlmPriprot = _T5DlmPriprot_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 6),
    _T5DlmPriprot_Type()
)
t5DlmPriprot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmPriprot.setStatus("mandatory")


class _T5DlmSecprot_Type(OctetString):
    """Custom type t5DlmSecprot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmSecprot_Type.__name__ = "OctetString"
_T5DlmSecprot_Object = MibTableColumn
t5DlmSecprot = _T5DlmSecprot_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 7),
    _T5DlmSecprot_Type()
)
t5DlmSecprot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmSecprot.setStatus("mandatory")


class _T5DlmComprot_Type(OctetString):
    """Custom type t5DlmComprot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_T5DlmComprot_Type.__name__ = "OctetString"
_T5DlmComprot_Object = MibTableColumn
t5DlmComprot = _T5DlmComprot_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 8),
    _T5DlmComprot_Type()
)
t5DlmComprot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmComprot.setStatus("mandatory")


class _T5DlmRusizes_Type(OctetString):
    """Custom type t5DlmRusizes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_T5DlmRusizes_Type.__name__ = "OctetString"
_T5DlmRusizes_Object = MibTableColumn
t5DlmRusizes = _T5DlmRusizes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 9),
    _T5DlmRusizes_Type()
)
t5DlmRusizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmRusizes.setStatus("mandatory")


class _T5DlmPservic_Type(OctetString):
    """Custom type t5DlmPservic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_T5DlmPservic_Type.__name__ = "OctetString"
_T5DlmPservic_Object = MibTableColumn
t5DlmPservic = _T5DlmPservic_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 10),
    _T5DlmPservic_Type()
)
t5DlmPservic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmPservic.setStatus("mandatory")


class _T5DlmPsndpac_Type(OctetString):
    """Custom type t5DlmPsndpac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmPsndpac_Type.__name__ = "OctetString"
_T5DlmPsndpac_Object = MibTableColumn
t5DlmPsndpac = _T5DlmPsndpac_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 11),
    _T5DlmPsndpac_Type()
)
t5DlmPsndpac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmPsndpac.setStatus("mandatory")


class _T5DlmPrcvpac_Type(OctetString):
    """Custom type t5DlmPrcvpac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmPrcvpac_Type.__name__ = "OctetString"
_T5DlmPrcvpac_Object = MibTableColumn
t5DlmPrcvpac = _T5DlmPrcvpac_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 12),
    _T5DlmPrcvpac_Type()
)
t5DlmPrcvpac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmPrcvpac.setStatus("mandatory")


class _T5DlmSsndpac_Type(OctetString):
    """Custom type t5DlmSsndpac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmSsndpac_Type.__name__ = "OctetString"
_T5DlmSsndpac_Object = MibTableColumn
t5DlmSsndpac = _T5DlmSsndpac_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 13),
    _T5DlmSsndpac_Type()
)
t5DlmSsndpac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmSsndpac.setStatus("mandatory")


class _T5DlmSrcvpac_Type(OctetString):
    """Custom type t5DlmSrcvpac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T5DlmSrcvpac_Type.__name__ = "OctetString"
_T5DlmSrcvpac_Object = MibTableColumn
t5DlmSrcvpac = _T5DlmSrcvpac_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 14),
    _T5DlmSrcvpac_Type()
)
t5DlmSrcvpac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmSrcvpac.setStatus("mandatory")


class _T5DlmEncr_Type(Integer32):
    """Custom type t5DlmEncr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_T5DlmEncr_Type.__name__ = "Integer32"
_T5DlmEncr_Object = MibTableColumn
t5DlmEncr = _T5DlmEncr_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 15),
    _T5DlmEncr_Type()
)
t5DlmEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmEncr.setStatus("mandatory")


class _T5DlmBindType_Type(Integer32):
    """Custom type t5DlmBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_T5DlmBindType_Type.__name__ = "Integer32"
_T5DlmBindType_Object = MibTableColumn
t5DlmBindType = _T5DlmBindType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 16),
    _T5DlmBindType_Type()
)
t5DlmBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmBindType.setStatus("mandatory")


class _T5DlmCos_Type(DisplayString):
    """Custom type t5DlmCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5DlmCos_Type.__name__ = "DisplayString"
_T5DlmCos_Object = MibTableColumn
t5DlmCos = _T5DlmCos_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 4, 1, 17),
    _T5DlmCos_Type()
)
t5DlmCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5DlmCos.setStatus("mandatory")
_T5CosTable_Object = MibTable
t5CosTable = _T5CosTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 5)
)
if mibBuilder.loadTexts:
    t5CosTable.setStatus("mandatory")
_T5CosEntry_Object = MibTableRow
t5CosEntry = _T5CosEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 5, 1)
)
t5CosEntry.setIndexNames(
    (0, "SNANET-MIB", "t5CosT5nodeIndex"),
    (0, "SNANET-MIB", "t5CosName"),
)
if mibBuilder.loadTexts:
    t5CosEntry.setStatus("mandatory")
_T5CosT5nodeIndex_Type = Integer32
_T5CosT5nodeIndex_Object = MibTableColumn
t5CosT5nodeIndex = _T5CosT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 5, 1, 1),
    _T5CosT5nodeIndex_Type()
)
t5CosT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CosT5nodeIndex.setStatus("mandatory")


class _T5CosName_Type(DisplayString):
    """Custom type t5CosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5CosName_Type.__name__ = "DisplayString"
_T5CosName_Object = MibTableColumn
t5CosName = _T5CosName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 5, 1, 2),
    _T5CosName_Type()
)
t5CosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CosName.setStatus("mandatory")


class _T5CosSnaName_Type(DisplayString):
    """Custom type t5CosSnaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_T5CosSnaName_Type.__name__ = "DisplayString"
_T5CosSnaName_Object = MibTableColumn
t5CosSnaName = _T5CosSnaName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 5, 1, 3),
    _T5CosSnaName_Type()
)
t5CosSnaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CosSnaName.setStatus("mandatory")


class _T5CosVrids_Type(OctetString):
    """Custom type t5CosVrids based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 48),
    )


_T5CosVrids_Type.__name__ = "OctetString"
_T5CosVrids_Object = MibTableColumn
t5CosVrids = _T5CosVrids_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 5, 1, 4),
    _T5CosVrids_Type()
)
t5CosVrids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5CosVrids.setStatus("mandatory")
_T5AliasTable_Object = MibTable
t5AliasTable = _T5AliasTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 6)
)
if mibBuilder.loadTexts:
    t5AliasTable.setStatus("mandatory")
_T5AliasEntry_Object = MibTableRow
t5AliasEntry = _T5AliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 6, 1)
)
t5AliasEntry.setIndexNames(
    (0, "SNANET-MIB", "t5AliasT5nodeIndex"),
    (0, "SNANET-MIB", "t5AliasName"),
)
if mibBuilder.loadTexts:
    t5AliasEntry.setStatus("mandatory")
_T5AliasT5nodeIndex_Type = Integer32
_T5AliasT5nodeIndex_Object = MibTableColumn
t5AliasT5nodeIndex = _T5AliasT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 6, 1, 1),
    _T5AliasT5nodeIndex_Type()
)
t5AliasT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5AliasT5nodeIndex.setStatus("mandatory")


class _T5AliasName_Type(DisplayString):
    """Custom type t5AliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T5AliasName_Type.__name__ = "DisplayString"
_T5AliasName_Object = MibTableColumn
t5AliasName = _T5AliasName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 6, 1, 2),
    _T5AliasName_Type()
)
t5AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5AliasName.setStatus("mandatory")
_T5AliasResourceId_Type = ObjectIdentifier
_T5AliasResourceId_Object = MibTableColumn
t5AliasResourceId = _T5AliasResourceId_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 2, 6, 1, 3),
    _T5AliasResourceId_Type()
)
t5AliasResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t5AliasResourceId.setStatus("mandatory")
_Subarea_ObjectIdentity = ObjectIdentity
subarea = _Subarea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3)
)
_SaErTable_Object = MibTable
saErTable = _SaErTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1)
)
if mibBuilder.loadTexts:
    saErTable.setStatus("mandatory")
_SaErEntry_Object = MibTableRow
saErEntry = _SaErEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1, 1)
)
saErEntry.setIndexNames(
    (0, "SNANET-MIB", "saErT5nodeIndex"),
    (0, "SNANET-MIB", "saErDestinationSubarea"),
    (0, "SNANET-MIB", "saErNumber"),
)
if mibBuilder.loadTexts:
    saErEntry.setStatus("mandatory")
_SaErT5nodeIndex_Type = Integer32
_SaErT5nodeIndex_Object = MibTableColumn
saErT5nodeIndex = _SaErT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1, 1, 1),
    _SaErT5nodeIndex_Type()
)
saErT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saErT5nodeIndex.setStatus("mandatory")


class _SaErDestinationSubarea_Type(Integer32):
    """Custom type saErDestinationSubarea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SaErDestinationSubarea_Type.__name__ = "Integer32"
_SaErDestinationSubarea_Object = MibTableColumn
saErDestinationSubarea = _SaErDestinationSubarea_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1, 1, 2),
    _SaErDestinationSubarea_Type()
)
saErDestinationSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saErDestinationSubarea.setStatus("mandatory")


class _SaErNumber_Type(Integer32):
    """Custom type saErNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SaErNumber_Type.__name__ = "Integer32"
_SaErNumber_Object = MibTableColumn
saErNumber = _SaErNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1, 1, 3),
    _SaErNumber_Type()
)
saErNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saErNumber.setStatus("mandatory")


class _SaErTgNumber_Type(Integer32):
    """Custom type saErTgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaErTgNumber_Type.__name__ = "Integer32"
_SaErTgNumber_Object = MibTableColumn
saErTgNumber = _SaErTgNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1, 1, 4),
    _SaErTgNumber_Type()
)
saErTgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saErTgNumber.setStatus("mandatory")


class _SaErOperState_Type(Integer32):
    """Custom type saErOperState based on Integer32"""
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
        *(("actNoSend", 7),
          ("actPend", 4),
          ("active", 8),
          ("innAct", 6),
          ("innActPend", 5),
          ("inoperative", 2),
          ("operative", 3),
          ("other", 1))
    )


_SaErOperState_Type.__name__ = "Integer32"
_SaErOperState_Object = MibTableColumn
saErOperState = _SaErOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 1, 1, 5),
    _SaErOperState_Type()
)
saErOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saErOperState.setStatus("mandatory")
_SaVrTable_Object = MibTable
saVrTable = _SaVrTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2)
)
if mibBuilder.loadTexts:
    saVrTable.setStatus("mandatory")
_SaVrEntry_Object = MibTableRow
saVrEntry = _SaVrEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1)
)
saVrEntry.setIndexNames(
    (0, "SNANET-MIB", "saVrT5nodeIndex"),
    (0, "SNANET-MIB", "saVrErNumber"),
    (0, "SNANET-MIB", "saVrNumber"),
    (0, "SNANET-MIB", "saVrTransmissionPriority"),
)
if mibBuilder.loadTexts:
    saVrEntry.setStatus("mandatory")
_SaVrT5nodeIndex_Type = Integer32
_SaVrT5nodeIndex_Object = MibTableColumn
saVrT5nodeIndex = _SaVrT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 1),
    _SaVrT5nodeIndex_Type()
)
saVrT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrT5nodeIndex.setStatus("mandatory")


class _SaVrErNumber_Type(Integer32):
    """Custom type saVrErNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SaVrErNumber_Type.__name__ = "Integer32"
_SaVrErNumber_Object = MibTableColumn
saVrErNumber = _SaVrErNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 2),
    _SaVrErNumber_Type()
)
saVrErNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrErNumber.setStatus("mandatory")


class _SaVrNumber_Type(Integer32):
    """Custom type saVrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SaVrNumber_Type.__name__ = "Integer32"
_SaVrNumber_Object = MibTableColumn
saVrNumber = _SaVrNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 3),
    _SaVrNumber_Type()
)
saVrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrNumber.setStatus("mandatory")


class _SaVrTransmissionPriority_Type(Integer32):
    """Custom type saVrTransmissionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SaVrTransmissionPriority_Type.__name__ = "Integer32"
_SaVrTransmissionPriority_Object = MibTableColumn
saVrTransmissionPriority = _SaVrTransmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 4),
    _SaVrTransmissionPriority_Type()
)
saVrTransmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrTransmissionPriority.setStatus("mandatory")


class _SaVrWindowSize_Type(Integer32):
    """Custom type saVrWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaVrWindowSize_Type.__name__ = "Integer32"
_SaVrWindowSize_Object = MibTableColumn
saVrWindowSize = _SaVrWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 5),
    _SaVrWindowSize_Type()
)
saVrWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrWindowSize.setStatus("mandatory")


class _SaVrMinWindowSize_Type(Integer32):
    """Custom type saVrMinWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaVrMinWindowSize_Type.__name__ = "Integer32"
_SaVrMinWindowSize_Object = MibTableColumn
saVrMinWindowSize = _SaVrMinWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 6),
    _SaVrMinWindowSize_Type()
)
saVrMinWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrMinWindowSize.setStatus("mandatory")


class _SaVrMaxWindowSize_Type(Integer32):
    """Custom type saVrMaxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaVrMaxWindowSize_Type.__name__ = "Integer32"
_SaVrMaxWindowSize_Object = MibTableColumn
saVrMaxWindowSize = _SaVrMaxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 7),
    _SaVrMaxWindowSize_Type()
)
saVrMaxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrMaxWindowSize.setStatus("mandatory")


class _SaVrPacingCount_Type(Integer32):
    """Custom type saVrPacingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaVrPacingCount_Type.__name__ = "Integer32"
_SaVrPacingCount_Object = MibTableColumn
saVrPacingCount = _SaVrPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 2, 1, 8),
    _SaVrPacingCount_Type()
)
saVrPacingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saVrPacingCount.setStatus("mandatory")
_SaTransmissionGroup_ObjectIdentity = ObjectIdentity
saTransmissionGroup = _SaTransmissionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3)
)
_SaTgTable_Object = MibTable
saTgTable = _SaTgTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    saTgTable.setStatus("mandatory")
_SaTgEntry_Object = MibTableRow
saTgEntry = _SaTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1)
)
saTgEntry.setIndexNames(
    (0, "SNANET-MIB", "saTgT5nodeIndex"),
    (0, "SNANET-MIB", "saTgNumber"),
    (0, "SNANET-MIB", "saTgAdjacentSubarea"),
)
if mibBuilder.loadTexts:
    saTgEntry.setStatus("mandatory")
_SaTgT5nodeIndex_Type = Integer32
_SaTgT5nodeIndex_Object = MibTableColumn
saTgT5nodeIndex = _SaTgT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 1),
    _SaTgT5nodeIndex_Type()
)
saTgT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgT5nodeIndex.setStatus("mandatory")


class _SaTgNumber_Type(Integer32):
    """Custom type saTgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SaTgNumber_Type.__name__ = "Integer32"
_SaTgNumber_Object = MibTableColumn
saTgNumber = _SaTgNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 2),
    _SaTgNumber_Type()
)
saTgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgNumber.setStatus("mandatory")


class _SaTgAdjacentSubarea_Type(Integer32):
    """Custom type saTgAdjacentSubarea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SaTgAdjacentSubarea_Type.__name__ = "Integer32"
_SaTgAdjacentSubarea_Object = MibTableColumn
saTgAdjacentSubarea = _SaTgAdjacentSubarea_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 3),
    _SaTgAdjacentSubarea_Type()
)
saTgAdjacentSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgAdjacentSubarea.setStatus("mandatory")


class _SaTgOperState_Type(Integer32):
    """Custom type saTgOperState based on Integer32"""
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
        *(("active", 2),
          ("inactive", 1),
          ("pendActive", 3),
          ("pendInactive", 4))
    )


_SaTgOperState_Type.__name__ = "Integer32"
_SaTgOperState_Object = MibTableColumn
saTgOperState = _SaTgOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 4),
    _SaTgOperState_Type()
)
saTgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgOperState.setStatus("mandatory")


class _SaTgMaxSendPiuSize_Type(Integer32):
    """Custom type saTgMaxSendPiuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65565),
    )


_SaTgMaxSendPiuSize_Type.__name__ = "Integer32"
_SaTgMaxSendPiuSize_Object = MibTableColumn
saTgMaxSendPiuSize = _SaTgMaxSendPiuSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 5),
    _SaTgMaxSendPiuSize_Type()
)
saTgMaxSendPiuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgMaxSendPiuSize.setStatus("mandatory")


class _SaTgMaxReceivePiuSize_Type(Integer32):
    """Custom type saTgMaxReceivePiuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SaTgMaxReceivePiuSize_Type.__name__ = "Integer32"
_SaTgMaxReceivePiuSize_Object = MibTableColumn
saTgMaxReceivePiuSize = _SaTgMaxReceivePiuSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 6),
    _SaTgMaxReceivePiuSize_Type()
)
saTgMaxReceivePiuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgMaxReceivePiuSize.setStatus("mandatory")
_SaTgActiveTime_Type = TimeTicks
_SaTgActiveTime_Object = MibTableColumn
saTgActiveTime = _SaTgActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 7),
    _SaTgActiveTime_Type()
)
saTgActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgActiveTime.setStatus("mandatory")
_SaTgLastStateChange_Type = TimeTicks
_SaTgLastStateChange_Object = MibTableColumn
saTgLastStateChange = _SaTgLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 8),
    _SaTgLastStateChange_Type()
)
saTgLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLastStateChange.setStatus("mandatory")
_SaTgSentBytes_Type = Counter32
_SaTgSentBytes_Object = MibTableColumn
saTgSentBytes = _SaTgSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 9),
    _SaTgSentBytes_Type()
)
saTgSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgSentBytes.setStatus("mandatory")
_SaTgReceivedBytes_Type = Counter32
_SaTgReceivedBytes_Object = MibTableColumn
saTgReceivedBytes = _SaTgReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 10),
    _SaTgReceivedBytes_Type()
)
saTgReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgReceivedBytes.setStatus("mandatory")
_SaTgSentBtus_Type = Counter32
_SaTgSentBtus_Object = MibTableColumn
saTgSentBtus = _SaTgSentBtus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 11),
    _SaTgSentBtus_Type()
)
saTgSentBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgSentBtus.setStatus("mandatory")
_SaTgReceivedBtus_Type = Counter32
_SaTgReceivedBtus_Object = MibTableColumn
saTgReceivedBtus = _SaTgReceivedBtus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 1, 1, 12),
    _SaTgReceivedBtus_Type()
)
saTgReceivedBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgReceivedBtus.setStatus("mandatory")
_SaTgLinkTable_Object = MibTable
saTgLinkTable = _SaTgLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    saTgLinkTable.setStatus("mandatory")
_SaTgLinkEntry_Object = MibTableRow
saTgLinkEntry = _SaTgLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1)
)
saTgLinkEntry.setIndexNames(
    (0, "SNANET-MIB", "saTgLinkT5nodeIndex"),
    (0, "SNANET-MIB", "saTgLinkIndex"),
)
if mibBuilder.loadTexts:
    saTgLinkEntry.setStatus("mandatory")
_SaTgLinkT5nodeIndex_Type = Integer32
_SaTgLinkT5nodeIndex_Object = MibTableColumn
saTgLinkT5nodeIndex = _SaTgLinkT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 1),
    _SaTgLinkT5nodeIndex_Type()
)
saTgLinkT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkT5nodeIndex.setStatus("mandatory")
_SaTgLinkIndex_Type = Integer32
_SaTgLinkIndex_Object = MibTableColumn
saTgLinkIndex = _SaTgLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 2),
    _SaTgLinkIndex_Type()
)
saTgLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkIndex.setStatus("mandatory")


class _SaTgLinkTgNumber_Type(Integer32):
    """Custom type saTgLinkTgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaTgLinkTgNumber_Type.__name__ = "Integer32"
_SaTgLinkTgNumber_Object = MibTableColumn
saTgLinkTgNumber = _SaTgLinkTgNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 3),
    _SaTgLinkTgNumber_Type()
)
saTgLinkTgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkTgNumber.setStatus("mandatory")


class _SaTgLinkAdjacentSubarea_Type(Integer32):
    """Custom type saTgLinkAdjacentSubarea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SaTgLinkAdjacentSubarea_Type.__name__ = "Integer32"
_SaTgLinkAdjacentSubarea_Object = MibTableColumn
saTgLinkAdjacentSubarea = _SaTgLinkAdjacentSubarea_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 4),
    _SaTgLinkAdjacentSubarea_Type()
)
saTgLinkAdjacentSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkAdjacentSubarea.setStatus("mandatory")


class _SaTgLinkName_Type(DisplayString):
    """Custom type saTgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SaTgLinkName_Type.__name__ = "DisplayString"
_SaTgLinkName_Object = MibTableColumn
saTgLinkName = _SaTgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 5),
    _SaTgLinkName_Type()
)
saTgLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkName.setStatus("mandatory")


class _SaTgLinkOperState_Type(Integer32):
    """Custom type saTgLinkOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SaTgLinkOperState_Type.__name__ = "Integer32"
_SaTgLinkOperState_Object = MibTableColumn
saTgLinkOperState = _SaTgLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 6),
    _SaTgLinkOperState_Type()
)
saTgLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkOperState.setStatus("mandatory")


class _SaTgLinkAdminState_Type(Integer32):
    """Custom type saTgLinkAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_SaTgLinkAdminState_Type.__name__ = "Integer32"
_SaTgLinkAdminState_Object = MibTableColumn
saTgLinkAdminState = _SaTgLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 7),
    _SaTgLinkAdminState_Type()
)
saTgLinkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTgLinkAdminState.setStatus("mandatory")


class _SaTgLinkType_Type(Integer32):
    """Custom type saTgLinkType based on Integer32"""
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
        *(("channel", 5),
          ("internal", 1),
          ("link8022", 2),
          ("qllc", 3),
          ("sdlc", 4))
    )


_SaTgLinkType_Type.__name__ = "Integer32"
_SaTgLinkType_Object = MibTableColumn
saTgLinkType = _SaTgLinkType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 8),
    _SaTgLinkType_Type()
)
saTgLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkType.setStatus("mandatory")
_SaTgLinkSpecific_Type = ObjectIdentifier
_SaTgLinkSpecific_Object = MibTableColumn
saTgLinkSpecific = _SaTgLinkSpecific_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 9),
    _SaTgLinkSpecific_Type()
)
saTgLinkSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkSpecific.setStatus("mandatory")
_SaTgLinkActiveTime_Type = TimeTicks
_SaTgLinkActiveTime_Object = MibTableColumn
saTgLinkActiveTime = _SaTgLinkActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 10),
    _SaTgLinkActiveTime_Type()
)
saTgLinkActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkActiveTime.setStatus("mandatory")
_SaTgLinkLastStateChange_Type = TimeTicks
_SaTgLinkLastStateChange_Object = MibTableColumn
saTgLinkLastStateChange = _SaTgLinkLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 11),
    _SaTgLinkLastStateChange_Type()
)
saTgLinkLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkLastStateChange.setStatus("mandatory")
_SaTgLinkSentBytes_Type = Counter32
_SaTgLinkSentBytes_Object = MibTableColumn
saTgLinkSentBytes = _SaTgLinkSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 12),
    _SaTgLinkSentBytes_Type()
)
saTgLinkSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkSentBytes.setStatus("mandatory")
_SaTgLinkReceivedBytes_Type = Counter32
_SaTgLinkReceivedBytes_Object = MibTableColumn
saTgLinkReceivedBytes = _SaTgLinkReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 13),
    _SaTgLinkReceivedBytes_Type()
)
saTgLinkReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkReceivedBytes.setStatus("mandatory")
_SaTgLinkSentBtus_Type = Counter32
_SaTgLinkSentBtus_Object = MibTableColumn
saTgLinkSentBtus = _SaTgLinkSentBtus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 14),
    _SaTgLinkSentBtus_Type()
)
saTgLinkSentBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkSentBtus.setStatus("mandatory")
_SaTgLinkReceivedBtus_Type = Counter32
_SaTgLinkReceivedBtus_Object = MibTableColumn
saTgLinkReceivedBtus = _SaTgLinkReceivedBtus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 3, 3, 2, 1, 15),
    _SaTgLinkReceivedBtus_Type()
)
saTgLinkReceivedBtus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTgLinkReceivedBtus.setStatus("mandatory")
_SnaNau_ObjectIdentity = ObjectIdentity
snaNau = _SnaNau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4)
)
_T2node_ObjectIdentity = ObjectIdentity
t2node = _T2node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1)
)
_T2nodeTable_Object = MibTable
t2nodeTable = _T2nodeTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    t2nodeTable.setStatus("mandatory")
_T2nodeEntry_Object = MibTableRow
t2nodeEntry = _T2nodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1)
)
t2nodeEntry.setIndexNames(
    (0, "SNANET-MIB", "t2nodeT5nodeIndex"),
    (0, "SNANET-MIB", "t2nodeIndex"),
)
if mibBuilder.loadTexts:
    t2nodeEntry.setStatus("mandatory")
_T2nodeT5nodeIndex_Type = Integer32
_T2nodeT5nodeIndex_Object = MibTableColumn
t2nodeT5nodeIndex = _T2nodeT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 1),
    _T2nodeT5nodeIndex_Type()
)
t2nodeT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeT5nodeIndex.setStatus("mandatory")
_T2nodeIndex_Type = Integer32
_T2nodeIndex_Object = MibTableColumn
t2nodeIndex = _T2nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 2),
    _T2nodeIndex_Type()
)
t2nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeIndex.setStatus("mandatory")


class _T2nodeName_Type(DisplayString):
    """Custom type t2nodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_T2nodeName_Type.__name__ = "DisplayString"
_T2nodeName_Object = MibTableColumn
t2nodeName = _T2nodeName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 3),
    _T2nodeName_Type()
)
t2nodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeName.setStatus("mandatory")


class _T2nodeType_Type(Integer32):
    """Custom type t2nodeType based on Integer32"""
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
        *(("other", 1),
          ("pu20prim", 2),
          ("pu20sec", 3),
          ("t21LEN", 4))
    )


_T2nodeType_Type.__name__ = "Integer32"
_T2nodeType_Object = MibTableColumn
t2nodeType = _T2nodeType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 4),
    _T2nodeType_Type()
)
t2nodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeType.setStatus("mandatory")


class _T2nodeBlockNum_Type(DisplayString):
    """Custom type t2nodeBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T2nodeBlockNum_Type.__name__ = "DisplayString"
_T2nodeBlockNum_Object = MibTableColumn
t2nodeBlockNum = _T2nodeBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 5),
    _T2nodeBlockNum_Type()
)
t2nodeBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeBlockNum.setStatus("mandatory")


class _T2nodeIdNum_Type(OctetString):
    """Custom type t2nodeIdNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_T2nodeIdNum_Type.__name__ = "OctetString"
_T2nodeIdNum_Object = MibTableColumn
t2nodeIdNum = _T2nodeIdNum_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 6),
    _T2nodeIdNum_Type()
)
t2nodeIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeIdNum.setStatus("mandatory")
_T2nodeMaxPiu_Type = Integer32
_T2nodeMaxPiu_Object = MibTableColumn
t2nodeMaxPiu = _T2nodeMaxPiu_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 7),
    _T2nodeMaxPiu_Type()
)
t2nodeMaxPiu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeMaxPiu.setStatus("mandatory")


class _T2nodeLinkType_Type(Integer32):
    """Custom type t2nodeLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("channelAttach", 5),
          ("internal", 1),
          ("link8022", 2),
          ("qllc", 3),
          ("sdlc", 4),
          ("tcpip", 6))
    )


_T2nodeLinkType_Type.__name__ = "Integer32"
_T2nodeLinkType_Object = MibTableColumn
t2nodeLinkType = _T2nodeLinkType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 8),
    _T2nodeLinkType_Type()
)
t2nodeLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeLinkType.setStatus("mandatory")
_T2nodeLinkSpecific_Type = ObjectIdentifier
_T2nodeLinkSpecific_Object = MibTableColumn
t2nodeLinkSpecific = _T2nodeLinkSpecific_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 9),
    _T2nodeLinkSpecific_Type()
)
t2nodeLinkSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeLinkSpecific.setStatus("mandatory")


class _T2nodeOperState_Type(Integer32):
    """Custom type t2nodeOperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_T2nodeOperState_Type.__name__ = "Integer32"
_T2nodeOperState_Object = MibTableColumn
t2nodeOperState = _T2nodeOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 10),
    _T2nodeOperState_Type()
)
t2nodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeOperState.setStatus("mandatory")


class _T2nodeAdminState_Type(Integer32):
    """Custom type t2nodeAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2),
          ("stop", 3))
    )


_T2nodeAdminState_Type.__name__ = "Integer32"
_T2nodeAdminState_Object = MibTableColumn
t2nodeAdminState = _T2nodeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 11),
    _T2nodeAdminState_Type()
)
t2nodeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t2nodeAdminState.setStatus("mandatory")
_T2nodeStartTime_Type = TimeTicks
_T2nodeStartTime_Object = MibTableColumn
t2nodeStartTime = _T2nodeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 12),
    _T2nodeStartTime_Type()
)
t2nodeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStartTime.setStatus("mandatory")
_T2nodeLastStateChange_Type = TimeTicks
_T2nodeLastStateChange_Object = MibTableColumn
t2nodeLastStateChange = _T2nodeLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 13),
    _T2nodeLastStateChange_Type()
)
t2nodeLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeLastStateChange.setStatus("mandatory")
_T2nodeActFailureReason_Type = Integer32
_T2nodeActFailureReason_Object = MibTableColumn
t2nodeActFailureReason = _T2nodeActFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 1, 1, 14),
    _T2nodeActFailureReason_Type()
)
t2nodeActFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeActFailureReason.setStatus("mandatory")
_T2nodeStatsTable_Object = MibTable
t2nodeStatsTable = _T2nodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    t2nodeStatsTable.setStatus("mandatory")
_T2nodeStatsEntry_Object = MibTableRow
t2nodeStatsEntry = _T2nodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1)
)
t2nodeStatsEntry.setIndexNames(
    (0, "SNANET-MIB", "t2nodeStatsT5nodeIndex"),
    (0, "SNANET-MIB", "t2nodeStatsIndex"),
)
if mibBuilder.loadTexts:
    t2nodeStatsEntry.setStatus("mandatory")
_T2nodeStatsT5nodeIndex_Type = Integer32
_T2nodeStatsT5nodeIndex_Object = MibTableColumn
t2nodeStatsT5nodeIndex = _T2nodeStatsT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 1),
    _T2nodeStatsT5nodeIndex_Type()
)
t2nodeStatsT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsT5nodeIndex.setStatus("mandatory")
_T2nodeStatsIndex_Type = Integer32
_T2nodeStatsIndex_Object = MibTableColumn
t2nodeStatsIndex = _T2nodeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 2),
    _T2nodeStatsIndex_Type()
)
t2nodeStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsIndex.setStatus("mandatory")
_T2nodeStatsSentBytes_Type = Counter32
_T2nodeStatsSentBytes_Object = MibTableColumn
t2nodeStatsSentBytes = _T2nodeStatsSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 3),
    _T2nodeStatsSentBytes_Type()
)
t2nodeStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsSentBytes.setStatus("mandatory")
_T2nodeStatsReceivedBytes_Type = Counter32
_T2nodeStatsReceivedBytes_Object = MibTableColumn
t2nodeStatsReceivedBytes = _T2nodeStatsReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 4),
    _T2nodeStatsReceivedBytes_Type()
)
t2nodeStatsReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsReceivedBytes.setStatus("mandatory")
_T2nodeStatsSentPius_Type = Counter32
_T2nodeStatsSentPius_Object = MibTableColumn
t2nodeStatsSentPius = _T2nodeStatsSentPius_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 5),
    _T2nodeStatsSentPius_Type()
)
t2nodeStatsSentPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsSentPius.setStatus("mandatory")
_T2nodeStatsReceivedPius_Type = Counter32
_T2nodeStatsReceivedPius_Object = MibTableColumn
t2nodeStatsReceivedPius = _T2nodeStatsReceivedPius_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 6),
    _T2nodeStatsReceivedPius_Type()
)
t2nodeStatsReceivedPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsReceivedPius.setStatus("mandatory")
_T2nodeStatsSentNegativeResps_Type = Counter32
_T2nodeStatsSentNegativeResps_Object = MibTableColumn
t2nodeStatsSentNegativeResps = _T2nodeStatsSentNegativeResps_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 7),
    _T2nodeStatsSentNegativeResps_Type()
)
t2nodeStatsSentNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsSentNegativeResps.setStatus("mandatory")
_T2nodeStatsReceivedNegativeResps_Type = Counter32
_T2nodeStatsReceivedNegativeResps_Object = MibTableColumn
t2nodeStatsReceivedNegativeResps = _T2nodeStatsReceivedNegativeResps_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 8),
    _T2nodeStatsReceivedNegativeResps_Type()
)
t2nodeStatsReceivedNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsReceivedNegativeResps.setStatus("mandatory")
_T2nodeStatsActiveLus_Type = Gauge32
_T2nodeStatsActiveLus_Object = MibTableColumn
t2nodeStatsActiveLus = _T2nodeStatsActiveLus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 9),
    _T2nodeStatsActiveLus_Type()
)
t2nodeStatsActiveLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsActiveLus.setStatus("mandatory")
_T2nodeStatsActLus_Type = Gauge32
_T2nodeStatsActLus_Object = MibTableColumn
t2nodeStatsActLus = _T2nodeStatsActLus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 10),
    _T2nodeStatsActLus_Type()
)
t2nodeStatsActLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsActLus.setStatus("mandatory")
_T2nodeStatsInActLus_Type = Gauge32
_T2nodeStatsInActLus_Object = MibTableColumn
t2nodeStatsInActLus = _T2nodeStatsInActLus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 11),
    _T2nodeStatsInActLus_Type()
)
t2nodeStatsInActLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsInActLus.setStatus("mandatory")
_T2nodeStatsBindLus_Type = Gauge32
_T2nodeStatsBindLus_Object = MibTableColumn
t2nodeStatsBindLus = _T2nodeStatsBindLus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 1, 2, 1, 12),
    _T2nodeStatsBindLus_Type()
)
t2nodeStatsBindLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2nodeStatsBindLus.setStatus("mandatory")
_SnaLu_ObjectIdentity = ObjectIdentity
snaLu = _SnaLu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2)
)
_SnaLuTable_Object = MibTable
snaLuTable = _SnaLuTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    snaLuTable.setStatus("mandatory")
_SnaLuEntry_Object = MibTableRow
snaLuEntry = _SnaLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1)
)
snaLuEntry.setIndexNames(
    (0, "SNANET-MIB", "snaLuT5nodeIndex"),
    (0, "SNANET-MIB", "snaLuT2nodeIndex"),
    (0, "SNANET-MIB", "snaLuIndex"),
)
if mibBuilder.loadTexts:
    snaLuEntry.setStatus("mandatory")
_SnaLuT5nodeIndex_Type = Integer32
_SnaLuT5nodeIndex_Object = MibTableColumn
snaLuT5nodeIndex = _SnaLuT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 1),
    _SnaLuT5nodeIndex_Type()
)
snaLuT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuT5nodeIndex.setStatus("mandatory")
_SnaLuT2nodeIndex_Type = Integer32
_SnaLuT2nodeIndex_Object = MibTableColumn
snaLuT2nodeIndex = _SnaLuT2nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 2),
    _SnaLuT2nodeIndex_Type()
)
snaLuT2nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuT2nodeIndex.setStatus("mandatory")
_SnaLuIndex_Type = Integer32
_SnaLuIndex_Object = MibTableColumn
snaLuIndex = _SnaLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 3),
    _SnaLuIndex_Type()
)
snaLuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuIndex.setStatus("mandatory")


class _SnaLuName_Type(DisplayString):
    """Custom type snaLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnaLuName_Type.__name__ = "DisplayString"
_SnaLuName_Object = MibTableColumn
snaLuName = _SnaLuName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 4),
    _SnaLuName_Type()
)
snaLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuName.setStatus("mandatory")


class _SnaLuType_Type(Integer32):
    """Custom type snaLuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lu0", 2),
          ("lu1", 3),
          ("lu2", 4),
          ("lu3", 5),
          ("lu62", 6),
          ("other", 1))
    )


_SnaLuType_Type.__name__ = "Integer32"
_SnaLuType_Object = MibTableColumn
snaLuType = _SnaLuType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 5),
    _SnaLuType_Type()
)
snaLuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuType.setStatus("mandatory")


class _SnaLuLocalAddress_Type(OctetString):
    """Custom type snaLuLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SnaLuLocalAddress_Type.__name__ = "OctetString"
_SnaLuLocalAddress_Object = MibTableColumn
snaLuLocalAddress = _SnaLuLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 6),
    _SnaLuLocalAddress_Type()
)
snaLuLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuLocalAddress.setStatus("mandatory")


class _SnaLuUserName_Type(DisplayString):
    """Custom type snaLuUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnaLuUserName_Type.__name__ = "DisplayString"
_SnaLuUserName_Object = MibTableColumn
snaLuUserName = _SnaLuUserName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 7),
    _SnaLuUserName_Type()
)
snaLuUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuUserName.setStatus("mandatory")


class _SnaLuPoolName_Type(DisplayString):
    """Custom type snaLuPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnaLuPoolName_Type.__name__ = "DisplayString"
_SnaLuPoolName_Object = MibTableColumn
snaLuPoolName = _SnaLuPoolName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 8),
    _SnaLuPoolName_Type()
)
snaLuPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuPoolName.setStatus("mandatory")


class _SnaLuOperState_Type(Integer32):
    """Custom type snaLuOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SnaLuOperState_Type.__name__ = "Integer32"
_SnaLuOperState_Object = MibTableColumn
snaLuOperState = _SnaLuOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 9),
    _SnaLuOperState_Type()
)
snaLuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperState.setStatus("mandatory")


class _SnaLuAdminState_Type(Integer32):
    """Custom type snaLuAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_SnaLuAdminState_Type.__name__ = "Integer32"
_SnaLuAdminState_Object = MibTableColumn
snaLuAdminState = _SnaLuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 10),
    _SnaLuAdminState_Type()
)
snaLuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snaLuAdminState.setStatus("mandatory")
_SnaLuLastStateChange_Type = TimeTicks
_SnaLuLastStateChange_Object = MibTableColumn
snaLuLastStateChange = _SnaLuLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 11),
    _SnaLuLastStateChange_Type()
)
snaLuLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuLastStateChange.setStatus("mandatory")
_SnaLuActiveTime_Type = TimeTicks
_SnaLuActiveTime_Object = MibTableColumn
snaLuActiveTime = _SnaLuActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 12),
    _SnaLuActiveTime_Type()
)
snaLuActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuActiveTime.setStatus("mandatory")
_SnaLuBindFailureReason_Type = Integer32
_SnaLuBindFailureReason_Object = MibTableColumn
snaLuBindFailureReason = _SnaLuBindFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 2, 1, 1, 13),
    _SnaLuBindFailureReason_Type()
)
snaLuBindFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuBindFailureReason.setStatus("mandatory")
_ApplicationLu_ObjectIdentity = ObjectIdentity
applicationLu = _ApplicationLu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3)
)
_ApplicationLuTable_Object = MibTable
applicationLuTable = _ApplicationLuTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    applicationLuTable.setStatus("mandatory")
_AppLuEntry_Object = MibTableRow
appLuEntry = _AppLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1)
)
appLuEntry.setIndexNames(
    (0, "SNANET-MIB", "appLuT5nodeIndex"),
    (0, "SNANET-MIB", "appLuIndex"),
)
if mibBuilder.loadTexts:
    appLuEntry.setStatus("mandatory")
_AppLuT5nodeIndex_Type = Integer32
_AppLuT5nodeIndex_Object = MibTableColumn
appLuT5nodeIndex = _AppLuT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 1),
    _AppLuT5nodeIndex_Type()
)
appLuT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuT5nodeIndex.setStatus("mandatory")
_AppLuIndex_Type = Integer32
_AppLuIndex_Object = MibTableColumn
appLuIndex = _AppLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 2),
    _AppLuIndex_Type()
)
appLuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuIndex.setStatus("mandatory")


class _AppLuName_Type(DisplayString):
    """Custom type appLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppLuName_Type.__name__ = "DisplayString"
_AppLuName_Object = MibTableColumn
appLuName = _AppLuName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 3),
    _AppLuName_Type()
)
appLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuName.setStatus("mandatory")


class _AppLuConversionType_Type(Integer32):
    """Custom type appLuConversionType based on Integer32"""
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
        *(("interactive", 1),
          ("native", 3),
          ("netvOper", 4),
          ("transparent", 2))
    )


_AppLuConversionType_Type.__name__ = "Integer32"
_AppLuConversionType_Object = MibTableColumn
appLuConversionType = _AppLuConversionType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 4),
    _AppLuConversionType_Type()
)
appLuConversionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuConversionType.setStatus("mandatory")


class _AppLuHostInterfaceType_Type(Integer32):
    """Custom type appLuHostInterfaceType based on Integer32"""
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
        *(("appc", 3),
          ("batch", 4),
          ("interactive", 1),
          ("outbound", 2),
          ("rbfte", 5))
    )


_AppLuHostInterfaceType_Type.__name__ = "Integer32"
_AppLuHostInterfaceType_Object = MibTableColumn
appLuHostInterfaceType = _AppLuHostInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 5),
    _AppLuHostInterfaceType_Type()
)
appLuHostInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuHostInterfaceType.setStatus("mandatory")


class _AppLuApplicationName_Type(DisplayString):
    """Custom type appLuApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppLuApplicationName_Type.__name__ = "DisplayString"
_AppLuApplicationName_Object = MibTableColumn
appLuApplicationName = _AppLuApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 6),
    _AppLuApplicationName_Type()
)
appLuApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuApplicationName.setStatus("mandatory")


class _AppLuGatewayName_Type(DisplayString):
    """Custom type appLuGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppLuGatewayName_Type.__name__ = "DisplayString"
_AppLuGatewayName_Object = MibTableColumn
appLuGatewayName = _AppLuGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 7),
    _AppLuGatewayName_Type()
)
appLuGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuGatewayName.setStatus("mandatory")


class _AppLuAdminState_Type(Integer32):
    """Custom type appLuAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_AppLuAdminState_Type.__name__ = "Integer32"
_AppLuAdminState_Object = MibTableColumn
appLuAdminState = _AppLuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 8),
    _AppLuAdminState_Type()
)
appLuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appLuAdminState.setStatus("mandatory")


class _AppLuOperState_Type(Integer32):
    """Custom type appLuOperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("inactive", 3),
          ("other", 1))
    )


_AppLuOperState_Type.__name__ = "Integer32"
_AppLuOperState_Object = MibTableColumn
appLuOperState = _AppLuOperState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 9),
    _AppLuOperState_Type()
)
appLuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuOperState.setStatus("mandatory")
_AppLuActiveTime_Type = TimeTicks
_AppLuActiveTime_Object = MibTableColumn
appLuActiveTime = _AppLuActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 10),
    _AppLuActiveTime_Type()
)
appLuActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuActiveTime.setStatus("mandatory")
_AppLuLastStateChange_Type = TimeTicks
_AppLuLastStateChange_Object = MibTableColumn
appLuLastStateChange = _AppLuLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 11),
    _AppLuLastStateChange_Type()
)
appLuLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuLastStateChange.setStatus("mandatory")
_AppLuBindFailureReason_Type = Integer32
_AppLuBindFailureReason_Object = MibTableColumn
appLuBindFailureReason = _AppLuBindFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 1, 1, 12),
    _AppLuBindFailureReason_Type()
)
appLuBindFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuBindFailureReason.setStatus("mandatory")
_AppLuBatchDeviceTable_Object = MibTable
appLuBatchDeviceTable = _AppLuBatchDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    appLuBatchDeviceTable.setStatus("mandatory")
_AppLuBatchDeviceEntry_Object = MibTableRow
appLuBatchDeviceEntry = _AppLuBatchDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2, 1)
)
appLuBatchDeviceEntry.setIndexNames(
    (0, "SNANET-MIB", "appLuBatchDeviceT5nodeIndex"),
    (0, "SNANET-MIB", "appLuBatchDeviceLuIndex"),
    (0, "SNANET-MIB", "appLuBatchDeviceName"),
)
if mibBuilder.loadTexts:
    appLuBatchDeviceEntry.setStatus("mandatory")
_AppLuBatchDeviceT5nodeIndex_Type = Integer32
_AppLuBatchDeviceT5nodeIndex_Object = MibTableColumn
appLuBatchDeviceT5nodeIndex = _AppLuBatchDeviceT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2, 1, 1),
    _AppLuBatchDeviceT5nodeIndex_Type()
)
appLuBatchDeviceT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuBatchDeviceT5nodeIndex.setStatus("mandatory")
_AppLuBatchDeviceLuIndex_Type = Integer32
_AppLuBatchDeviceLuIndex_Object = MibTableColumn
appLuBatchDeviceLuIndex = _AppLuBatchDeviceLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2, 1, 2),
    _AppLuBatchDeviceLuIndex_Type()
)
appLuBatchDeviceLuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuBatchDeviceLuIndex.setStatus("mandatory")


class _AppLuBatchDeviceName_Type(DisplayString):
    """Custom type appLuBatchDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppLuBatchDeviceName_Type.__name__ = "DisplayString"
_AppLuBatchDeviceName_Object = MibTableColumn
appLuBatchDeviceName = _AppLuBatchDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2, 1, 3),
    _AppLuBatchDeviceName_Type()
)
appLuBatchDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuBatchDeviceName.setStatus("mandatory")


class _AppLuBatchDeviceType_Type(Integer32):
    """Custom type appLuBatchDeviceType based on Integer32"""
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
        *(("cardpunch", 3),
          ("cardreader", 2),
          ("console", 1),
          ("printer", 4))
    )


_AppLuBatchDeviceType_Type.__name__ = "Integer32"
_AppLuBatchDeviceType_Object = MibTableColumn
appLuBatchDeviceType = _AppLuBatchDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2, 1, 4),
    _AppLuBatchDeviceType_Type()
)
appLuBatchDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuBatchDeviceType.setStatus("mandatory")


class _AppLuBatchDeviceNumber_Type(Integer32):
    """Custom type appLuBatchDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_AppLuBatchDeviceNumber_Type.__name__ = "Integer32"
_AppLuBatchDeviceNumber_Object = MibTableColumn
appLuBatchDeviceNumber = _AppLuBatchDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 4, 3, 2, 1, 5),
    _AppLuBatchDeviceNumber_Type()
)
appLuBatchDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLuBatchDeviceNumber.setStatus("mandatory")
_SnaSession_ObjectIdentity = ObjectIdentity
snaSession = _SnaSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5)
)
_SnaSessionTable_Object = MibTable
snaSessionTable = _SnaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1)
)
if mibBuilder.loadTexts:
    snaSessionTable.setStatus("mandatory")
_SnaSessionEntry_Object = MibTableRow
snaSessionEntry = _SnaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1)
)
snaSessionEntry.setIndexNames(
    (0, "SNANET-MIB", "snaSessT5nodeIndex"),
    (0, "SNANET-MIB", "snaSessNauName"),
    (0, "SNANET-MIB", "snaSessNauSessNumber"),
)
if mibBuilder.loadTexts:
    snaSessionEntry.setStatus("mandatory")
_SnaSessT5nodeIndex_Type = Integer32
_SnaSessT5nodeIndex_Object = MibTableColumn
snaSessT5nodeIndex = _SnaSessT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 1),
    _SnaSessT5nodeIndex_Type()
)
snaSessT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessT5nodeIndex.setStatus("mandatory")


class _SnaSessNauName_Type(DisplayString):
    """Custom type snaSessNauName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnaSessNauName_Type.__name__ = "DisplayString"
_SnaSessNauName_Object = MibTableColumn
snaSessNauName = _SnaSessNauName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 2),
    _SnaSessNauName_Type()
)
snaSessNauName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessNauName.setStatus("mandatory")


class _SnaSessNauSessNumber_Type(Integer32):
    """Custom type snaSessNauSessNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaSessNauSessNumber_Type.__name__ = "Integer32"
_SnaSessNauSessNumber_Object = MibTableColumn
snaSessNauSessNumber = _SnaSessNauSessNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 3),
    _SnaSessNauSessNumber_Type()
)
snaSessNauSessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessNauSessNumber.setStatus("mandatory")


class _SnaSessType_Type(Integer32):
    """Custom type snaSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lu-lu", 2),
          ("sscp-sscp", 1))
    )


_SnaSessType_Type.__name__ = "Integer32"
_SnaSessType_Object = MibTableColumn
snaSessType = _SnaSessType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 4),
    _SnaSessType_Type()
)
snaSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessType.setStatus("mandatory")
_SnaSessNauElementAddress_Type = Integer32
_SnaSessNauElementAddress_Object = MibTableColumn
snaSessNauElementAddress = _SnaSessNauElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 5),
    _SnaSessNauElementAddress_Type()
)
snaSessNauElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessNauElementAddress.setStatus("mandatory")


class _SnaSessState_Type(Integer32):
    """Custom type snaSessState based on Integer32"""
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
        *(("active", 4),
          ("initiating", 1),
          ("queued", 3),
          ("terminating", 2))
    )


_SnaSessState_Type.__name__ = "Integer32"
_SnaSessState_Object = MibTableColumn
snaSessState = _SnaSessState_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 6),
    _SnaSessState_Type()
)
snaSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessState.setStatus("mandatory")
_SnaSessActiveTime_Type = TimeTicks
_SnaSessActiveTime_Object = MibTableColumn
snaSessActiveTime = _SnaSessActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 7),
    _SnaSessActiveTime_Type()
)
snaSessActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessActiveTime.setStatus("mandatory")
_SnaSessSentBytes_Type = Counter32
_SnaSessSentBytes_Object = MibTableColumn
snaSessSentBytes = _SnaSessSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 8),
    _SnaSessSentBytes_Type()
)
snaSessSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessSentBytes.setStatus("mandatory")
_SnaSessReceivedBytes_Type = Counter32
_SnaSessReceivedBytes_Object = MibTableColumn
snaSessReceivedBytes = _SnaSessReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 9),
    _SnaSessReceivedBytes_Type()
)
snaSessReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessReceivedBytes.setStatus("mandatory")
_SnaSessSentRus_Type = Counter32
_SnaSessSentRus_Object = MibTableColumn
snaSessSentRus = _SnaSessSentRus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 10),
    _SnaSessSentRus_Type()
)
snaSessSentRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessSentRus.setStatus("mandatory")
_SnaSessReceivedRus_Type = Counter32
_SnaSessReceivedRus_Object = MibTableColumn
snaSessReceivedRus = _SnaSessReceivedRus_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 11),
    _SnaSessReceivedRus_Type()
)
snaSessReceivedRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessReceivedRus.setStatus("mandatory")
_SnaSessSentNegativeResps_Type = Counter32
_SnaSessSentNegativeResps_Object = MibTableColumn
snaSessSentNegativeResps = _SnaSessSentNegativeResps_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 12),
    _SnaSessSentNegativeResps_Type()
)
snaSessSentNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessSentNegativeResps.setStatus("mandatory")
_SnaSessReceivedNegativeResps_Type = Counter32
_SnaSessReceivedNegativeResps_Object = MibTableColumn
snaSessReceivedNegativeResps = _SnaSessReceivedNegativeResps_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 13),
    _SnaSessReceivedNegativeResps_Type()
)
snaSessReceivedNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessReceivedNegativeResps.setStatus("mandatory")


class _SnaSessPartnerNauName_Type(DisplayString):
    """Custom type snaSessPartnerNauName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnaSessPartnerNauName_Type.__name__ = "DisplayString"
_SnaSessPartnerNauName_Object = MibTableColumn
snaSessPartnerNauName = _SnaSessPartnerNauName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 14),
    _SnaSessPartnerNauName_Type()
)
snaSessPartnerNauName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessPartnerNauName.setStatus("mandatory")


class _SnaSessPartnerNauSubarea_Type(Integer32):
    """Custom type snaSessPartnerNauSubarea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnaSessPartnerNauSubarea_Type.__name__ = "Integer32"
_SnaSessPartnerNauSubarea_Object = MibTableColumn
snaSessPartnerNauSubarea = _SnaSessPartnerNauSubarea_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 15),
    _SnaSessPartnerNauSubarea_Type()
)
snaSessPartnerNauSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessPartnerNauSubarea.setStatus("mandatory")


class _SnaSessPartnerNauElementAddress_Type(Integer32):
    """Custom type snaSessPartnerNauElementAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_SnaSessPartnerNauElementAddress_Type.__name__ = "Integer32"
_SnaSessPartnerNauElementAddress_Object = MibTableColumn
snaSessPartnerNauElementAddress = _SnaSessPartnerNauElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 16),
    _SnaSessPartnerNauElementAddress_Type()
)
snaSessPartnerNauElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessPartnerNauElementAddress.setStatus("mandatory")


class _SnaSessVirtualRouteNumber_Type(Integer32):
    """Custom type snaSessVirtualRouteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnaSessVirtualRouteNumber_Type.__name__ = "Integer32"
_SnaSessVirtualRouteNumber_Object = MibTableColumn
snaSessVirtualRouteNumber = _SnaSessVirtualRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 17),
    _SnaSessVirtualRouteNumber_Type()
)
snaSessVirtualRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessVirtualRouteNumber.setStatus("mandatory")


class _SnaSessTransmissionPriority_Type(Integer32):
    """Custom type snaSessTransmissionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SnaSessTransmissionPriority_Type.__name__ = "Integer32"
_SnaSessTransmissionPriority_Object = MibTableColumn
snaSessTransmissionPriority = _SnaSessTransmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 18),
    _SnaSessTransmissionPriority_Type()
)
snaSessTransmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessTransmissionPriority.setStatus("mandatory")


class _SnaSessProcCorrelationId_Type(OctetString):
    """Custom type snaSessProcCorrelationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnaSessProcCorrelationId_Type.__name__ = "OctetString"
_SnaSessProcCorrelationId_Object = MibTableColumn
snaSessProcCorrelationId = _SnaSessProcCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 19),
    _SnaSessProcCorrelationId_Type()
)
snaSessProcCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessProcCorrelationId.setStatus("mandatory")


class _SnaSessPluIndicator_Type(Integer32):
    """Custom type snaSessPluIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("plu", 2),
          ("slu", 3))
    )


_SnaSessPluIndicator_Type.__name__ = "Integer32"
_SnaSessPluIndicator_Object = MibTableColumn
snaSessPluIndicator = _SnaSessPluIndicator_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 20),
    _SnaSessPluIndicator_Type()
)
snaSessPluIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessPluIndicator.setStatus("mandatory")


class _SnaSessModeName_Type(DisplayString):
    """Custom type snaSessModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnaSessModeName_Type.__name__ = "DisplayString"
_SnaSessModeName_Object = MibTableColumn
snaSessModeName = _SnaSessModeName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 5, 1, 1, 21),
    _SnaSessModeName_Type()
)
snaSessModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaSessModeName.setStatus("mandatory")
_SnaLink_ObjectIdentity = ObjectIdentity
snaLink = _SnaLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6)
)
_SnaLink802Dot2Table_Object = MibTable
snaLink802Dot2Table = _SnaLink802Dot2Table_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1)
)
if mibBuilder.loadTexts:
    snaLink802Dot2Table.setStatus("mandatory")
_SnaLink802Dot2Entry_Object = MibTableRow
snaLink802Dot2Entry = _SnaLink802Dot2Entry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1)
)
snaLink802Dot2Entry.setIndexNames(
    (0, "SNANET-MIB", "snaLink802Dot2T5nodeIndex"),
    (0, "SNANET-MIB", "snaLink802Dot2Index"),
)
if mibBuilder.loadTexts:
    snaLink802Dot2Entry.setStatus("mandatory")


class _SnaLink802Dot2T5nodeIndex_Type(Integer32):
    """Custom type snaLink802Dot2T5nodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLink802Dot2T5nodeIndex_Type.__name__ = "Integer32"
_SnaLink802Dot2T5nodeIndex_Object = MibTableColumn
snaLink802Dot2T5nodeIndex = _SnaLink802Dot2T5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 1),
    _SnaLink802Dot2T5nodeIndex_Type()
)
snaLink802Dot2T5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2T5nodeIndex.setStatus("mandatory")


class _SnaLink802Dot2Index_Type(Integer32):
    """Custom type snaLink802Dot2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLink802Dot2Index_Type.__name__ = "Integer32"
_SnaLink802Dot2Index_Object = MibTableColumn
snaLink802Dot2Index = _SnaLink802Dot2Index_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 2),
    _SnaLink802Dot2Index_Type()
)
snaLink802Dot2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2Index.setStatus("mandatory")


class _SnaLink802Dot2SourceAddress_Type(OctetString):
    """Custom type snaLink802Dot2SourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SnaLink802Dot2SourceAddress_Type.__name__ = "OctetString"
_SnaLink802Dot2SourceAddress_Object = MibTableColumn
snaLink802Dot2SourceAddress = _SnaLink802Dot2SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 3),
    _SnaLink802Dot2SourceAddress_Type()
)
snaLink802Dot2SourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2SourceAddress.setStatus("mandatory")
_SnaLink802Dot2SourceSAP_Type = Integer32
_SnaLink802Dot2SourceSAP_Object = MibTableColumn
snaLink802Dot2SourceSAP = _SnaLink802Dot2SourceSAP_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 4),
    _SnaLink802Dot2SourceSAP_Type()
)
snaLink802Dot2SourceSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2SourceSAP.setStatus("mandatory")


class _SnaLink802Dot2DestinationAddress_Type(OctetString):
    """Custom type snaLink802Dot2DestinationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SnaLink802Dot2DestinationAddress_Type.__name__ = "OctetString"
_SnaLink802Dot2DestinationAddress_Object = MibTableColumn
snaLink802Dot2DestinationAddress = _SnaLink802Dot2DestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 5),
    _SnaLink802Dot2DestinationAddress_Type()
)
snaLink802Dot2DestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2DestinationAddress.setStatus("mandatory")
_SnaLink802Dot2DestinationSAP_Type = Integer32
_SnaLink802Dot2DestinationSAP_Object = MibTableColumn
snaLink802Dot2DestinationSAP = _SnaLink802Dot2DestinationSAP_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 6),
    _SnaLink802Dot2DestinationSAP_Type()
)
snaLink802Dot2DestinationSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2DestinationSAP.setStatus("mandatory")


class _SnaLink802Dot2MediaType_Type(DisplayString):
    """Custom type snaLink802Dot2MediaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SnaLink802Dot2MediaType_Type.__name__ = "DisplayString"
_SnaLink802Dot2MediaType_Object = MibTableColumn
snaLink802Dot2MediaType = _SnaLink802Dot2MediaType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 7),
    _SnaLink802Dot2MediaType_Type()
)
snaLink802Dot2MediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2MediaType.setStatus("mandatory")


class _SnaLink802Dot2Role_Type(Integer32):
    """Custom type snaLink802Dot2Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("primary", 2),
          ("secondary", 1))
    )


_SnaLink802Dot2Role_Type.__name__ = "Integer32"
_SnaLink802Dot2Role_Object = MibTableColumn
snaLink802Dot2Role = _SnaLink802Dot2Role_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 8),
    _SnaLink802Dot2Role_Type()
)
snaLink802Dot2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2Role.setStatus("mandatory")


class _SnaLink802Dot2LineName_Type(DisplayString):
    """Custom type snaLink802Dot2LineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnaLink802Dot2LineName_Type.__name__ = "DisplayString"
_SnaLink802Dot2LineName_Object = MibTableColumn
snaLink802Dot2LineName = _SnaLink802Dot2LineName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 9),
    _SnaLink802Dot2LineName_Type()
)
snaLink802Dot2LineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2LineName.setStatus("mandatory")


class _SnaLink802Dot2Port_Type(OctetString):
    """Custom type snaLink802Dot2Port based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SnaLink802Dot2Port_Type.__name__ = "OctetString"
_SnaLink802Dot2Port_Object = MibTableColumn
snaLink802Dot2Port = _SnaLink802Dot2Port_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 10),
    _SnaLink802Dot2Port_Type()
)
snaLink802Dot2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2Port.setStatus("mandatory")
_SnaLink802Dot2IfIndex_Type = Integer32
_SnaLink802Dot2IfIndex_Object = MibTableColumn
snaLink802Dot2IfIndex = _SnaLink802Dot2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 1, 1, 11),
    _SnaLink802Dot2IfIndex_Type()
)
snaLink802Dot2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLink802Dot2IfIndex.setStatus("mandatory")
_SnaLinkSdlcTable_Object = MibTable
snaLinkSdlcTable = _SnaLinkSdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2)
)
if mibBuilder.loadTexts:
    snaLinkSdlcTable.setStatus("mandatory")
_SnaLinkSdlcEntry_Object = MibTableRow
snaLinkSdlcEntry = _SnaLinkSdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1)
)
snaLinkSdlcEntry.setIndexNames(
    (0, "SNANET-MIB", "snaLinkSdlcT5nodeIndex"),
    (0, "SNANET-MIB", "snaLinkSdlcIndex"),
)
if mibBuilder.loadTexts:
    snaLinkSdlcEntry.setStatus("mandatory")


class _SnaLinkSdlcT5nodeIndex_Type(Integer32):
    """Custom type snaLinkSdlcT5nodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLinkSdlcT5nodeIndex_Type.__name__ = "Integer32"
_SnaLinkSdlcT5nodeIndex_Object = MibTableColumn
snaLinkSdlcT5nodeIndex = _SnaLinkSdlcT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 1),
    _SnaLinkSdlcT5nodeIndex_Type()
)
snaLinkSdlcT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcT5nodeIndex.setStatus("mandatory")
_SnaLinkSdlcIndex_Type = Integer32
_SnaLinkSdlcIndex_Object = MibTableColumn
snaLinkSdlcIndex = _SnaLinkSdlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 2),
    _SnaLinkSdlcIndex_Type()
)
snaLinkSdlcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcIndex.setStatus("mandatory")


class _SnaLinkSdlcDestinationStationAddr_Type(OctetString):
    """Custom type snaLinkSdlcDestinationStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SnaLinkSdlcDestinationStationAddr_Type.__name__ = "OctetString"
_SnaLinkSdlcDestinationStationAddr_Object = MibTableColumn
snaLinkSdlcDestinationStationAddr = _SnaLinkSdlcDestinationStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 3),
    _SnaLinkSdlcDestinationStationAddr_Type()
)
snaLinkSdlcDestinationStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcDestinationStationAddr.setStatus("mandatory")


class _SnaLinkSdlcStationRole_Type(Integer32):
    """Custom type snaLinkSdlcStationRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("primary", 2),
          ("secondary", 1))
    )


_SnaLinkSdlcStationRole_Type.__name__ = "Integer32"
_SnaLinkSdlcStationRole_Object = MibTableColumn
snaLinkSdlcStationRole = _SnaLinkSdlcStationRole_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 4),
    _SnaLinkSdlcStationRole_Type()
)
snaLinkSdlcStationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcStationRole.setStatus("mandatory")
_SnaLinkSdlcLineName_Type = DisplayString
_SnaLinkSdlcLineName_Object = MibTableColumn
snaLinkSdlcLineName = _SnaLinkSdlcLineName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 5),
    _SnaLinkSdlcLineName_Type()
)
snaLinkSdlcLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcLineName.setStatus("mandatory")


class _SnaLinkSdlcPort_Type(OctetString):
    """Custom type snaLinkSdlcPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SnaLinkSdlcPort_Type.__name__ = "OctetString"
_SnaLinkSdlcPort_Object = MibTableColumn
snaLinkSdlcPort = _SnaLinkSdlcPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 6),
    _SnaLinkSdlcPort_Type()
)
snaLinkSdlcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcPort.setStatus("mandatory")
_SnaLinkSdlcIfIndex_Type = Integer32
_SnaLinkSdlcIfIndex_Object = MibTableColumn
snaLinkSdlcIfIndex = _SnaLinkSdlcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 2, 1, 7),
    _SnaLinkSdlcIfIndex_Type()
)
snaLinkSdlcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkSdlcIfIndex.setStatus("mandatory")
_SnaLinkQllcTable_Object = MibTable
snaLinkQllcTable = _SnaLinkQllcTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3)
)
if mibBuilder.loadTexts:
    snaLinkQllcTable.setStatus("mandatory")
_SnaLinkQllcEntry_Object = MibTableRow
snaLinkQllcEntry = _SnaLinkQllcEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1)
)
snaLinkQllcEntry.setIndexNames(
    (0, "SNANET-MIB", "snaLinkQllcT5nodeIndex"),
    (0, "SNANET-MIB", "snaLinkQllcIndex"),
)
if mibBuilder.loadTexts:
    snaLinkQllcEntry.setStatus("mandatory")


class _SnaLinkQllcT5nodeIndex_Type(Integer32):
    """Custom type snaLinkQllcT5nodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLinkQllcT5nodeIndex_Type.__name__ = "Integer32"
_SnaLinkQllcT5nodeIndex_Object = MibTableColumn
snaLinkQllcT5nodeIndex = _SnaLinkQllcT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 1),
    _SnaLinkQllcT5nodeIndex_Type()
)
snaLinkQllcT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcT5nodeIndex.setStatus("mandatory")


class _SnaLinkQllcIndex_Type(Integer32):
    """Custom type snaLinkQllcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLinkQllcIndex_Type.__name__ = "Integer32"
_SnaLinkQllcIndex_Object = MibTableColumn
snaLinkQllcIndex = _SnaLinkQllcIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 2),
    _SnaLinkQllcIndex_Type()
)
snaLinkQllcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcIndex.setStatus("mandatory")
_SnaLinkQllcLcn_Type = Integer32
_SnaLinkQllcLcn_Object = MibTableColumn
snaLinkQllcLcn = _SnaLinkQllcLcn_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 3),
    _SnaLinkQllcLcn_Type()
)
snaLinkQllcLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcLcn.setStatus("mandatory")


class _SnaLinkQllcSourceDteAddr_Type(OctetString):
    """Custom type snaLinkQllcSourceDteAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SnaLinkQllcSourceDteAddr_Type.__name__ = "OctetString"
_SnaLinkQllcSourceDteAddr_Object = MibTableColumn
snaLinkQllcSourceDteAddr = _SnaLinkQllcSourceDteAddr_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 4),
    _SnaLinkQllcSourceDteAddr_Type()
)
snaLinkQllcSourceDteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcSourceDteAddr.setStatus("mandatory")


class _SnaLinkQllcDestinationDteAddr_Type(OctetString):
    """Custom type snaLinkQllcDestinationDteAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SnaLinkQllcDestinationDteAddr_Type.__name__ = "OctetString"
_SnaLinkQllcDestinationDteAddr_Object = MibTableColumn
snaLinkQllcDestinationDteAddr = _SnaLinkQllcDestinationDteAddr_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 5),
    _SnaLinkQllcDestinationDteAddr_Type()
)
snaLinkQllcDestinationDteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcDestinationDteAddr.setStatus("mandatory")


class _SnaLinkQllcRole_Type(Integer32):
    """Custom type snaLinkQllcRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("primary", 2),
          ("secondary", 1))
    )


_SnaLinkQllcRole_Type.__name__ = "Integer32"
_SnaLinkQllcRole_Object = MibTableColumn
snaLinkQllcRole = _SnaLinkQllcRole_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 6),
    _SnaLinkQllcRole_Type()
)
snaLinkQllcRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcRole.setStatus("mandatory")


class _SnaLinkQllcPdnGroupName_Type(DisplayString):
    """Custom type snaLinkQllcPdnGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnaLinkQllcPdnGroupName_Type.__name__ = "DisplayString"
_SnaLinkQllcPdnGroupName_Object = MibTableColumn
snaLinkQllcPdnGroupName = _SnaLinkQllcPdnGroupName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 7),
    _SnaLinkQllcPdnGroupName_Type()
)
snaLinkQllcPdnGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcPdnGroupName.setStatus("mandatory")


class _SnaLinkQllcLineName_Type(DisplayString):
    """Custom type snaLinkQllcLineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnaLinkQllcLineName_Type.__name__ = "DisplayString"
_SnaLinkQllcLineName_Object = MibTableColumn
snaLinkQllcLineName = _SnaLinkQllcLineName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 8),
    _SnaLinkQllcLineName_Type()
)
snaLinkQllcLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcLineName.setStatus("mandatory")


class _SnaLinkQllcPort_Type(OctetString):
    """Custom type snaLinkQllcPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SnaLinkQllcPort_Type.__name__ = "OctetString"
_SnaLinkQllcPort_Object = MibTableColumn
snaLinkQllcPort = _SnaLinkQllcPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 9),
    _SnaLinkQllcPort_Type()
)
snaLinkQllcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcPort.setStatus("mandatory")
_SnaLinkQllcIfIndex_Type = Integer32
_SnaLinkQllcIfIndex_Object = MibTableColumn
snaLinkQllcIfIndex = _SnaLinkQllcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 3, 1, 10),
    _SnaLinkQllcIfIndex_Type()
)
snaLinkQllcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkQllcIfIndex.setStatus("mandatory")
_SnaLinkChannelTable_Object = MibTable
snaLinkChannelTable = _SnaLinkChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4)
)
if mibBuilder.loadTexts:
    snaLinkChannelTable.setStatus("mandatory")
_SnaLinkChannelEntry_Object = MibTableRow
snaLinkChannelEntry = _SnaLinkChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4, 1)
)
snaLinkChannelEntry.setIndexNames(
    (0, "SNANET-MIB", "snaLinkChannelT5nodeIndex"),
    (0, "SNANET-MIB", "snaLinkChannelIndex"),
)
if mibBuilder.loadTexts:
    snaLinkChannelEntry.setStatus("mandatory")


class _SnaLinkChannelT5nodeIndex_Type(Integer32):
    """Custom type snaLinkChannelT5nodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLinkChannelT5nodeIndex_Type.__name__ = "Integer32"
_SnaLinkChannelT5nodeIndex_Object = MibTableColumn
snaLinkChannelT5nodeIndex = _SnaLinkChannelT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4, 1, 1),
    _SnaLinkChannelT5nodeIndex_Type()
)
snaLinkChannelT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkChannelT5nodeIndex.setStatus("mandatory")
_SnaLinkChannelIndex_Type = Integer32
_SnaLinkChannelIndex_Object = MibTableColumn
snaLinkChannelIndex = _SnaLinkChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4, 1, 2),
    _SnaLinkChannelIndex_Type()
)
snaLinkChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkChannelIndex.setStatus("mandatory")


class _SnaLinkChannelLineName_Type(DisplayString):
    """Custom type snaLinkChannelLineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnaLinkChannelLineName_Type.__name__ = "DisplayString"
_SnaLinkChannelLineName_Object = MibTableColumn
snaLinkChannelLineName = _SnaLinkChannelLineName_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4, 1, 3),
    _SnaLinkChannelLineName_Type()
)
snaLinkChannelLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkChannelLineName.setStatus("mandatory")


class _SnaLinkChannelPort_Type(OctetString):
    """Custom type snaLinkChannelPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SnaLinkChannelPort_Type.__name__ = "OctetString"
_SnaLinkChannelPort_Object = MibTableColumn
snaLinkChannelPort = _SnaLinkChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4, 1, 4),
    _SnaLinkChannelPort_Type()
)
snaLinkChannelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkChannelPort.setStatus("mandatory")
_SnaLinkChannelIfIndex_Type = Integer32
_SnaLinkChannelIfIndex_Object = MibTableColumn
snaLinkChannelIfIndex = _SnaLinkChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 4, 1, 5),
    _SnaLinkChannelIfIndex_Type()
)
snaLinkChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkChannelIfIndex.setStatus("mandatory")
_SnaLinkIntTable_Object = MibTable
snaLinkIntTable = _SnaLinkIntTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5)
)
if mibBuilder.loadTexts:
    snaLinkIntTable.setStatus("mandatory")
_SnaLinkIntEntry_Object = MibTableRow
snaLinkIntEntry = _SnaLinkIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5, 1)
)
snaLinkIntEntry.setIndexNames(
    (0, "SNANET-MIB", "snaLinkIntT5nodeIndex"),
    (0, "SNANET-MIB", "snaLinkIntIndex"),
)
if mibBuilder.loadTexts:
    snaLinkIntEntry.setStatus("mandatory")


class _SnaLinkIntT5nodeIndex_Type(Integer32):
    """Custom type snaLinkIntT5nodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnaLinkIntT5nodeIndex_Type.__name__ = "Integer32"
_SnaLinkIntT5nodeIndex_Object = MibTableColumn
snaLinkIntT5nodeIndex = _SnaLinkIntT5nodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5, 1, 1),
    _SnaLinkIntT5nodeIndex_Type()
)
snaLinkIntT5nodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkIntT5nodeIndex.setStatus("mandatory")
_SnaLinkIntIndex_Type = Integer32
_SnaLinkIntIndex_Object = MibTableColumn
snaLinkIntIndex = _SnaLinkIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5, 1, 2),
    _SnaLinkIntIndex_Type()
)
snaLinkIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkIntIndex.setStatus("mandatory")


class _SnaLinkIntServiceType_Type(Integer32):
    """Custom type snaLinkIntServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3270", 3),
          ("tglink", 1),
          ("uniscope", 2))
    )


_SnaLinkIntServiceType_Type.__name__ = "Integer32"
_SnaLinkIntServiceType_Object = MibTableColumn
snaLinkIntServiceType = _SnaLinkIntServiceType_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5, 1, 3),
    _SnaLinkIntServiceType_Type()
)
snaLinkIntServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkIntServiceType.setStatus("mandatory")


class _SnaLinkIntOutputCredit_Type(Integer32):
    """Custom type snaLinkIntOutputCredit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnaLinkIntOutputCredit_Type.__name__ = "Integer32"
_SnaLinkIntOutputCredit_Object = MibTableColumn
snaLinkIntOutputCredit = _SnaLinkIntOutputCredit_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5, 1, 4),
    _SnaLinkIntOutputCredit_Type()
)
snaLinkIntOutputCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkIntOutputCredit.setStatus("mandatory")


class _SnaLinkIntOutputPacing_Type(Integer32):
    """Custom type snaLinkIntOutputPacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnaLinkIntOutputPacing_Type.__name__ = "Integer32"
_SnaLinkIntOutputPacing_Object = MibTableColumn
snaLinkIntOutputPacing = _SnaLinkIntOutputPacing_Object(
    (1, 3, 6, 1, 4, 1, 223, 8, 3, 6, 5, 1, 5),
    _SnaLinkIntOutputPacing_Type()
)
snaLinkIntOutputPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLinkIntOutputPacing.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNANET-MIB",
    **{"unisys": unisys,
       "dcp": dcp,
       "snanet": snanet,
       "prodInfo": prodInfo,
       "prodInfoDesc": prodInfoDesc,
       "prodInfoFeatures": prodInfoFeatures,
       "t5node": t5node,
       "t5nodeTable": t5nodeTable,
       "t5nodeEntry": t5nodeEntry,
       "t5nodeIndex": t5nodeIndex,
       "t5nodeDomainName": t5nodeDomainName,
       "t5nodeOperState": t5nodeOperState,
       "t5nodeSubareaNumber": t5nodeSubareaNumber,
       "t5nodeSscpName": t5nodeSscpName,
       "t5nodeNetworkName": t5nodeNetworkName,
       "t5nodeSscpId": t5nodeSscpId,
       "t5nodePuName": t5nodePuName,
       "t5CdrmTable": t5CdrmTable,
       "t5CdrmEntry": t5CdrmEntry,
       "t5CdrmT5nodeIndex": t5CdrmT5nodeIndex,
       "t5CdrmName": t5CdrmName,
       "t5CdrmSnaName": t5CdrmSnaName,
       "t5CdrmType": t5CdrmType,
       "t5CdrmAdminState": t5CdrmAdminState,
       "t5CdrmOperState": t5CdrmOperState,
       "t5CdrmSubareaNumber": t5CdrmSubareaNumber,
       "t5CdrmNetworkName": t5CdrmNetworkName,
       "t5CdrmElementAddress": t5CdrmElementAddress,
       "t5CdrscTable": t5CdrscTable,
       "t5CdrscEntry": t5CdrscEntry,
       "t5CdrscT5nodeIndex": t5CdrscT5nodeIndex,
       "t5CdrscName": t5CdrscName,
       "t5CdrscSnaName": t5CdrscSnaName,
       "t5CdrscCdrmName": t5CdrscCdrmName,
       "t5CdrscAdminState": t5CdrscAdminState,
       "t5CdrscOperState": t5CdrscOperState,
       "t5CdrscSessions": t5CdrscSessions,
       "t5CdrscDlmName": t5CdrscDlmName,
       "t5CdrscCosName": t5CdrscCosName,
       "t5DlmTable": t5DlmTable,
       "t5DlmEntry": t5DlmEntry,
       "t5DlmT5nodeIndex": t5DlmT5nodeIndex,
       "t5DlmName": t5DlmName,
       "t5DlmSnaName": t5DlmSnaName,
       "t5DlmFmprof": t5DlmFmprof,
       "t5DlmTsprof": t5DlmTsprof,
       "t5DlmPriprot": t5DlmPriprot,
       "t5DlmSecprot": t5DlmSecprot,
       "t5DlmComprot": t5DlmComprot,
       "t5DlmRusizes": t5DlmRusizes,
       "t5DlmPservic": t5DlmPservic,
       "t5DlmPsndpac": t5DlmPsndpac,
       "t5DlmPrcvpac": t5DlmPrcvpac,
       "t5DlmSsndpac": t5DlmSsndpac,
       "t5DlmSrcvpac": t5DlmSrcvpac,
       "t5DlmEncr": t5DlmEncr,
       "t5DlmBindType": t5DlmBindType,
       "t5DlmCos": t5DlmCos,
       "t5CosTable": t5CosTable,
       "t5CosEntry": t5CosEntry,
       "t5CosT5nodeIndex": t5CosT5nodeIndex,
       "t5CosName": t5CosName,
       "t5CosSnaName": t5CosSnaName,
       "t5CosVrids": t5CosVrids,
       "t5AliasTable": t5AliasTable,
       "t5AliasEntry": t5AliasEntry,
       "t5AliasT5nodeIndex": t5AliasT5nodeIndex,
       "t5AliasName": t5AliasName,
       "t5AliasResourceId": t5AliasResourceId,
       "subarea": subarea,
       "saErTable": saErTable,
       "saErEntry": saErEntry,
       "saErT5nodeIndex": saErT5nodeIndex,
       "saErDestinationSubarea": saErDestinationSubarea,
       "saErNumber": saErNumber,
       "saErTgNumber": saErTgNumber,
       "saErOperState": saErOperState,
       "saVrTable": saVrTable,
       "saVrEntry": saVrEntry,
       "saVrT5nodeIndex": saVrT5nodeIndex,
       "saVrErNumber": saVrErNumber,
       "saVrNumber": saVrNumber,
       "saVrTransmissionPriority": saVrTransmissionPriority,
       "saVrWindowSize": saVrWindowSize,
       "saVrMinWindowSize": saVrMinWindowSize,
       "saVrMaxWindowSize": saVrMaxWindowSize,
       "saVrPacingCount": saVrPacingCount,
       "saTransmissionGroup": saTransmissionGroup,
       "saTgTable": saTgTable,
       "saTgEntry": saTgEntry,
       "saTgT5nodeIndex": saTgT5nodeIndex,
       "saTgNumber": saTgNumber,
       "saTgAdjacentSubarea": saTgAdjacentSubarea,
       "saTgOperState": saTgOperState,
       "saTgMaxSendPiuSize": saTgMaxSendPiuSize,
       "saTgMaxReceivePiuSize": saTgMaxReceivePiuSize,
       "saTgActiveTime": saTgActiveTime,
       "saTgLastStateChange": saTgLastStateChange,
       "saTgSentBytes": saTgSentBytes,
       "saTgReceivedBytes": saTgReceivedBytes,
       "saTgSentBtus": saTgSentBtus,
       "saTgReceivedBtus": saTgReceivedBtus,
       "saTgLinkTable": saTgLinkTable,
       "saTgLinkEntry": saTgLinkEntry,
       "saTgLinkT5nodeIndex": saTgLinkT5nodeIndex,
       "saTgLinkIndex": saTgLinkIndex,
       "saTgLinkTgNumber": saTgLinkTgNumber,
       "saTgLinkAdjacentSubarea": saTgLinkAdjacentSubarea,
       "saTgLinkName": saTgLinkName,
       "saTgLinkOperState": saTgLinkOperState,
       "saTgLinkAdminState": saTgLinkAdminState,
       "saTgLinkType": saTgLinkType,
       "saTgLinkSpecific": saTgLinkSpecific,
       "saTgLinkActiveTime": saTgLinkActiveTime,
       "saTgLinkLastStateChange": saTgLinkLastStateChange,
       "saTgLinkSentBytes": saTgLinkSentBytes,
       "saTgLinkReceivedBytes": saTgLinkReceivedBytes,
       "saTgLinkSentBtus": saTgLinkSentBtus,
       "saTgLinkReceivedBtus": saTgLinkReceivedBtus,
       "snaNau": snaNau,
       "t2node": t2node,
       "t2nodeTable": t2nodeTable,
       "t2nodeEntry": t2nodeEntry,
       "t2nodeT5nodeIndex": t2nodeT5nodeIndex,
       "t2nodeIndex": t2nodeIndex,
       "t2nodeName": t2nodeName,
       "t2nodeType": t2nodeType,
       "t2nodeBlockNum": t2nodeBlockNum,
       "t2nodeIdNum": t2nodeIdNum,
       "t2nodeMaxPiu": t2nodeMaxPiu,
       "t2nodeLinkType": t2nodeLinkType,
       "t2nodeLinkSpecific": t2nodeLinkSpecific,
       "t2nodeOperState": t2nodeOperState,
       "t2nodeAdminState": t2nodeAdminState,
       "t2nodeStartTime": t2nodeStartTime,
       "t2nodeLastStateChange": t2nodeLastStateChange,
       "t2nodeActFailureReason": t2nodeActFailureReason,
       "t2nodeStatsTable": t2nodeStatsTable,
       "t2nodeStatsEntry": t2nodeStatsEntry,
       "t2nodeStatsT5nodeIndex": t2nodeStatsT5nodeIndex,
       "t2nodeStatsIndex": t2nodeStatsIndex,
       "t2nodeStatsSentBytes": t2nodeStatsSentBytes,
       "t2nodeStatsReceivedBytes": t2nodeStatsReceivedBytes,
       "t2nodeStatsSentPius": t2nodeStatsSentPius,
       "t2nodeStatsReceivedPius": t2nodeStatsReceivedPius,
       "t2nodeStatsSentNegativeResps": t2nodeStatsSentNegativeResps,
       "t2nodeStatsReceivedNegativeResps": t2nodeStatsReceivedNegativeResps,
       "t2nodeStatsActiveLus": t2nodeStatsActiveLus,
       "t2nodeStatsActLus": t2nodeStatsActLus,
       "t2nodeStatsInActLus": t2nodeStatsInActLus,
       "t2nodeStatsBindLus": t2nodeStatsBindLus,
       "snaLu": snaLu,
       "snaLuTable": snaLuTable,
       "snaLuEntry": snaLuEntry,
       "snaLuT5nodeIndex": snaLuT5nodeIndex,
       "snaLuT2nodeIndex": snaLuT2nodeIndex,
       "snaLuIndex": snaLuIndex,
       "snaLuName": snaLuName,
       "snaLuType": snaLuType,
       "snaLuLocalAddress": snaLuLocalAddress,
       "snaLuUserName": snaLuUserName,
       "snaLuPoolName": snaLuPoolName,
       "snaLuOperState": snaLuOperState,
       "snaLuAdminState": snaLuAdminState,
       "snaLuLastStateChange": snaLuLastStateChange,
       "snaLuActiveTime": snaLuActiveTime,
       "snaLuBindFailureReason": snaLuBindFailureReason,
       "applicationLu": applicationLu,
       "applicationLuTable": applicationLuTable,
       "appLuEntry": appLuEntry,
       "appLuT5nodeIndex": appLuT5nodeIndex,
       "appLuIndex": appLuIndex,
       "appLuName": appLuName,
       "appLuConversionType": appLuConversionType,
       "appLuHostInterfaceType": appLuHostInterfaceType,
       "appLuApplicationName": appLuApplicationName,
       "appLuGatewayName": appLuGatewayName,
       "appLuAdminState": appLuAdminState,
       "appLuOperState": appLuOperState,
       "appLuActiveTime": appLuActiveTime,
       "appLuLastStateChange": appLuLastStateChange,
       "appLuBindFailureReason": appLuBindFailureReason,
       "appLuBatchDeviceTable": appLuBatchDeviceTable,
       "appLuBatchDeviceEntry": appLuBatchDeviceEntry,
       "appLuBatchDeviceT5nodeIndex": appLuBatchDeviceT5nodeIndex,
       "appLuBatchDeviceLuIndex": appLuBatchDeviceLuIndex,
       "appLuBatchDeviceName": appLuBatchDeviceName,
       "appLuBatchDeviceType": appLuBatchDeviceType,
       "appLuBatchDeviceNumber": appLuBatchDeviceNumber,
       "snaSession": snaSession,
       "snaSessionTable": snaSessionTable,
       "snaSessionEntry": snaSessionEntry,
       "snaSessT5nodeIndex": snaSessT5nodeIndex,
       "snaSessNauName": snaSessNauName,
       "snaSessNauSessNumber": snaSessNauSessNumber,
       "snaSessType": snaSessType,
       "snaSessNauElementAddress": snaSessNauElementAddress,
       "snaSessState": snaSessState,
       "snaSessActiveTime": snaSessActiveTime,
       "snaSessSentBytes": snaSessSentBytes,
       "snaSessReceivedBytes": snaSessReceivedBytes,
       "snaSessSentRus": snaSessSentRus,
       "snaSessReceivedRus": snaSessReceivedRus,
       "snaSessSentNegativeResps": snaSessSentNegativeResps,
       "snaSessReceivedNegativeResps": snaSessReceivedNegativeResps,
       "snaSessPartnerNauName": snaSessPartnerNauName,
       "snaSessPartnerNauSubarea": snaSessPartnerNauSubarea,
       "snaSessPartnerNauElementAddress": snaSessPartnerNauElementAddress,
       "snaSessVirtualRouteNumber": snaSessVirtualRouteNumber,
       "snaSessTransmissionPriority": snaSessTransmissionPriority,
       "snaSessProcCorrelationId": snaSessProcCorrelationId,
       "snaSessPluIndicator": snaSessPluIndicator,
       "snaSessModeName": snaSessModeName,
       "snaLink": snaLink,
       "snaLink802Dot2Table": snaLink802Dot2Table,
       "snaLink802Dot2Entry": snaLink802Dot2Entry,
       "snaLink802Dot2T5nodeIndex": snaLink802Dot2T5nodeIndex,
       "snaLink802Dot2Index": snaLink802Dot2Index,
       "snaLink802Dot2SourceAddress": snaLink802Dot2SourceAddress,
       "snaLink802Dot2SourceSAP": snaLink802Dot2SourceSAP,
       "snaLink802Dot2DestinationAddress": snaLink802Dot2DestinationAddress,
       "snaLink802Dot2DestinationSAP": snaLink802Dot2DestinationSAP,
       "snaLink802Dot2MediaType": snaLink802Dot2MediaType,
       "snaLink802Dot2Role": snaLink802Dot2Role,
       "snaLink802Dot2LineName": snaLink802Dot2LineName,
       "snaLink802Dot2Port": snaLink802Dot2Port,
       "snaLink802Dot2IfIndex": snaLink802Dot2IfIndex,
       "snaLinkSdlcTable": snaLinkSdlcTable,
       "snaLinkSdlcEntry": snaLinkSdlcEntry,
       "snaLinkSdlcT5nodeIndex": snaLinkSdlcT5nodeIndex,
       "snaLinkSdlcIndex": snaLinkSdlcIndex,
       "snaLinkSdlcDestinationStationAddr": snaLinkSdlcDestinationStationAddr,
       "snaLinkSdlcStationRole": snaLinkSdlcStationRole,
       "snaLinkSdlcLineName": snaLinkSdlcLineName,
       "snaLinkSdlcPort": snaLinkSdlcPort,
       "snaLinkSdlcIfIndex": snaLinkSdlcIfIndex,
       "snaLinkQllcTable": snaLinkQllcTable,
       "snaLinkQllcEntry": snaLinkQllcEntry,
       "snaLinkQllcT5nodeIndex": snaLinkQllcT5nodeIndex,
       "snaLinkQllcIndex": snaLinkQllcIndex,
       "snaLinkQllcLcn": snaLinkQllcLcn,
       "snaLinkQllcSourceDteAddr": snaLinkQllcSourceDteAddr,
       "snaLinkQllcDestinationDteAddr": snaLinkQllcDestinationDteAddr,
       "snaLinkQllcRole": snaLinkQllcRole,
       "snaLinkQllcPdnGroupName": snaLinkQllcPdnGroupName,
       "snaLinkQllcLineName": snaLinkQllcLineName,
       "snaLinkQllcPort": snaLinkQllcPort,
       "snaLinkQllcIfIndex": snaLinkQllcIfIndex,
       "snaLinkChannelTable": snaLinkChannelTable,
       "snaLinkChannelEntry": snaLinkChannelEntry,
       "snaLinkChannelT5nodeIndex": snaLinkChannelT5nodeIndex,
       "snaLinkChannelIndex": snaLinkChannelIndex,
       "snaLinkChannelLineName": snaLinkChannelLineName,
       "snaLinkChannelPort": snaLinkChannelPort,
       "snaLinkChannelIfIndex": snaLinkChannelIfIndex,
       "snaLinkIntTable": snaLinkIntTable,
       "snaLinkIntEntry": snaLinkIntEntry,
       "snaLinkIntT5nodeIndex": snaLinkIntT5nodeIndex,
       "snaLinkIntIndex": snaLinkIntIndex,
       "snaLinkIntServiceType": snaLinkIntServiceType,
       "snaLinkIntOutputCredit": snaLinkIntOutputCredit,
       "snaLinkIntOutputPacing": snaLinkIntOutputPacing}
)
