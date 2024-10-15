# SNMP MIB module (MICOMFLTR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOMFLTR
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:55 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class SapType(OctetString):
    """Custom type SapType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mcmfilter_ObjectIdentity = ObjectIdentity
mcmfilter = _Mcmfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12)
)
_McmipxMacFltrTable_Object = MibTable
mcmipxMacFltrTable = _McmipxMacFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1)
)
if mibBuilder.loadTexts:
    mcmipxMacFltrTable.setStatus("obsolete")
_McmipxMacFltrEntry_Object = MibTableRow
mcmipxMacFltrEntry = _McmipxMacFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1)
)
mcmipxMacFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmipxMacFltrSysInstance"),
    (0, "MICOMFLTR", "mcmipxMacFltrId"),
)
if mibBuilder.loadTexts:
    mcmipxMacFltrEntry.setStatus("obsolete")
_McmipxMacFltrSysInstance_Type = Integer32
_McmipxMacFltrSysInstance_Object = MibTableColumn
mcmipxMacFltrSysInstance = _McmipxMacFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 1),
    _McmipxMacFltrSysInstance_Type()
)
mcmipxMacFltrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrSysInstance.setStatus("obsolete")
_McmipxMacFltrId_Type = Integer32
_McmipxMacFltrId_Object = MibTableColumn
mcmipxMacFltrId = _McmipxMacFltrId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 2),
    _McmipxMacFltrId_Type()
)
mcmipxMacFltrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrId.setStatus("obsolete")


class _McmipxMacFltrStatus_Type(Integer32):
    """Custom type mcmipxMacFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_McmipxMacFltrStatus_Type.__name__ = "Integer32"
_McmipxMacFltrStatus_Object = MibTableColumn
mcmipxMacFltrStatus = _McmipxMacFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 3),
    _McmipxMacFltrStatus_Type()
)
mcmipxMacFltrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrStatus.setStatus("obsolete")
_McmipxMacFltrSrcAddress_Type = OctetString
_McmipxMacFltrSrcAddress_Object = MibTableColumn
mcmipxMacFltrSrcAddress = _McmipxMacFltrSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 4),
    _McmipxMacFltrSrcAddress_Type()
)
mcmipxMacFltrSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrSrcAddress.setStatus("obsolete")
_McmipxMacFltrDstAddress_Type = OctetString
_McmipxMacFltrDstAddress_Object = MibTableColumn
mcmipxMacFltrDstAddress = _McmipxMacFltrDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 5),
    _McmipxMacFltrDstAddress_Type()
)
mcmipxMacFltrDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrDstAddress.setStatus("obsolete")
_McmipxMacFltrSrcMask_Type = OctetString
_McmipxMacFltrSrcMask_Object = MibTableColumn
mcmipxMacFltrSrcMask = _McmipxMacFltrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 6),
    _McmipxMacFltrSrcMask_Type()
)
mcmipxMacFltrSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrSrcMask.setStatus("obsolete")
_McmipxMacFltrDstMask_Type = OctetString
_McmipxMacFltrDstMask_Object = MibTableColumn
mcmipxMacFltrDstMask = _McmipxMacFltrDstMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 7),
    _McmipxMacFltrDstMask_Type()
)
mcmipxMacFltrDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrDstMask.setStatus("obsolete")
_McmipxMacFltrPort_Type = Integer32
_McmipxMacFltrPort_Object = MibTableColumn
mcmipxMacFltrPort = _McmipxMacFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 8),
    _McmipxMacFltrPort_Type()
)
mcmipxMacFltrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrPort.setStatus("obsolete")


class _McmipxMacFltrDir_Type(Integer32):
    """Custom type mcmipxMacFltrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_McmipxMacFltrDir_Type.__name__ = "Integer32"
_McmipxMacFltrDir_Object = MibTableColumn
mcmipxMacFltrDir = _McmipxMacFltrDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 1, 1, 9),
    _McmipxMacFltrDir_Type()
)
mcmipxMacFltrDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxMacFltrDir.setStatus("obsolete")
_McmipxNetFltrTable_Object = MibTable
mcmipxNetFltrTable = _McmipxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2)
)
if mibBuilder.loadTexts:
    mcmipxNetFltrTable.setStatus("obsolete")
_McmipxNetFltrEntry_Object = MibTableRow
mcmipxNetFltrEntry = _McmipxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1)
)
mcmipxNetFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmipxNetFltrSysInstance"),
    (0, "MICOMFLTR", "mcmipxNetFltrId"),
)
if mibBuilder.loadTexts:
    mcmipxNetFltrEntry.setStatus("obsolete")
_McmipxNetFltrSysInstance_Type = Integer32
_McmipxNetFltrSysInstance_Object = MibTableColumn
mcmipxNetFltrSysInstance = _McmipxNetFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 1),
    _McmipxNetFltrSysInstance_Type()
)
mcmipxNetFltrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrSysInstance.setStatus("obsolete")
_McmipxNetFltrId_Type = Integer32
_McmipxNetFltrId_Object = MibTableColumn
mcmipxNetFltrId = _McmipxNetFltrId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 2),
    _McmipxNetFltrId_Type()
)
mcmipxNetFltrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrId.setStatus("obsolete")


class _McmipxNetFltrStatus_Type(Integer32):
    """Custom type mcmipxNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_McmipxNetFltrStatus_Type.__name__ = "Integer32"
_McmipxNetFltrStatus_Object = MibTableColumn
mcmipxNetFltrStatus = _McmipxNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 3),
    _McmipxNetFltrStatus_Type()
)
mcmipxNetFltrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrStatus.setStatus("obsolete")
_McmipxNetFltrNetNumber_Type = NetNumber
_McmipxNetFltrNetNumber_Object = MibTableColumn
mcmipxNetFltrNetNumber = _McmipxNetFltrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 4),
    _McmipxNetFltrNetNumber_Type()
)
mcmipxNetFltrNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrNetNumber.setStatus("obsolete")
_McmipxNetFltrSapType_Type = SapType
_McmipxNetFltrSapType_Object = MibTableColumn
mcmipxNetFltrSapType = _McmipxNetFltrSapType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 5),
    _McmipxNetFltrSapType_Type()
)
mcmipxNetFltrSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrSapType.setStatus("obsolete")
_McmipxNetFltrNetMask_Type = NetNumber
_McmipxNetFltrNetMask_Object = MibTableColumn
mcmipxNetFltrNetMask = _McmipxNetFltrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 6),
    _McmipxNetFltrNetMask_Type()
)
mcmipxNetFltrNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrNetMask.setStatus("obsolete")
_McmipxNetFltrSapMask_Type = SapType
_McmipxNetFltrSapMask_Object = MibTableColumn
mcmipxNetFltrSapMask = _McmipxNetFltrSapMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 7),
    _McmipxNetFltrSapMask_Type()
)
mcmipxNetFltrSapMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrSapMask.setStatus("obsolete")
_McmipxNetFltrPort_Type = Integer32
_McmipxNetFltrPort_Object = MibTableColumn
mcmipxNetFltrPort = _McmipxNetFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 8),
    _McmipxNetFltrPort_Type()
)
mcmipxNetFltrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrPort.setStatus("obsolete")


class _McmipxNetFltrDir_Type(Integer32):
    """Custom type mcmipxNetFltrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_McmipxNetFltrDir_Type.__name__ = "Integer32"
_McmipxNetFltrDir_Object = MibTableColumn
mcmipxNetFltrDir = _McmipxNetFltrDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 2, 1, 9),
    _McmipxNetFltrDir_Type()
)
mcmipxNetFltrDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxNetFltrDir.setStatus("obsolete")
_NvmipxMacFltrTable_Object = MibTable
nvmipxMacFltrTable = _NvmipxMacFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3)
)
if mibBuilder.loadTexts:
    nvmipxMacFltrTable.setStatus("obsolete")
_NvmipxMacFltrEntry_Object = MibTableRow
nvmipxMacFltrEntry = _NvmipxMacFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1)
)
nvmipxMacFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmipxMacFltrSysInstance"),
    (0, "MICOMFLTR", "nvmipxMacFltrId"),
)
if mibBuilder.loadTexts:
    nvmipxMacFltrEntry.setStatus("obsolete")
_NvmipxMacFltrSysInstance_Type = Integer32
_NvmipxMacFltrSysInstance_Object = MibTableColumn
nvmipxMacFltrSysInstance = _NvmipxMacFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 1),
    _NvmipxMacFltrSysInstance_Type()
)
nvmipxMacFltrSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrSysInstance.setStatus("obsolete")
_NvmipxMacFltrId_Type = Integer32
_NvmipxMacFltrId_Object = MibTableColumn
nvmipxMacFltrId = _NvmipxMacFltrId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 2),
    _NvmipxMacFltrId_Type()
)
nvmipxMacFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrId.setStatus("obsolete")


class _NvmipxMacFltrStatus_Type(Integer32):
    """Custom type nvmipxMacFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NvmipxMacFltrStatus_Type.__name__ = "Integer32"
_NvmipxMacFltrStatus_Object = MibTableColumn
nvmipxMacFltrStatus = _NvmipxMacFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 3),
    _NvmipxMacFltrStatus_Type()
)
nvmipxMacFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrStatus.setStatus("obsolete")
_NvmipxMacFltrSrcAddress_Type = OctetString
_NvmipxMacFltrSrcAddress_Object = MibTableColumn
nvmipxMacFltrSrcAddress = _NvmipxMacFltrSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 4),
    _NvmipxMacFltrSrcAddress_Type()
)
nvmipxMacFltrSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrSrcAddress.setStatus("obsolete")
_NvmipxMacFltrDstAddress_Type = OctetString
_NvmipxMacFltrDstAddress_Object = MibTableColumn
nvmipxMacFltrDstAddress = _NvmipxMacFltrDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 5),
    _NvmipxMacFltrDstAddress_Type()
)
nvmipxMacFltrDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrDstAddress.setStatus("obsolete")
_NvmipxMacFltrSrcMask_Type = OctetString
_NvmipxMacFltrSrcMask_Object = MibTableColumn
nvmipxMacFltrSrcMask = _NvmipxMacFltrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 6),
    _NvmipxMacFltrSrcMask_Type()
)
nvmipxMacFltrSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrSrcMask.setStatus("obsolete")
_NvmipxMacFltrDstMask_Type = OctetString
_NvmipxMacFltrDstMask_Object = MibTableColumn
nvmipxMacFltrDstMask = _NvmipxMacFltrDstMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 7),
    _NvmipxMacFltrDstMask_Type()
)
nvmipxMacFltrDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrDstMask.setStatus("obsolete")
_NvmipxMacFltrPort_Type = Integer32
_NvmipxMacFltrPort_Object = MibTableColumn
nvmipxMacFltrPort = _NvmipxMacFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 8),
    _NvmipxMacFltrPort_Type()
)
nvmipxMacFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrPort.setStatus("obsolete")


class _NvmipxMacFltrDir_Type(Integer32):
    """Custom type nvmipxMacFltrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_NvmipxMacFltrDir_Type.__name__ = "Integer32"
_NvmipxMacFltrDir_Object = MibTableColumn
nvmipxMacFltrDir = _NvmipxMacFltrDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 3, 1, 9),
    _NvmipxMacFltrDir_Type()
)
nvmipxMacFltrDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxMacFltrDir.setStatus("obsolete")
_NvmipxNetFltrTable_Object = MibTable
nvmipxNetFltrTable = _NvmipxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4)
)
if mibBuilder.loadTexts:
    nvmipxNetFltrTable.setStatus("obsolete")
_NvmipxNetFltrEntry_Object = MibTableRow
nvmipxNetFltrEntry = _NvmipxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1)
)
nvmipxNetFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmipxNetFltrSysInstance"),
    (0, "MICOMFLTR", "nvmipxNetFltrId"),
)
if mibBuilder.loadTexts:
    nvmipxNetFltrEntry.setStatus("obsolete")
_NvmipxNetFltrSysInstance_Type = Integer32
_NvmipxNetFltrSysInstance_Object = MibTableColumn
nvmipxNetFltrSysInstance = _NvmipxNetFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 1),
    _NvmipxNetFltrSysInstance_Type()
)
nvmipxNetFltrSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrSysInstance.setStatus("obsolete")
_NvmipxNetFltrId_Type = Integer32
_NvmipxNetFltrId_Object = MibTableColumn
nvmipxNetFltrId = _NvmipxNetFltrId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 2),
    _NvmipxNetFltrId_Type()
)
nvmipxNetFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrId.setStatus("obsolete")


class _NvmipxNetFltrStatus_Type(Integer32):
    """Custom type nvmipxNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NvmipxNetFltrStatus_Type.__name__ = "Integer32"
_NvmipxNetFltrStatus_Object = MibTableColumn
nvmipxNetFltrStatus = _NvmipxNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 3),
    _NvmipxNetFltrStatus_Type()
)
nvmipxNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrStatus.setStatus("obsolete")
_NvmipxNetFltrNetNumber_Type = NetNumber
_NvmipxNetFltrNetNumber_Object = MibTableColumn
nvmipxNetFltrNetNumber = _NvmipxNetFltrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 4),
    _NvmipxNetFltrNetNumber_Type()
)
nvmipxNetFltrNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrNetNumber.setStatus("obsolete")
_NvmipxNetFltrSapType_Type = SapType
_NvmipxNetFltrSapType_Object = MibTableColumn
nvmipxNetFltrSapType = _NvmipxNetFltrSapType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 5),
    _NvmipxNetFltrSapType_Type()
)
nvmipxNetFltrSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrSapType.setStatus("obsolete")
_NvmipxNetFltrNetMask_Type = NetNumber
_NvmipxNetFltrNetMask_Object = MibTableColumn
nvmipxNetFltrNetMask = _NvmipxNetFltrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 6),
    _NvmipxNetFltrNetMask_Type()
)
nvmipxNetFltrNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrNetMask.setStatus("obsolete")
_NvmipxNetFltrSapMask_Type = SapType
_NvmipxNetFltrSapMask_Object = MibTableColumn
nvmipxNetFltrSapMask = _NvmipxNetFltrSapMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 7),
    _NvmipxNetFltrSapMask_Type()
)
nvmipxNetFltrSapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrSapMask.setStatus("obsolete")
_NvmipxNetFltrPort_Type = Integer32
_NvmipxNetFltrPort_Object = MibTableColumn
nvmipxNetFltrPort = _NvmipxNetFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 8),
    _NvmipxNetFltrPort_Type()
)
nvmipxNetFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrPort.setStatus("obsolete")


class _NvmipxNetFltrDir_Type(Integer32):
    """Custom type nvmipxNetFltrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_NvmipxNetFltrDir_Type.__name__ = "Integer32"
_NvmipxNetFltrDir_Object = MibTableColumn
nvmipxNetFltrDir = _NvmipxNetFltrDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 4, 1, 9),
    _NvmipxNetFltrDir_Type()
)
nvmipxNetFltrDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxNetFltrDir.setStatus("obsolete")
_McmIpRipInFltrTable_Object = MibTable
mcmIpRipInFltrTable = _McmIpRipInFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 5)
)
if mibBuilder.loadTexts:
    mcmIpRipInFltrTable.setStatus("mandatory")
_McmIpRipInFltrEntry_Object = MibTableRow
mcmIpRipInFltrEntry = _McmIpRipInFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 5, 1)
)
mcmIpRipInFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpRipInFltrMask"),
    (0, "MICOMFLTR", "mcmIpRipInFltrAddr"),
)
if mibBuilder.loadTexts:
    mcmIpRipInFltrEntry.setStatus("mandatory")
_McmIpRipInFltrMask_Type = IpAddress
_McmIpRipInFltrMask_Object = MibTableColumn
mcmIpRipInFltrMask = _McmIpRipInFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 5, 1, 1),
    _McmIpRipInFltrMask_Type()
)
mcmIpRipInFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipInFltrMask.setStatus("mandatory")
_McmIpRipInFltrAddr_Type = IpAddress
_McmIpRipInFltrAddr_Object = MibTableColumn
mcmIpRipInFltrAddr = _McmIpRipInFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 5, 1, 2),
    _McmIpRipInFltrAddr_Type()
)
mcmIpRipInFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipInFltrAddr.setStatus("mandatory")


class _McmIpRipInFltrAction_Type(Integer32):
    """Custom type mcmIpRipInFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpRipInFltrAction_Type.__name__ = "Integer32"
_McmIpRipInFltrAction_Object = MibTableColumn
mcmIpRipInFltrAction = _McmIpRipInFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 5, 1, 3),
    _McmIpRipInFltrAction_Type()
)
mcmIpRipInFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipInFltrAction.setStatus("mandatory")
_McmIpRipOutFltrTable_Object = MibTable
mcmIpRipOutFltrTable = _McmIpRipOutFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 6)
)
if mibBuilder.loadTexts:
    mcmIpRipOutFltrTable.setStatus("mandatory")
_McmIpRipOutFltrEntry_Object = MibTableRow
mcmIpRipOutFltrEntry = _McmIpRipOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 6, 1)
)
mcmIpRipOutFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpRipOutFltrMask"),
    (0, "MICOMFLTR", "mcmIpRipOutFltrAddr"),
)
if mibBuilder.loadTexts:
    mcmIpRipOutFltrEntry.setStatus("mandatory")
_McmIpRipOutFltrMask_Type = IpAddress
_McmIpRipOutFltrMask_Object = MibTableColumn
mcmIpRipOutFltrMask = _McmIpRipOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 6, 1, 1),
    _McmIpRipOutFltrMask_Type()
)
mcmIpRipOutFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipOutFltrMask.setStatus("mandatory")
_McmIpRipOutFltrAddr_Type = IpAddress
_McmIpRipOutFltrAddr_Object = MibTableColumn
mcmIpRipOutFltrAddr = _McmIpRipOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 6, 1, 2),
    _McmIpRipOutFltrAddr_Type()
)
mcmIpRipOutFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipOutFltrAddr.setStatus("mandatory")


class _McmIpRipOutFltrAction_Type(Integer32):
    """Custom type mcmIpRipOutFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpRipOutFltrAction_Type.__name__ = "Integer32"
_McmIpRipOutFltrAction_Object = MibTableColumn
mcmIpRipOutFltrAction = _McmIpRipOutFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 6, 1, 3),
    _McmIpRipOutFltrAction_Type()
)
mcmIpRipOutFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipOutFltrAction.setStatus("mandatory")
_McmIpRipGwyFltrTable_Object = MibTable
mcmIpRipGwyFltrTable = _McmIpRipGwyFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 7)
)
if mibBuilder.loadTexts:
    mcmIpRipGwyFltrTable.setStatus("mandatory")
_McmIpRipGwyFltrEntry_Object = MibTableRow
mcmIpRipGwyFltrEntry = _McmIpRipGwyFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 7, 1)
)
mcmIpRipGwyFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpRipGwyFltrMask"),
    (0, "MICOMFLTR", "mcmIpRipGwyFltrAddr"),
)
if mibBuilder.loadTexts:
    mcmIpRipGwyFltrEntry.setStatus("mandatory")
_McmIpRipGwyFltrMask_Type = IpAddress
_McmIpRipGwyFltrMask_Object = MibTableColumn
mcmIpRipGwyFltrMask = _McmIpRipGwyFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 7, 1, 1),
    _McmIpRipGwyFltrMask_Type()
)
mcmIpRipGwyFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipGwyFltrMask.setStatus("mandatory")
_McmIpRipGwyFltrAddr_Type = IpAddress
_McmIpRipGwyFltrAddr_Object = MibTableColumn
mcmIpRipGwyFltrAddr = _McmIpRipGwyFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 7, 1, 2),
    _McmIpRipGwyFltrAddr_Type()
)
mcmIpRipGwyFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipGwyFltrAddr.setStatus("mandatory")


class _McmIpRipGwyFltrAction_Type(Integer32):
    """Custom type mcmIpRipGwyFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpRipGwyFltrAction_Type.__name__ = "Integer32"
_McmIpRipGwyFltrAction_Object = MibTableColumn
mcmIpRipGwyFltrAction = _McmIpRipGwyFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 7, 1, 3),
    _McmIpRipGwyFltrAction_Type()
)
mcmIpRipGwyFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpRipGwyFltrAction.setStatus("mandatory")
_McmIpOspfOutFltrTable_Object = MibTable
mcmIpOspfOutFltrTable = _McmIpOspfOutFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 8)
)
if mibBuilder.loadTexts:
    mcmIpOspfOutFltrTable.setStatus("mandatory")
_McmIpOspfOutFltrEntry_Object = MibTableRow
mcmIpOspfOutFltrEntry = _McmIpOspfOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 8, 1)
)
mcmIpOspfOutFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpOspfOutFltrMask"),
    (0, "MICOMFLTR", "mcmIpOspfOutFltrAddr"),
)
if mibBuilder.loadTexts:
    mcmIpOspfOutFltrEntry.setStatus("mandatory")
_McmIpOspfOutFltrMask_Type = IpAddress
_McmIpOspfOutFltrMask_Object = MibTableColumn
mcmIpOspfOutFltrMask = _McmIpOspfOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 8, 1, 1),
    _McmIpOspfOutFltrMask_Type()
)
mcmIpOspfOutFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpOspfOutFltrMask.setStatus("mandatory")
_McmIpOspfOutFltrAddr_Type = IpAddress
_McmIpOspfOutFltrAddr_Object = MibTableColumn
mcmIpOspfOutFltrAddr = _McmIpOspfOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 8, 1, 2),
    _McmIpOspfOutFltrAddr_Type()
)
mcmIpOspfOutFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpOspfOutFltrAddr.setStatus("mandatory")


class _McmIpOspfOutFltrAction_Type(Integer32):
    """Custom type mcmIpOspfOutFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpOspfOutFltrAction_Type.__name__ = "Integer32"
_McmIpOspfOutFltrAction_Object = MibTableColumn
mcmIpOspfOutFltrAction = _McmIpOspfOutFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 8, 1, 3),
    _McmIpOspfOutFltrAction_Type()
)
mcmIpOspfOutFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpOspfOutFltrAction.setStatus("mandatory")
_McmIpFwdPortInFltrTable_Object = MibTable
mcmIpFwdPortInFltrTable = _McmIpFwdPortInFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9)
)
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrTable.setStatus("mandatory")
_McmIpFwdPortInFltrEntry_Object = MibTableRow
mcmIpFwdPortInFltrEntry = _McmIpFwdPortInFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1)
)
mcmIpFwdPortInFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpFwdPortInFltrPortNo"),
    (0, "MICOMFLTR", "mcmIpFwdPortInFltrMask"),
    (0, "MICOMFLTR", "mcmIpFwdPortInFltrAddr"),
    (0, "MICOMFLTR", "mcmIpFwdPortInFltrProtId"),
    (0, "MICOMFLTR", "mcmIpFwdPortInFltrPortId"),
)
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrEntry.setStatus("mandatory")
_McmIpFwdPortInFltrPortNo_Type = Integer32
_McmIpFwdPortInFltrPortNo_Object = MibTableColumn
mcmIpFwdPortInFltrPortNo = _McmIpFwdPortInFltrPortNo_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 1),
    _McmIpFwdPortInFltrPortNo_Type()
)
mcmIpFwdPortInFltrPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrPortNo.setStatus("mandatory")
_McmIpFwdPortInFltrMask_Type = IpAddress
_McmIpFwdPortInFltrMask_Object = MibTableColumn
mcmIpFwdPortInFltrMask = _McmIpFwdPortInFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 2),
    _McmIpFwdPortInFltrMask_Type()
)
mcmIpFwdPortInFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrMask.setStatus("mandatory")
_McmIpFwdPortInFltrAddr_Type = IpAddress
_McmIpFwdPortInFltrAddr_Object = MibTableColumn
mcmIpFwdPortInFltrAddr = _McmIpFwdPortInFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 3),
    _McmIpFwdPortInFltrAddr_Type()
)
mcmIpFwdPortInFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrAddr.setStatus("mandatory")
_McmIpFwdPortInFltrProtId_Type = Integer32
_McmIpFwdPortInFltrProtId_Object = MibTableColumn
mcmIpFwdPortInFltrProtId = _McmIpFwdPortInFltrProtId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 4),
    _McmIpFwdPortInFltrProtId_Type()
)
mcmIpFwdPortInFltrProtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrProtId.setStatus("mandatory")
_McmIpFwdPortInFltrPortId_Type = Integer32
_McmIpFwdPortInFltrPortId_Object = MibTableColumn
mcmIpFwdPortInFltrPortId = _McmIpFwdPortInFltrPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 5),
    _McmIpFwdPortInFltrPortId_Type()
)
mcmIpFwdPortInFltrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrPortId.setStatus("mandatory")


class _McmIpFwdPortInFltrSrcDst_Type(Integer32):
    """Custom type mcmIpFwdPortInFltrSrcDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_McmIpFwdPortInFltrSrcDst_Type.__name__ = "Integer32"
_McmIpFwdPortInFltrSrcDst_Object = MibTableColumn
mcmIpFwdPortInFltrSrcDst = _McmIpFwdPortInFltrSrcDst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 6),
    _McmIpFwdPortInFltrSrcDst_Type()
)
mcmIpFwdPortInFltrSrcDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrSrcDst.setStatus("mandatory")


class _McmIpFwdPortInFltrAction_Type(Integer32):
    """Custom type mcmIpFwdPortInFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpFwdPortInFltrAction_Type.__name__ = "Integer32"
_McmIpFwdPortInFltrAction_Object = MibTableColumn
mcmIpFwdPortInFltrAction = _McmIpFwdPortInFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 9, 1, 7),
    _McmIpFwdPortInFltrAction_Type()
)
mcmIpFwdPortInFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortInFltrAction.setStatus("mandatory")
_McmIpFwdPortOutFltrTable_Object = MibTable
mcmIpFwdPortOutFltrTable = _McmIpFwdPortOutFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10)
)
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrTable.setStatus("mandatory")
_McmIpFwdPortOutFltrEntry_Object = MibTableRow
mcmIpFwdPortOutFltrEntry = _McmIpFwdPortOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1)
)
mcmIpFwdPortOutFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpFwdPortOutFltrPortNo"),
    (0, "MICOMFLTR", "mcmIpFwdPortOutFltrMask"),
    (0, "MICOMFLTR", "mcmIpFwdPortOutFltrAddr"),
    (0, "MICOMFLTR", "mcmIpFwdPortOutFltrProtId"),
    (0, "MICOMFLTR", "mcmIpFwdPortOutFltrPortId"),
)
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrEntry.setStatus("mandatory")
_McmIpFwdPortOutFltrPortNo_Type = Integer32
_McmIpFwdPortOutFltrPortNo_Object = MibTableColumn
mcmIpFwdPortOutFltrPortNo = _McmIpFwdPortOutFltrPortNo_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 1),
    _McmIpFwdPortOutFltrPortNo_Type()
)
mcmIpFwdPortOutFltrPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrPortNo.setStatus("mandatory")
_McmIpFwdPortOutFltrMask_Type = IpAddress
_McmIpFwdPortOutFltrMask_Object = MibTableColumn
mcmIpFwdPortOutFltrMask = _McmIpFwdPortOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 2),
    _McmIpFwdPortOutFltrMask_Type()
)
mcmIpFwdPortOutFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrMask.setStatus("mandatory")
_McmIpFwdPortOutFltrAddr_Type = IpAddress
_McmIpFwdPortOutFltrAddr_Object = MibTableColumn
mcmIpFwdPortOutFltrAddr = _McmIpFwdPortOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 3),
    _McmIpFwdPortOutFltrAddr_Type()
)
mcmIpFwdPortOutFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrAddr.setStatus("mandatory")
_McmIpFwdPortOutFltrProtId_Type = Integer32
_McmIpFwdPortOutFltrProtId_Object = MibTableColumn
mcmIpFwdPortOutFltrProtId = _McmIpFwdPortOutFltrProtId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 4),
    _McmIpFwdPortOutFltrProtId_Type()
)
mcmIpFwdPortOutFltrProtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrProtId.setStatus("mandatory")
_McmIpFwdPortOutFltrPortId_Type = Integer32
_McmIpFwdPortOutFltrPortId_Object = MibTableColumn
mcmIpFwdPortOutFltrPortId = _McmIpFwdPortOutFltrPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 5),
    _McmIpFwdPortOutFltrPortId_Type()
)
mcmIpFwdPortOutFltrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrPortId.setStatus("mandatory")


class _McmIpFwdPortOutFltrSrcDst_Type(Integer32):
    """Custom type mcmIpFwdPortOutFltrSrcDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_McmIpFwdPortOutFltrSrcDst_Type.__name__ = "Integer32"
_McmIpFwdPortOutFltrSrcDst_Object = MibTableColumn
mcmIpFwdPortOutFltrSrcDst = _McmIpFwdPortOutFltrSrcDst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 6),
    _McmIpFwdPortOutFltrSrcDst_Type()
)
mcmIpFwdPortOutFltrSrcDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrSrcDst.setStatus("mandatory")


class _McmIpFwdPortOutFltrAction_Type(Integer32):
    """Custom type mcmIpFwdPortOutFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpFwdPortOutFltrAction_Type.__name__ = "Integer32"
_McmIpFwdPortOutFltrAction_Object = MibTableColumn
mcmIpFwdPortOutFltrAction = _McmIpFwdPortOutFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 10, 1, 7),
    _McmIpFwdPortOutFltrAction_Type()
)
mcmIpFwdPortOutFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpFwdPortOutFltrAction.setStatus("mandatory")
_McmIpSysFltrTable_Object = MibTable
mcmIpSysFltrTable = _McmIpSysFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11)
)
if mibBuilder.loadTexts:
    mcmIpSysFltrTable.setStatus("mandatory")
_McmIpSysFltrEntry_Object = MibTableRow
mcmIpSysFltrEntry = _McmIpSysFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1)
)
mcmIpSysFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpSysFltrDstMask"),
    (0, "MICOMFLTR", "mcmIpSysFltrDstAddr"),
    (0, "MICOMFLTR", "mcmIpSysFltrSrcMask"),
    (0, "MICOMFLTR", "mcmIpSysFltrSrcAddr"),
    (0, "MICOMFLTR", "mcmIpSysFltrProtId"),
    (0, "MICOMFLTR", "mcmIpSysFltrPortId"),
)
if mibBuilder.loadTexts:
    mcmIpSysFltrEntry.setStatus("mandatory")
_McmIpSysFltrDstMask_Type = IpAddress
_McmIpSysFltrDstMask_Object = MibTableColumn
mcmIpSysFltrDstMask = _McmIpSysFltrDstMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 1),
    _McmIpSysFltrDstMask_Type()
)
mcmIpSysFltrDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrDstMask.setStatus("mandatory")
_McmIpSysFltrDstAddr_Type = IpAddress
_McmIpSysFltrDstAddr_Object = MibTableColumn
mcmIpSysFltrDstAddr = _McmIpSysFltrDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 2),
    _McmIpSysFltrDstAddr_Type()
)
mcmIpSysFltrDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrDstAddr.setStatus("mandatory")
_McmIpSysFltrSrcMask_Type = IpAddress
_McmIpSysFltrSrcMask_Object = MibTableColumn
mcmIpSysFltrSrcMask = _McmIpSysFltrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 3),
    _McmIpSysFltrSrcMask_Type()
)
mcmIpSysFltrSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrSrcMask.setStatus("mandatory")
_McmIpSysFltrSrcAddr_Type = IpAddress
_McmIpSysFltrSrcAddr_Object = MibTableColumn
mcmIpSysFltrSrcAddr = _McmIpSysFltrSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 4),
    _McmIpSysFltrSrcAddr_Type()
)
mcmIpSysFltrSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrSrcAddr.setStatus("mandatory")
_McmIpSysFltrProtId_Type = Integer32
_McmIpSysFltrProtId_Object = MibTableColumn
mcmIpSysFltrProtId = _McmIpSysFltrProtId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 5),
    _McmIpSysFltrProtId_Type()
)
mcmIpSysFltrProtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrProtId.setStatus("mandatory")
_McmIpSysFltrPortId_Type = Integer32
_McmIpSysFltrPortId_Object = MibTableColumn
mcmIpSysFltrPortId = _McmIpSysFltrPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 6),
    _McmIpSysFltrPortId_Type()
)
mcmIpSysFltrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrPortId.setStatus("mandatory")


class _McmIpSysFltrAction_Type(Integer32):
    """Custom type mcmIpSysFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_McmIpSysFltrAction_Type.__name__ = "Integer32"
_McmIpSysFltrAction_Object = MibTableColumn
mcmIpSysFltrAction = _McmIpSysFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 11, 1, 7),
    _McmIpSysFltrAction_Type()
)
mcmIpSysFltrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpSysFltrAction.setStatus("mandatory")
_NvmIpRipInFltrTable_Object = MibTable
nvmIpRipInFltrTable = _NvmIpRipInFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 12)
)
if mibBuilder.loadTexts:
    nvmIpRipInFltrTable.setStatus("mandatory")
_NvmIpRipInFltrEntry_Object = MibTableRow
nvmIpRipInFltrEntry = _NvmIpRipInFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 12, 1)
)
nvmIpRipInFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpRipInFltrMask"),
    (0, "MICOMFLTR", "nvmIpRipInFltrAddr"),
)
if mibBuilder.loadTexts:
    nvmIpRipInFltrEntry.setStatus("mandatory")
_NvmIpRipInFltrMask_Type = IpAddress
_NvmIpRipInFltrMask_Object = MibTableColumn
nvmIpRipInFltrMask = _NvmIpRipInFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 12, 1, 1),
    _NvmIpRipInFltrMask_Type()
)
nvmIpRipInFltrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipInFltrMask.setStatus("mandatory")
_NvmIpRipInFltrAddr_Type = IpAddress
_NvmIpRipInFltrAddr_Object = MibTableColumn
nvmIpRipInFltrAddr = _NvmIpRipInFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 12, 1, 2),
    _NvmIpRipInFltrAddr_Type()
)
nvmIpRipInFltrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipInFltrAddr.setStatus("mandatory")


class _NvmIpRipInFltrAction_Type(Integer32):
    """Custom type nvmIpRipInFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpRipInFltrAction_Type.__name__ = "Integer32"
_NvmIpRipInFltrAction_Object = MibTableColumn
nvmIpRipInFltrAction = _NvmIpRipInFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 12, 1, 3),
    _NvmIpRipInFltrAction_Type()
)
nvmIpRipInFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipInFltrAction.setStatus("mandatory")
_NvmIpRipOutFltrTable_Object = MibTable
nvmIpRipOutFltrTable = _NvmIpRipOutFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 13)
)
if mibBuilder.loadTexts:
    nvmIpRipOutFltrTable.setStatus("mandatory")
_NvmIpRipOutFltrEntry_Object = MibTableRow
nvmIpRipOutFltrEntry = _NvmIpRipOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 13, 1)
)
nvmIpRipOutFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpRipOutFltrMask"),
    (0, "MICOMFLTR", "nvmIpRipOutFltrAddr"),
)
if mibBuilder.loadTexts:
    nvmIpRipOutFltrEntry.setStatus("mandatory")
_NvmIpRipOutFltrMask_Type = IpAddress
_NvmIpRipOutFltrMask_Object = MibTableColumn
nvmIpRipOutFltrMask = _NvmIpRipOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 13, 1, 1),
    _NvmIpRipOutFltrMask_Type()
)
nvmIpRipOutFltrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipOutFltrMask.setStatus("mandatory")
_NvmIpRipOutFltrAddr_Type = IpAddress
_NvmIpRipOutFltrAddr_Object = MibTableColumn
nvmIpRipOutFltrAddr = _NvmIpRipOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 13, 1, 2),
    _NvmIpRipOutFltrAddr_Type()
)
nvmIpRipOutFltrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipOutFltrAddr.setStatus("mandatory")


class _NvmIpRipOutFltrAction_Type(Integer32):
    """Custom type nvmIpRipOutFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpRipOutFltrAction_Type.__name__ = "Integer32"
_NvmIpRipOutFltrAction_Object = MibTableColumn
nvmIpRipOutFltrAction = _NvmIpRipOutFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 13, 1, 3),
    _NvmIpRipOutFltrAction_Type()
)
nvmIpRipOutFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipOutFltrAction.setStatus("mandatory")
_NvmIpRipGwyFltrTable_Object = MibTable
nvmIpRipGwyFltrTable = _NvmIpRipGwyFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 14)
)
if mibBuilder.loadTexts:
    nvmIpRipGwyFltrTable.setStatus("mandatory")
_NvmIpRipGwyFltrEntry_Object = MibTableRow
nvmIpRipGwyFltrEntry = _NvmIpRipGwyFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 14, 1)
)
nvmIpRipGwyFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpRipGwyFltrMask"),
    (0, "MICOMFLTR", "nvmIpRipGwyFltrAddr"),
)
if mibBuilder.loadTexts:
    nvmIpRipGwyFltrEntry.setStatus("mandatory")
_NvmIpRipGwyFltrMask_Type = IpAddress
_NvmIpRipGwyFltrMask_Object = MibTableColumn
nvmIpRipGwyFltrMask = _NvmIpRipGwyFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 14, 1, 1),
    _NvmIpRipGwyFltrMask_Type()
)
nvmIpRipGwyFltrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipGwyFltrMask.setStatus("mandatory")
_NvmIpRipGwyFltrAddr_Type = IpAddress
_NvmIpRipGwyFltrAddr_Object = MibTableColumn
nvmIpRipGwyFltrAddr = _NvmIpRipGwyFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 14, 1, 2),
    _NvmIpRipGwyFltrAddr_Type()
)
nvmIpRipGwyFltrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipGwyFltrAddr.setStatus("mandatory")


class _NvmIpRipGwyFltrAction_Type(Integer32):
    """Custom type nvmIpRipGwyFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpRipGwyFltrAction_Type.__name__ = "Integer32"
_NvmIpRipGwyFltrAction_Object = MibTableColumn
nvmIpRipGwyFltrAction = _NvmIpRipGwyFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 14, 1, 3),
    _NvmIpRipGwyFltrAction_Type()
)
nvmIpRipGwyFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpRipGwyFltrAction.setStatus("mandatory")
_NvmIpOspfOutFltrTable_Object = MibTable
nvmIpOspfOutFltrTable = _NvmIpOspfOutFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 15)
)
if mibBuilder.loadTexts:
    nvmIpOspfOutFltrTable.setStatus("mandatory")
_NvmIpOspfOutFltrEntry_Object = MibTableRow
nvmIpOspfOutFltrEntry = _NvmIpOspfOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 15, 1)
)
nvmIpOspfOutFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpOspfOutFltrMask"),
    (0, "MICOMFLTR", "nvmIpOspfOutFltrAddr"),
)
if mibBuilder.loadTexts:
    nvmIpOspfOutFltrEntry.setStatus("mandatory")
_NvmIpOspfOutFltrMask_Type = IpAddress
_NvmIpOspfOutFltrMask_Object = MibTableColumn
nvmIpOspfOutFltrMask = _NvmIpOspfOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 15, 1, 1),
    _NvmIpOspfOutFltrMask_Type()
)
nvmIpOspfOutFltrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpOspfOutFltrMask.setStatus("mandatory")
_NvmIpOspfOutFltrAddr_Type = IpAddress
_NvmIpOspfOutFltrAddr_Object = MibTableColumn
nvmIpOspfOutFltrAddr = _NvmIpOspfOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 15, 1, 2),
    _NvmIpOspfOutFltrAddr_Type()
)
nvmIpOspfOutFltrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpOspfOutFltrAddr.setStatus("mandatory")


class _NvmIpOspfOutFltrAction_Type(Integer32):
    """Custom type nvmIpOspfOutFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpOspfOutFltrAction_Type.__name__ = "Integer32"
_NvmIpOspfOutFltrAction_Object = MibTableColumn
nvmIpOspfOutFltrAction = _NvmIpOspfOutFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 15, 1, 3),
    _NvmIpOspfOutFltrAction_Type()
)
nvmIpOspfOutFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpOspfOutFltrAction.setStatus("mandatory")
_NvmIpFwdPortInFltrTable_Object = MibTable
nvmIpFwdPortInFltrTable = _NvmIpFwdPortInFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16)
)
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrTable.setStatus("mandatory")
_NvmIpFwdPortInFltrEntry_Object = MibTableRow
nvmIpFwdPortInFltrEntry = _NvmIpFwdPortInFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1)
)
nvmIpFwdPortInFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpFwdPortInFltrPortNo"),
    (0, "MICOMFLTR", "nvmIpFwdPortInFltrMask"),
    (0, "MICOMFLTR", "nvmIpFwdPortInFltrAddr"),
    (0, "MICOMFLTR", "nvmIpFwdPortInFltrProtId"),
    (0, "MICOMFLTR", "nvmIpFwdPortInFltrPortId"),
)
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrEntry.setStatus("mandatory")


class _NvmIpFwdPortInFltrPortNo_Type(Integer32):
    """Custom type nvmIpFwdPortInFltrPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmIpFwdPortInFltrPortNo_Type.__name__ = "Integer32"
_NvmIpFwdPortInFltrPortNo_Object = MibTableColumn
nvmIpFwdPortInFltrPortNo = _NvmIpFwdPortInFltrPortNo_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 1),
    _NvmIpFwdPortInFltrPortNo_Type()
)
nvmIpFwdPortInFltrPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrPortNo.setStatus("mandatory")
_NvmIpFwdPortInFltrMask_Type = IpAddress
_NvmIpFwdPortInFltrMask_Object = MibTableColumn
nvmIpFwdPortInFltrMask = _NvmIpFwdPortInFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 2),
    _NvmIpFwdPortInFltrMask_Type()
)
nvmIpFwdPortInFltrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrMask.setStatus("mandatory")
_NvmIpFwdPortInFltrAddr_Type = IpAddress
_NvmIpFwdPortInFltrAddr_Object = MibTableColumn
nvmIpFwdPortInFltrAddr = _NvmIpFwdPortInFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 3),
    _NvmIpFwdPortInFltrAddr_Type()
)
nvmIpFwdPortInFltrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrAddr.setStatus("mandatory")


class _NvmIpFwdPortInFltrProtId_Type(Integer32):
    """Custom type nvmIpFwdPortInFltrProtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmIpFwdPortInFltrProtId_Type.__name__ = "Integer32"
_NvmIpFwdPortInFltrProtId_Object = MibTableColumn
nvmIpFwdPortInFltrProtId = _NvmIpFwdPortInFltrProtId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 4),
    _NvmIpFwdPortInFltrProtId_Type()
)
nvmIpFwdPortInFltrProtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrProtId.setStatus("mandatory")


class _NvmIpFwdPortInFltrPortId_Type(Integer32):
    """Custom type nvmIpFwdPortInFltrPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmIpFwdPortInFltrPortId_Type.__name__ = "Integer32"
_NvmIpFwdPortInFltrPortId_Object = MibTableColumn
nvmIpFwdPortInFltrPortId = _NvmIpFwdPortInFltrPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 5),
    _NvmIpFwdPortInFltrPortId_Type()
)
nvmIpFwdPortInFltrPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrPortId.setStatus("mandatory")


class _NvmIpFwdPortInFltrSrcDst_Type(Integer32):
    """Custom type nvmIpFwdPortInFltrSrcDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_NvmIpFwdPortInFltrSrcDst_Type.__name__ = "Integer32"
_NvmIpFwdPortInFltrSrcDst_Object = MibTableColumn
nvmIpFwdPortInFltrSrcDst = _NvmIpFwdPortInFltrSrcDst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 6),
    _NvmIpFwdPortInFltrSrcDst_Type()
)
nvmIpFwdPortInFltrSrcDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrSrcDst.setStatus("mandatory")


class _NvmIpFwdPortInFltrAction_Type(Integer32):
    """Custom type nvmIpFwdPortInFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpFwdPortInFltrAction_Type.__name__ = "Integer32"
_NvmIpFwdPortInFltrAction_Object = MibTableColumn
nvmIpFwdPortInFltrAction = _NvmIpFwdPortInFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 16, 1, 7),
    _NvmIpFwdPortInFltrAction_Type()
)
nvmIpFwdPortInFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortInFltrAction.setStatus("mandatory")
_NvmIpFwdPortOutFltrTable_Object = MibTable
nvmIpFwdPortOutFltrTable = _NvmIpFwdPortOutFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17)
)
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrTable.setStatus("mandatory")
_NvmIpFwdPortOutFltrEntry_Object = MibTableRow
nvmIpFwdPortOutFltrEntry = _NvmIpFwdPortOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1)
)
nvmIpFwdPortOutFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpFwdPortOutFltrPortNo"),
    (0, "MICOMFLTR", "nvmIpFwdPortOutFltrMask"),
    (0, "MICOMFLTR", "nvmIpFwdPortOutFltrAddr"),
    (0, "MICOMFLTR", "nvmIpFwdPortOutFltrProtId"),
    (0, "MICOMFLTR", "nvmIpFwdPortOutFltrPortId"),
)
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrEntry.setStatus("mandatory")


class _NvmIpFwdPortOutFltrPortNo_Type(Integer32):
    """Custom type nvmIpFwdPortOutFltrPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmIpFwdPortOutFltrPortNo_Type.__name__ = "Integer32"
_NvmIpFwdPortOutFltrPortNo_Object = MibTableColumn
nvmIpFwdPortOutFltrPortNo = _NvmIpFwdPortOutFltrPortNo_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 1),
    _NvmIpFwdPortOutFltrPortNo_Type()
)
nvmIpFwdPortOutFltrPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrPortNo.setStatus("mandatory")
_NvmIpFwdPortOutFltrMask_Type = IpAddress
_NvmIpFwdPortOutFltrMask_Object = MibTableColumn
nvmIpFwdPortOutFltrMask = _NvmIpFwdPortOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 2),
    _NvmIpFwdPortOutFltrMask_Type()
)
nvmIpFwdPortOutFltrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrMask.setStatus("mandatory")
_NvmIpFwdPortOutFltrAddr_Type = IpAddress
_NvmIpFwdPortOutFltrAddr_Object = MibTableColumn
nvmIpFwdPortOutFltrAddr = _NvmIpFwdPortOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 3),
    _NvmIpFwdPortOutFltrAddr_Type()
)
nvmIpFwdPortOutFltrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrAddr.setStatus("mandatory")


class _NvmIpFwdPortOutFltrProtId_Type(Integer32):
    """Custom type nvmIpFwdPortOutFltrProtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmIpFwdPortOutFltrProtId_Type.__name__ = "Integer32"
_NvmIpFwdPortOutFltrProtId_Object = MibTableColumn
nvmIpFwdPortOutFltrProtId = _NvmIpFwdPortOutFltrProtId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 4),
    _NvmIpFwdPortOutFltrProtId_Type()
)
nvmIpFwdPortOutFltrProtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrProtId.setStatus("mandatory")


class _NvmIpFwdPortOutFltrPortId_Type(Integer32):
    """Custom type nvmIpFwdPortOutFltrPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmIpFwdPortOutFltrPortId_Type.__name__ = "Integer32"
_NvmIpFwdPortOutFltrPortId_Object = MibTableColumn
nvmIpFwdPortOutFltrPortId = _NvmIpFwdPortOutFltrPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 5),
    _NvmIpFwdPortOutFltrPortId_Type()
)
nvmIpFwdPortOutFltrPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrPortId.setStatus("mandatory")


class _NvmIpFwdPortOutFltrSrcDst_Type(Integer32):
    """Custom type nvmIpFwdPortOutFltrSrcDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_NvmIpFwdPortOutFltrSrcDst_Type.__name__ = "Integer32"
_NvmIpFwdPortOutFltrSrcDst_Object = MibTableColumn
nvmIpFwdPortOutFltrSrcDst = _NvmIpFwdPortOutFltrSrcDst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 6),
    _NvmIpFwdPortOutFltrSrcDst_Type()
)
nvmIpFwdPortOutFltrSrcDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrSrcDst.setStatus("mandatory")


class _NvmIpFwdPortOutFltrAction_Type(Integer32):
    """Custom type nvmIpFwdPortOutFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpFwdPortOutFltrAction_Type.__name__ = "Integer32"
_NvmIpFwdPortOutFltrAction_Object = MibTableColumn
nvmIpFwdPortOutFltrAction = _NvmIpFwdPortOutFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 17, 1, 7),
    _NvmIpFwdPortOutFltrAction_Type()
)
nvmIpFwdPortOutFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpFwdPortOutFltrAction.setStatus("mandatory")
_NvmIpSysFltrTable_Object = MibTable
nvmIpSysFltrTable = _NvmIpSysFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18)
)
if mibBuilder.loadTexts:
    nvmIpSysFltrTable.setStatus("mandatory")
_NvmIpSysFltrEntry_Object = MibTableRow
nvmIpSysFltrEntry = _NvmIpSysFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1)
)
nvmIpSysFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpSysFltrDstMask"),
    (0, "MICOMFLTR", "nvmIpSysFltrDstAddr"),
    (0, "MICOMFLTR", "nvmIpSysFltrSrcMask"),
    (0, "MICOMFLTR", "nvmIpSysFltrSrcAddr"),
    (0, "MICOMFLTR", "nvmIpSysFltrProtId"),
    (0, "MICOMFLTR", "nvmIpSysFltrPortId"),
)
if mibBuilder.loadTexts:
    nvmIpSysFltrEntry.setStatus("mandatory")
_NvmIpSysFltrDstMask_Type = IpAddress
_NvmIpSysFltrDstMask_Object = MibTableColumn
nvmIpSysFltrDstMask = _NvmIpSysFltrDstMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 1),
    _NvmIpSysFltrDstMask_Type()
)
nvmIpSysFltrDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrDstMask.setStatus("mandatory")
_NvmIpSysFltrDstAddr_Type = IpAddress
_NvmIpSysFltrDstAddr_Object = MibTableColumn
nvmIpSysFltrDstAddr = _NvmIpSysFltrDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 2),
    _NvmIpSysFltrDstAddr_Type()
)
nvmIpSysFltrDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrDstAddr.setStatus("mandatory")
_NvmIpSysFltrSrcMask_Type = IpAddress
_NvmIpSysFltrSrcMask_Object = MibTableColumn
nvmIpSysFltrSrcMask = _NvmIpSysFltrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 3),
    _NvmIpSysFltrSrcMask_Type()
)
nvmIpSysFltrSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrSrcMask.setStatus("mandatory")
_NvmIpSysFltrSrcAddr_Type = IpAddress
_NvmIpSysFltrSrcAddr_Object = MibTableColumn
nvmIpSysFltrSrcAddr = _NvmIpSysFltrSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 4),
    _NvmIpSysFltrSrcAddr_Type()
)
nvmIpSysFltrSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrSrcAddr.setStatus("mandatory")


class _NvmIpSysFltrProtId_Type(Integer32):
    """Custom type nvmIpSysFltrProtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmIpSysFltrProtId_Type.__name__ = "Integer32"
_NvmIpSysFltrProtId_Object = MibTableColumn
nvmIpSysFltrProtId = _NvmIpSysFltrProtId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 5),
    _NvmIpSysFltrProtId_Type()
)
nvmIpSysFltrProtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrProtId.setStatus("mandatory")


class _NvmIpSysFltrPortId_Type(Integer32):
    """Custom type nvmIpSysFltrPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmIpSysFltrPortId_Type.__name__ = "Integer32"
_NvmIpSysFltrPortId_Object = MibTableColumn
nvmIpSysFltrPortId = _NvmIpSysFltrPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 6),
    _NvmIpSysFltrPortId_Type()
)
nvmIpSysFltrPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrPortId.setStatus("mandatory")


class _NvmIpSysFltrAction_Type(Integer32):
    """Custom type nvmIpSysFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_NvmIpSysFltrAction_Type.__name__ = "Integer32"
_NvmIpSysFltrAction_Object = MibTableColumn
nvmIpSysFltrAction = _NvmIpSysFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 18, 1, 7),
    _NvmIpSysFltrAction_Type()
)
nvmIpSysFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpSysFltrAction.setStatus("mandatory")
_McmipxSysFilterGroup_ObjectIdentity = ObjectIdentity
mcmipxSysFilterGroup = _McmipxSysFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 19)
)


class _McmipxSysRipFilter_Type(Integer32):
    """Custom type mcmipxSysRipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_McmipxSysRipFilter_Type.__name__ = "Integer32"
_McmipxSysRipFilter_Object = MibScalar
mcmipxSysRipFilter = _McmipxSysRipFilter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 19, 1),
    _McmipxSysRipFilter_Type()
)
mcmipxSysRipFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxSysRipFilter.setStatus("mandatory")


class _McmipxSysSapFilter_Type(Integer32):
    """Custom type mcmipxSysSapFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_McmipxSysSapFilter_Type.__name__ = "Integer32"
_McmipxSysSapFilter_Object = MibScalar
mcmipxSysSapFilter = _McmipxSysSapFilter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 19, 2),
    _McmipxSysSapFilter_Type()
)
mcmipxSysSapFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxSysSapFilter.setStatus("mandatory")


class _McmipxSysNetFilter_Type(Integer32):
    """Custom type mcmipxSysNetFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_McmipxSysNetFilter_Type.__name__ = "Integer32"
_McmipxSysNetFilter_Object = MibScalar
mcmipxSysNetFilter = _McmipxSysNetFilter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 19, 3),
    _McmipxSysNetFilter_Type()
)
mcmipxSysNetFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmipxSysNetFilter.setStatus("mandatory")
_NvmipxSysFilterGroup_ObjectIdentity = ObjectIdentity
nvmipxSysFilterGroup = _NvmipxSysFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 20)
)


class _NvmipxSysRipFilter_Type(Integer32):
    """Custom type nvmipxSysRipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_NvmipxSysRipFilter_Type.__name__ = "Integer32"
_NvmipxSysRipFilter_Object = MibScalar
nvmipxSysRipFilter = _NvmipxSysRipFilter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 20, 1),
    _NvmipxSysRipFilter_Type()
)
nvmipxSysRipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxSysRipFilter.setStatus("mandatory")


class _NvmipxSysSapFilter_Type(Integer32):
    """Custom type nvmipxSysSapFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_NvmipxSysSapFilter_Type.__name__ = "Integer32"
_NvmipxSysSapFilter_Object = MibScalar
nvmipxSysSapFilter = _NvmipxSysSapFilter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 20, 2),
    _NvmipxSysSapFilter_Type()
)
nvmipxSysSapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxSysSapFilter.setStatus("mandatory")


class _NvmipxSysNetFilter_Type(Integer32):
    """Custom type nvmipxSysNetFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_NvmipxSysNetFilter_Type.__name__ = "Integer32"
_NvmipxSysNetFilter_Object = MibScalar
nvmipxSysNetFilter = _NvmipxSysNetFilter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 20, 3),
    _NvmipxSysNetFilter_Type()
)
nvmipxSysNetFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmipxSysNetFilter.setStatus("mandatory")
_McmIpxRipFltrTable_Object = MibTable
mcmIpxRipFltrTable = _McmIpxRipFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 21)
)
if mibBuilder.loadTexts:
    mcmIpxRipFltrTable.setStatus("mandatory")
_McmIpxRipFltrEntry_Object = MibTableRow
mcmIpxRipFltrEntry = _McmIpxRipFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 21, 1)
)
mcmIpxRipFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpxRipFltrSysInstance"),
    (0, "MICOMFLTR", "mcmIpxRipFltrNetNumber"),
)
if mibBuilder.loadTexts:
    mcmIpxRipFltrEntry.setStatus("mandatory")


class _McmIpxRipFltrSysInstance_Type(Integer32):
    """Custom type mcmIpxRipFltrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_McmIpxRipFltrSysInstance_Type.__name__ = "Integer32"
_McmIpxRipFltrSysInstance_Object = MibTableColumn
mcmIpxRipFltrSysInstance = _McmIpxRipFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 21, 1, 1),
    _McmIpxRipFltrSysInstance_Type()
)
mcmIpxRipFltrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxRipFltrSysInstance.setStatus("mandatory")
_McmIpxRipFltrNetNumber_Type = NetNumber
_McmIpxRipFltrNetNumber_Object = MibTableColumn
mcmIpxRipFltrNetNumber = _McmIpxRipFltrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 21, 1, 2),
    _McmIpxRipFltrNetNumber_Type()
)
mcmIpxRipFltrNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxRipFltrNetNumber.setStatus("mandatory")


class _McmIpxRipFltrPort_Type(Integer32):
    """Custom type mcmIpxRipFltrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet", 2),
          ("wan", 1))
    )


_McmIpxRipFltrPort_Type.__name__ = "Integer32"
_McmIpxRipFltrPort_Object = MibTableColumn
mcmIpxRipFltrPort = _McmIpxRipFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 21, 1, 3),
    _McmIpxRipFltrPort_Type()
)
mcmIpxRipFltrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxRipFltrPort.setStatus("mandatory")
_McmIpxSapFltrTable_Object = MibTable
mcmIpxSapFltrTable = _McmIpxSapFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 22)
)
if mibBuilder.loadTexts:
    mcmIpxSapFltrTable.setStatus("mandatory")
_McmIpxSapFltrEntry_Object = MibTableRow
mcmIpxSapFltrEntry = _McmIpxSapFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 22, 1)
)
mcmIpxSapFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpxSapFltrSysInstance"),
    (0, "MICOMFLTR", "mcmIpxSapFltrSapType"),
)
if mibBuilder.loadTexts:
    mcmIpxSapFltrEntry.setStatus("mandatory")


class _McmIpxSapFltrSysInstance_Type(Integer32):
    """Custom type mcmIpxSapFltrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_McmIpxSapFltrSysInstance_Type.__name__ = "Integer32"
_McmIpxSapFltrSysInstance_Object = MibTableColumn
mcmIpxSapFltrSysInstance = _McmIpxSapFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 22, 1, 1),
    _McmIpxSapFltrSysInstance_Type()
)
mcmIpxSapFltrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxSapFltrSysInstance.setStatus("mandatory")
_McmIpxSapFltrSapType_Type = SapType
_McmIpxSapFltrSapType_Object = MibTableColumn
mcmIpxSapFltrSapType = _McmIpxSapFltrSapType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 22, 1, 2),
    _McmIpxSapFltrSapType_Type()
)
mcmIpxSapFltrSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxSapFltrSapType.setStatus("mandatory")


class _McmIpxSapFltrPort_Type(Integer32):
    """Custom type mcmIpxSapFltrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet", 2),
          ("wan", 1))
    )


_McmIpxSapFltrPort_Type.__name__ = "Integer32"
_McmIpxSapFltrPort_Object = MibTableColumn
mcmIpxSapFltrPort = _McmIpxSapFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 22, 1, 3),
    _McmIpxSapFltrPort_Type()
)
mcmIpxSapFltrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxSapFltrPort.setStatus("mandatory")
_McmIpxNetFltrTable_Object = MibTable
mcmIpxNetFltrTable = _McmIpxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 23)
)
if mibBuilder.loadTexts:
    mcmIpxNetFltrTable.setStatus("mandatory")
_McmIpxNetFltrEntry_Object = MibTableRow
mcmIpxNetFltrEntry = _McmIpxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 23, 1)
)
mcmIpxNetFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "mcmIpxNetFltrSysInstance"),
    (0, "MICOMFLTR", "mcmIpxNetFltrNetNumber"),
)
if mibBuilder.loadTexts:
    mcmIpxNetFltrEntry.setStatus("mandatory")


class _McmIpxNetFltrSysInstance_Type(Integer32):
    """Custom type mcmIpxNetFltrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_McmIpxNetFltrSysInstance_Type.__name__ = "Integer32"
_McmIpxNetFltrSysInstance_Object = MibTableColumn
mcmIpxNetFltrSysInstance = _McmIpxNetFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 23, 1, 1),
    _McmIpxNetFltrSysInstance_Type()
)
mcmIpxNetFltrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxNetFltrSysInstance.setStatus("mandatory")
_McmIpxNetFltrNetNumber_Type = NetNumber
_McmIpxNetFltrNetNumber_Object = MibTableColumn
mcmIpxNetFltrNetNumber = _McmIpxNetFltrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 23, 1, 2),
    _McmIpxNetFltrNetNumber_Type()
)
mcmIpxNetFltrNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxNetFltrNetNumber.setStatus("mandatory")


class _McmIpxNetFltrPort_Type(Integer32):
    """Custom type mcmIpxNetFltrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet", 2),
          ("wan", 1))
    )


_McmIpxNetFltrPort_Type.__name__ = "Integer32"
_McmIpxNetFltrPort_Object = MibTableColumn
mcmIpxNetFltrPort = _McmIpxNetFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 23, 1, 3),
    _McmIpxNetFltrPort_Type()
)
mcmIpxNetFltrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxNetFltrPort.setStatus("mandatory")


class _McmIpxNetFltrDir_Type(Integer32):
    """Custom type mcmIpxNetFltrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("destination", 2),
          ("source", 1))
    )


_McmIpxNetFltrDir_Type.__name__ = "Integer32"
_McmIpxNetFltrDir_Object = MibTableColumn
mcmIpxNetFltrDir = _McmIpxNetFltrDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 23, 1, 4),
    _McmIpxNetFltrDir_Type()
)
mcmIpxNetFltrDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIpxNetFltrDir.setStatus("mandatory")
_NvmIpxRipFltrTable_Object = MibTable
nvmIpxRipFltrTable = _NvmIpxRipFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 24)
)
if mibBuilder.loadTexts:
    nvmIpxRipFltrTable.setStatus("mandatory")
_NvmIpxRipFltrEntry_Object = MibTableRow
nvmIpxRipFltrEntry = _NvmIpxRipFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 24, 1)
)
nvmIpxRipFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpxRipFltrSysInstance"),
    (0, "MICOMFLTR", "nvmIpxRipFltrNetNumber"),
)
if mibBuilder.loadTexts:
    nvmIpxRipFltrEntry.setStatus("mandatory")


class _NvmIpxRipFltrSysInstance_Type(Integer32):
    """Custom type nvmIpxRipFltrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NvmIpxRipFltrSysInstance_Type.__name__ = "Integer32"
_NvmIpxRipFltrSysInstance_Object = MibTableColumn
nvmIpxRipFltrSysInstance = _NvmIpxRipFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 24, 1, 1),
    _NvmIpxRipFltrSysInstance_Type()
)
nvmIpxRipFltrSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxRipFltrSysInstance.setStatus("mandatory")
_NvmIpxRipFltrNetNumber_Type = NetNumber
_NvmIpxRipFltrNetNumber_Object = MibTableColumn
nvmIpxRipFltrNetNumber = _NvmIpxRipFltrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 24, 1, 2),
    _NvmIpxRipFltrNetNumber_Type()
)
nvmIpxRipFltrNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxRipFltrNetNumber.setStatus("mandatory")


class _NvmIpxRipFltrPort_Type(Integer32):
    """Custom type nvmIpxRipFltrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet", 2),
          ("wan", 1))
    )


_NvmIpxRipFltrPort_Type.__name__ = "Integer32"
_NvmIpxRipFltrPort_Object = MibTableColumn
nvmIpxRipFltrPort = _NvmIpxRipFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 24, 1, 3),
    _NvmIpxRipFltrPort_Type()
)
nvmIpxRipFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxRipFltrPort.setStatus("mandatory")


class _NvmIpxRipFltrRowStatus_Type(Integer32):
    """Custom type nvmIpxRipFltrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_NvmIpxRipFltrRowStatus_Type.__name__ = "Integer32"
_NvmIpxRipFltrRowStatus_Object = MibTableColumn
nvmIpxRipFltrRowStatus = _NvmIpxRipFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 24, 1, 4),
    _NvmIpxRipFltrRowStatus_Type()
)
nvmIpxRipFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxRipFltrRowStatus.setStatus("mandatory")
_NvmIpxSapFltrTable_Object = MibTable
nvmIpxSapFltrTable = _NvmIpxSapFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 25)
)
if mibBuilder.loadTexts:
    nvmIpxSapFltrTable.setStatus("mandatory")
_NvmIpxSapFltrEntry_Object = MibTableRow
nvmIpxSapFltrEntry = _NvmIpxSapFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 25, 1)
)
nvmIpxSapFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpxSapFltrSysInstance"),
    (0, "MICOMFLTR", "nvmIpxSapFltrSapType"),
)
if mibBuilder.loadTexts:
    nvmIpxSapFltrEntry.setStatus("mandatory")


class _NvmIpxSapFltrSysInstance_Type(Integer32):
    """Custom type nvmIpxSapFltrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NvmIpxSapFltrSysInstance_Type.__name__ = "Integer32"
_NvmIpxSapFltrSysInstance_Object = MibTableColumn
nvmIpxSapFltrSysInstance = _NvmIpxSapFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 25, 1, 1),
    _NvmIpxSapFltrSysInstance_Type()
)
nvmIpxSapFltrSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxSapFltrSysInstance.setStatus("mandatory")
_NvmIpxSapFltrSapType_Type = SapType
_NvmIpxSapFltrSapType_Object = MibTableColumn
nvmIpxSapFltrSapType = _NvmIpxSapFltrSapType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 25, 1, 2),
    _NvmIpxSapFltrSapType_Type()
)
nvmIpxSapFltrSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxSapFltrSapType.setStatus("mandatory")


class _NvmIpxSapFltrPort_Type(Integer32):
    """Custom type nvmIpxSapFltrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet", 2),
          ("wan", 1))
    )


_NvmIpxSapFltrPort_Type.__name__ = "Integer32"
_NvmIpxSapFltrPort_Object = MibTableColumn
nvmIpxSapFltrPort = _NvmIpxSapFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 25, 1, 3),
    _NvmIpxSapFltrPort_Type()
)
nvmIpxSapFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxSapFltrPort.setStatus("mandatory")


class _NvmIpxSapFltrRowStatus_Type(Integer32):
    """Custom type nvmIpxSapFltrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_NvmIpxSapFltrRowStatus_Type.__name__ = "Integer32"
_NvmIpxSapFltrRowStatus_Object = MibTableColumn
nvmIpxSapFltrRowStatus = _NvmIpxSapFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 25, 1, 4),
    _NvmIpxSapFltrRowStatus_Type()
)
nvmIpxSapFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxSapFltrRowStatus.setStatus("mandatory")
_NvmIpxNetFltrTable_Object = MibTable
nvmIpxNetFltrTable = _NvmIpxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26)
)
if mibBuilder.loadTexts:
    nvmIpxNetFltrTable.setStatus("mandatory")
_NvmIpxNetFltrEntry_Object = MibTableRow
nvmIpxNetFltrEntry = _NvmIpxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26, 1)
)
nvmIpxNetFltrEntry.setIndexNames(
    (0, "MICOMFLTR", "nvmIpxNetFltrSysInstance"),
    (0, "MICOMFLTR", "nvmIpxNetFltrNetNumber"),
)
if mibBuilder.loadTexts:
    nvmIpxNetFltrEntry.setStatus("mandatory")


class _NvmIpxNetFltrSysInstance_Type(Integer32):
    """Custom type nvmIpxNetFltrSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NvmIpxNetFltrSysInstance_Type.__name__ = "Integer32"
_NvmIpxNetFltrSysInstance_Object = MibTableColumn
nvmIpxNetFltrSysInstance = _NvmIpxNetFltrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26, 1, 1),
    _NvmIpxNetFltrSysInstance_Type()
)
nvmIpxNetFltrSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxNetFltrSysInstance.setStatus("mandatory")
_NvmIpxNetFltrNetNumber_Type = NetNumber
_NvmIpxNetFltrNetNumber_Object = MibTableColumn
nvmIpxNetFltrNetNumber = _NvmIpxNetFltrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26, 1, 2),
    _NvmIpxNetFltrNetNumber_Type()
)
nvmIpxNetFltrNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxNetFltrNetNumber.setStatus("mandatory")


class _NvmIpxNetFltrPort_Type(Integer32):
    """Custom type nvmIpxNetFltrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernet", 2),
          ("wan", 1))
    )


_NvmIpxNetFltrPort_Type.__name__ = "Integer32"
_NvmIpxNetFltrPort_Object = MibTableColumn
nvmIpxNetFltrPort = _NvmIpxNetFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26, 1, 3),
    _NvmIpxNetFltrPort_Type()
)
nvmIpxNetFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxNetFltrPort.setStatus("mandatory")


class _NvmIpxNetFltrDir_Type(Integer32):
    """Custom type nvmIpxNetFltrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("destination", 2),
          ("source", 1))
    )


_NvmIpxNetFltrDir_Type.__name__ = "Integer32"
_NvmIpxNetFltrDir_Object = MibTableColumn
nvmIpxNetFltrDir = _NvmIpxNetFltrDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26, 1, 4),
    _NvmIpxNetFltrDir_Type()
)
nvmIpxNetFltrDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxNetFltrDir.setStatus("mandatory")


class _NvmIpxNetFltrRowStatus_Type(Integer32):
    """Custom type nvmIpxNetFltrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_NvmIpxNetFltrRowStatus_Type.__name__ = "Integer32"
_NvmIpxNetFltrRowStatus_Object = MibTableColumn
nvmIpxNetFltrRowStatus = _NvmIpxNetFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 12, 26, 1, 5),
    _NvmIpxNetFltrRowStatus_Type()
)
nvmIpxNetFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIpxNetFltrRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOMFLTR",
    **{"NetNumber": NetNumber,
       "SapType": SapType,
       "mcmfilter": mcmfilter,
       "mcmipxMacFltrTable": mcmipxMacFltrTable,
       "mcmipxMacFltrEntry": mcmipxMacFltrEntry,
       "mcmipxMacFltrSysInstance": mcmipxMacFltrSysInstance,
       "mcmipxMacFltrId": mcmipxMacFltrId,
       "mcmipxMacFltrStatus": mcmipxMacFltrStatus,
       "mcmipxMacFltrSrcAddress": mcmipxMacFltrSrcAddress,
       "mcmipxMacFltrDstAddress": mcmipxMacFltrDstAddress,
       "mcmipxMacFltrSrcMask": mcmipxMacFltrSrcMask,
       "mcmipxMacFltrDstMask": mcmipxMacFltrDstMask,
       "mcmipxMacFltrPort": mcmipxMacFltrPort,
       "mcmipxMacFltrDir": mcmipxMacFltrDir,
       "mcmipxNetFltrTable": mcmipxNetFltrTable,
       "mcmipxNetFltrEntry": mcmipxNetFltrEntry,
       "mcmipxNetFltrSysInstance": mcmipxNetFltrSysInstance,
       "mcmipxNetFltrId": mcmipxNetFltrId,
       "mcmipxNetFltrStatus": mcmipxNetFltrStatus,
       "mcmipxNetFltrNetNumber": mcmipxNetFltrNetNumber,
       "mcmipxNetFltrSapType": mcmipxNetFltrSapType,
       "mcmipxNetFltrNetMask": mcmipxNetFltrNetMask,
       "mcmipxNetFltrSapMask": mcmipxNetFltrSapMask,
       "mcmipxNetFltrPort": mcmipxNetFltrPort,
       "mcmipxNetFltrDir": mcmipxNetFltrDir,
       "nvmipxMacFltrTable": nvmipxMacFltrTable,
       "nvmipxMacFltrEntry": nvmipxMacFltrEntry,
       "nvmipxMacFltrSysInstance": nvmipxMacFltrSysInstance,
       "nvmipxMacFltrId": nvmipxMacFltrId,
       "nvmipxMacFltrStatus": nvmipxMacFltrStatus,
       "nvmipxMacFltrSrcAddress": nvmipxMacFltrSrcAddress,
       "nvmipxMacFltrDstAddress": nvmipxMacFltrDstAddress,
       "nvmipxMacFltrSrcMask": nvmipxMacFltrSrcMask,
       "nvmipxMacFltrDstMask": nvmipxMacFltrDstMask,
       "nvmipxMacFltrPort": nvmipxMacFltrPort,
       "nvmipxMacFltrDir": nvmipxMacFltrDir,
       "nvmipxNetFltrTable": nvmipxNetFltrTable,
       "nvmipxNetFltrEntry": nvmipxNetFltrEntry,
       "nvmipxNetFltrSysInstance": nvmipxNetFltrSysInstance,
       "nvmipxNetFltrId": nvmipxNetFltrId,
       "nvmipxNetFltrStatus": nvmipxNetFltrStatus,
       "nvmipxNetFltrNetNumber": nvmipxNetFltrNetNumber,
       "nvmipxNetFltrSapType": nvmipxNetFltrSapType,
       "nvmipxNetFltrNetMask": nvmipxNetFltrNetMask,
       "nvmipxNetFltrSapMask": nvmipxNetFltrSapMask,
       "nvmipxNetFltrPort": nvmipxNetFltrPort,
       "nvmipxNetFltrDir": nvmipxNetFltrDir,
       "mcmIpRipInFltrTable": mcmIpRipInFltrTable,
       "mcmIpRipInFltrEntry": mcmIpRipInFltrEntry,
       "mcmIpRipInFltrMask": mcmIpRipInFltrMask,
       "mcmIpRipInFltrAddr": mcmIpRipInFltrAddr,
       "mcmIpRipInFltrAction": mcmIpRipInFltrAction,
       "mcmIpRipOutFltrTable": mcmIpRipOutFltrTable,
       "mcmIpRipOutFltrEntry": mcmIpRipOutFltrEntry,
       "mcmIpRipOutFltrMask": mcmIpRipOutFltrMask,
       "mcmIpRipOutFltrAddr": mcmIpRipOutFltrAddr,
       "mcmIpRipOutFltrAction": mcmIpRipOutFltrAction,
       "mcmIpRipGwyFltrTable": mcmIpRipGwyFltrTable,
       "mcmIpRipGwyFltrEntry": mcmIpRipGwyFltrEntry,
       "mcmIpRipGwyFltrMask": mcmIpRipGwyFltrMask,
       "mcmIpRipGwyFltrAddr": mcmIpRipGwyFltrAddr,
       "mcmIpRipGwyFltrAction": mcmIpRipGwyFltrAction,
       "mcmIpOspfOutFltrTable": mcmIpOspfOutFltrTable,
       "mcmIpOspfOutFltrEntry": mcmIpOspfOutFltrEntry,
       "mcmIpOspfOutFltrMask": mcmIpOspfOutFltrMask,
       "mcmIpOspfOutFltrAddr": mcmIpOspfOutFltrAddr,
       "mcmIpOspfOutFltrAction": mcmIpOspfOutFltrAction,
       "mcmIpFwdPortInFltrTable": mcmIpFwdPortInFltrTable,
       "mcmIpFwdPortInFltrEntry": mcmIpFwdPortInFltrEntry,
       "mcmIpFwdPortInFltrPortNo": mcmIpFwdPortInFltrPortNo,
       "mcmIpFwdPortInFltrMask": mcmIpFwdPortInFltrMask,
       "mcmIpFwdPortInFltrAddr": mcmIpFwdPortInFltrAddr,
       "mcmIpFwdPortInFltrProtId": mcmIpFwdPortInFltrProtId,
       "mcmIpFwdPortInFltrPortId": mcmIpFwdPortInFltrPortId,
       "mcmIpFwdPortInFltrSrcDst": mcmIpFwdPortInFltrSrcDst,
       "mcmIpFwdPortInFltrAction": mcmIpFwdPortInFltrAction,
       "mcmIpFwdPortOutFltrTable": mcmIpFwdPortOutFltrTable,
       "mcmIpFwdPortOutFltrEntry": mcmIpFwdPortOutFltrEntry,
       "mcmIpFwdPortOutFltrPortNo": mcmIpFwdPortOutFltrPortNo,
       "mcmIpFwdPortOutFltrMask": mcmIpFwdPortOutFltrMask,
       "mcmIpFwdPortOutFltrAddr": mcmIpFwdPortOutFltrAddr,
       "mcmIpFwdPortOutFltrProtId": mcmIpFwdPortOutFltrProtId,
       "mcmIpFwdPortOutFltrPortId": mcmIpFwdPortOutFltrPortId,
       "mcmIpFwdPortOutFltrSrcDst": mcmIpFwdPortOutFltrSrcDst,
       "mcmIpFwdPortOutFltrAction": mcmIpFwdPortOutFltrAction,
       "mcmIpSysFltrTable": mcmIpSysFltrTable,
       "mcmIpSysFltrEntry": mcmIpSysFltrEntry,
       "mcmIpSysFltrDstMask": mcmIpSysFltrDstMask,
       "mcmIpSysFltrDstAddr": mcmIpSysFltrDstAddr,
       "mcmIpSysFltrSrcMask": mcmIpSysFltrSrcMask,
       "mcmIpSysFltrSrcAddr": mcmIpSysFltrSrcAddr,
       "mcmIpSysFltrProtId": mcmIpSysFltrProtId,
       "mcmIpSysFltrPortId": mcmIpSysFltrPortId,
       "mcmIpSysFltrAction": mcmIpSysFltrAction,
       "nvmIpRipInFltrTable": nvmIpRipInFltrTable,
       "nvmIpRipInFltrEntry": nvmIpRipInFltrEntry,
       "nvmIpRipInFltrMask": nvmIpRipInFltrMask,
       "nvmIpRipInFltrAddr": nvmIpRipInFltrAddr,
       "nvmIpRipInFltrAction": nvmIpRipInFltrAction,
       "nvmIpRipOutFltrTable": nvmIpRipOutFltrTable,
       "nvmIpRipOutFltrEntry": nvmIpRipOutFltrEntry,
       "nvmIpRipOutFltrMask": nvmIpRipOutFltrMask,
       "nvmIpRipOutFltrAddr": nvmIpRipOutFltrAddr,
       "nvmIpRipOutFltrAction": nvmIpRipOutFltrAction,
       "nvmIpRipGwyFltrTable": nvmIpRipGwyFltrTable,
       "nvmIpRipGwyFltrEntry": nvmIpRipGwyFltrEntry,
       "nvmIpRipGwyFltrMask": nvmIpRipGwyFltrMask,
       "nvmIpRipGwyFltrAddr": nvmIpRipGwyFltrAddr,
       "nvmIpRipGwyFltrAction": nvmIpRipGwyFltrAction,
       "nvmIpOspfOutFltrTable": nvmIpOspfOutFltrTable,
       "nvmIpOspfOutFltrEntry": nvmIpOspfOutFltrEntry,
       "nvmIpOspfOutFltrMask": nvmIpOspfOutFltrMask,
       "nvmIpOspfOutFltrAddr": nvmIpOspfOutFltrAddr,
       "nvmIpOspfOutFltrAction": nvmIpOspfOutFltrAction,
       "nvmIpFwdPortInFltrTable": nvmIpFwdPortInFltrTable,
       "nvmIpFwdPortInFltrEntry": nvmIpFwdPortInFltrEntry,
       "nvmIpFwdPortInFltrPortNo": nvmIpFwdPortInFltrPortNo,
       "nvmIpFwdPortInFltrMask": nvmIpFwdPortInFltrMask,
       "nvmIpFwdPortInFltrAddr": nvmIpFwdPortInFltrAddr,
       "nvmIpFwdPortInFltrProtId": nvmIpFwdPortInFltrProtId,
       "nvmIpFwdPortInFltrPortId": nvmIpFwdPortInFltrPortId,
       "nvmIpFwdPortInFltrSrcDst": nvmIpFwdPortInFltrSrcDst,
       "nvmIpFwdPortInFltrAction": nvmIpFwdPortInFltrAction,
       "nvmIpFwdPortOutFltrTable": nvmIpFwdPortOutFltrTable,
       "nvmIpFwdPortOutFltrEntry": nvmIpFwdPortOutFltrEntry,
       "nvmIpFwdPortOutFltrPortNo": nvmIpFwdPortOutFltrPortNo,
       "nvmIpFwdPortOutFltrMask": nvmIpFwdPortOutFltrMask,
       "nvmIpFwdPortOutFltrAddr": nvmIpFwdPortOutFltrAddr,
       "nvmIpFwdPortOutFltrProtId": nvmIpFwdPortOutFltrProtId,
       "nvmIpFwdPortOutFltrPortId": nvmIpFwdPortOutFltrPortId,
       "nvmIpFwdPortOutFltrSrcDst": nvmIpFwdPortOutFltrSrcDst,
       "nvmIpFwdPortOutFltrAction": nvmIpFwdPortOutFltrAction,
       "nvmIpSysFltrTable": nvmIpSysFltrTable,
       "nvmIpSysFltrEntry": nvmIpSysFltrEntry,
       "nvmIpSysFltrDstMask": nvmIpSysFltrDstMask,
       "nvmIpSysFltrDstAddr": nvmIpSysFltrDstAddr,
       "nvmIpSysFltrSrcMask": nvmIpSysFltrSrcMask,
       "nvmIpSysFltrSrcAddr": nvmIpSysFltrSrcAddr,
       "nvmIpSysFltrProtId": nvmIpSysFltrProtId,
       "nvmIpSysFltrPortId": nvmIpSysFltrPortId,
       "nvmIpSysFltrAction": nvmIpSysFltrAction,
       "mcmipxSysFilterGroup": mcmipxSysFilterGroup,
       "mcmipxSysRipFilter": mcmipxSysRipFilter,
       "mcmipxSysSapFilter": mcmipxSysSapFilter,
       "mcmipxSysNetFilter": mcmipxSysNetFilter,
       "nvmipxSysFilterGroup": nvmipxSysFilterGroup,
       "nvmipxSysRipFilter": nvmipxSysRipFilter,
       "nvmipxSysSapFilter": nvmipxSysSapFilter,
       "nvmipxSysNetFilter": nvmipxSysNetFilter,
       "mcmIpxRipFltrTable": mcmIpxRipFltrTable,
       "mcmIpxRipFltrEntry": mcmIpxRipFltrEntry,
       "mcmIpxRipFltrSysInstance": mcmIpxRipFltrSysInstance,
       "mcmIpxRipFltrNetNumber": mcmIpxRipFltrNetNumber,
       "mcmIpxRipFltrPort": mcmIpxRipFltrPort,
       "mcmIpxSapFltrTable": mcmIpxSapFltrTable,
       "mcmIpxSapFltrEntry": mcmIpxSapFltrEntry,
       "mcmIpxSapFltrSysInstance": mcmIpxSapFltrSysInstance,
       "mcmIpxSapFltrSapType": mcmIpxSapFltrSapType,
       "mcmIpxSapFltrPort": mcmIpxSapFltrPort,
       "mcmIpxNetFltrTable": mcmIpxNetFltrTable,
       "mcmIpxNetFltrEntry": mcmIpxNetFltrEntry,
       "mcmIpxNetFltrSysInstance": mcmIpxNetFltrSysInstance,
       "mcmIpxNetFltrNetNumber": mcmIpxNetFltrNetNumber,
       "mcmIpxNetFltrPort": mcmIpxNetFltrPort,
       "mcmIpxNetFltrDir": mcmIpxNetFltrDir,
       "nvmIpxRipFltrTable": nvmIpxRipFltrTable,
       "nvmIpxRipFltrEntry": nvmIpxRipFltrEntry,
       "nvmIpxRipFltrSysInstance": nvmIpxRipFltrSysInstance,
       "nvmIpxRipFltrNetNumber": nvmIpxRipFltrNetNumber,
       "nvmIpxRipFltrPort": nvmIpxRipFltrPort,
       "nvmIpxRipFltrRowStatus": nvmIpxRipFltrRowStatus,
       "nvmIpxSapFltrTable": nvmIpxSapFltrTable,
       "nvmIpxSapFltrEntry": nvmIpxSapFltrEntry,
       "nvmIpxSapFltrSysInstance": nvmIpxSapFltrSysInstance,
       "nvmIpxSapFltrSapType": nvmIpxSapFltrSapType,
       "nvmIpxSapFltrPort": nvmIpxSapFltrPort,
       "nvmIpxSapFltrRowStatus": nvmIpxSapFltrRowStatus,
       "nvmIpxNetFltrTable": nvmIpxNetFltrTable,
       "nvmIpxNetFltrEntry": nvmIpxNetFltrEntry,
       "nvmIpxNetFltrSysInstance": nvmIpxNetFltrSysInstance,
       "nvmIpxNetFltrNetNumber": nvmIpxNetFltrNetNumber,
       "nvmIpxNetFltrPort": nvmIpxNetFltrPort,
       "nvmIpxNetFltrDir": nvmIpxNetFltrDir,
       "nvmIpxNetFltrRowStatus": nvmIpxNetFltrRowStatus}
)
