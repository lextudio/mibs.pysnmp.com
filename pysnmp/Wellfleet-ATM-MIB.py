# SNMP MIB module (Wellfleet-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:50 2024
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

(wfAtmGroup,
 wfAtmInterfaceGroup,
 wfSonetGroup) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAtmGroup",
    "wfAtmInterfaceGroup",
    "wfSonetGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAtmCommonGroup_ObjectIdentity = ObjectIdentity
wfAtmCommonGroup = _WfAtmCommonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1)
)
_WfAtmInterfaceConfTable_Object = MibTable
wfAtmInterfaceConfTable = _WfAtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1)
)
if mibBuilder.loadTexts:
    wfAtmInterfaceConfTable.setStatus("mandatory")
_WfAtmInterfaceConfEntry_Object = MibTableRow
wfAtmInterfaceConfEntry = _WfAtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1)
)
wfAtmInterfaceConfEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    wfAtmInterfaceConfEntry.setStatus("mandatory")


class _WfAtmInterfaceConfDelete_Type(Integer32):
    """Custom type wfAtmInterfaceConfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmInterfaceConfDelete_Type.__name__ = "Integer32"
_WfAtmInterfaceConfDelete_Object = MibTableColumn
wfAtmInterfaceConfDelete = _WfAtmInterfaceConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 1),
    _WfAtmInterfaceConfDelete_Type()
)
wfAtmInterfaceConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceConfDelete.setStatus("mandatory")
_WfAtmInterfaceConfIndex_Type = Integer32
_WfAtmInterfaceConfIndex_Object = MibTableColumn
wfAtmInterfaceConfIndex = _WfAtmInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 2),
    _WfAtmInterfaceConfIndex_Type()
)
wfAtmInterfaceConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceConfIndex.setStatus("mandatory")


class _WfAtmInterfaceAdminStatus_Type(Integer32):
    """Custom type wfAtmInterfaceAdminStatus based on Integer32"""
    defaultValue = 1

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


_WfAtmInterfaceAdminStatus_Type.__name__ = "Integer32"
_WfAtmInterfaceAdminStatus_Object = MibTableColumn
wfAtmInterfaceAdminStatus = _WfAtmInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 3),
    _WfAtmInterfaceAdminStatus_Type()
)
wfAtmInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceAdminStatus.setStatus("mandatory")


class _WfAtmInterfaceOperStatus_Type(Integer32):
    """Custom type wfAtmInterfaceOperStatus based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmInterfaceOperStatus_Type.__name__ = "Integer32"
_WfAtmInterfaceOperStatus_Object = MibTableColumn
wfAtmInterfaceOperStatus = _WfAtmInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 4),
    _WfAtmInterfaceOperStatus_Type()
)
wfAtmInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceOperStatus.setStatus("mandatory")


class _WfAtmInterfaceMaxVpcs_Type(Integer32):
    """Custom type wfAtmInterfaceMaxVpcs based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WfAtmInterfaceMaxVpcs_Type.__name__ = "Integer32"
_WfAtmInterfaceMaxVpcs_Object = MibTableColumn
wfAtmInterfaceMaxVpcs = _WfAtmInterfaceMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 5),
    _WfAtmInterfaceMaxVpcs_Type()
)
wfAtmInterfaceMaxVpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceMaxVpcs.setStatus("mandatory")


class _WfAtmInterfaceMaxVccs_Type(Integer32):
    """Custom type wfAtmInterfaceMaxVccs based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_WfAtmInterfaceMaxVccs_Type.__name__ = "Integer32"
_WfAtmInterfaceMaxVccs_Object = MibTableColumn
wfAtmInterfaceMaxVccs = _WfAtmInterfaceMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 6),
    _WfAtmInterfaceMaxVccs_Type()
)
wfAtmInterfaceMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceMaxVccs.setStatus("mandatory")
_WfAtmInterfaceConfVpcs_Type = Integer32
_WfAtmInterfaceConfVpcs_Object = MibTableColumn
wfAtmInterfaceConfVpcs = _WfAtmInterfaceConfVpcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 7),
    _WfAtmInterfaceConfVpcs_Type()
)
wfAtmInterfaceConfVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceConfVpcs.setStatus("mandatory")
_WfAtmInterfaceConfVccs_Type = Integer32
_WfAtmInterfaceConfVccs_Object = MibTableColumn
wfAtmInterfaceConfVccs = _WfAtmInterfaceConfVccs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 8),
    _WfAtmInterfaceConfVccs_Type()
)
wfAtmInterfaceConfVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceConfVccs.setStatus("mandatory")


class _WfAtmInterfaceMaxActiveVpiBits_Type(Integer32):
    """Custom type wfAtmInterfaceMaxActiveVpiBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WfAtmInterfaceMaxActiveVpiBits_Type.__name__ = "Integer32"
_WfAtmInterfaceMaxActiveVpiBits_Object = MibTableColumn
wfAtmInterfaceMaxActiveVpiBits = _WfAtmInterfaceMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 9),
    _WfAtmInterfaceMaxActiveVpiBits_Type()
)
wfAtmInterfaceMaxActiveVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceMaxActiveVpiBits.setStatus("mandatory")


class _WfAtmInterfaceMaxActiveVciBits_Type(Integer32):
    """Custom type wfAtmInterfaceMaxActiveVciBits based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfAtmInterfaceMaxActiveVciBits_Type.__name__ = "Integer32"
_WfAtmInterfaceMaxActiveVciBits_Object = MibTableColumn
wfAtmInterfaceMaxActiveVciBits = _WfAtmInterfaceMaxActiveVciBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 10),
    _WfAtmInterfaceMaxActiveVciBits_Type()
)
wfAtmInterfaceMaxActiveVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceMaxActiveVciBits.setStatus("mandatory")


class _WfAtmInterfaceIlmiVpi_Type(Integer32):
    """Custom type wfAtmInterfaceIlmiVpi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("default", 1)
    )


_WfAtmInterfaceIlmiVpi_Type.__name__ = "Integer32"
_WfAtmInterfaceIlmiVpi_Object = MibTableColumn
wfAtmInterfaceIlmiVpi = _WfAtmInterfaceIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 11),
    _WfAtmInterfaceIlmiVpi_Type()
)
wfAtmInterfaceIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceIlmiVpi.setStatus("mandatory")


class _WfAtmInterfaceIlmiVci_Type(Integer32):
    """Custom type wfAtmInterfaceIlmiVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16
        )
    )
    namedValues = NamedValues(
        ("default", 16)
    )


_WfAtmInterfaceIlmiVci_Type.__name__ = "Integer32"
_WfAtmInterfaceIlmiVci_Object = MibTableColumn
wfAtmInterfaceIlmiVci = _WfAtmInterfaceIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 12),
    _WfAtmInterfaceIlmiVci_Type()
)
wfAtmInterfaceIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceIlmiVci.setStatus("mandatory")


class _WfAtmInterfaceAddressType_Type(Integer32):
    """Custom type wfAtmInterfaceAddressType based on Integer32"""
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
        *(("nativee164", 3),
          ("nsape164", 2),
          ("other", 4),
          ("private", 1))
    )


_WfAtmInterfaceAddressType_Type.__name__ = "Integer32"
_WfAtmInterfaceAddressType_Object = MibTableColumn
wfAtmInterfaceAddressType = _WfAtmInterfaceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 13),
    _WfAtmInterfaceAddressType_Type()
)
wfAtmInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceAddressType.setStatus("mandatory")
_WfAtmInterfaceCct_Type = Integer32
_WfAtmInterfaceCct_Object = MibTableColumn
wfAtmInterfaceCct = _WfAtmInterfaceCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 14),
    _WfAtmInterfaceCct_Type()
)
wfAtmInterfaceCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceCct.setStatus("mandatory")
_WfAtmInterfaceDrops_Type = Counter32
_WfAtmInterfaceDrops_Object = MibTableColumn
wfAtmInterfaceDrops = _WfAtmInterfaceDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 15),
    _WfAtmInterfaceDrops_Type()
)
wfAtmInterfaceDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceDrops.setStatus("mandatory")


class _WfAtmInterfaceSigEnable_Type(Integer32):
    """Custom type wfAtmInterfaceSigEnable based on Integer32"""
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


_WfAtmInterfaceSigEnable_Type.__name__ = "Integer32"
_WfAtmInterfaceSigEnable_Object = MibTableColumn
wfAtmInterfaceSigEnable = _WfAtmInterfaceSigEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 16),
    _WfAtmInterfaceSigEnable_Type()
)
wfAtmInterfaceSigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceSigEnable.setStatus("mandatory")


class _WfAtmInterfaceDebug_Type(Integer32):
    """Custom type wfAtmInterfaceDebug based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("all", 2147483647),
          ("appMsgs", 16),
          ("disabled", 1),
          ("drvMsgs", 32),
          ("msgs", 2),
          ("msgsIn", 4),
          ("msgsOut", 8),
          ("oam", 512),
          ("pvcFsm", 128),
          ("svcFsm", 256),
          ("trilMsgs", 64))
    )


_WfAtmInterfaceDebug_Type.__name__ = "Integer32"
_WfAtmInterfaceDebug_Object = MibTableColumn
wfAtmInterfaceDebug = _WfAtmInterfaceDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 17),
    _WfAtmInterfaceDebug_Type()
)
wfAtmInterfaceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceDebug.setStatus("mandatory")


class _WfAtmInterfaceUseHwMacAddr_Type(Integer32):
    """Custom type wfAtmInterfaceUseHwMacAddr based on Integer32"""
    defaultValue = 1

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


_WfAtmInterfaceUseHwMacAddr_Type.__name__ = "Integer32"
_WfAtmInterfaceUseHwMacAddr_Object = MibTableColumn
wfAtmInterfaceUseHwMacAddr = _WfAtmInterfaceUseHwMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 18),
    _WfAtmInterfaceUseHwMacAddr_Type()
)
wfAtmInterfaceUseHwMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceUseHwMacAddr.setStatus("mandatory")
_WfAtmInterfaceHwMacOverride_Type = OctetString
_WfAtmInterfaceHwMacOverride_Object = MibTableColumn
wfAtmInterfaceHwMacOverride = _WfAtmInterfaceHwMacOverride_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 19),
    _WfAtmInterfaceHwMacOverride_Type()
)
wfAtmInterfaceHwMacOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceHwMacOverride.setStatus("mandatory")


class _WfAtmServicePqOverride_Type(Integer32):
    """Custom type wfAtmServicePqOverride based on Integer32"""
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


_WfAtmServicePqOverride_Type.__name__ = "Integer32"
_WfAtmServicePqOverride_Object = MibTableColumn
wfAtmServicePqOverride = _WfAtmServicePqOverride_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 1, 1, 20),
    _WfAtmServicePqOverride_Type()
)
wfAtmServicePqOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServicePqOverride.setStatus("mandatory")
_WfAtmServiceRecordTable_Object = MibTable
wfAtmServiceRecordTable = _WfAtmServiceRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2)
)
if mibBuilder.loadTexts:
    wfAtmServiceRecordTable.setStatus("mandatory")
_WfAtmServiceRecordEntry_Object = MibTableRow
wfAtmServiceRecordEntry = _WfAtmServiceRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1)
)
wfAtmServiceRecordEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmServiceRecordIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmServiceRecordCct"),
)
if mibBuilder.loadTexts:
    wfAtmServiceRecordEntry.setStatus("mandatory")


class _WfAtmServiceRecordDelete_Type(Integer32):
    """Custom type wfAtmServiceRecordDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmServiceRecordDelete_Type.__name__ = "Integer32"
_WfAtmServiceRecordDelete_Object = MibTableColumn
wfAtmServiceRecordDelete = _WfAtmServiceRecordDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 1),
    _WfAtmServiceRecordDelete_Type()
)
wfAtmServiceRecordDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordDelete.setStatus("mandatory")


class _WfAtmServiceRecordEnable_Type(Integer32):
    """Custom type wfAtmServiceRecordEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmServiceRecordEnable_Type.__name__ = "Integer32"
_WfAtmServiceRecordEnable_Object = MibTableColumn
wfAtmServiceRecordEnable = _WfAtmServiceRecordEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 2),
    _WfAtmServiceRecordEnable_Type()
)
wfAtmServiceRecordEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordEnable.setStatus("mandatory")
_WfAtmServiceRecordIndex_Type = Integer32
_WfAtmServiceRecordIndex_Object = MibTableColumn
wfAtmServiceRecordIndex = _WfAtmServiceRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 3),
    _WfAtmServiceRecordIndex_Type()
)
wfAtmServiceRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmServiceRecordIndex.setStatus("mandatory")
_WfAtmServiceRecordCct_Type = Integer32
_WfAtmServiceRecordCct_Object = MibTableColumn
wfAtmServiceRecordCct = _WfAtmServiceRecordCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 4),
    _WfAtmServiceRecordCct_Type()
)
wfAtmServiceRecordCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmServiceRecordCct.setStatus("mandatory")


class _WfAtmServiceRecordAalEncapsType_Type(Integer32):
    """Custom type wfAtmServiceRecordAalEncapsType based on Integer32"""
    defaultValue = 7

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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bridged8023", 2),
          ("bridged8025", 3),
          ("bridged8026", 4),
          ("frinterwork", 11),
          ("frsscs", 8),
          ("lane8023", 5),
          ("lane8025", 6),
          ("llcencaps", 7),
          ("mpsencaps", 12),
          ("other", 9),
          ("routedproto", 1),
          ("unknown", 10))
    )


_WfAtmServiceRecordAalEncapsType_Type.__name__ = "Integer32"
_WfAtmServiceRecordAalEncapsType_Object = MibTableColumn
wfAtmServiceRecordAalEncapsType = _WfAtmServiceRecordAalEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 5),
    _WfAtmServiceRecordAalEncapsType_Type()
)
wfAtmServiceRecordAalEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordAalEncapsType.setStatus("mandatory")


class _WfAtmServiceRecordState_Type(Integer32):
    """Custom type wfAtmServiceRecordState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 5),
          ("oamlost", 6),
          ("reject", 4),
          ("up", 1))
    )


_WfAtmServiceRecordState_Type.__name__ = "Integer32"
_WfAtmServiceRecordState_Object = MibTableColumn
wfAtmServiceRecordState = _WfAtmServiceRecordState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 6),
    _WfAtmServiceRecordState_Type()
)
wfAtmServiceRecordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmServiceRecordState.setStatus("mandatory")


class _WfAtmServiceRecordVcType_Type(Integer32):
    """Custom type wfAtmServiceRecordVcType based on Integer32"""
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
        *(("control", 3),
          ("muxedSvc", 4),
          ("pvc", 1),
          ("svc", 2))
    )


_WfAtmServiceRecordVcType_Type.__name__ = "Integer32"
_WfAtmServiceRecordVcType_Object = MibTableColumn
wfAtmServiceRecordVcType = _WfAtmServiceRecordVcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 7),
    _WfAtmServiceRecordVcType_Type()
)
wfAtmServiceRecordVcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordVcType.setStatus("mandatory")


class _WfAtmServiceRecordNetworkPrefix_Type(OctetString):
    """Custom type wfAtmServiceRecordNetworkPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_WfAtmServiceRecordNetworkPrefix_Type.__name__ = "OctetString"
_WfAtmServiceRecordNetworkPrefix_Object = MibTableColumn
wfAtmServiceRecordNetworkPrefix = _WfAtmServiceRecordNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 8),
    _WfAtmServiceRecordNetworkPrefix_Type()
)
wfAtmServiceRecordNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordNetworkPrefix.setStatus("mandatory")


class _WfAtmServiceRecordUserSuffix_Type(OctetString):
    """Custom type wfAtmServiceRecordUserSuffix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_WfAtmServiceRecordUserSuffix_Type.__name__ = "OctetString"
_WfAtmServiceRecordUserSuffix_Object = MibTableColumn
wfAtmServiceRecordUserSuffix = _WfAtmServiceRecordUserSuffix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 9),
    _WfAtmServiceRecordUserSuffix_Type()
)
wfAtmServiceRecordUserSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordUserSuffix.setStatus("mandatory")
_WfAtmServiceRecordAtmAddress_Type = OctetString
_WfAtmServiceRecordAtmAddress_Object = MibTableColumn
wfAtmServiceRecordAtmAddress = _WfAtmServiceRecordAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 10),
    _WfAtmServiceRecordAtmAddress_Type()
)
wfAtmServiceRecordAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmServiceRecordAtmAddress.setStatus("mandatory")


class _WfAtmServiceRecordFlag_Type(Integer32):
    """Custom type wfAtmServiceRecordFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("autoaddr", 1)
    )


_WfAtmServiceRecordFlag_Type.__name__ = "Integer32"
_WfAtmServiceRecordFlag_Object = MibTableColumn
wfAtmServiceRecordFlag = _WfAtmServiceRecordFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 11),
    _WfAtmServiceRecordFlag_Type()
)
wfAtmServiceRecordFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordFlag.setStatus("mandatory")


class _WfAtmServiceRecordMtu_Type(Integer32):
    """Custom type wfAtmServiceRecordMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9188),
    )


_WfAtmServiceRecordMtu_Type.__name__ = "Integer32"
_WfAtmServiceRecordMtu_Object = MibTableColumn
wfAtmServiceRecordMtu = _WfAtmServiceRecordMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 12),
    _WfAtmServiceRecordMtu_Type()
)
wfAtmServiceRecordMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordMtu.setStatus("mandatory")


class _WfAtmServiceRecordLossPriorityPolicy_Type(Integer32):
    """Custom type wfAtmServiceRecordLossPriorityPolicy based on Integer32"""
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


_WfAtmServiceRecordLossPriorityPolicy_Type.__name__ = "Integer32"
_WfAtmServiceRecordLossPriorityPolicy_Object = MibTableColumn
wfAtmServiceRecordLossPriorityPolicy = _WfAtmServiceRecordLossPriorityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 13),
    _WfAtmServiceRecordLossPriorityPolicy_Type()
)
wfAtmServiceRecordLossPriorityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordLossPriorityPolicy.setStatus("mandatory")


class _WfAtmServiceRecordDebug_Type(Integer32):
    """Custom type wfAtmServiceRecordDebug based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("all", 2147483647),
          ("disabled", 1),
          ("llcSvcMux", 8),
          ("pvcFsm", 2),
          ("svcFsm", 4))
    )


_WfAtmServiceRecordDebug_Type.__name__ = "Integer32"
_WfAtmServiceRecordDebug_Object = MibTableColumn
wfAtmServiceRecordDebug = _WfAtmServiceRecordDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 14),
    _WfAtmServiceRecordDebug_Type()
)
wfAtmServiceRecordDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordDebug.setStatus("mandatory")
_WfAtmServiceRecordName_Type = DisplayString
_WfAtmServiceRecordName_Object = MibTableColumn
wfAtmServiceRecordName = _WfAtmServiceRecordName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 15),
    _WfAtmServiceRecordName_Type()
)
wfAtmServiceRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordName.setStatus("mandatory")


class _WfAtmServiceRecordWanSvcRoutingMode_Type(Integer32):
    """Custom type wfAtmServiceRecordWanSvcRoutingMode based on Integer32"""
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
        *(("dialOptimized", 3),
          ("disabled", 1),
          ("normal", 2))
    )


_WfAtmServiceRecordWanSvcRoutingMode_Type.__name__ = "Integer32"
_WfAtmServiceRecordWanSvcRoutingMode_Object = MibTableColumn
wfAtmServiceRecordWanSvcRoutingMode = _WfAtmServiceRecordWanSvcRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 2, 1, 16),
    _WfAtmServiceRecordWanSvcRoutingMode_Type()
)
wfAtmServiceRecordWanSvcRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmServiceRecordWanSvcRoutingMode.setStatus("mandatory")
_WfAtmVclConfTable_Object = MibTable
wfAtmVclConfTable = _WfAtmVclConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5)
)
if mibBuilder.loadTexts:
    wfAtmVclConfTable.setStatus("mandatory")
_WfAtmVclConfEntry_Object = MibTableRow
wfAtmVclConfEntry = _WfAtmVclConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1)
)
wfAtmVclConfEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVclConfIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVclConfVpi"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVclConfVci"),
)
if mibBuilder.loadTexts:
    wfAtmVclConfEntry.setStatus("mandatory")


class _WfAtmVclConfDelete_Type(Integer32):
    """Custom type wfAtmVclConfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmVclConfDelete_Type.__name__ = "Integer32"
_WfAtmVclConfDelete_Object = MibTableColumn
wfAtmVclConfDelete = _WfAtmVclConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 1),
    _WfAtmVclConfDelete_Type()
)
wfAtmVclConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclConfDelete.setStatus("mandatory")
_WfAtmVclConfIndex_Type = Integer32
_WfAtmVclConfIndex_Object = MibTableColumn
wfAtmVclConfIndex = _WfAtmVclConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 2),
    _WfAtmVclConfIndex_Type()
)
wfAtmVclConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclConfIndex.setStatus("mandatory")
_WfAtmVclConfVpi_Type = Integer32
_WfAtmVclConfVpi_Object = MibTableColumn
wfAtmVclConfVpi = _WfAtmVclConfVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 3),
    _WfAtmVclConfVpi_Type()
)
wfAtmVclConfVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclConfVpi.setStatus("mandatory")
_WfAtmVclConfVci_Type = Integer32
_WfAtmVclConfVci_Object = MibTableColumn
wfAtmVclConfVci = _WfAtmVclConfVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 4),
    _WfAtmVclConfVci_Type()
)
wfAtmVclConfVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclConfVci.setStatus("mandatory")


class _WfAtmVclAdminStatus_Type(Integer32):
    """Custom type wfAtmVclAdminStatus based on Integer32"""
    defaultValue = 1

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


_WfAtmVclAdminStatus_Type.__name__ = "Integer32"
_WfAtmVclAdminStatus_Object = MibTableColumn
wfAtmVclAdminStatus = _WfAtmVclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 5),
    _WfAtmVclAdminStatus_Type()
)
wfAtmVclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclAdminStatus.setStatus("mandatory")


class _WfAtmVclOperStatus_Type(Integer32):
    """Custom type wfAtmVclOperStatus based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("misconfig", 6),
          ("notpresent", 4),
          ("oamlost", 5),
          ("up", 1))
    )


_WfAtmVclOperStatus_Type.__name__ = "Integer32"
_WfAtmVclOperStatus_Object = MibTableColumn
wfAtmVclOperStatus = _WfAtmVclOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 6),
    _WfAtmVclOperStatus_Type()
)
wfAtmVclOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclOperStatus.setStatus("mandatory")
_WfAtmVclLastChange_Type = TimeTicks
_WfAtmVclLastChange_Object = MibTableColumn
wfAtmVclLastChange = _WfAtmVclLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 7),
    _WfAtmVclLastChange_Type()
)
wfAtmVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclLastChange.setStatus("mandatory")


class _WfAtmVclXmtPeakCellRate_Type(Integer32):
    """Custom type wfAtmVclXmtPeakCellRate based on Integer32"""
    defaultValue = 4716

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365566),
    )


_WfAtmVclXmtPeakCellRate_Type.__name__ = "Integer32"
_WfAtmVclXmtPeakCellRate_Object = MibTableColumn
wfAtmVclXmtPeakCellRate = _WfAtmVclXmtPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 8),
    _WfAtmVclXmtPeakCellRate_Type()
)
wfAtmVclXmtPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtPeakCellRate.setStatus("mandatory")


class _WfAtmVclXmtSustainableCellRate_Type(Integer32):
    """Custom type wfAtmVclXmtSustainableCellRate based on Integer32"""
    defaultValue = 4716

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365566),
    )


_WfAtmVclXmtSustainableCellRate_Type.__name__ = "Integer32"
_WfAtmVclXmtSustainableCellRate_Object = MibTableColumn
wfAtmVclXmtSustainableCellRate = _WfAtmVclXmtSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 9),
    _WfAtmVclXmtSustainableCellRate_Type()
)
wfAtmVclXmtSustainableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtSustainableCellRate.setStatus("mandatory")


class _WfAtmVclXmtBurstSize_Type(Integer32):
    """Custom type wfAtmVclXmtBurstSize based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmVclXmtBurstSize_Type.__name__ = "Integer32"
_WfAtmVclXmtBurstSize_Object = MibTableColumn
wfAtmVclXmtBurstSize = _WfAtmVclXmtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 10),
    _WfAtmVclXmtBurstSize_Type()
)
wfAtmVclXmtBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtBurstSize.setStatus("mandatory")


class _WfAtmVclXmtQosClass_Type(Integer32):
    """Custom type wfAtmVclXmtQosClass based on Integer32"""
    defaultValue = 4

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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_WfAtmVclXmtQosClass_Type.__name__ = "Integer32"
_WfAtmVclXmtQosClass_Object = MibTableColumn
wfAtmVclXmtQosClass = _WfAtmVclXmtQosClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 11),
    _WfAtmVclXmtQosClass_Type()
)
wfAtmVclXmtQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtQosClass.setStatus("mandatory")


class _WfAtmVclRcvPeakCellRate_Type(Integer32):
    """Custom type wfAtmVclRcvPeakCellRate based on Integer32"""
    defaultValue = 4716

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365566),
    )


_WfAtmVclRcvPeakCellRate_Type.__name__ = "Integer32"
_WfAtmVclRcvPeakCellRate_Object = MibTableColumn
wfAtmVclRcvPeakCellRate = _WfAtmVclRcvPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 12),
    _WfAtmVclRcvPeakCellRate_Type()
)
wfAtmVclRcvPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclRcvPeakCellRate.setStatus("mandatory")


class _WfAtmVclRcvSustainableCellRate_Type(Integer32):
    """Custom type wfAtmVclRcvSustainableCellRate based on Integer32"""
    defaultValue = 4716

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365566),
    )


_WfAtmVclRcvSustainableCellRate_Type.__name__ = "Integer32"
_WfAtmVclRcvSustainableCellRate_Object = MibTableColumn
wfAtmVclRcvSustainableCellRate = _WfAtmVclRcvSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 13),
    _WfAtmVclRcvSustainableCellRate_Type()
)
wfAtmVclRcvSustainableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclRcvSustainableCellRate.setStatus("mandatory")


class _WfAtmVclRcvBurstSize_Type(Integer32):
    """Custom type wfAtmVclRcvBurstSize based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmVclRcvBurstSize_Type.__name__ = "Integer32"
_WfAtmVclRcvBurstSize_Object = MibTableColumn
wfAtmVclRcvBurstSize = _WfAtmVclRcvBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 14),
    _WfAtmVclRcvBurstSize_Type()
)
wfAtmVclRcvBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclRcvBurstSize.setStatus("mandatory")


class _WfAtmVclRcvQosClass_Type(Integer32):
    """Custom type wfAtmVclRcvQosClass based on Integer32"""
    defaultValue = 4

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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_WfAtmVclRcvQosClass_Type.__name__ = "Integer32"
_WfAtmVclRcvQosClass_Object = MibTableColumn
wfAtmVclRcvQosClass = _WfAtmVclRcvQosClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 15),
    _WfAtmVclRcvQosClass_Type()
)
wfAtmVclRcvQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclRcvQosClass.setStatus("mandatory")


class _WfAtmVclAalType_Type(Integer32):
    """Custom type wfAtmVclAalType based on Integer32"""
    defaultValue = 3

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
        *(("other", 4),
          ("type1", 1),
          ("type34", 2),
          ("type5", 3),
          ("unknown", 5))
    )


_WfAtmVclAalType_Type.__name__ = "Integer32"
_WfAtmVclAalType_Object = MibTableColumn
wfAtmVclAalType = _WfAtmVclAalType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 16),
    _WfAtmVclAalType_Type()
)
wfAtmVclAalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclAalType.setStatus("mandatory")


class _WfAtmVclAalCpcsTransmitSduSize_Type(Integer32):
    """Custom type wfAtmVclAalCpcsTransmitSduSize based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmVclAalCpcsTransmitSduSize_Type.__name__ = "Integer32"
_WfAtmVclAalCpcsTransmitSduSize_Object = MibTableColumn
wfAtmVclAalCpcsTransmitSduSize = _WfAtmVclAalCpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 17),
    _WfAtmVclAalCpcsTransmitSduSize_Type()
)
wfAtmVclAalCpcsTransmitSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclAalCpcsTransmitSduSize.setStatus("mandatory")


class _WfAtmVclAalCpcsReceiveSduSize_Type(Integer32):
    """Custom type wfAtmVclAalCpcsReceiveSduSize based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmVclAalCpcsReceiveSduSize_Type.__name__ = "Integer32"
_WfAtmVclAalCpcsReceiveSduSize_Object = MibTableColumn
wfAtmVclAalCpcsReceiveSduSize = _WfAtmVclAalCpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 18),
    _WfAtmVclAalCpcsReceiveSduSize_Type()
)
wfAtmVclAalCpcsReceiveSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclAalCpcsReceiveSduSize.setStatus("mandatory")


class _WfAtmVclAalEncapsType_Type(Integer32):
    """Custom type wfAtmVclAalEncapsType based on Integer32"""
    defaultValue = 7

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bridged8023", 2),
          ("bridged8025", 3),
          ("bridged8026", 4),
          ("frsscs", 8),
          ("lane8023", 5),
          ("lane8025", 6),
          ("llcencaps", 7),
          ("other", 9),
          ("routedproto", 1),
          ("unknown", 10))
    )


_WfAtmVclAalEncapsType_Type.__name__ = "Integer32"
_WfAtmVclAalEncapsType_Object = MibTableColumn
wfAtmVclAalEncapsType = _WfAtmVclAalEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 19),
    _WfAtmVclAalEncapsType_Type()
)
wfAtmVclAalEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclAalEncapsType.setStatus("mandatory")


class _WfAtmVclCongestionIndication_Type(Integer32):
    """Custom type wfAtmVclCongestionIndication based on Integer32"""
    defaultValue = 1

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


_WfAtmVclCongestionIndication_Type.__name__ = "Integer32"
_WfAtmVclCongestionIndication_Object = MibTableColumn
wfAtmVclCongestionIndication = _WfAtmVclCongestionIndication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 20),
    _WfAtmVclCongestionIndication_Type()
)
wfAtmVclCongestionIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclCongestionIndication.setStatus("mandatory")


class _WfAtmVclCellLossPriority_Type(Integer32):
    """Custom type wfAtmVclCellLossPriority based on Integer32"""
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
        *(("drop-preference", 3),
          ("off", 1),
          ("on", 2))
    )


_WfAtmVclCellLossPriority_Type.__name__ = "Integer32"
_WfAtmVclCellLossPriority_Object = MibTableColumn
wfAtmVclCellLossPriority = _WfAtmVclCellLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 21),
    _WfAtmVclCellLossPriority_Type()
)
wfAtmVclCellLossPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclCellLossPriority.setStatus("mandatory")
_WfAtmVclCct_Type = Integer32
_WfAtmVclCct_Object = MibTableColumn
wfAtmVclCct = _WfAtmVclCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 22),
    _WfAtmVclCct_Type()
)
wfAtmVclCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclCct.setStatus("mandatory")
_WfAtmVclDirectAccessCct_Type = Integer32
_WfAtmVclDirectAccessCct_Object = MibTableColumn
wfAtmVclDirectAccessCct = _WfAtmVclDirectAccessCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 23),
    _WfAtmVclDirectAccessCct_Type()
)
wfAtmVclDirectAccessCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclDirectAccessCct.setStatus("mandatory")


class _WfAtmVclMulticast_Type(Integer32):
    """Custom type wfAtmVclMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_WfAtmVclMulticast_Type.__name__ = "Integer32"
_WfAtmVclMulticast_Object = MibTableColumn
wfAtmVclMulticast = _WfAtmVclMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 24),
    _WfAtmVclMulticast_Type()
)
wfAtmVclMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclMulticast.setStatus("mandatory")


class _WfAtmVclMode_Type(Integer32):
    """Custom type wfAtmVclMode based on Integer32"""
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
        *(("direct", 3),
          ("groupaccess", 1),
          ("hybridaccess", 2))
    )


_WfAtmVclMode_Type.__name__ = "Integer32"
_WfAtmVclMode_Object = MibTableColumn
wfAtmVclMode = _WfAtmVclMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 25),
    _WfAtmVclMode_Type()
)
wfAtmVclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclMode.setStatus("mandatory")
_WfAtmVclDrops_Type = Counter32
_WfAtmVclDrops_Object = MibTableColumn
wfAtmVclDrops = _WfAtmVclDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 26),
    _WfAtmVclDrops_Type()
)
wfAtmVclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclDrops.setStatus("mandatory")
_WfAtmVclVcIndex_Type = Integer32
_WfAtmVclVcIndex_Object = MibTableColumn
wfAtmVclVcIndex = _WfAtmVclVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 27),
    _WfAtmVclVcIndex_Type()
)
wfAtmVclVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclVcIndex.setStatus("mandatory")


class _WfAtmVclVcType_Type(Integer32):
    """Custom type wfAtmVclVcType based on Integer32"""
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
        *(("control", 3),
          ("permanent", 1),
          ("switched", 2),
          ("switchedMux", 4))
    )


_WfAtmVclVcType_Type.__name__ = "Integer32"
_WfAtmVclVcType_Object = MibTableColumn
wfAtmVclVcType = _WfAtmVclVcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 28),
    _WfAtmVclVcType_Type()
)
wfAtmVclVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclVcType.setStatus("mandatory")


class _WfAtmVclXmtTagging_Type(Integer32):
    """Custom type wfAtmVclXmtTagging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfAtmVclXmtTagging_Type.__name__ = "Integer32"
_WfAtmVclXmtTagging_Object = MibTableColumn
wfAtmVclXmtTagging = _WfAtmVclXmtTagging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 29),
    _WfAtmVclXmtTagging_Type()
)
wfAtmVclXmtTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtTagging.setStatus("mandatory")


class _WfAtmVclRcvTagging_Type(Integer32):
    """Custom type wfAtmVclRcvTagging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfAtmVclRcvTagging_Type.__name__ = "Integer32"
_WfAtmVclRcvTagging_Object = MibTableColumn
wfAtmVclRcvTagging = _WfAtmVclRcvTagging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 30),
    _WfAtmVclRcvTagging_Type()
)
wfAtmVclRcvTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclRcvTagging.setStatus("mandatory")


class _WfAtmVclOamLpbkEnable_Type(Integer32):
    """Custom type wfAtmVclOamLpbkEnable based on Integer32"""
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


_WfAtmVclOamLpbkEnable_Type.__name__ = "Integer32"
_WfAtmVclOamLpbkEnable_Object = MibTableColumn
wfAtmVclOamLpbkEnable = _WfAtmVclOamLpbkEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 31),
    _WfAtmVclOamLpbkEnable_Type()
)
wfAtmVclOamLpbkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclOamLpbkEnable.setStatus("mandatory")


class _WfAtmVclOamLpbkCellInterval_Type(Integer32):
    """Custom type wfAtmVclOamLpbkCellInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmVclOamLpbkCellInterval_Type.__name__ = "Integer32"
_WfAtmVclOamLpbkCellInterval_Object = MibTableColumn
wfAtmVclOamLpbkCellInterval = _WfAtmVclOamLpbkCellInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 32),
    _WfAtmVclOamLpbkCellInterval_Type()
)
wfAtmVclOamLpbkCellInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclOamLpbkCellInterval.setStatus("mandatory")


class _WfAtmVclOamLpbkThreshold1_Type(Integer32):
    """Custom type wfAtmVclOamLpbkThreshold1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmVclOamLpbkThreshold1_Type.__name__ = "Integer32"
_WfAtmVclOamLpbkThreshold1_Object = MibTableColumn
wfAtmVclOamLpbkThreshold1 = _WfAtmVclOamLpbkThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 33),
    _WfAtmVclOamLpbkThreshold1_Type()
)
wfAtmVclOamLpbkThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclOamLpbkThreshold1.setStatus("mandatory")


class _WfAtmVclOamLpbkThreshold2_Type(Integer32):
    """Custom type wfAtmVclOamLpbkThreshold2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmVclOamLpbkThreshold2_Type.__name__ = "Integer32"
_WfAtmVclOamLpbkThreshold2_Object = MibTableColumn
wfAtmVclOamLpbkThreshold2 = _WfAtmVclOamLpbkThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 34),
    _WfAtmVclOamLpbkThreshold2_Type()
)
wfAtmVclOamLpbkThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclOamLpbkThreshold2.setStatus("mandatory")


class _WfAtmVclOamAlarmEnable_Type(Integer32):
    """Custom type wfAtmVclOamAlarmEnable based on Integer32"""
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


_WfAtmVclOamAlarmEnable_Type.__name__ = "Integer32"
_WfAtmVclOamAlarmEnable_Object = MibTableColumn
wfAtmVclOamAlarmEnable = _WfAtmVclOamAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 35),
    _WfAtmVclOamAlarmEnable_Type()
)
wfAtmVclOamAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclOamAlarmEnable.setStatus("mandatory")
_WfAtmVclVcGroup_Type = Integer32
_WfAtmVclVcGroup_Object = MibTableColumn
wfAtmVclVcGroup = _WfAtmVclVcGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 36),
    _WfAtmVclVcGroup_Type()
)
wfAtmVclVcGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclVcGroup.setStatus("mandatory")


class _WfAtmVclServiceClass_Type(Integer32):
    """Custom type wfAtmVclServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WfAtmVclServiceClass_Type.__name__ = "Integer32"
_WfAtmVclServiceClass_Object = MibTableColumn
wfAtmVclServiceClass = _WfAtmVclServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 37),
    _WfAtmVclServiceClass_Type()
)
wfAtmVclServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclServiceClass.setStatus("mandatory")


class _WfAtmVclServiceCategory_Type(Integer32):
    """Custom type wfAtmVclServiceCategory based on Integer32"""
    defaultValue = 1

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
        *(("abr", 5),
          ("cbr", 2),
          ("other", 1),
          ("ubr", 6),
          ("ubrplus", 7),
          ("vbrNRt", 4),
          ("vbrRt", 3))
    )


_WfAtmVclServiceCategory_Type.__name__ = "Integer32"
_WfAtmVclServiceCategory_Object = MibTableColumn
wfAtmVclServiceCategory = _WfAtmVclServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 38),
    _WfAtmVclServiceCategory_Type()
)
wfAtmVclServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclServiceCategory.setStatus("mandatory")


class _WfAtmVclVBRType_Type(Integer32):
    """Custom type wfAtmVclVBRType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_WfAtmVclVBRType_Type.__name__ = "Integer32"
_WfAtmVclVBRType_Object = MibTableColumn
wfAtmVclVBRType = _WfAtmVclVBRType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 39),
    _WfAtmVclVBRType_Type()
)
wfAtmVclVBRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclVBRType.setStatus("mandatory")


class _WfAtmVclXmtMinimumCellRate_Type(Integer32):
    """Custom type wfAtmVclXmtMinimumCellRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365566),
    )


_WfAtmVclXmtMinimumCellRate_Type.__name__ = "Integer32"
_WfAtmVclXmtMinimumCellRate_Object = MibTableColumn
wfAtmVclXmtMinimumCellRate = _WfAtmVclXmtMinimumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 40),
    _WfAtmVclXmtMinimumCellRate_Type()
)
wfAtmVclXmtMinimumCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtMinimumCellRate.setStatus("mandatory")


class _WfAtmVclXmtInitialCellRate_Type(Integer32):
    """Custom type wfAtmVclXmtInitialCellRate based on Integer32"""
    defaultValue = 4716

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365566),
    )


_WfAtmVclXmtInitialCellRate_Type.__name__ = "Integer32"
_WfAtmVclXmtInitialCellRate_Object = MibTableColumn
wfAtmVclXmtInitialCellRate = _WfAtmVclXmtInitialCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 41),
    _WfAtmVclXmtInitialCellRate_Type()
)
wfAtmVclXmtInitialCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtInitialCellRate.setStatus("mandatory")


class _WfAtmVclXmtRateIncreaseFactor_Type(Integer32):
    """Custom type wfAtmVclXmtRateIncreaseFactor based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfAtmVclXmtRateIncreaseFactor_Type.__name__ = "Integer32"
_WfAtmVclXmtRateIncreaseFactor_Object = MibTableColumn
wfAtmVclXmtRateIncreaseFactor = _WfAtmVclXmtRateIncreaseFactor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 42),
    _WfAtmVclXmtRateIncreaseFactor_Type()
)
wfAtmVclXmtRateIncreaseFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtRateIncreaseFactor.setStatus("mandatory")


class _WfAtmVclXmtRateDecreaseFactor_Type(Integer32):
    """Custom type wfAtmVclXmtRateDecreaseFactor based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfAtmVclXmtRateDecreaseFactor_Type.__name__ = "Integer32"
_WfAtmVclXmtRateDecreaseFactor_Object = MibTableColumn
wfAtmVclXmtRateDecreaseFactor = _WfAtmVclXmtRateDecreaseFactor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 5, 1, 43),
    _WfAtmVclXmtRateDecreaseFactor_Type()
)
wfAtmVclXmtRateDecreaseFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVclXmtRateDecreaseFactor.setStatus("mandatory")
_WfAtmVclStatsTable_Object = MibTable
wfAtmVclStatsTable = _WfAtmVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6)
)
if mibBuilder.loadTexts:
    wfAtmVclStatsTable.setStatus("mandatory")
_WfAtmVclStatsEntry_Object = MibTableRow
wfAtmVclStatsEntry = _WfAtmVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1)
)
wfAtmVclStatsEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVclStatsIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVclStatsVpi"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVclStatsVci"),
)
if mibBuilder.loadTexts:
    wfAtmVclStatsEntry.setStatus("mandatory")
_WfAtmVclStatsIndex_Type = Integer32
_WfAtmVclStatsIndex_Object = MibTableColumn
wfAtmVclStatsIndex = _WfAtmVclStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 1),
    _WfAtmVclStatsIndex_Type()
)
wfAtmVclStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclStatsIndex.setStatus("mandatory")
_WfAtmVclStatsVpi_Type = Integer32
_WfAtmVclStatsVpi_Object = MibTableColumn
wfAtmVclStatsVpi = _WfAtmVclStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 2),
    _WfAtmVclStatsVpi_Type()
)
wfAtmVclStatsVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclStatsVpi.setStatus("mandatory")
_WfAtmVclStatsVci_Type = Integer32
_WfAtmVclStatsVci_Object = MibTableColumn
wfAtmVclStatsVci = _WfAtmVclStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 3),
    _WfAtmVclStatsVci_Type()
)
wfAtmVclStatsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclStatsVci.setStatus("mandatory")
_WfAtmVclStatsVcIndex_Type = Integer32
_WfAtmVclStatsVcIndex_Object = MibTableColumn
wfAtmVclStatsVcIndex = _WfAtmVclStatsVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 4),
    _WfAtmVclStatsVcIndex_Type()
)
wfAtmVclStatsVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclStatsVcIndex.setStatus("mandatory")
_WfAtmVclXmtCells_Type = OctetString
_WfAtmVclXmtCells_Object = MibTableColumn
wfAtmVclXmtCells = _WfAtmVclXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 5),
    _WfAtmVclXmtCells_Type()
)
wfAtmVclXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclXmtCells.setStatus("mandatory")
_WfAtmVclRcvCells_Type = OctetString
_WfAtmVclRcvCells_Object = MibTableColumn
wfAtmVclRcvCells = _WfAtmVclRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 6),
    _WfAtmVclRcvCells_Type()
)
wfAtmVclRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvCells.setStatus("mandatory")
_WfAtmVclRcvSequenceNumErrs_Type = Counter32
_WfAtmVclRcvSequenceNumErrs_Object = MibTableColumn
wfAtmVclRcvSequenceNumErrs = _WfAtmVclRcvSequenceNumErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 7),
    _WfAtmVclRcvSequenceNumErrs_Type()
)
wfAtmVclRcvSequenceNumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvSequenceNumErrs.setStatus("mandatory")
_WfAtmVclRcvInvalidLenErrs_Type = Counter32
_WfAtmVclRcvInvalidLenErrs_Object = MibTableColumn
wfAtmVclRcvInvalidLenErrs = _WfAtmVclRcvInvalidLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 8),
    _WfAtmVclRcvInvalidLenErrs_Type()
)
wfAtmVclRcvInvalidLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvInvalidLenErrs.setStatus("mandatory")
_WfAtmVclRcvMissingEomErrs_Type = Counter32
_WfAtmVclRcvMissingEomErrs_Object = MibTableColumn
wfAtmVclRcvMissingEomErrs = _WfAtmVclRcvMissingEomErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 9),
    _WfAtmVclRcvMissingEomErrs_Type()
)
wfAtmVclRcvMissingEomErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvMissingEomErrs.setStatus("mandatory")
_WfAtmVclRcvBufferOflowErrs_Type = Counter32
_WfAtmVclRcvBufferOflowErrs_Object = MibTableColumn
wfAtmVclRcvBufferOflowErrs = _WfAtmVclRcvBufferOflowErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 10),
    _WfAtmVclRcvBufferOflowErrs_Type()
)
wfAtmVclRcvBufferOflowErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvBufferOflowErrs.setStatus("mandatory")
_WfAtmVclRcvMaxLenExceedErrs_Type = Counter32
_WfAtmVclRcvMaxLenExceedErrs_Object = MibTableColumn
wfAtmVclRcvMaxLenExceedErrs = _WfAtmVclRcvMaxLenExceedErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 11),
    _WfAtmVclRcvMaxLenExceedErrs_Type()
)
wfAtmVclRcvMaxLenExceedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvMaxLenExceedErrs.setStatus("mandatory")
_WfAtmVclRcvTrailerErrs_Type = Counter32
_WfAtmVclRcvTrailerErrs_Object = MibTableColumn
wfAtmVclRcvTrailerErrs = _WfAtmVclRcvTrailerErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 12),
    _WfAtmVclRcvTrailerErrs_Type()
)
wfAtmVclRcvTrailerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvTrailerErrs.setStatus("mandatory")
_WfAtmVclRcvAbortErrs_Type = Counter32
_WfAtmVclRcvAbortErrs_Object = MibTableColumn
wfAtmVclRcvAbortErrs = _WfAtmVclRcvAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 13),
    _WfAtmVclRcvAbortErrs_Type()
)
wfAtmVclRcvAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvAbortErrs.setStatus("mandatory")
_WfAtmVclRcvPacketLengthErrs_Type = Counter32
_WfAtmVclRcvPacketLengthErrs_Object = MibTableColumn
wfAtmVclRcvPacketLengthErrs = _WfAtmVclRcvPacketLengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 14),
    _WfAtmVclRcvPacketLengthErrs_Type()
)
wfAtmVclRcvPacketLengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvPacketLengthErrs.setStatus("mandatory")
_WfAtmVclRcvReassemAbortErrs_Type = Counter32
_WfAtmVclRcvReassemAbortErrs_Object = MibTableColumn
wfAtmVclRcvReassemAbortErrs = _WfAtmVclRcvReassemAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 15),
    _WfAtmVclRcvReassemAbortErrs_Type()
)
wfAtmVclRcvReassemAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvReassemAbortErrs.setStatus("mandatory")
_WfAtmVclRcvCrcErrs_Type = Counter32
_WfAtmVclRcvCrcErrs_Object = MibTableColumn
wfAtmVclRcvCrcErrs = _WfAtmVclRcvCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 16),
    _WfAtmVclRcvCrcErrs_Type()
)
wfAtmVclRcvCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvCrcErrs.setStatus("mandatory")
_WfAtmVclXmtOamCells_Type = Counter32
_WfAtmVclXmtOamCells_Object = MibTableColumn
wfAtmVclXmtOamCells = _WfAtmVclXmtOamCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 17),
    _WfAtmVclXmtOamCells_Type()
)
wfAtmVclXmtOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclXmtOamCells.setStatus("mandatory")
_WfAtmVclRcvOamCells_Type = Counter32
_WfAtmVclRcvOamCells_Object = MibTableColumn
wfAtmVclRcvOamCells = _WfAtmVclRcvOamCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 18),
    _WfAtmVclRcvOamCells_Type()
)
wfAtmVclRcvOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvOamCells.setStatus("mandatory")
_WfAtmVclRcvOamCrcErrs_Type = Counter32
_WfAtmVclRcvOamCrcErrs_Object = MibTableColumn
wfAtmVclRcvOamCrcErrs = _WfAtmVclRcvOamCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 6, 1, 19),
    _WfAtmVclRcvOamCrcErrs_Type()
)
wfAtmVclRcvOamCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVclRcvOamCrcErrs.setStatus("mandatory")
_WfAtmSigTable_Object = MibTable
wfAtmSigTable = _WfAtmSigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7)
)
if mibBuilder.loadTexts:
    wfAtmSigTable.setStatus("mandatory")
_WfAtmSigEntry_Object = MibTableRow
wfAtmSigEntry = _WfAtmSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1)
)
wfAtmSigEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmSigLineNumber"),
)
if mibBuilder.loadTexts:
    wfAtmSigEntry.setStatus("mandatory")


class _WfAtmSigDelete_Type(Integer32):
    """Custom type wfAtmSigDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmSigDelete_Type.__name__ = "Integer32"
_WfAtmSigDelete_Object = MibTableColumn
wfAtmSigDelete = _WfAtmSigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 1),
    _WfAtmSigDelete_Type()
)
wfAtmSigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigDelete.setStatus("mandatory")


class _WfAtmSigDisable_Type(Integer32):
    """Custom type wfAtmSigDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmSigDisable_Type.__name__ = "Integer32"
_WfAtmSigDisable_Object = MibTableColumn
wfAtmSigDisable = _WfAtmSigDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 2),
    _WfAtmSigDisable_Type()
)
wfAtmSigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigDisable.setStatus("mandatory")
_WfAtmSigLineNumber_Type = Integer32
_WfAtmSigLineNumber_Object = MibTableColumn
wfAtmSigLineNumber = _WfAtmSigLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 3),
    _WfAtmSigLineNumber_Type()
)
wfAtmSigLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSigLineNumber.setStatus("mandatory")
_WfAtmSigAtmCct_Type = Integer32
_WfAtmSigAtmCct_Object = MibTableColumn
wfAtmSigAtmCct = _WfAtmSigAtmCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 4),
    _WfAtmSigAtmCct_Type()
)
wfAtmSigAtmCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSigAtmCct.setStatus("mandatory")


class _WfAtmSigState_Type(Integer32):
    """Custom type wfAtmSigState based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmSigState_Type.__name__ = "Integer32"
_WfAtmSigState_Object = MibTableColumn
wfAtmSigState = _WfAtmSigState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 5),
    _WfAtmSigState_Type()
)
wfAtmSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSigState.setStatus("mandatory")


class _WfAtmSigMaxServiceUsers_Type(Integer32):
    """Custom type wfAtmSigMaxServiceUsers based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_WfAtmSigMaxServiceUsers_Type.__name__ = "Integer32"
_WfAtmSigMaxServiceUsers_Object = MibTableColumn
wfAtmSigMaxServiceUsers = _WfAtmSigMaxServiceUsers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 6),
    _WfAtmSigMaxServiceUsers_Type()
)
wfAtmSigMaxServiceUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxServiceUsers.setStatus("mandatory")


class _WfAtmSigMaxPtPtConnections_Type(Integer32):
    """Custom type wfAtmSigMaxPtPtConnections based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_WfAtmSigMaxPtPtConnections_Type.__name__ = "Integer32"
_WfAtmSigMaxPtPtConnections_Object = MibTableColumn
wfAtmSigMaxPtPtConnections = _WfAtmSigMaxPtPtConnections_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 7),
    _WfAtmSigMaxPtPtConnections_Type()
)
wfAtmSigMaxPtPtConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxPtPtConnections.setStatus("mandatory")


class _WfAtmSigMaxPtMultConnections_Type(Integer32):
    """Custom type wfAtmSigMaxPtMultConnections based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_WfAtmSigMaxPtMultConnections_Type.__name__ = "Integer32"
_WfAtmSigMaxPtMultConnections_Object = MibTableColumn
wfAtmSigMaxPtMultConnections = _WfAtmSigMaxPtMultConnections_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 8),
    _WfAtmSigMaxPtMultConnections_Type()
)
wfAtmSigMaxPtMultConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxPtMultConnections.setStatus("mandatory")


class _WfAtmSigMaxPartiesInMultConnect_Type(Integer32):
    """Custom type wfAtmSigMaxPartiesInMultConnect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_WfAtmSigMaxPartiesInMultConnect_Type.__name__ = "Integer32"
_WfAtmSigMaxPartiesInMultConnect_Object = MibTableColumn
wfAtmSigMaxPartiesInMultConnect = _WfAtmSigMaxPartiesInMultConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 9),
    _WfAtmSigMaxPartiesInMultConnect_Type()
)
wfAtmSigMaxPartiesInMultConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxPartiesInMultConnect.setStatus("mandatory")


class _WfAtmSigMaxRoutingRegistrations_Type(Integer32):
    """Custom type wfAtmSigMaxRoutingRegistrations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_WfAtmSigMaxRoutingRegistrations_Type.__name__ = "Integer32"
_WfAtmSigMaxRoutingRegistrations_Object = MibTableColumn
wfAtmSigMaxRoutingRegistrations = _WfAtmSigMaxRoutingRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 10),
    _WfAtmSigMaxRoutingRegistrations_Type()
)
wfAtmSigMaxRoutingRegistrations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxRoutingRegistrations.setStatus("mandatory")


class _WfAtmSigMinBufferThreshold_Type(Integer32):
    """Custom type wfAtmSigMinBufferThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfAtmSigMinBufferThreshold_Type.__name__ = "Integer32"
_WfAtmSigMinBufferThreshold_Object = MibTableColumn
wfAtmSigMinBufferThreshold = _WfAtmSigMinBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 11),
    _WfAtmSigMinBufferThreshold_Type()
)
wfAtmSigMinBufferThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMinBufferThreshold.setStatus("mandatory")


class _WfAtmSigTimerResolution_Type(Integer32):
    """Custom type wfAtmSigTimerResolution based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255000),
    )


_WfAtmSigTimerResolution_Type.__name__ = "Integer32"
_WfAtmSigTimerResolution_Object = MibTableColumn
wfAtmSigTimerResolution = _WfAtmSigTimerResolution_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 12),
    _WfAtmSigTimerResolution_Type()
)
wfAtmSigTimerResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigTimerResolution.setStatus("mandatory")


class _WfAtmSigVpi_Type(Integer32):
    """Custom type wfAtmSigVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmSigVpi_Type.__name__ = "Integer32"
_WfAtmSigVpi_Object = MibTableColumn
wfAtmSigVpi = _WfAtmSigVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 13),
    _WfAtmSigVpi_Type()
)
wfAtmSigVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigVpi.setStatus("mandatory")


class _WfAtmSigVci_Type(Integer32):
    """Custom type wfAtmSigVci based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmSigVci_Type.__name__ = "Integer32"
_WfAtmSigVci_Object = MibTableColumn
wfAtmSigVci = _WfAtmSigVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 14),
    _WfAtmSigVci_Type()
)
wfAtmSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigVci.setStatus("mandatory")


class _WfAtmSigStandard_Type(Integer32):
    """Custom type wfAtmSigStandard based on Integer32"""
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
        *(("sym", 4),
          ("v30", 1),
          ("v31", 2),
          ("v40", 3))
    )


_WfAtmSigStandard_Type.__name__ = "Integer32"
_WfAtmSigStandard_Object = MibTableColumn
wfAtmSigStandard = _WfAtmSigStandard_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 15),
    _WfAtmSigStandard_Type()
)
wfAtmSigStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigStandard.setStatus("mandatory")


class _WfAtmSigInterfaceType_Type(Integer32):
    """Custom type wfAtmSigInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_WfAtmSigInterfaceType_Type.__name__ = "Integer32"
_WfAtmSigInterfaceType_Object = MibTableColumn
wfAtmSigInterfaceType = _WfAtmSigInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 16),
    _WfAtmSigInterfaceType_Type()
)
wfAtmSigInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigInterfaceType.setStatus("mandatory")


class _WfAtmSigMinVciPtPt_Type(Integer32):
    """Custom type wfAtmSigMinVciPtPt based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfAtmSigMinVciPtPt_Type.__name__ = "Integer32"
_WfAtmSigMinVciPtPt_Object = MibTableColumn
wfAtmSigMinVciPtPt = _WfAtmSigMinVciPtPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 17),
    _WfAtmSigMinVciPtPt_Type()
)
wfAtmSigMinVciPtPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMinVciPtPt.setStatus("mandatory")


class _WfAtmSigMaxVciPtPt_Type(Integer32):
    """Custom type wfAtmSigMaxVciPtPt based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfAtmSigMaxVciPtPt_Type.__name__ = "Integer32"
_WfAtmSigMaxVciPtPt_Object = MibTableColumn
wfAtmSigMaxVciPtPt = _WfAtmSigMaxVciPtPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 18),
    _WfAtmSigMaxVciPtPt_Type()
)
wfAtmSigMaxVciPtPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxVciPtPt.setStatus("mandatory")


class _WfAtmSigMinVpiPtPt_Type(Integer32):
    """Custom type wfAtmSigMinVpiPtPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmSigMinVpiPtPt_Type.__name__ = "Integer32"
_WfAtmSigMinVpiPtPt_Object = MibTableColumn
wfAtmSigMinVpiPtPt = _WfAtmSigMinVpiPtPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 19),
    _WfAtmSigMinVpiPtPt_Type()
)
wfAtmSigMinVpiPtPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMinVpiPtPt.setStatus("mandatory")


class _WfAtmSigMaxVpiPtPt_Type(Integer32):
    """Custom type wfAtmSigMaxVpiPtPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmSigMaxVpiPtPt_Type.__name__ = "Integer32"
_WfAtmSigMaxVpiPtPt_Object = MibTableColumn
wfAtmSigMaxVpiPtPt = _WfAtmSigMaxVpiPtPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 20),
    _WfAtmSigMaxVpiPtPt_Type()
)
wfAtmSigMaxVpiPtPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxVpiPtPt.setStatus("mandatory")


class _WfAtmSigMinVciPtMltPt_Type(Integer32):
    """Custom type wfAtmSigMinVciPtMltPt based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfAtmSigMinVciPtMltPt_Type.__name__ = "Integer32"
_WfAtmSigMinVciPtMltPt_Object = MibTableColumn
wfAtmSigMinVciPtMltPt = _WfAtmSigMinVciPtMltPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 21),
    _WfAtmSigMinVciPtMltPt_Type()
)
wfAtmSigMinVciPtMltPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMinVciPtMltPt.setStatus("mandatory")


class _WfAtmSigMaxVciPtMltPt_Type(Integer32):
    """Custom type wfAtmSigMaxVciPtMltPt based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfAtmSigMaxVciPtMltPt_Type.__name__ = "Integer32"
_WfAtmSigMaxVciPtMltPt_Object = MibTableColumn
wfAtmSigMaxVciPtMltPt = _WfAtmSigMaxVciPtMltPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 22),
    _WfAtmSigMaxVciPtMltPt_Type()
)
wfAtmSigMaxVciPtMltPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxVciPtMltPt.setStatus("mandatory")


class _WfAtmSigMinVpiPtMltPt_Type(Integer32):
    """Custom type wfAtmSigMinVpiPtMltPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmSigMinVpiPtMltPt_Type.__name__ = "Integer32"
_WfAtmSigMinVpiPtMltPt_Object = MibTableColumn
wfAtmSigMinVpiPtMltPt = _WfAtmSigMinVpiPtMltPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 23),
    _WfAtmSigMinVpiPtMltPt_Type()
)
wfAtmSigMinVpiPtMltPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMinVpiPtMltPt.setStatus("mandatory")


class _WfAtmSigMaxVpiPtMltPt_Type(Integer32):
    """Custom type wfAtmSigMaxVpiPtMltPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmSigMaxVpiPtMltPt_Type.__name__ = "Integer32"
_WfAtmSigMaxVpiPtMltPt_Object = MibTableColumn
wfAtmSigMaxVpiPtMltPt = _WfAtmSigMaxVpiPtMltPt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 24),
    _WfAtmSigMaxVpiPtMltPt_Type()
)
wfAtmSigMaxVpiPtMltPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigMaxVpiPtMltPt.setStatus("mandatory")


class _WfAtmSigT303_Type(Integer32):
    """Custom type wfAtmSigT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfAtmSigT303_Type.__name__ = "Integer32"
_WfAtmSigT303_Object = MibTableColumn
wfAtmSigT303 = _WfAtmSigT303_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 25),
    _WfAtmSigT303_Type()
)
wfAtmSigT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT303.setStatus("mandatory")


class _WfAtmSigT308_Type(Integer32):
    """Custom type wfAtmSigT308 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_WfAtmSigT308_Type.__name__ = "Integer32"
_WfAtmSigT308_Object = MibTableColumn
wfAtmSigT308 = _WfAtmSigT308_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 26),
    _WfAtmSigT308_Type()
)
wfAtmSigT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT308.setStatus("mandatory")


class _WfAtmSigT309_Type(Integer32):
    """Custom type wfAtmSigT309 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 540),
    )


_WfAtmSigT309_Type.__name__ = "Integer32"
_WfAtmSigT309_Object = MibTableColumn
wfAtmSigT309 = _WfAtmSigT309_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 27),
    _WfAtmSigT309_Type()
)
wfAtmSigT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT309.setStatus("mandatory")


class _WfAtmSigT310_Type(Integer32):
    """Custom type wfAtmSigT310 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfAtmSigT310_Type.__name__ = "Integer32"
_WfAtmSigT310_Object = MibTableColumn
wfAtmSigT310 = _WfAtmSigT310_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 28),
    _WfAtmSigT310_Type()
)
wfAtmSigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT310.setStatus("mandatory")


class _WfAtmSigT313_Type(Integer32):
    """Custom type wfAtmSigT313 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfAtmSigT313_Type.__name__ = "Integer32"
_WfAtmSigT313_Object = MibTableColumn
wfAtmSigT313 = _WfAtmSigT313_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 29),
    _WfAtmSigT313_Type()
)
wfAtmSigT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT313.setStatus("mandatory")


class _WfAtmSigT316_Type(Integer32):
    """Custom type wfAtmSigT316 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_WfAtmSigT316_Type.__name__ = "Integer32"
_WfAtmSigT316_Object = MibTableColumn
wfAtmSigT316 = _WfAtmSigT316_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 30),
    _WfAtmSigT316_Type()
)
wfAtmSigT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT316.setStatus("mandatory")


class _WfAtmSigT316c_Type(Integer32):
    """Custom type wfAtmSigT316c based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_WfAtmSigT316c_Type.__name__ = "Integer32"
_WfAtmSigT316c_Object = MibTableColumn
wfAtmSigT316c = _WfAtmSigT316c_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 31),
    _WfAtmSigT316c_Type()
)
wfAtmSigT316c.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT316c.setStatus("mandatory")


class _WfAtmSigT322_Type(Integer32):
    """Custom type wfAtmSigT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfAtmSigT322_Type.__name__ = "Integer32"
_WfAtmSigT322_Object = MibTableColumn
wfAtmSigT322 = _WfAtmSigT322_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 32),
    _WfAtmSigT322_Type()
)
wfAtmSigT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT322.setStatus("mandatory")


class _WfAtmSigTDisc_Type(Integer32):
    """Custom type wfAtmSigTDisc based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_WfAtmSigTDisc_Type.__name__ = "Integer32"
_WfAtmSigTDisc_Object = MibTableColumn
wfAtmSigTDisc = _WfAtmSigTDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 33),
    _WfAtmSigTDisc_Type()
)
wfAtmSigTDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigTDisc.setStatus("mandatory")


class _WfAtmSigT398_Type(Integer32):
    """Custom type wfAtmSigT398 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfAtmSigT398_Type.__name__ = "Integer32"
_WfAtmSigT398_Object = MibTableColumn
wfAtmSigT398 = _WfAtmSigT398_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 34),
    _WfAtmSigT398_Type()
)
wfAtmSigT398.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT398.setStatus("mandatory")


class _WfAtmSigT399_Type(Integer32):
    """Custom type wfAtmSigT399 based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_WfAtmSigT399_Type.__name__ = "Integer32"
_WfAtmSigT399_Object = MibTableColumn
wfAtmSigT399 = _WfAtmSigT399_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 35),
    _WfAtmSigT399_Type()
)
wfAtmSigT399.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT399.setStatus("mandatory")


class _WfAtmSigNumRst_Type(Integer32):
    """Custom type wfAtmSigNumRst based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfAtmSigNumRst_Type.__name__ = "Integer32"
_WfAtmSigNumRst_Object = MibTableColumn
wfAtmSigNumRst = _WfAtmSigNumRst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 36),
    _WfAtmSigNumRst_Type()
)
wfAtmSigNumRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigNumRst.setStatus("mandatory")


class _WfAtmSigNumStat_Type(Integer32):
    """Custom type wfAtmSigNumStat based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfAtmSigNumStat_Type.__name__ = "Integer32"
_WfAtmSigNumStat_Object = MibTableColumn
wfAtmSigNumStat = _WfAtmSigNumStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 37),
    _WfAtmSigNumStat_Type()
)
wfAtmSigNumStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigNumStat.setStatus("mandatory")


class _WfAtmSigRestart_Type(Integer32):
    """Custom type wfAtmSigRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfAtmSigRestart_Type.__name__ = "Integer32"
_WfAtmSigRestart_Object = MibTableColumn
wfAtmSigRestart = _WfAtmSigRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 38),
    _WfAtmSigRestart_Type()
)
wfAtmSigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigRestart.setStatus("mandatory")


class _WfAtmSigDebug_Type(Integer32):
    """Custom type wfAtmSigDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("all", 2147483647),
          ("detail", 4),
          ("disabled", 1),
          ("status", 2))
    )


_WfAtmSigDebug_Type.__name__ = "Integer32"
_WfAtmSigDebug_Object = MibTableColumn
wfAtmSigDebug = _WfAtmSigDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 39),
    _WfAtmSigDebug_Type()
)
wfAtmSigDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigDebug.setStatus("mandatory")


class _WfAtmSigCallsSec_Type(Integer32):
    """Custom type wfAtmSigCallsSec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfAtmSigCallsSec_Type.__name__ = "Integer32"
_WfAtmSigCallsSec_Object = MibTableColumn
wfAtmSigCallsSec = _WfAtmSigCallsSec_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 40),
    _WfAtmSigCallsSec_Type()
)
wfAtmSigCallsSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigCallsSec.setStatus("mandatory")


class _WfAtmSigT301_Type(Integer32):
    """Custom type wfAtmSigT301 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 1024),
    )


_WfAtmSigT301_Type.__name__ = "Integer32"
_WfAtmSigT301_Object = MibTableColumn
wfAtmSigT301 = _WfAtmSigT301_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 41),
    _WfAtmSigT301_Type()
)
wfAtmSigT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT301.setStatus("mandatory")


class _WfAtmSigT304_Type(Integer32):
    """Custom type wfAtmSigT304 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_WfAtmSigT304_Type.__name__ = "Integer32"
_WfAtmSigT304_Object = MibTableColumn
wfAtmSigT304 = _WfAtmSigT304_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 42),
    _WfAtmSigT304_Type()
)
wfAtmSigT304.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT304.setStatus("mandatory")


class _WfAtmSigT397_Type(Integer32):
    """Custom type wfAtmSigT397 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 1024),
    )


_WfAtmSigT397_Type.__name__ = "Integer32"
_WfAtmSigT397_Object = MibTableColumn
wfAtmSigT397 = _WfAtmSigT397_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 7, 1, 43),
    _WfAtmSigT397_Type()
)
wfAtmSigT397.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSigT397.setStatus("mandatory")
_WfAtmSscopTable_Object = MibTable
wfAtmSscopTable = _WfAtmSscopTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8)
)
if mibBuilder.loadTexts:
    wfAtmSscopTable.setStatus("mandatory")
_WfAtmSscopEntry_Object = MibTableRow
wfAtmSscopEntry = _WfAtmSscopEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1)
)
wfAtmSscopEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmSscopLineNumber"),
)
if mibBuilder.loadTexts:
    wfAtmSscopEntry.setStatus("mandatory")


class _WfAtmSscopDelete_Type(Integer32):
    """Custom type wfAtmSscopDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmSscopDelete_Type.__name__ = "Integer32"
_WfAtmSscopDelete_Object = MibTableColumn
wfAtmSscopDelete = _WfAtmSscopDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 1),
    _WfAtmSscopDelete_Type()
)
wfAtmSscopDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopDelete.setStatus("mandatory")


class _WfAtmSscopDisable_Type(Integer32):
    """Custom type wfAtmSscopDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmSscopDisable_Type.__name__ = "Integer32"
_WfAtmSscopDisable_Object = MibTableColumn
wfAtmSscopDisable = _WfAtmSscopDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 2),
    _WfAtmSscopDisable_Type()
)
wfAtmSscopDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopDisable.setStatus("mandatory")
_WfAtmSscopLineNumber_Type = Integer32
_WfAtmSscopLineNumber_Object = MibTableColumn
wfAtmSscopLineNumber = _WfAtmSscopLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 3),
    _WfAtmSscopLineNumber_Type()
)
wfAtmSscopLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSscopLineNumber.setStatus("mandatory")
_WfAtmSscopAtmCct_Type = Integer32
_WfAtmSscopAtmCct_Object = MibTableColumn
wfAtmSscopAtmCct = _WfAtmSscopAtmCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 4),
    _WfAtmSscopAtmCct_Type()
)
wfAtmSscopAtmCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSscopAtmCct.setStatus("mandatory")


class _WfAtmSscopState_Type(Integer32):
    """Custom type wfAtmSscopState based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmSscopState_Type.__name__ = "Integer32"
_WfAtmSscopState_Object = MibTableColumn
wfAtmSscopState = _WfAtmSscopState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 5),
    _WfAtmSscopState_Type()
)
wfAtmSscopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSscopState.setStatus("mandatory")


class _WfAtmSscopLowThreshold_Type(Integer32):
    """Custom type wfAtmSscopLowThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfAtmSscopLowThreshold_Type.__name__ = "Integer32"
_WfAtmSscopLowThreshold_Object = MibTableColumn
wfAtmSscopLowThreshold = _WfAtmSscopLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 6),
    _WfAtmSscopLowThreshold_Type()
)
wfAtmSscopLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopLowThreshold.setStatus("mandatory")


class _WfAtmSscopUpThreshold_Type(Integer32):
    """Custom type wfAtmSscopUpThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfAtmSscopUpThreshold_Type.__name__ = "Integer32"
_WfAtmSscopUpThreshold_Object = MibTableColumn
wfAtmSscopUpThreshold = _WfAtmSscopUpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 7),
    _WfAtmSscopUpThreshold_Type()
)
wfAtmSscopUpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopUpThreshold.setStatus("mandatory")


class _WfAtmSscopArbitration_Type(Integer32):
    """Custom type wfAtmSscopArbitration based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_WfAtmSscopArbitration_Type.__name__ = "Integer32"
_WfAtmSscopArbitration_Object = MibTableColumn
wfAtmSscopArbitration = _WfAtmSscopArbitration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 8),
    _WfAtmSscopArbitration_Type()
)
wfAtmSscopArbitration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopArbitration.setStatus("mandatory")


class _WfAtmSscopPollTimer_Type(Integer32):
    """Custom type wfAtmSscopPollTimer based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmSscopPollTimer_Type.__name__ = "Integer32"
_WfAtmSscopPollTimer_Object = MibTableColumn
wfAtmSscopPollTimer = _WfAtmSscopPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 9),
    _WfAtmSscopPollTimer_Type()
)
wfAtmSscopPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopPollTimer.setStatus("mandatory")


class _WfAtmSscopKeepAliveTimer_Type(Integer32):
    """Custom type wfAtmSscopKeepAliveTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmSscopKeepAliveTimer_Type.__name__ = "Integer32"
_WfAtmSscopKeepAliveTimer_Object = MibTableColumn
wfAtmSscopKeepAliveTimer = _WfAtmSscopKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 10),
    _WfAtmSscopKeepAliveTimer_Type()
)
wfAtmSscopKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopKeepAliveTimer.setStatus("mandatory")


class _WfAtmSscopNoResponseTimer_Type(Integer32):
    """Custom type wfAtmSscopNoResponseTimer based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmSscopNoResponseTimer_Type.__name__ = "Integer32"
_WfAtmSscopNoResponseTimer_Object = MibTableColumn
wfAtmSscopNoResponseTimer = _WfAtmSscopNoResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 11),
    _WfAtmSscopNoResponseTimer_Type()
)
wfAtmSscopNoResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopNoResponseTimer.setStatus("mandatory")


class _WfAtmSscopConnectControlTimer_Type(Integer32):
    """Custom type wfAtmSscopConnectControlTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmSscopConnectControlTimer_Type.__name__ = "Integer32"
_WfAtmSscopConnectControlTimer_Object = MibTableColumn
wfAtmSscopConnectControlTimer = _WfAtmSscopConnectControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 12),
    _WfAtmSscopConnectControlTimer_Type()
)
wfAtmSscopConnectControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopConnectControlTimer.setStatus("mandatory")


class _WfAtmSscopMaxCc_Type(Integer32):
    """Custom type wfAtmSscopMaxCc based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfAtmSscopMaxCc_Type.__name__ = "Integer32"
_WfAtmSscopMaxCc_Object = MibTableColumn
wfAtmSscopMaxCc = _WfAtmSscopMaxCc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 13),
    _WfAtmSscopMaxCc_Type()
)
wfAtmSscopMaxCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopMaxCc.setStatus("mandatory")


class _WfAtmSscopMaxPd_Type(Integer32):
    """Custom type wfAtmSscopMaxPd based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmSscopMaxPd_Type.__name__ = "Integer32"
_WfAtmSscopMaxPd_Object = MibTableColumn
wfAtmSscopMaxPd = _WfAtmSscopMaxPd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 14),
    _WfAtmSscopMaxPd_Type()
)
wfAtmSscopMaxPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopMaxPd.setStatus("mandatory")


class _WfAtmSscopMaxStat_Type(Integer32):
    """Custom type wfAtmSscopMaxStat based on Integer32"""
    defaultValue = 67

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmSscopMaxStat_Type.__name__ = "Integer32"
_WfAtmSscopMaxStat_Object = MibTableColumn
wfAtmSscopMaxStat = _WfAtmSscopMaxStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 15),
    _WfAtmSscopMaxStat_Type()
)
wfAtmSscopMaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopMaxStat.setStatus("mandatory")


class _WfAtmSscopIdleTimer_Type(Integer32):
    """Custom type wfAtmSscopIdleTimer based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_WfAtmSscopIdleTimer_Type.__name__ = "Integer32"
_WfAtmSscopIdleTimer_Object = MibTableColumn
wfAtmSscopIdleTimer = _WfAtmSscopIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 16),
    _WfAtmSscopIdleTimer_Type()
)
wfAtmSscopIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopIdleTimer.setStatus("mandatory")


class _WfAtmSscopStandard_Type(Integer32):
    """Custom type wfAtmSscopStandard based on Integer32"""
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
        *(("v30", 1),
          ("v31", 2),
          ("v40", 3))
    )


_WfAtmSscopStandard_Type.__name__ = "Integer32"
_WfAtmSscopStandard_Object = MibTableColumn
wfAtmSscopStandard = _WfAtmSscopStandard_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 17),
    _WfAtmSscopStandard_Type()
)
wfAtmSscopStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopStandard.setStatus("mandatory")


class _WfAtmSscopDebug_Type(Integer32):
    """Custom type wfAtmSscopDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("all", 2147483647),
          ("detail", 4),
          ("disabled", 1),
          ("status", 2))
    )


_WfAtmSscopDebug_Type.__name__ = "Integer32"
_WfAtmSscopDebug_Object = MibTableColumn
wfAtmSscopDebug = _WfAtmSscopDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 8, 1, 18),
    _WfAtmSscopDebug_Type()
)
wfAtmSscopDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSscopDebug.setStatus("mandatory")
_WfAtmIlmiTable_Object = MibTable
wfAtmIlmiTable = _WfAtmIlmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9)
)
if mibBuilder.loadTexts:
    wfAtmIlmiTable.setStatus("mandatory")
_WfAtmIlmiEntry_Object = MibTableRow
wfAtmIlmiEntry = _WfAtmIlmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1)
)
wfAtmIlmiEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmIlmiLineNumber"),
)
if mibBuilder.loadTexts:
    wfAtmIlmiEntry.setStatus("mandatory")


class _WfAtmIlmiDelete_Type(Integer32):
    """Custom type wfAtmIlmiDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmIlmiDelete_Type.__name__ = "Integer32"
_WfAtmIlmiDelete_Object = MibTableColumn
wfAtmIlmiDelete = _WfAtmIlmiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 1),
    _WfAtmIlmiDelete_Type()
)
wfAtmIlmiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiDelete.setStatus("mandatory")


class _WfAtmIlmiDisable_Type(Integer32):
    """Custom type wfAtmIlmiDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmIlmiDisable_Type.__name__ = "Integer32"
_WfAtmIlmiDisable_Object = MibTableColumn
wfAtmIlmiDisable = _WfAtmIlmiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 2),
    _WfAtmIlmiDisable_Type()
)
wfAtmIlmiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiDisable.setStatus("mandatory")
_WfAtmIlmiLineNumber_Type = Integer32
_WfAtmIlmiLineNumber_Object = MibTableColumn
wfAtmIlmiLineNumber = _WfAtmIlmiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 3),
    _WfAtmIlmiLineNumber_Type()
)
wfAtmIlmiLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmIlmiLineNumber.setStatus("mandatory")
_WfAtmIlmiAtmCct_Type = Integer32
_WfAtmIlmiAtmCct_Object = MibTableColumn
wfAtmIlmiAtmCct = _WfAtmIlmiAtmCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 4),
    _WfAtmIlmiAtmCct_Type()
)
wfAtmIlmiAtmCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmIlmiAtmCct.setStatus("mandatory")


class _WfAtmIlmiState_Type(Integer32):
    """Custom type wfAtmIlmiState based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmIlmiState_Type.__name__ = "Integer32"
_WfAtmIlmiState_Object = MibTableColumn
wfAtmIlmiState = _WfAtmIlmiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 5),
    _WfAtmIlmiState_Type()
)
wfAtmIlmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmIlmiState.setStatus("mandatory")


class _WfAtmIlmiLowThreshold_Type(Integer32):
    """Custom type wfAtmIlmiLowThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfAtmIlmiLowThreshold_Type.__name__ = "Integer32"
_WfAtmIlmiLowThreshold_Object = MibTableColumn
wfAtmIlmiLowThreshold = _WfAtmIlmiLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 6),
    _WfAtmIlmiLowThreshold_Type()
)
wfAtmIlmiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiLowThreshold.setStatus("mandatory")


class _WfAtmIlmiUpThreshold_Type(Integer32):
    """Custom type wfAtmIlmiUpThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfAtmIlmiUpThreshold_Type.__name__ = "Integer32"
_WfAtmIlmiUpThreshold_Object = MibTableColumn
wfAtmIlmiUpThreshold = _WfAtmIlmiUpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 7),
    _WfAtmIlmiUpThreshold_Type()
)
wfAtmIlmiUpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiUpThreshold.setStatus("mandatory")


class _WfAtmIlmiVpi_Type(Integer32):
    """Custom type wfAtmIlmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmIlmiVpi_Type.__name__ = "Integer32"
_WfAtmIlmiVpi_Object = MibTableColumn
wfAtmIlmiVpi = _WfAtmIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 8),
    _WfAtmIlmiVpi_Type()
)
wfAtmIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiVpi.setStatus("mandatory")


class _WfAtmIlmiVci_Type(Integer32):
    """Custom type wfAtmIlmiVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmIlmiVci_Type.__name__ = "Integer32"
_WfAtmIlmiVci_Object = MibTableColumn
wfAtmIlmiVci = _WfAtmIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 9),
    _WfAtmIlmiVci_Type()
)
wfAtmIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiVci.setStatus("mandatory")


class _WfAtmIlmiInterfaceType_Type(Integer32):
    """Custom type wfAtmIlmiInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_WfAtmIlmiInterfaceType_Type.__name__ = "Integer32"
_WfAtmIlmiInterfaceType_Object = MibTableColumn
wfAtmIlmiInterfaceType = _WfAtmIlmiInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 10),
    _WfAtmIlmiInterfaceType_Type()
)
wfAtmIlmiInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiInterfaceType.setStatus("mandatory")
_WfAtmIlmiLocalPort_Type = Integer32
_WfAtmIlmiLocalPort_Object = MibTableColumn
wfAtmIlmiLocalPort = _WfAtmIlmiLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 11),
    _WfAtmIlmiLocalPort_Type()
)
wfAtmIlmiLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmIlmiLocalPort.setStatus("mandatory")
_WfAtmIlmiRemotePort_Type = Integer32
_WfAtmIlmiRemotePort_Object = MibTableColumn
wfAtmIlmiRemotePort = _WfAtmIlmiRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 12),
    _WfAtmIlmiRemotePort_Type()
)
wfAtmIlmiRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmIlmiRemotePort.setStatus("mandatory")


class _WfAtmIlmiGetTimer_Type(Integer32):
    """Custom type wfAtmIlmiGetTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmIlmiGetTimer_Type.__name__ = "Integer32"
_WfAtmIlmiGetTimer_Object = MibTableColumn
wfAtmIlmiGetTimer = _WfAtmIlmiGetTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 13),
    _WfAtmIlmiGetTimer_Type()
)
wfAtmIlmiGetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiGetTimer.setStatus("mandatory")


class _WfAtmIlmiGetRetryCnt_Type(Integer32):
    """Custom type wfAtmIlmiGetRetryCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfAtmIlmiGetRetryCnt_Type.__name__ = "Integer32"
_WfAtmIlmiGetRetryCnt_Object = MibTableColumn
wfAtmIlmiGetRetryCnt = _WfAtmIlmiGetRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 14),
    _WfAtmIlmiGetRetryCnt_Type()
)
wfAtmIlmiGetRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiGetRetryCnt.setStatus("mandatory")


class _WfAtmIlmiGetNextTimer_Type(Integer32):
    """Custom type wfAtmIlmiGetNextTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmIlmiGetNextTimer_Type.__name__ = "Integer32"
_WfAtmIlmiGetNextTimer_Object = MibTableColumn
wfAtmIlmiGetNextTimer = _WfAtmIlmiGetNextTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 15),
    _WfAtmIlmiGetNextTimer_Type()
)
wfAtmIlmiGetNextTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiGetNextTimer.setStatus("mandatory")


class _WfAtmIlmiGetNextRetryCnt_Type(Integer32):
    """Custom type wfAtmIlmiGetNextRetryCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfAtmIlmiGetNextRetryCnt_Type.__name__ = "Integer32"
_WfAtmIlmiGetNextRetryCnt_Object = MibTableColumn
wfAtmIlmiGetNextRetryCnt = _WfAtmIlmiGetNextRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 16),
    _WfAtmIlmiGetNextRetryCnt_Type()
)
wfAtmIlmiGetNextRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiGetNextRetryCnt.setStatus("mandatory")


class _WfAtmIlmiSetTimer_Type(Integer32):
    """Custom type wfAtmIlmiSetTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmIlmiSetTimer_Type.__name__ = "Integer32"
_WfAtmIlmiSetTimer_Object = MibTableColumn
wfAtmIlmiSetTimer = _WfAtmIlmiSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 17),
    _WfAtmIlmiSetTimer_Type()
)
wfAtmIlmiSetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiSetTimer.setStatus("mandatory")


class _WfAtmIlmiSetRetryCnt_Type(Integer32):
    """Custom type wfAtmIlmiSetRetryCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfAtmIlmiSetRetryCnt_Type.__name__ = "Integer32"
_WfAtmIlmiSetRetryCnt_Object = MibTableColumn
wfAtmIlmiSetRetryCnt = _WfAtmIlmiSetRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 18),
    _WfAtmIlmiSetRetryCnt_Type()
)
wfAtmIlmiSetRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiSetRetryCnt.setStatus("mandatory")
_WfAtmIlmiLocalOid_Type = ObjectIdentifier
_WfAtmIlmiLocalOid_Object = MibTableColumn
wfAtmIlmiLocalOid = _WfAtmIlmiLocalOid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 19),
    _WfAtmIlmiLocalOid_Type()
)
wfAtmIlmiLocalOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmIlmiLocalOid.setStatus("mandatory")


class _WfAtmIlmiDebug_Type(Integer32):
    """Custom type wfAtmIlmiDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("all", 2147483647),
          ("detail", 4),
          ("disabled", 1),
          ("status", 2))
    )


_WfAtmIlmiDebug_Type.__name__ = "Integer32"
_WfAtmIlmiDebug_Object = MibTableColumn
wfAtmIlmiDebug = _WfAtmIlmiDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 20),
    _WfAtmIlmiDebug_Type()
)
wfAtmIlmiDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiDebug.setStatus("mandatory")


class _WfAtmIlmiNetPrefixTimer_Type(Integer32):
    """Custom type wfAtmIlmiNetPrefixTimer based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfAtmIlmiNetPrefixTimer_Type.__name__ = "Integer32"
_WfAtmIlmiNetPrefixTimer_Object = MibTableColumn
wfAtmIlmiNetPrefixTimer = _WfAtmIlmiNetPrefixTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 9, 1, 21),
    _WfAtmIlmiNetPrefixTimer_Type()
)
wfAtmIlmiNetPrefixTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmIlmiNetPrefixTimer.setStatus("mandatory")
_WfAtmNetPrefixTable_Object = MibTable
wfAtmNetPrefixTable = _WfAtmNetPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 10)
)
if mibBuilder.loadTexts:
    wfAtmNetPrefixTable.setStatus("mandatory")
_WfAtmNetPrefixEntry_Object = MibTableRow
wfAtmNetPrefixEntry = _WfAtmNetPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 10, 1)
)
wfAtmNetPrefixEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmNetPrefixPort"),
    (0, "Wellfleet-ATM-MIB", "wfAtmNetPrefixPrefix"),
)
if mibBuilder.loadTexts:
    wfAtmNetPrefixEntry.setStatus("mandatory")
_WfAtmNetPrefixPort_Type = Integer32
_WfAtmNetPrefixPort_Object = MibTableColumn
wfAtmNetPrefixPort = _WfAtmNetPrefixPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 10, 1, 1),
    _WfAtmNetPrefixPort_Type()
)
wfAtmNetPrefixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmNetPrefixPort.setStatus("mandatory")
_WfAtmNetPrefixPrefix_Type = OctetString
_WfAtmNetPrefixPrefix_Object = MibTableColumn
wfAtmNetPrefixPrefix = _WfAtmNetPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 10, 1, 2),
    _WfAtmNetPrefixPrefix_Type()
)
wfAtmNetPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmNetPrefixPrefix.setStatus("mandatory")


class _WfAtmNetPrefixStatus_Type(Integer32):
    """Custom type wfAtmNetPrefixStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfAtmNetPrefixStatus_Type.__name__ = "Integer32"
_WfAtmNetPrefixStatus_Object = MibTableColumn
wfAtmNetPrefixStatus = _WfAtmNetPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 10, 1, 3),
    _WfAtmNetPrefixStatus_Type()
)
wfAtmNetPrefixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmNetPrefixStatus.setStatus("mandatory")
_WfAtmTableDebugTable_Object = MibTable
wfAtmTableDebugTable = _WfAtmTableDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 11)
)
if mibBuilder.loadTexts:
    wfAtmTableDebugTable.setStatus("mandatory")
_WfAtmTableDebugEntry_Object = MibTableRow
wfAtmTableDebugEntry = _WfAtmTableDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 11, 1)
)
wfAtmTableDebugEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmTableDebugSlot"),
)
if mibBuilder.loadTexts:
    wfAtmTableDebugEntry.setStatus("mandatory")


class _WfAtmTableDebugDelete_Type(Integer32):
    """Custom type wfAtmTableDebugDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmTableDebugDelete_Type.__name__ = "Integer32"
_WfAtmTableDebugDelete_Object = MibTableColumn
wfAtmTableDebugDelete = _WfAtmTableDebugDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 11, 1, 1),
    _WfAtmTableDebugDelete_Type()
)
wfAtmTableDebugDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmTableDebugDelete.setStatus("mandatory")
_WfAtmTableDebugSlot_Type = Integer32
_WfAtmTableDebugSlot_Object = MibTableColumn
wfAtmTableDebugSlot = _WfAtmTableDebugSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 11, 1, 2),
    _WfAtmTableDebugSlot_Type()
)
wfAtmTableDebugSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmTableDebugSlot.setStatus("mandatory")
_WfAtmTableDebugType_Type = Integer32
_WfAtmTableDebugType_Object = MibTableColumn
wfAtmTableDebugType = _WfAtmTableDebugType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 11, 1, 3),
    _WfAtmTableDebugType_Type()
)
wfAtmTableDebugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmTableDebugType.setStatus("mandatory")
_WfAtmVcGroupTable_Object = MibTable
wfAtmVcGroupTable = _WfAtmVcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 12)
)
if mibBuilder.loadTexts:
    wfAtmVcGroupTable.setStatus("mandatory")
_WfAtmVcGroupEntry_Object = MibTableRow
wfAtmVcGroupEntry = _WfAtmVcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 12, 1)
)
wfAtmVcGroupEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVcGroupCct"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVcGroupIndex"),
)
if mibBuilder.loadTexts:
    wfAtmVcGroupEntry.setStatus("mandatory")


class _WfAtmVcGroupDelete_Type(Integer32):
    """Custom type wfAtmVcGroupDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmVcGroupDelete_Type.__name__ = "Integer32"
_WfAtmVcGroupDelete_Object = MibTableColumn
wfAtmVcGroupDelete = _WfAtmVcGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 12, 1, 1),
    _WfAtmVcGroupDelete_Type()
)
wfAtmVcGroupDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVcGroupDelete.setStatus("mandatory")
_WfAtmVcGroupCct_Type = Integer32
_WfAtmVcGroupCct_Object = MibTableColumn
wfAtmVcGroupCct = _WfAtmVcGroupCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 12, 1, 2),
    _WfAtmVcGroupCct_Type()
)
wfAtmVcGroupCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVcGroupCct.setStatus("mandatory")
_WfAtmVcGroupIndex_Type = Integer32
_WfAtmVcGroupIndex_Object = MibTableColumn
wfAtmVcGroupIndex = _WfAtmVcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 12, 1, 3),
    _WfAtmVcGroupIndex_Type()
)
wfAtmVcGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVcGroupIndex.setStatus("mandatory")
_WfAtmVcGroupName_Type = DisplayString
_WfAtmVcGroupName_Object = MibTableColumn
wfAtmVcGroupName = _WfAtmVcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 12, 1, 4),
    _WfAtmVcGroupName_Type()
)
wfAtmVcGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmVcGroupName.setStatus("mandatory")
_WfAtmSVCOptionsTable_Object = MibTable
wfAtmSVCOptionsTable = _WfAtmSVCOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13)
)
if mibBuilder.loadTexts:
    wfAtmSVCOptionsTable.setStatus("mandatory")
_WfAtmSVCOptionsEntry_Object = MibTableRow
wfAtmSVCOptionsEntry = _WfAtmSVCOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1)
)
wfAtmSVCOptionsEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmSVCOptionsCct"),
    (0, "Wellfleet-ATM-MIB", "wfAtmSVCOptionsIndex"),
)
if mibBuilder.loadTexts:
    wfAtmSVCOptionsEntry.setStatus("mandatory")


class _WfAtmSVCOptionsDelete_Type(Integer32):
    """Custom type wfAtmSVCOptionsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmSVCOptionsDelete_Type.__name__ = "Integer32"
_WfAtmSVCOptionsDelete_Object = MibTableColumn
wfAtmSVCOptionsDelete = _WfAtmSVCOptionsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 1),
    _WfAtmSVCOptionsDelete_Type()
)
wfAtmSVCOptionsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsDelete.setStatus("mandatory")


class _WfAtmSVCOptionsDisable_Type(Integer32):
    """Custom type wfAtmSVCOptionsDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmSVCOptionsDisable_Type.__name__ = "Integer32"
_WfAtmSVCOptionsDisable_Object = MibTableColumn
wfAtmSVCOptionsDisable = _WfAtmSVCOptionsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 2),
    _WfAtmSVCOptionsDisable_Type()
)
wfAtmSVCOptionsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsDisable.setStatus("mandatory")
_WfAtmSVCOptionsCct_Type = Integer32
_WfAtmSVCOptionsCct_Object = MibTableColumn
wfAtmSVCOptionsCct = _WfAtmSVCOptionsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 3),
    _WfAtmSVCOptionsCct_Type()
)
wfAtmSVCOptionsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsCct.setStatus("mandatory")
_WfAtmSVCOptionsIndex_Type = Integer32
_WfAtmSVCOptionsIndex_Object = MibTableColumn
wfAtmSVCOptionsIndex = _WfAtmSVCOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 4),
    _WfAtmSVCOptionsIndex_Type()
)
wfAtmSVCOptionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsIndex.setStatus("mandatory")


class _WfAtmSVCOptionsAdjHostAtmAddr_Type(OctetString):
    """Custom type wfAtmSVCOptionsAdjHostAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfAtmSVCOptionsAdjHostAtmAddr_Type.__name__ = "OctetString"
_WfAtmSVCOptionsAdjHostAtmAddr_Object = MibTableColumn
wfAtmSVCOptionsAdjHostAtmAddr = _WfAtmSVCOptionsAdjHostAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 5),
    _WfAtmSVCOptionsAdjHostAtmAddr_Type()
)
wfAtmSVCOptionsAdjHostAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsAdjHostAtmAddr.setStatus("mandatory")


class _WfAtmSVCOptionsXmtPeakCellRate_Type(Integer32):
    """Custom type wfAtmSVCOptionsXmtPeakCellRate based on Integer32"""
    defaultValue = 4716


_WfAtmSVCOptionsXmtPeakCellRate_Object = MibTableColumn
wfAtmSVCOptionsXmtPeakCellRate = _WfAtmSVCOptionsXmtPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 6),
    _WfAtmSVCOptionsXmtPeakCellRate_Type()
)
wfAtmSVCOptionsXmtPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsXmtPeakCellRate.setStatus("mandatory")


class _WfAtmSVCOptionsXmtSustCellRate_Type(Integer32):
    """Custom type wfAtmSVCOptionsXmtSustCellRate based on Integer32"""
    defaultValue = 4716


_WfAtmSVCOptionsXmtSustCellRate_Object = MibTableColumn
wfAtmSVCOptionsXmtSustCellRate = _WfAtmSVCOptionsXmtSustCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 7),
    _WfAtmSVCOptionsXmtSustCellRate_Type()
)
wfAtmSVCOptionsXmtSustCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsXmtSustCellRate.setStatus("mandatory")


class _WfAtmSVCOptionsRcvPeakCellRate_Type(Integer32):
    """Custom type wfAtmSVCOptionsRcvPeakCellRate based on Integer32"""
    defaultValue = 4716


_WfAtmSVCOptionsRcvPeakCellRate_Object = MibTableColumn
wfAtmSVCOptionsRcvPeakCellRate = _WfAtmSVCOptionsRcvPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 8),
    _WfAtmSVCOptionsRcvPeakCellRate_Type()
)
wfAtmSVCOptionsRcvPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsRcvPeakCellRate.setStatus("mandatory")


class _WfAtmSVCOptionsRcvSustCellRate_Type(Integer32):
    """Custom type wfAtmSVCOptionsRcvSustCellRate based on Integer32"""
    defaultValue = 4716


_WfAtmSVCOptionsRcvSustCellRate_Object = MibTableColumn
wfAtmSVCOptionsRcvSustCellRate = _WfAtmSVCOptionsRcvSustCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 9),
    _WfAtmSVCOptionsRcvSustCellRate_Type()
)
wfAtmSVCOptionsRcvSustCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsRcvSustCellRate.setStatus("mandatory")
_WfAtmSVCOptionsName_Type = DisplayString
_WfAtmSVCOptionsName_Object = MibTableColumn
wfAtmSVCOptionsName = _WfAtmSVCOptionsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 1, 13, 1, 10),
    _WfAtmSVCOptionsName_Type()
)
wfAtmSVCOptionsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmSVCOptionsName.setStatus("mandatory")
_WfAtmLinkModuleGroup_ObjectIdentity = ObjectIdentity
wfAtmLinkModuleGroup = _WfAtmLinkModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2)
)
_WfAtmAlcDrvTable_Object = MibTable
wfAtmAlcDrvTable = _WfAtmAlcDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1)
)
if mibBuilder.loadTexts:
    wfAtmAlcDrvTable.setStatus("mandatory")
_WfAtmAlcDrvEntry_Object = MibTableRow
wfAtmAlcDrvEntry = _WfAtmAlcDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1)
)
wfAtmAlcDrvEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcSlot"),
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcPort"),
)
if mibBuilder.loadTexts:
    wfAtmAlcDrvEntry.setStatus("mandatory")


class _WfAtmAlcDelete_Type(Integer32):
    """Custom type wfAtmAlcDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmAlcDelete_Type.__name__ = "Integer32"
_WfAtmAlcDelete_Object = MibTableColumn
wfAtmAlcDelete = _WfAtmAlcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 1),
    _WfAtmAlcDelete_Type()
)
wfAtmAlcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcDelete.setStatus("mandatory")


class _WfAtmAlcDisable_Type(Integer32):
    """Custom type wfAtmAlcDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcDisable_Type.__name__ = "Integer32"
_WfAtmAlcDisable_Object = MibTableColumn
wfAtmAlcDisable = _WfAtmAlcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 2),
    _WfAtmAlcDisable_Type()
)
wfAtmAlcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcDisable.setStatus("mandatory")


class _WfAtmAlcState_Type(Integer32):
    """Custom type wfAtmAlcState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              20)
        )
    )
    namedValues = NamedValues(
        *(("config", 5),
          ("down", 2),
          ("download", 4),
          ("init", 3),
          ("notpresent", 20),
          ("up", 1))
    )


_WfAtmAlcState_Type.__name__ = "Integer32"
_WfAtmAlcState_Object = MibTableColumn
wfAtmAlcState = _WfAtmAlcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 3),
    _WfAtmAlcState_Type()
)
wfAtmAlcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcState.setStatus("mandatory")


class _WfAtmAlcSlot_Type(Integer32):
    """Custom type wfAtmAlcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfAtmAlcSlot_Type.__name__ = "Integer32"
_WfAtmAlcSlot_Object = MibTableColumn
wfAtmAlcSlot = _WfAtmAlcSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 4),
    _WfAtmAlcSlot_Type()
)
wfAtmAlcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSlot.setStatus("mandatory")


class _WfAtmAlcPort_Type(Integer32):
    """Custom type wfAtmAlcPort based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfAtmAlcPort_Type.__name__ = "Integer32"
_WfAtmAlcPort_Object = MibTableColumn
wfAtmAlcPort = _WfAtmAlcPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 5),
    _WfAtmAlcPort_Type()
)
wfAtmAlcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcPort.setStatus("mandatory")


class _WfAtmAlcCct_Type(Integer32):
    """Custom type wfAtmAlcCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfAtmAlcCct_Type.__name__ = "Integer32"
_WfAtmAlcCct_Object = MibTableColumn
wfAtmAlcCct = _WfAtmAlcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 6),
    _WfAtmAlcCct_Type()
)
wfAtmAlcCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCct.setStatus("mandatory")
_WfAtmAlcLineNumber_Type = Integer32
_WfAtmAlcLineNumber_Object = MibTableColumn
wfAtmAlcLineNumber = _WfAtmAlcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 7),
    _WfAtmAlcLineNumber_Type()
)
wfAtmAlcLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcLineNumber.setStatus("mandatory")


class _WfAtmAlcType_Type(Integer32):
    """Custom type wfAtmAlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type100mb", 3),
          ("typeds3", 2),
          ("typesonet", 1))
    )


_WfAtmAlcType_Type.__name__ = "Integer32"
_WfAtmAlcType_Object = MibTableColumn
wfAtmAlcType = _WfAtmAlcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 8),
    _WfAtmAlcType_Type()
)
wfAtmAlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcType.setStatus("mandatory")


class _WfAtmAlcMtu_Type(Integer32):
    """Custom type wfAtmAlcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4608
        )
    )
    namedValues = NamedValues(
        ("default", 4608)
    )


_WfAtmAlcMtu_Type.__name__ = "Integer32"
_WfAtmAlcMtu_Object = MibTableColumn
wfAtmAlcMtu = _WfAtmAlcMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 9),
    _WfAtmAlcMtu_Type()
)
wfAtmAlcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcMtu.setStatus("mandatory")


class _WfAtmAlcSpeed_Type(Integer32):
    """Custom type wfAtmAlcSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(44736000,
              100000000,
              155520000)
        )
    )
    namedValues = NamedValues(
        *(("speed100mb", 100000000),
          ("speed155mb", 155520000),
          ("speed45mb", 44736000))
    )


_WfAtmAlcSpeed_Type.__name__ = "Integer32"
_WfAtmAlcSpeed_Object = MibTableColumn
wfAtmAlcSpeed = _WfAtmAlcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 10),
    _WfAtmAlcSpeed_Type()
)
wfAtmAlcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSpeed.setStatus("mandatory")
_WfAtmAlcLastChange_Type = TimeTicks
_WfAtmAlcLastChange_Object = MibTableColumn
wfAtmAlcLastChange = _WfAtmAlcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 11),
    _WfAtmAlcLastChange_Type()
)
wfAtmAlcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcLastChange.setStatus("mandatory")


class _WfAtmAlcInterfaceStatus_Type(Integer32):
    """Custom type wfAtmAlcInterfaceStatus based on Integer32"""
    defaultValue = 4

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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_WfAtmAlcInterfaceStatus_Type.__name__ = "Integer32"
_WfAtmAlcInterfaceStatus_Object = MibTableColumn
wfAtmAlcInterfaceStatus = _WfAtmAlcInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 12),
    _WfAtmAlcInterfaceStatus_Type()
)
wfAtmAlcInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcInterfaceStatus.setStatus("mandatory")
_WfAtmAlcInterfaceIndex_Type = Integer32
_WfAtmAlcInterfaceIndex_Object = MibTableColumn
wfAtmAlcInterfaceIndex = _WfAtmAlcInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 13),
    _WfAtmAlcInterfaceIndex_Type()
)
wfAtmAlcInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcInterfaceIndex.setStatus("mandatory")


class _WfAtmAlcDpNotify_Type(Integer32):
    """Custom type wfAtmAlcDpNotify based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcDpNotify_Type.__name__ = "Integer32"
_WfAtmAlcDpNotify_Object = MibTableColumn
wfAtmAlcDpNotify = _WfAtmAlcDpNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 14),
    _WfAtmAlcDpNotify_Type()
)
wfAtmAlcDpNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcDpNotify.setStatus("mandatory")


class _WfAtmAlcDpNotifyTimeout_Type(Integer32):
    """Custom type wfAtmAlcDpNotifyTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WfAtmAlcDpNotifyTimeout_Type.__name__ = "Integer32"
_WfAtmAlcDpNotifyTimeout_Object = MibTableColumn
wfAtmAlcDpNotifyTimeout = _WfAtmAlcDpNotifyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 15),
    _WfAtmAlcDpNotifyTimeout_Type()
)
wfAtmAlcDpNotifyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcDpNotifyTimeout.setStatus("mandatory")


class _WfAtmAlcConfControlQSize_Type(Integer32):
    """Custom type wfAtmAlcConfControlQSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("default", 10)
    )


_WfAtmAlcConfControlQSize_Type.__name__ = "Integer32"
_WfAtmAlcConfControlQSize_Object = MibTableColumn
wfAtmAlcConfControlQSize = _WfAtmAlcConfControlQSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 16),
    _WfAtmAlcConfControlQSize_Type()
)
wfAtmAlcConfControlQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfControlQSize.setStatus("mandatory")


class _WfAtmAlcConfIntqSize_Type(Integer32):
    """Custom type wfAtmAlcConfIntqSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("default", 100)
    )


_WfAtmAlcConfIntqSize_Type.__name__ = "Integer32"
_WfAtmAlcConfIntqSize_Object = MibTableColumn
wfAtmAlcConfIntqSize = _WfAtmAlcConfIntqSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 17),
    _WfAtmAlcConfIntqSize_Type()
)
wfAtmAlcConfIntqSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfIntqSize.setStatus("mandatory")


class _WfAtmAlcConfLogqSize_Type(Integer32):
    """Custom type wfAtmAlcConfLogqSize based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            25
        )
    )
    namedValues = NamedValues(
        ("default", 25)
    )


_WfAtmAlcConfLogqSize_Type.__name__ = "Integer32"
_WfAtmAlcConfLogqSize_Object = MibTableColumn
wfAtmAlcConfLogqSize = _WfAtmAlcConfLogqSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 18),
    _WfAtmAlcConfLogqSize_Type()
)
wfAtmAlcConfLogqSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfLogqSize.setStatus("mandatory")


class _WfAtmAlcConfNumXmtQueues_Type(Integer32):
    """Custom type wfAtmAlcConfNumXmtQueues based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 29),
    )


_WfAtmAlcConfNumXmtQueues_Type.__name__ = "Integer32"
_WfAtmAlcConfNumXmtQueues_Object = MibTableColumn
wfAtmAlcConfNumXmtQueues = _WfAtmAlcConfNumXmtQueues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 19),
    _WfAtmAlcConfNumXmtQueues_Type()
)
wfAtmAlcConfNumXmtQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfNumXmtQueues.setStatus("mandatory")


class _WfAtmAlcUseDebugger_Type(Integer32):
    """Custom type wfAtmAlcUseDebugger based on Integer32"""
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


_WfAtmAlcUseDebugger_Type.__name__ = "Integer32"
_WfAtmAlcUseDebugger_Object = MibTableColumn
wfAtmAlcUseDebugger = _WfAtmAlcUseDebugger_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 20),
    _WfAtmAlcUseDebugger_Type()
)
wfAtmAlcUseDebugger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcUseDebugger.setStatus("mandatory")
_WfAtmAlcConfXmtClipSlotMax_Type = Integer32
_WfAtmAlcConfXmtClipSlotMax_Object = MibTableColumn
wfAtmAlcConfXmtClipSlotMax = _WfAtmAlcConfXmtClipSlotMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 21),
    _WfAtmAlcConfXmtClipSlotMax_Type()
)
wfAtmAlcConfXmtClipSlotMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfXmtClipSlotMax.setStatus("mandatory")
_WfAtmAlcXmtClipSlotMax_Type = Integer32
_WfAtmAlcXmtClipSlotMax_Object = MibTableColumn
wfAtmAlcXmtClipSlotMax = _WfAtmAlcXmtClipSlotMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 22),
    _WfAtmAlcXmtClipSlotMax_Type()
)
wfAtmAlcXmtClipSlotMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtClipSlotMax.setStatus("mandatory")
_WfAtmAlcConfXmtClipQueueMax_Type = Integer32
_WfAtmAlcConfXmtClipQueueMax_Object = MibTableColumn
wfAtmAlcConfXmtClipQueueMax = _WfAtmAlcConfXmtClipQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 23),
    _WfAtmAlcConfXmtClipQueueMax_Type()
)
wfAtmAlcConfXmtClipQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfXmtClipQueueMax.setStatus("mandatory")
_WfAtmAlcXmtClipQueueMax_Type = Integer32
_WfAtmAlcXmtClipQueueMax_Object = MibTableColumn
wfAtmAlcXmtClipQueueMax = _WfAtmAlcXmtClipQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 24),
    _WfAtmAlcXmtClipQueueMax_Type()
)
wfAtmAlcXmtClipQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtClipQueueMax.setStatus("mandatory")
_WfAtmAlcConfXmtClipQueueMin_Type = Integer32
_WfAtmAlcConfXmtClipQueueMin_Object = MibTableColumn
wfAtmAlcConfXmtClipQueueMin = _WfAtmAlcConfXmtClipQueueMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 25),
    _WfAtmAlcConfXmtClipQueueMin_Type()
)
wfAtmAlcConfXmtClipQueueMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfXmtClipQueueMin.setStatus("mandatory")
_WfAtmAlcXmtClipQueueMin_Type = Integer32
_WfAtmAlcXmtClipQueueMin_Object = MibTableColumn
wfAtmAlcXmtClipQueueMin = _WfAtmAlcXmtClipQueueMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 26),
    _WfAtmAlcXmtClipQueueMin_Type()
)
wfAtmAlcXmtClipQueueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtClipQueueMin.setStatus("mandatory")


class _WfAtmAlcXmtQueueBurst_Type(Integer32):
    """Custom type wfAtmAlcXmtQueueBurst based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("default", 40)
    )


_WfAtmAlcXmtQueueBurst_Type.__name__ = "Integer32"
_WfAtmAlcXmtQueueBurst_Object = MibTableColumn
wfAtmAlcXmtQueueBurst = _WfAtmAlcXmtQueueBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 27),
    _WfAtmAlcXmtQueueBurst_Type()
)
wfAtmAlcXmtQueueBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcXmtQueueBurst.setStatus("mandatory")
_WfAtmAlcXmtPackets_Type = Counter32
_WfAtmAlcXmtPackets_Object = MibTableColumn
wfAtmAlcXmtPackets = _WfAtmAlcXmtPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 28),
    _WfAtmAlcXmtPackets_Type()
)
wfAtmAlcXmtPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtPackets.setStatus("mandatory")
_WfAtmAlcXmtPacketClips_Type = Counter32
_WfAtmAlcXmtPacketClips_Object = MibTableColumn
wfAtmAlcXmtPacketClips = _WfAtmAlcXmtPacketClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 29),
    _WfAtmAlcXmtPacketClips_Type()
)
wfAtmAlcXmtPacketClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtPacketClips.setStatus("mandatory")
_WfAtmAlcXmtOctets_Type = Counter32
_WfAtmAlcXmtOctets_Object = MibTableColumn
wfAtmAlcXmtOctets = _WfAtmAlcXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 30),
    _WfAtmAlcXmtOctets_Type()
)
wfAtmAlcXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtOctets.setStatus("mandatory")
_WfAtmAlcOutQLen_Type = Gauge32
_WfAtmAlcOutQLen_Object = MibTableColumn
wfAtmAlcOutQLen = _WfAtmAlcOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 31),
    _WfAtmAlcOutQLen_Type()
)
wfAtmAlcOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcOutQLen.setStatus("mandatory")
_WfAtmAlcRcvPackets_Type = Counter32
_WfAtmAlcRcvPackets_Object = MibTableColumn
wfAtmAlcRcvPackets = _WfAtmAlcRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 32),
    _WfAtmAlcRcvPackets_Type()
)
wfAtmAlcRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcRcvPackets.setStatus("mandatory")
_WfAtmAlcRcvReplenMisses_Type = Counter32
_WfAtmAlcRcvReplenMisses_Object = MibTableColumn
wfAtmAlcRcvReplenMisses = _WfAtmAlcRcvReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 33),
    _WfAtmAlcRcvReplenMisses_Type()
)
wfAtmAlcRcvReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcRcvReplenMisses.setStatus("mandatory")
_WfAtmAlcConfRcvBuffersMax_Type = Integer32
_WfAtmAlcConfRcvBuffersMax_Object = MibTableColumn
wfAtmAlcConfRcvBuffersMax = _WfAtmAlcConfRcvBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 34),
    _WfAtmAlcConfRcvBuffersMax_Type()
)
wfAtmAlcConfRcvBuffersMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcConfRcvBuffersMax.setStatus("mandatory")
_WfAtmAlcRcvBuffersMax_Type = Integer32
_WfAtmAlcRcvBuffersMax_Object = MibTableColumn
wfAtmAlcRcvBuffersMax = _WfAtmAlcRcvBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 35),
    _WfAtmAlcRcvBuffersMax_Type()
)
wfAtmAlcRcvBuffersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcRcvBuffersMax.setStatus("mandatory")
_WfAtmAlcMadrCt_Type = Integer32
_WfAtmAlcMadrCt_Object = MibTableColumn
wfAtmAlcMadrCt = _WfAtmAlcMadrCt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 36),
    _WfAtmAlcMadrCt_Type()
)
wfAtmAlcMadrCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcMadrCt.setStatus("mandatory")
_WfAtmAlcMadr_Type = OctetString
_WfAtmAlcMadr_Object = MibTableColumn
wfAtmAlcMadr = _WfAtmAlcMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 37),
    _WfAtmAlcMadr_Type()
)
wfAtmAlcMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcMadr.setStatus("mandatory")


class _WfAtmAlcVcInactEnable_Type(Integer32):
    """Custom type wfAtmAlcVcInactEnable based on Integer32"""
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


_WfAtmAlcVcInactEnable_Type.__name__ = "Integer32"
_WfAtmAlcVcInactEnable_Object = MibTableColumn
wfAtmAlcVcInactEnable = _WfAtmAlcVcInactEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 38),
    _WfAtmAlcVcInactEnable_Type()
)
wfAtmAlcVcInactEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcVcInactEnable.setStatus("mandatory")
_WfAtmAlcXmtBadVcs_Type = Counter32
_WfAtmAlcXmtBadVcs_Object = MibTableColumn
wfAtmAlcXmtBadVcs = _WfAtmAlcXmtBadVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 1, 1, 39),
    _WfAtmAlcXmtBadVcs_Type()
)
wfAtmAlcXmtBadVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtBadVcs.setStatus("mandatory")
_WfAtmAlcXmtqTable_Object = MibTable
wfAtmAlcXmtqTable = _WfAtmAlcXmtqTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2)
)
if mibBuilder.loadTexts:
    wfAtmAlcXmtqTable.setStatus("mandatory")
_WfAtmAlcXmtqEntry_Object = MibTableRow
wfAtmAlcXmtqEntry = _WfAtmAlcXmtqEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1)
)
wfAtmAlcXmtqEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcXmtqIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcXmtqNumber"),
)
if mibBuilder.loadTexts:
    wfAtmAlcXmtqEntry.setStatus("mandatory")
_WfAtmAlcXmtqIndex_Type = Integer32
_WfAtmAlcXmtqIndex_Object = MibTableColumn
wfAtmAlcXmtqIndex = _WfAtmAlcXmtqIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 1),
    _WfAtmAlcXmtqIndex_Type()
)
wfAtmAlcXmtqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqIndex.setStatus("mandatory")


class _WfAtmAlcXmtqNumber_Type(Integer32):
    """Custom type wfAtmAlcXmtqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 28),
    )


_WfAtmAlcXmtqNumber_Type.__name__ = "Integer32"
_WfAtmAlcXmtqNumber_Object = MibTableColumn
wfAtmAlcXmtqNumber = _WfAtmAlcXmtqNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 2),
    _WfAtmAlcXmtqNumber_Type()
)
wfAtmAlcXmtqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqNumber.setStatus("mandatory")


class _WfAtmAlcXmtqState_Type(Integer32):
    """Custom type wfAtmAlcXmtqState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              20)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("initdone", 2),
          ("msgsent", 3),
          ("notpresent", 20))
    )


_WfAtmAlcXmtqState_Type.__name__ = "Integer32"
_WfAtmAlcXmtqState_Object = MibTableColumn
wfAtmAlcXmtqState = _WfAtmAlcXmtqState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 3),
    _WfAtmAlcXmtqState_Type()
)
wfAtmAlcXmtqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqState.setStatus("mandatory")


class _WfAtmAlcXmtqStickyMask_Type(Integer32):
    """Custom type wfAtmAlcXmtqStickyMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAtmAlcXmtqStickyMask_Type.__name__ = "Integer32"
_WfAtmAlcXmtqStickyMask_Object = MibTableColumn
wfAtmAlcXmtqStickyMask = _WfAtmAlcXmtqStickyMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 4),
    _WfAtmAlcXmtqStickyMask_Type()
)
wfAtmAlcXmtqStickyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqStickyMask.setStatus("mandatory")
_WfAtmAlcXmtqVcs_Type = Integer32
_WfAtmAlcXmtqVcs_Object = MibTableColumn
wfAtmAlcXmtqVcs = _WfAtmAlcXmtqVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 5),
    _WfAtmAlcXmtqVcs_Type()
)
wfAtmAlcXmtqVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqVcs.setStatus("mandatory")
_WfAtmAlcXmtqOutQLen_Type = Gauge32
_WfAtmAlcXmtqOutQLen_Object = MibTableColumn
wfAtmAlcXmtqOutQLen = _WfAtmAlcXmtqOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 6),
    _WfAtmAlcXmtqOutQLen_Type()
)
wfAtmAlcXmtqOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqOutQLen.setStatus("mandatory")
_WfAtmAlcXmtqOctets_Type = Counter32
_WfAtmAlcXmtqOctets_Object = MibTableColumn
wfAtmAlcXmtqOctets = _WfAtmAlcXmtqOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 7),
    _WfAtmAlcXmtqOctets_Type()
)
wfAtmAlcXmtqOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqOctets.setStatus("mandatory")
_WfAtmAlcXmtqPackets_Type = Counter32
_WfAtmAlcXmtqPackets_Object = MibTableColumn
wfAtmAlcXmtqPackets = _WfAtmAlcXmtqPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 8),
    _WfAtmAlcXmtqPackets_Type()
)
wfAtmAlcXmtqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqPackets.setStatus("mandatory")
_WfAtmAlcXmtqPacketClips_Type = Counter32
_WfAtmAlcXmtqPacketClips_Object = MibTableColumn
wfAtmAlcXmtqPacketClips = _WfAtmAlcXmtqPacketClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 2, 1, 9),
    _WfAtmAlcXmtqPacketClips_Type()
)
wfAtmAlcXmtqPacketClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcXmtqPacketClips.setStatus("mandatory")
_WfAtmAlcCopConfTable_Object = MibTable
wfAtmAlcCopConfTable = _WfAtmAlcCopConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3)
)
if mibBuilder.loadTexts:
    wfAtmAlcCopConfTable.setStatus("mandatory")
_WfAtmAlcCopConfEntry_Object = MibTableRow
wfAtmAlcCopConfEntry = _WfAtmAlcCopConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1)
)
wfAtmAlcCopConfEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcCopConfIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcCopConfEntry.setStatus("mandatory")


class _WfAtmAlcCopConfDelete_Type(Integer32):
    """Custom type wfAtmAlcCopConfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmAlcCopConfDelete_Type.__name__ = "Integer32"
_WfAtmAlcCopConfDelete_Object = MibTableColumn
wfAtmAlcCopConfDelete = _WfAtmAlcCopConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 1),
    _WfAtmAlcCopConfDelete_Type()
)
wfAtmAlcCopConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopConfDelete.setStatus("mandatory")
_WfAtmAlcCopConfIndex_Type = Integer32
_WfAtmAlcCopConfIndex_Object = MibTableColumn
wfAtmAlcCopConfIndex = _WfAtmAlcCopConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 2),
    _WfAtmAlcCopConfIndex_Type()
)
wfAtmAlcCopConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopConfIndex.setStatus("mandatory")


class _WfAtmAlcCopBufSize_Type(Integer32):
    """Custom type wfAtmAlcCopBufSize based on Integer32"""
    defaultValue = 532

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1024),
    )


_WfAtmAlcCopBufSize_Type.__name__ = "Integer32"
_WfAtmAlcCopBufSize_Object = MibTableColumn
wfAtmAlcCopBufSize = _WfAtmAlcCopBufSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 3),
    _WfAtmAlcCopBufSize_Type()
)
wfAtmAlcCopBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopBufSize.setStatus("mandatory")


class _WfAtmAlcCopConfXmtBufs_Type(Integer32):
    """Custom type wfAtmAlcCopConfXmtBufs based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 90),
    )


_WfAtmAlcCopConfXmtBufs_Type.__name__ = "Integer32"
_WfAtmAlcCopConfXmtBufs_Object = MibTableColumn
wfAtmAlcCopConfXmtBufs = _WfAtmAlcCopConfXmtBufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 4),
    _WfAtmAlcCopConfXmtBufs_Type()
)
wfAtmAlcCopConfXmtBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopConfXmtBufs.setStatus("mandatory")


class _WfAtmAlcCopConfRcvBufs_Type(Integer32):
    """Custom type wfAtmAlcCopConfRcvBufs based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 90),
    )


_WfAtmAlcCopConfRcvBufs_Type.__name__ = "Integer32"
_WfAtmAlcCopConfRcvBufs_Object = MibTableColumn
wfAtmAlcCopConfRcvBufs = _WfAtmAlcCopConfRcvBufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 5),
    _WfAtmAlcCopConfRcvBufs_Type()
)
wfAtmAlcCopConfRcvBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopConfRcvBufs.setStatus("mandatory")


class _WfAtmAlcCopDmaHighWatermark_Type(Integer32):
    """Custom type wfAtmAlcCopDmaHighWatermark based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WfAtmAlcCopDmaHighWatermark_Type.__name__ = "Integer32"
_WfAtmAlcCopDmaHighWatermark_Object = MibTableColumn
wfAtmAlcCopDmaHighWatermark = _WfAtmAlcCopDmaHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 6),
    _WfAtmAlcCopDmaHighWatermark_Type()
)
wfAtmAlcCopDmaHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopDmaHighWatermark.setStatus("mandatory")


class _WfAtmAlcCopDmaLowWatermark_Type(Integer32):
    """Custom type wfAtmAlcCopDmaLowWatermark based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WfAtmAlcCopDmaLowWatermark_Type.__name__ = "Integer32"
_WfAtmAlcCopDmaLowWatermark_Object = MibTableColumn
wfAtmAlcCopDmaLowWatermark = _WfAtmAlcCopDmaLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 7),
    _WfAtmAlcCopDmaLowWatermark_Type()
)
wfAtmAlcCopDmaLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopDmaLowWatermark.setStatus("mandatory")


class _WfAtmAlcCopCacheControl_Type(Integer32):
    """Custom type wfAtmAlcCopCacheControl based on Integer32"""
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
        *(("both", 1),
          ("dcache", 3),
          ("icache", 2),
          ("none", 4))
    )


_WfAtmAlcCopCacheControl_Type.__name__ = "Integer32"
_WfAtmAlcCopCacheControl_Object = MibTableColumn
wfAtmAlcCopCacheControl = _WfAtmAlcCopCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 8),
    _WfAtmAlcCopCacheControl_Type()
)
wfAtmAlcCopCacheControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopCacheControl.setStatus("mandatory")
_WfAtmAlcCopHwModId_Type = Integer32
_WfAtmAlcCopHwModId_Object = MibTableColumn
wfAtmAlcCopHwModId = _WfAtmAlcCopHwModId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 9),
    _WfAtmAlcCopHwModId_Type()
)
wfAtmAlcCopHwModId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopHwModId.setStatus("mandatory")


class _WfAtmAlcCopVcInactTimeout_Type(Integer32):
    """Custom type wfAtmAlcCopVcInactTimeout based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_WfAtmAlcCopVcInactTimeout_Type.__name__ = "Integer32"
_WfAtmAlcCopVcInactTimeout_Object = MibTableColumn
wfAtmAlcCopVcInactTimeout = _WfAtmAlcCopVcInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 3, 1, 10),
    _WfAtmAlcCopVcInactTimeout_Type()
)
wfAtmAlcCopVcInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcCopVcInactTimeout.setStatus("mandatory")
_WfAtmAlcCopHwTable_Object = MibTable
wfAtmAlcCopHwTable = _WfAtmAlcCopHwTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4)
)
if mibBuilder.loadTexts:
    wfAtmAlcCopHwTable.setStatus("mandatory")
_WfAtmAlcCopHwEntry_Object = MibTableRow
wfAtmAlcCopHwEntry = _WfAtmAlcCopHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1)
)
wfAtmAlcCopHwEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcCopHwIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcCopHwEntry.setStatus("mandatory")
_WfAtmAlcCopHwIndex_Type = Integer32
_WfAtmAlcCopHwIndex_Object = MibTableColumn
wfAtmAlcCopHwIndex = _WfAtmAlcCopHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 1),
    _WfAtmAlcCopHwIndex_Type()
)
wfAtmAlcCopHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopHwIndex.setStatus("mandatory")


class _WfAtmAlcCopType_Type(Integer32):
    """Custom type wfAtmAlcCopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("m68040", 1),
          ("m68060", 2))
    )


_WfAtmAlcCopType_Type.__name__ = "Integer32"
_WfAtmAlcCopType_Object = MibTableColumn
wfAtmAlcCopType = _WfAtmAlcCopType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 2),
    _WfAtmAlcCopType_Type()
)
wfAtmAlcCopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopType.setStatus("mandatory")
_WfAtmAlcCopPktMemSize_Type = Integer32
_WfAtmAlcCopPktMemSize_Object = MibTableColumn
wfAtmAlcCopPktMemSize = _WfAtmAlcCopPktMemSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 3),
    _WfAtmAlcCopPktMemSize_Type()
)
wfAtmAlcCopPktMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopPktMemSize.setStatus("mandatory")
_WfAtmAlcCopCtlMemSize_Type = Integer32
_WfAtmAlcCopCtlMemSize_Object = MibTableColumn
wfAtmAlcCopCtlMemSize = _WfAtmAlcCopCtlMemSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 4),
    _WfAtmAlcCopCtlMemSize_Type()
)
wfAtmAlcCopCtlMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopCtlMemSize.setStatus("mandatory")
_WfAtmAlcCopInsMemSize_Type = Integer32
_WfAtmAlcCopInsMemSize_Object = MibTableColumn
wfAtmAlcCopInsMemSize = _WfAtmAlcCopInsMemSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 5),
    _WfAtmAlcCopInsMemSize_Type()
)
wfAtmAlcCopInsMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopInsMemSize.setStatus("mandatory")
_WfAtmAlcCopAlcClockSpeed_Type = Integer32
_WfAtmAlcCopAlcClockSpeed_Object = MibTableColumn
wfAtmAlcCopAlcClockSpeed = _WfAtmAlcCopAlcClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 6),
    _WfAtmAlcCopAlcClockSpeed_Type()
)
wfAtmAlcCopAlcClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopAlcClockSpeed.setStatus("mandatory")
_WfAtmAlcCopAlcVersion_Type = Integer32
_WfAtmAlcCopAlcVersion_Object = MibTableColumn
wfAtmAlcCopAlcVersion = _WfAtmAlcCopAlcVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 7),
    _WfAtmAlcCopAlcVersion_Type()
)
wfAtmAlcCopAlcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopAlcVersion.setStatus("mandatory")
_WfAtmAlcCopNtcVersion_Type = Integer32
_WfAtmAlcCopNtcVersion_Object = MibTableColumn
wfAtmAlcCopNtcVersion = _WfAtmAlcCopNtcVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 8),
    _WfAtmAlcCopNtcVersion_Type()
)
wfAtmAlcCopNtcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopNtcVersion.setStatus("mandatory")
_WfAtmAlcCopAtcVersion_Type = Integer32
_WfAtmAlcCopAtcVersion_Object = MibTableColumn
wfAtmAlcCopAtcVersion = _WfAtmAlcCopAtcVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 4, 1, 9),
    _WfAtmAlcCopAtcVersion_Type()
)
wfAtmAlcCopAtcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopAtcVersion.setStatus("mandatory")
_WfAtmAlcCopInfoTable_Object = MibTable
wfAtmAlcCopInfoTable = _WfAtmAlcCopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5)
)
if mibBuilder.loadTexts:
    wfAtmAlcCopInfoTable.setStatus("mandatory")
_WfAtmAlcCopInfoEntry_Object = MibTableRow
wfAtmAlcCopInfoEntry = _WfAtmAlcCopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1)
)
wfAtmAlcCopInfoEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcCopInfoIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcCopInfoEntry.setStatus("mandatory")
_WfAtmAlcCopInfoIndex_Type = Integer32
_WfAtmAlcCopInfoIndex_Object = MibTableColumn
wfAtmAlcCopInfoIndex = _WfAtmAlcCopInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1, 1),
    _WfAtmAlcCopInfoIndex_Type()
)
wfAtmAlcCopInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopInfoIndex.setStatus("mandatory")


class _WfAtmAlcCopState_Type(Integer32):
    """Custom type wfAtmAlcCopState based on Integer32"""
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
        *(("config", 4),
          ("init", 3),
          ("nonoperational", 2),
          ("operational", 1))
    )


_WfAtmAlcCopState_Type.__name__ = "Integer32"
_WfAtmAlcCopState_Object = MibTableColumn
wfAtmAlcCopState = _WfAtmAlcCopState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1, 2),
    _WfAtmAlcCopState_Type()
)
wfAtmAlcCopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopState.setStatus("mandatory")


class _WfAtmAlcCopConfigState_Type(Integer32):
    """Custom type wfAtmAlcCopConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4095)
        )
    )
    namedValues = NamedValues(
        *(("dma", 1),
          ("done", 4095),
          ("frmcsi", 1024),
          ("frmdma", 2048),
          ("frmgen", 32),
          ("frmoam", 256),
          ("frmrcv", 64),
          ("frmstats", 512),
          ("frmxmt", 128),
          ("sar", 2),
          ("sarpcrq", 8),
          ("sarscrq", 16),
          ("sartraf", 4))
    )


_WfAtmAlcCopConfigState_Type.__name__ = "Integer32"
_WfAtmAlcCopConfigState_Object = MibTableColumn
wfAtmAlcCopConfigState = _WfAtmAlcCopConfigState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1, 3),
    _WfAtmAlcCopConfigState_Type()
)
wfAtmAlcCopConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopConfigState.setStatus("mandatory")
_WfAtmAlcCopTotalBufs_Type = Integer32
_WfAtmAlcCopTotalBufs_Object = MibTableColumn
wfAtmAlcCopTotalBufs = _WfAtmAlcCopTotalBufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1, 4),
    _WfAtmAlcCopTotalBufs_Type()
)
wfAtmAlcCopTotalBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopTotalBufs.setStatus("mandatory")
_WfAtmAlcCopTotalXmtBufs_Type = Integer32
_WfAtmAlcCopTotalXmtBufs_Object = MibTableColumn
wfAtmAlcCopTotalXmtBufs = _WfAtmAlcCopTotalXmtBufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1, 5),
    _WfAtmAlcCopTotalXmtBufs_Type()
)
wfAtmAlcCopTotalXmtBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopTotalXmtBufs.setStatus("mandatory")
_WfAtmAlcCopTotalRcvBufs_Type = Integer32
_WfAtmAlcCopTotalRcvBufs_Object = MibTableColumn
wfAtmAlcCopTotalRcvBufs = _WfAtmAlcCopTotalRcvBufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 5, 1, 6),
    _WfAtmAlcCopTotalRcvBufs_Type()
)
wfAtmAlcCopTotalRcvBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopTotalRcvBufs.setStatus("mandatory")
_WfAtmAlcCopDataPathTable_Object = MibTable
wfAtmAlcCopDataPathTable = _WfAtmAlcCopDataPathTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6)
)
if mibBuilder.loadTexts:
    wfAtmAlcCopDataPathTable.setStatus("mandatory")
_WfAtmAlcCopDataPathEntry_Object = MibTableRow
wfAtmAlcCopDataPathEntry = _WfAtmAlcCopDataPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1)
)
wfAtmAlcCopDataPathEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcCopDataPathIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcCopDataPathEntry.setStatus("mandatory")
_WfAtmAlcCopDataPathIndex_Type = Integer32
_WfAtmAlcCopDataPathIndex_Object = MibTableColumn
wfAtmAlcCopDataPathIndex = _WfAtmAlcCopDataPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 1),
    _WfAtmAlcCopDataPathIndex_Type()
)
wfAtmAlcCopDataPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopDataPathIndex.setStatus("mandatory")
_WfAtmAlcCopXmtPackets_Type = Counter32
_WfAtmAlcCopXmtPackets_Object = MibTableColumn
wfAtmAlcCopXmtPackets = _WfAtmAlcCopXmtPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 2),
    _WfAtmAlcCopXmtPackets_Type()
)
wfAtmAlcCopXmtPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtPackets.setStatus("mandatory")
_WfAtmAlcCopXmtBuffers_Type = Counter32
_WfAtmAlcCopXmtBuffers_Object = MibTableColumn
wfAtmAlcCopXmtBuffers = _WfAtmAlcCopXmtBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 3),
    _WfAtmAlcCopXmtBuffers_Type()
)
wfAtmAlcCopXmtBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtBuffers.setStatus("mandatory")
_WfAtmAlcCopXmtErrBuffers_Type = Counter32
_WfAtmAlcCopXmtErrBuffers_Object = MibTableColumn
wfAtmAlcCopXmtErrBuffers = _WfAtmAlcCopXmtErrBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 4),
    _WfAtmAlcCopXmtErrBuffers_Type()
)
wfAtmAlcCopXmtErrBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtErrBuffers.setStatus("mandatory")
_WfAtmAlcCopXmtCells_Type = OctetString
_WfAtmAlcCopXmtCells_Object = MibTableColumn
wfAtmAlcCopXmtCells = _WfAtmAlcCopXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 5),
    _WfAtmAlcCopXmtCells_Type()
)
wfAtmAlcCopXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtCells.setStatus("mandatory")
_WfAtmAlcCopXmtUnassCells_Type = Counter32
_WfAtmAlcCopXmtUnassCells_Object = MibTableColumn
wfAtmAlcCopXmtUnassCells = _WfAtmAlcCopXmtUnassCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 6),
    _WfAtmAlcCopXmtUnassCells_Type()
)
wfAtmAlcCopXmtUnassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtUnassCells.setStatus("mandatory")
_WfAtmAlcCopXmtIdleCells_Type = Counter32
_WfAtmAlcCopXmtIdleCells_Object = MibTableColumn
wfAtmAlcCopXmtIdleCells = _WfAtmAlcCopXmtIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 7),
    _WfAtmAlcCopXmtIdleCells_Type()
)
wfAtmAlcCopXmtIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtIdleCells.setStatus("mandatory")
_WfAtmAlcCopXmtUserCells_Type = Counter32
_WfAtmAlcCopXmtUserCells_Object = MibTableColumn
wfAtmAlcCopXmtUserCells = _WfAtmAlcCopXmtUserCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 8),
    _WfAtmAlcCopXmtUserCells_Type()
)
wfAtmAlcCopXmtUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtUserCells.setStatus("mandatory")
_WfAtmAlcCopXmtOctets_Type = Counter32
_WfAtmAlcCopXmtOctets_Object = MibTableColumn
wfAtmAlcCopXmtOctets = _WfAtmAlcCopXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 9),
    _WfAtmAlcCopXmtOctets_Type()
)
wfAtmAlcCopXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtOctets.setStatus("mandatory")
_WfAtmAlcCopRcvPackets_Type = Counter32
_WfAtmAlcCopRcvPackets_Object = MibTableColumn
wfAtmAlcCopRcvPackets = _WfAtmAlcCopRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 10),
    _WfAtmAlcCopRcvPackets_Type()
)
wfAtmAlcCopRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvPackets.setStatus("mandatory")
_WfAtmAlcCopRcvClipPackets_Type = Counter32
_WfAtmAlcCopRcvClipPackets_Object = MibTableColumn
wfAtmAlcCopRcvClipPackets = _WfAtmAlcCopRcvClipPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 11),
    _WfAtmAlcCopRcvClipPackets_Type()
)
wfAtmAlcCopRcvClipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvClipPackets.setStatus("mandatory")
_WfAtmAlcCopRcvBuffers_Type = Counter32
_WfAtmAlcCopRcvBuffers_Object = MibTableColumn
wfAtmAlcCopRcvBuffers = _WfAtmAlcCopRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 12),
    _WfAtmAlcCopRcvBuffers_Type()
)
wfAtmAlcCopRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvBuffers.setStatus("mandatory")
_WfAtmAlcCopRcvErrBuffers_Type = Counter32
_WfAtmAlcCopRcvErrBuffers_Object = MibTableColumn
wfAtmAlcCopRcvErrBuffers = _WfAtmAlcCopRcvErrBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 13),
    _WfAtmAlcCopRcvErrBuffers_Type()
)
wfAtmAlcCopRcvErrBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvErrBuffers.setStatus("mandatory")
_WfAtmAlcCopRcvClipBuffers_Type = Counter32
_WfAtmAlcCopRcvClipBuffers_Object = MibTableColumn
wfAtmAlcCopRcvClipBuffers = _WfAtmAlcCopRcvClipBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 14),
    _WfAtmAlcCopRcvClipBuffers_Type()
)
wfAtmAlcCopRcvClipBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvClipBuffers.setStatus("mandatory")
_WfAtmAlcCopRcvSarDropBuffers_Type = Counter32
_WfAtmAlcCopRcvSarDropBuffers_Object = MibTableColumn
wfAtmAlcCopRcvSarDropBuffers = _WfAtmAlcCopRcvSarDropBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 15),
    _WfAtmAlcCopRcvSarDropBuffers_Type()
)
wfAtmAlcCopRcvSarDropBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvSarDropBuffers.setStatus("mandatory")
_WfAtmAlcCopRcvCells_Type = OctetString
_WfAtmAlcCopRcvCells_Object = MibTableColumn
wfAtmAlcCopRcvCells = _WfAtmAlcCopRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 16),
    _WfAtmAlcCopRcvCells_Type()
)
wfAtmAlcCopRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvCells.setStatus("mandatory")
_WfAtmAlcCopRcvDropCells_Type = Counter32
_WfAtmAlcCopRcvDropCells_Object = MibTableColumn
wfAtmAlcCopRcvDropCells = _WfAtmAlcCopRcvDropCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 17),
    _WfAtmAlcCopRcvDropCells_Type()
)
wfAtmAlcCopRcvDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvDropCells.setStatus("mandatory")
_WfAtmAlcCopRcvUnassCells_Type = Counter32
_WfAtmAlcCopRcvUnassCells_Object = MibTableColumn
wfAtmAlcCopRcvUnassCells = _WfAtmAlcCopRcvUnassCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 18),
    _WfAtmAlcCopRcvUnassCells_Type()
)
wfAtmAlcCopRcvUnassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvUnassCells.setStatus("mandatory")
_WfAtmAlcCopRcvIdleCells_Type = Counter32
_WfAtmAlcCopRcvIdleCells_Object = MibTableColumn
wfAtmAlcCopRcvIdleCells = _WfAtmAlcCopRcvIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 19),
    _WfAtmAlcCopRcvIdleCells_Type()
)
wfAtmAlcCopRcvIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvIdleCells.setStatus("mandatory")
_WfAtmAlcCopRcvUserCells_Type = Counter32
_WfAtmAlcCopRcvUserCells_Object = MibTableColumn
wfAtmAlcCopRcvUserCells = _WfAtmAlcCopRcvUserCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 20),
    _WfAtmAlcCopRcvUserCells_Type()
)
wfAtmAlcCopRcvUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvUserCells.setStatus("mandatory")
_WfAtmAlcCopRcvSarDropCells_Type = Counter32
_WfAtmAlcCopRcvSarDropCells_Object = MibTableColumn
wfAtmAlcCopRcvSarDropCells = _WfAtmAlcCopRcvSarDropCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 21),
    _WfAtmAlcCopRcvSarDropCells_Type()
)
wfAtmAlcCopRcvSarDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvSarDropCells.setStatus("mandatory")
_WfAtmAlcCopRcvOctets_Type = Counter32
_WfAtmAlcCopRcvOctets_Object = MibTableColumn
wfAtmAlcCopRcvOctets = _WfAtmAlcCopRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 22),
    _WfAtmAlcCopRcvOctets_Type()
)
wfAtmAlcCopRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvOctets.setStatus("mandatory")
_WfAtmAlcCopXmtOamCells_Type = Counter32
_WfAtmAlcCopXmtOamCells_Object = MibTableColumn
wfAtmAlcCopXmtOamCells = _WfAtmAlcCopXmtOamCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 23),
    _WfAtmAlcCopXmtOamCells_Type()
)
wfAtmAlcCopXmtOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtOamCells.setStatus("mandatory")
_WfAtmAlcCopRcvOamCells_Type = Counter32
_WfAtmAlcCopRcvOamCells_Object = MibTableColumn
wfAtmAlcCopRcvOamCells = _WfAtmAlcCopRcvOamCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 24),
    _WfAtmAlcCopRcvOamCells_Type()
)
wfAtmAlcCopRcvOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvOamCells.setStatus("mandatory")
_WfAtmAlcCopRcvOamCrcErrs_Type = Counter32
_WfAtmAlcCopRcvOamCrcErrs_Object = MibTableColumn
wfAtmAlcCopRcvOamCrcErrs = _WfAtmAlcCopRcvOamCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 6, 1, 25),
    _WfAtmAlcCopRcvOamCrcErrs_Type()
)
wfAtmAlcCopRcvOamCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvOamCrcErrs.setStatus("mandatory")
_WfAtmAlcCopErrorTable_Object = MibTable
wfAtmAlcCopErrorTable = _WfAtmAlcCopErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7)
)
if mibBuilder.loadTexts:
    wfAtmAlcCopErrorTable.setStatus("mandatory")
_WfAtmAlcCopErrorEntry_Object = MibTableRow
wfAtmAlcCopErrorEntry = _WfAtmAlcCopErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1)
)
wfAtmAlcCopErrorEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcCopErrorIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcCopErrorEntry.setStatus("mandatory")
_WfAtmAlcCopErrorIndex_Type = Integer32
_WfAtmAlcCopErrorIndex_Object = MibTableColumn
wfAtmAlcCopErrorIndex = _WfAtmAlcCopErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 1),
    _WfAtmAlcCopErrorIndex_Type()
)
wfAtmAlcCopErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopErrorIndex.setStatus("mandatory")
_WfAtmAlcCopHecDetects_Type = Counter32
_WfAtmAlcCopHecDetects_Object = MibTableColumn
wfAtmAlcCopHecDetects = _WfAtmAlcCopHecDetects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 2),
    _WfAtmAlcCopHecDetects_Type()
)
wfAtmAlcCopHecDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopHecDetects.setStatus("mandatory")
_WfAtmAlcCopHecCorrects_Type = Counter32
_WfAtmAlcCopHecCorrects_Object = MibTableColumn
wfAtmAlcCopHecCorrects = _WfAtmAlcCopHecCorrects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 3),
    _WfAtmAlcCopHecCorrects_Type()
)
wfAtmAlcCopHecCorrects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopHecCorrects.setStatus("mandatory")
_WfAtmAlcCopB2Febes_Type = Counter32
_WfAtmAlcCopB2Febes_Object = MibTableColumn
wfAtmAlcCopB2Febes = _WfAtmAlcCopB2Febes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 4),
    _WfAtmAlcCopB2Febes_Type()
)
wfAtmAlcCopB2Febes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopB2Febes.setStatus("mandatory")
_WfAtmAlcCopB3Febes_Type = Counter32
_WfAtmAlcCopB3Febes_Object = MibTableColumn
wfAtmAlcCopB3Febes = _WfAtmAlcCopB3Febes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 5),
    _WfAtmAlcCopB3Febes_Type()
)
wfAtmAlcCopB3Febes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopB3Febes.setStatus("mandatory")
_WfAtmAlcCopF1Febes_Type = Counter32
_WfAtmAlcCopF1Febes_Object = MibTableColumn
wfAtmAlcCopF1Febes = _WfAtmAlcCopF1Febes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 6),
    _WfAtmAlcCopF1Febes_Type()
)
wfAtmAlcCopF1Febes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopF1Febes.setStatus("mandatory")
_WfAtmAlcCopF3Febes_Type = Counter32
_WfAtmAlcCopF3Febes_Object = MibTableColumn
wfAtmAlcCopF3Febes = _WfAtmAlcCopF3Febes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 7),
    _WfAtmAlcCopF3Febes_Type()
)
wfAtmAlcCopF3Febes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopF3Febes.setStatus("mandatory")
_WfAtmAlcCopG1Febes_Type = Counter32
_WfAtmAlcCopG1Febes_Object = MibTableColumn
wfAtmAlcCopG1Febes = _WfAtmAlcCopG1Febes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 8),
    _WfAtmAlcCopG1Febes_Type()
)
wfAtmAlcCopG1Febes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopG1Febes.setStatus("mandatory")
_WfAtmAlcCopDropIntqEvents_Type = Counter32
_WfAtmAlcCopDropIntqEvents_Object = MibTableColumn
wfAtmAlcCopDropIntqEvents = _WfAtmAlcCopDropIntqEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 9),
    _WfAtmAlcCopDropIntqEvents_Type()
)
wfAtmAlcCopDropIntqEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopDropIntqEvents.setStatus("mandatory")
_WfAtmAlcCopDropLogqEvents_Type = Counter32
_WfAtmAlcCopDropLogqEvents_Object = MibTableColumn
wfAtmAlcCopDropLogqEvents = _WfAtmAlcCopDropLogqEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 10),
    _WfAtmAlcCopDropLogqEvents_Type()
)
wfAtmAlcCopDropLogqEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopDropLogqEvents.setStatus("mandatory")
_WfAtmAlcCopDmaFifoOverruns_Type = Counter32
_WfAtmAlcCopDmaFifoOverruns_Object = MibTableColumn
wfAtmAlcCopDmaFifoOverruns = _WfAtmAlcCopDmaFifoOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 11),
    _WfAtmAlcCopDmaFifoOverruns_Type()
)
wfAtmAlcCopDmaFifoOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopDmaFifoOverruns.setStatus("mandatory")
_WfAtmAlcCopDmaFifoUnderruns_Type = Counter32
_WfAtmAlcCopDmaFifoUnderruns_Object = MibTableColumn
wfAtmAlcCopDmaFifoUnderruns = _WfAtmAlcCopDmaFifoUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 12),
    _WfAtmAlcCopDmaFifoUnderruns_Type()
)
wfAtmAlcCopDmaFifoUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopDmaFifoUnderruns.setStatus("mandatory")
_WfAtmAlcCopLossSignals_Type = Counter32
_WfAtmAlcCopLossSignals_Object = MibTableColumn
wfAtmAlcCopLossSignals = _WfAtmAlcCopLossSignals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 13),
    _WfAtmAlcCopLossSignals_Type()
)
wfAtmAlcCopLossSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopLossSignals.setStatus("mandatory")
_WfAtmAlcCopLossFrames_Type = Counter32
_WfAtmAlcCopLossFrames_Object = MibTableColumn
wfAtmAlcCopLossFrames = _WfAtmAlcCopLossFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 14),
    _WfAtmAlcCopLossFrames_Type()
)
wfAtmAlcCopLossFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopLossFrames.setStatus("mandatory")
_WfAtmAlcCopLossPointers_Type = Counter32
_WfAtmAlcCopLossPointers_Object = MibTableColumn
wfAtmAlcCopLossPointers = _WfAtmAlcCopLossPointers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 15),
    _WfAtmAlcCopLossPointers_Type()
)
wfAtmAlcCopLossPointers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopLossPointers.setStatus("mandatory")
_WfAtmAlcCopOutCellDelins_Type = Counter32
_WfAtmAlcCopOutCellDelins_Object = MibTableColumn
wfAtmAlcCopOutCellDelins = _WfAtmAlcCopOutCellDelins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 16),
    _WfAtmAlcCopOutCellDelins_Type()
)
wfAtmAlcCopOutCellDelins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopOutCellDelins.setStatus("mandatory")
_WfAtmAlcCopInCellDelins_Type = Counter32
_WfAtmAlcCopInCellDelins_Object = MibTableColumn
wfAtmAlcCopInCellDelins = _WfAtmAlcCopInCellDelins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 17),
    _WfAtmAlcCopInCellDelins_Type()
)
wfAtmAlcCopInCellDelins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopInCellDelins.setStatus("mandatory")
_WfAtmAlcCopBufOverflows_Type = Counter32
_WfAtmAlcCopBufOverflows_Object = MibTableColumn
wfAtmAlcCopBufOverflows = _WfAtmAlcCopBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 18),
    _WfAtmAlcCopBufOverflows_Type()
)
wfAtmAlcCopBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopBufOverflows.setStatus("mandatory")
_WfAtmAlcCopXmtQueueFulls_Type = Counter32
_WfAtmAlcCopXmtQueueFulls_Object = MibTableColumn
wfAtmAlcCopXmtQueueFulls = _WfAtmAlcCopXmtQueueFulls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 19),
    _WfAtmAlcCopXmtQueueFulls_Type()
)
wfAtmAlcCopXmtQueueFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtQueueFulls.setStatus("mandatory")
_WfAtmAlcCopXmtAtes_Type = Counter32
_WfAtmAlcCopXmtAtes_Object = MibTableColumn
wfAtmAlcCopXmtAtes = _WfAtmAlcCopXmtAtes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 20),
    _WfAtmAlcCopXmtAtes_Type()
)
wfAtmAlcCopXmtAtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopXmtAtes.setStatus("mandatory")
_WfAtmAlcCopRcvQueueEmptys_Type = Counter32
_WfAtmAlcCopRcvQueueEmptys_Object = MibTableColumn
wfAtmAlcCopRcvQueueEmptys = _WfAtmAlcCopRcvQueueEmptys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 21),
    _WfAtmAlcCopRcvQueueEmptys_Type()
)
wfAtmAlcCopRcvQueueEmptys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvQueueEmptys.setStatus("mandatory")
_WfAtmAlcCopRcvWriteFails_Type = Counter32
_WfAtmAlcCopRcvWriteFails_Object = MibTableColumn
wfAtmAlcCopRcvWriteFails = _WfAtmAlcCopRcvWriteFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 22),
    _WfAtmAlcCopRcvWriteFails_Type()
)
wfAtmAlcCopRcvWriteFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvWriteFails.setStatus("mandatory")
_WfAtmAlcCopRcvQueueFulls_Type = Counter32
_WfAtmAlcCopRcvQueueFulls_Object = MibTableColumn
wfAtmAlcCopRcvQueueFulls = _WfAtmAlcCopRcvQueueFulls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 23),
    _WfAtmAlcCopRcvQueueFulls_Type()
)
wfAtmAlcCopRcvQueueFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvQueueFulls.setStatus("mandatory")
_WfAtmAlcCopRcvAtes_Type = Counter32
_WfAtmAlcCopRcvAtes_Object = MibTableColumn
wfAtmAlcCopRcvAtes = _WfAtmAlcCopRcvAtes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 7, 1, 24),
    _WfAtmAlcCopRcvAtes_Type()
)
wfAtmAlcCopRcvAtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcCopRcvAtes.setStatus("mandatory")
_WfAtmAlcSarConfTable_Object = MibTable
wfAtmAlcSarConfTable = _WfAtmAlcSarConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8)
)
if mibBuilder.loadTexts:
    wfAtmAlcSarConfTable.setStatus("mandatory")
_WfAtmAlcSarConfEntry_Object = MibTableRow
wfAtmAlcSarConfEntry = _WfAtmAlcSarConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1)
)
wfAtmAlcSarConfEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcSarConfIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcSarConfEntry.setStatus("mandatory")


class _WfAtmAlcSarConfDelete_Type(Integer32):
    """Custom type wfAtmAlcSarConfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmAlcSarConfDelete_Type.__name__ = "Integer32"
_WfAtmAlcSarConfDelete_Object = MibTableColumn
wfAtmAlcSarConfDelete = _WfAtmAlcSarConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 1),
    _WfAtmAlcSarConfDelete_Type()
)
wfAtmAlcSarConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarConfDelete.setStatus("mandatory")
_WfAtmAlcSarConfIndex_Type = Integer32
_WfAtmAlcSarConfIndex_Object = MibTableColumn
wfAtmAlcSarConfIndex = _WfAtmAlcSarConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 2),
    _WfAtmAlcSarConfIndex_Type()
)
wfAtmAlcSarConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarConfIndex.setStatus("mandatory")


class _WfAtmAlcSarDmaBurstLength_Type(Integer32):
    """Custom type wfAtmAlcSarDmaBurstLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WfAtmAlcSarDmaBurstLength_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaBurstLength_Object = MibTableColumn
wfAtmAlcSarDmaBurstLength = _WfAtmAlcSarDmaBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 3),
    _WfAtmAlcSarDmaBurstLength_Type()
)
wfAtmAlcSarDmaBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaBurstLength.setStatus("mandatory")


class _WfAtmAlcSarDmaModeBw_Type(Integer32):
    """Custom type wfAtmAlcSarDmaModeBw based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bit32", 1),
          ("bit64", 2))
    )


_WfAtmAlcSarDmaModeBw_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaModeBw_Object = MibTableColumn
wfAtmAlcSarDmaModeBw = _WfAtmAlcSarDmaModeBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 4),
    _WfAtmAlcSarDmaModeBw_Type()
)
wfAtmAlcSarDmaModeBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaModeBw.setStatus("mandatory")


class _WfAtmAlcSarDmaModeBmode_Type(Integer32):
    """Custom type wfAtmAlcSarDmaModeBmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intel", 1),
          ("motorola", 2))
    )


_WfAtmAlcSarDmaModeBmode_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaModeBmode_Object = MibTableColumn
wfAtmAlcSarDmaModeBmode = _WfAtmAlcSarDmaModeBmode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 5),
    _WfAtmAlcSarDmaModeBmode_Type()
)
wfAtmAlcSarDmaModeBmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaModeBmode.setStatus("mandatory")


class _WfAtmAlcSarDmaModeOrder_Type(Integer32):
    """Custom type wfAtmAlcSarDmaModeOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bigendian", 1),
          ("littleendian", 2))
    )


_WfAtmAlcSarDmaModeOrder_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaModeOrder_Object = MibTableColumn
wfAtmAlcSarDmaModeOrder = _WfAtmAlcSarDmaModeOrder_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 6),
    _WfAtmAlcSarDmaModeOrder_Type()
)
wfAtmAlcSarDmaModeOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaModeOrder.setStatus("mandatory")


class _WfAtmAlcSarDmaModeMmode_Type(Integer32):
    """Custom type wfAtmAlcSarDmaModeMmode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ram", 2),
          ("system", 1))
    )


_WfAtmAlcSarDmaModeMmode_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaModeMmode_Object = MibTableColumn
wfAtmAlcSarDmaModeMmode = _WfAtmAlcSarDmaModeMmode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 7),
    _WfAtmAlcSarDmaModeMmode_Type()
)
wfAtmAlcSarDmaModeMmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaModeMmode.setStatus("mandatory")


class _WfAtmAlcSarDmaModeCmode_Type(Integer32):
    """Custom type wfAtmAlcSarDmaModeCmode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("standard", 1))
    )


_WfAtmAlcSarDmaModeCmode_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaModeCmode_Object = MibTableColumn
wfAtmAlcSarDmaModeCmode = _WfAtmAlcSarDmaModeCmode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 8),
    _WfAtmAlcSarDmaModeCmode_Type()
)
wfAtmAlcSarDmaModeCmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaModeCmode.setStatus("mandatory")


class _WfAtmAlcSarDmaModeSync_Type(Integer32):
    """Custom type wfAtmAlcSarDmaModeSync based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sync", 2))
    )


_WfAtmAlcSarDmaModeSync_Type.__name__ = "Integer32"
_WfAtmAlcSarDmaModeSync_Object = MibTableColumn
wfAtmAlcSarDmaModeSync = _WfAtmAlcSarDmaModeSync_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 9),
    _WfAtmAlcSarDmaModeSync_Type()
)
wfAtmAlcSarDmaModeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarDmaModeSync.setStatus("mandatory")


class _WfAtmAlcSarControlRif_Type(Integer32):
    """Custom type wfAtmAlcSarControlRif based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one", 1)
    )


_WfAtmAlcSarControlRif_Type.__name__ = "Integer32"
_WfAtmAlcSarControlRif_Object = MibTableColumn
wfAtmAlcSarControlRif = _WfAtmAlcSarControlRif_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 10),
    _WfAtmAlcSarControlRif_Type()
)
wfAtmAlcSarControlRif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarControlRif.setStatus("mandatory")


class _WfAtmAlcSarControlLoop_Type(Integer32):
    """Custom type wfAtmAlcSarControlLoop based on Integer32"""
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


_WfAtmAlcSarControlLoop_Type.__name__ = "Integer32"
_WfAtmAlcSarControlLoop_Object = MibTableColumn
wfAtmAlcSarControlLoop = _WfAtmAlcSarControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 11),
    _WfAtmAlcSarControlLoop_Type()
)
wfAtmAlcSarControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarControlLoop.setStatus("mandatory")


class _WfAtmAlcSarModeRtmr_Type(Integer32):
    """Custom type wfAtmAlcSarModeRtmr based on Integer32"""
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
        *(("notag", 1),
          ("oneoctettag", 2),
          ("threeoctettag", 4),
          ("twooctettag", 3))
    )


_WfAtmAlcSarModeRtmr_Type.__name__ = "Integer32"
_WfAtmAlcSarModeRtmr_Object = MibTableColumn
wfAtmAlcSarModeRtmr = _WfAtmAlcSarModeRtmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 12),
    _WfAtmAlcSarModeRtmr_Type()
)
wfAtmAlcSarModeRtmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeRtmr.setStatus("mandatory")


class _WfAtmAlcSarModeRid_Type(Integer32):
    """Custom type wfAtmAlcSarModeRid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mid", 2),
          ("vci", 1))
    )


_WfAtmAlcSarModeRid_Type.__name__ = "Integer32"
_WfAtmAlcSarModeRid_Object = MibTableColumn
wfAtmAlcSarModeRid = _WfAtmAlcSarModeRid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 13),
    _WfAtmAlcSarModeRid_Type()
)
wfAtmAlcSarModeRid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeRid.setStatus("mandatory")


class _WfAtmAlcSarModeAal_Type(Integer32):
    """Custom type wfAtmAlcSarModeAal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_WfAtmAlcSarModeAal_Type.__name__ = "Integer32"
_WfAtmAlcSarModeAal_Object = MibTableColumn
wfAtmAlcSarModeAal = _WfAtmAlcSarModeAal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 14),
    _WfAtmAlcSarModeAal_Type()
)
wfAtmAlcSarModeAal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeAal.setStatus("mandatory")


class _WfAtmAlcSarModeDmask_Type(Integer32):
    """Custom type wfAtmAlcSarModeDmask based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcSarModeDmask_Type.__name__ = "Integer32"
_WfAtmAlcSarModeDmask_Object = MibTableColumn
wfAtmAlcSarModeDmask = _WfAtmAlcSarModeDmask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 15),
    _WfAtmAlcSarModeDmask_Type()
)
wfAtmAlcSarModeDmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeDmask.setStatus("mandatory")


class _WfAtmAlcSarModeDchain_Type(Integer32):
    """Custom type wfAtmAlcSarModeDchain based on Integer32"""
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


_WfAtmAlcSarModeDchain_Type.__name__ = "Integer32"
_WfAtmAlcSarModeDchain_Object = MibTableColumn
wfAtmAlcSarModeDchain = _WfAtmAlcSarModeDchain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 16),
    _WfAtmAlcSarModeDchain_Type()
)
wfAtmAlcSarModeDchain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeDchain.setStatus("mandatory")


class _WfAtmAlcSarModeSmode_Type(Integer32):
    """Custom type wfAtmAlcSarModeSmode based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcSarModeSmode_Type.__name__ = "Integer32"
_WfAtmAlcSarModeSmode_Object = MibTableColumn
wfAtmAlcSarModeSmode = _WfAtmAlcSarModeSmode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 17),
    _WfAtmAlcSarModeSmode_Type()
)
wfAtmAlcSarModeSmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeSmode.setStatus("mandatory")


class _WfAtmAlcSarModeBchain_Type(Integer32):
    """Custom type wfAtmAlcSarModeBchain based on Integer32"""
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


_WfAtmAlcSarModeBchain_Type.__name__ = "Integer32"
_WfAtmAlcSarModeBchain_Object = MibTableColumn
wfAtmAlcSarModeBchain = _WfAtmAlcSarModeBchain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 18),
    _WfAtmAlcSarModeBchain_Type()
)
wfAtmAlcSarModeBchain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeBchain.setStatus("mandatory")


class _WfAtmAlcSarModeHec_Type(Integer32):
    """Custom type wfAtmAlcSarModeHec based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcSarModeHec_Type.__name__ = "Integer32"
_WfAtmAlcSarModeHec_Object = MibTableColumn
wfAtmAlcSarModeHec = _WfAtmAlcSarModeHec_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 19),
    _WfAtmAlcSarModeHec_Type()
)
wfAtmAlcSarModeHec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeHec.setStatus("mandatory")


class _WfAtmAlcSarModeVpf_Type(Integer32):
    """Custom type wfAtmAlcSarModeVpf based on Integer32"""
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


_WfAtmAlcSarModeVpf_Type.__name__ = "Integer32"
_WfAtmAlcSarModeVpf_Object = MibTableColumn
wfAtmAlcSarModeVpf = _WfAtmAlcSarModeVpf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 20),
    _WfAtmAlcSarModeVpf_Type()
)
wfAtmAlcSarModeVpf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeVpf.setStatus("mandatory")


class _WfAtmAlcSarModeBas_Type(Integer32):
    """Custom type wfAtmAlcSarModeBas based on Integer32"""
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


_WfAtmAlcSarModeBas_Type.__name__ = "Integer32"
_WfAtmAlcSarModeBas_Object = MibTableColumn
wfAtmAlcSarModeBas = _WfAtmAlcSarModeBas_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 21),
    _WfAtmAlcSarModeBas_Type()
)
wfAtmAlcSarModeBas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeBas.setStatus("mandatory")


class _WfAtmAlcSarModeAm_Type(Integer32):
    """Custom type wfAtmAlcSarModeAm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("burst", 2),
          ("trickle", 1))
    )


_WfAtmAlcSarModeAm_Type.__name__ = "Integer32"
_WfAtmAlcSarModeAm_Object = MibTableColumn
wfAtmAlcSarModeAm = _WfAtmAlcSarModeAm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 22),
    _WfAtmAlcSarModeAm_Type()
)
wfAtmAlcSarModeAm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeAm.setStatus("mandatory")


class _WfAtmAlcSarModeTrtl_Type(Integer32):
    """Custom type wfAtmAlcSarModeTrtl based on Integer32"""
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
        *(("notag", 1),
          ("oneoctettag", 2),
          ("threeoctettag", 4),
          ("twooctettag", 3))
    )


_WfAtmAlcSarModeTrtl_Type.__name__ = "Integer32"
_WfAtmAlcSarModeTrtl_Object = MibTableColumn
wfAtmAlcSarModeTrtl = _WfAtmAlcSarModeTrtl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 23),
    _WfAtmAlcSarModeTrtl_Type()
)
wfAtmAlcSarModeTrtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarModeTrtl.setStatus("mandatory")
_WfAtmAlcSarTimeoutCtrPeriod_Type = Integer32
_WfAtmAlcSarTimeoutCtrPeriod_Object = MibTableColumn
wfAtmAlcSarTimeoutCtrPeriod = _WfAtmAlcSarTimeoutCtrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 24),
    _WfAtmAlcSarTimeoutCtrPeriod_Type()
)
wfAtmAlcSarTimeoutCtrPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarTimeoutCtrPeriod.setStatus("mandatory")
_WfAtmAlcSarTimeoutCtrInt_Type = Integer32
_WfAtmAlcSarTimeoutCtrInt_Object = MibTableColumn
wfAtmAlcSarTimeoutCtrInt = _WfAtmAlcSarTimeoutCtrInt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 25),
    _WfAtmAlcSarTimeoutCtrInt_Type()
)
wfAtmAlcSarTimeoutCtrInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarTimeoutCtrInt.setStatus("mandatory")


class _WfAtmAlcSarMaxReceivePktLen_Type(Integer32):
    """Custom type wfAtmAlcSarMaxReceivePktLen based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4608
        )
    )
    namedValues = NamedValues(
        ("default", 4608)
    )


_WfAtmAlcSarMaxReceivePktLen_Type.__name__ = "Integer32"
_WfAtmAlcSarMaxReceivePktLen_Object = MibTableColumn
wfAtmAlcSarMaxReceivePktLen = _WfAtmAlcSarMaxReceivePktLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 8, 1, 26),
    _WfAtmAlcSarMaxReceivePktLen_Type()
)
wfAtmAlcSarMaxReceivePktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarMaxReceivePktLen.setStatus("mandatory")
_WfAtmAlcSarTrafficMgtTable_Object = MibTable
wfAtmAlcSarTrafficMgtTable = _WfAtmAlcSarTrafficMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9)
)
if mibBuilder.loadTexts:
    wfAtmAlcSarTrafficMgtTable.setStatus("mandatory")
_WfAtmAlcSarTrafficMgtEntry_Object = MibTableRow
wfAtmAlcSarTrafficMgtEntry = _WfAtmAlcSarTrafficMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1)
)
wfAtmAlcSarTrafficMgtEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcSarTrafficMgtIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcSarTrafficMgtEntry.setStatus("mandatory")


class _WfAtmAlcSarTrafficMgtDelete_Type(Integer32):
    """Custom type wfAtmAlcSarTrafficMgtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmAlcSarTrafficMgtDelete_Type.__name__ = "Integer32"
_WfAtmAlcSarTrafficMgtDelete_Object = MibTableColumn
wfAtmAlcSarTrafficMgtDelete = _WfAtmAlcSarTrafficMgtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 1),
    _WfAtmAlcSarTrafficMgtDelete_Type()
)
wfAtmAlcSarTrafficMgtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarTrafficMgtDelete.setStatus("mandatory")
_WfAtmAlcSarTrafficMgtIndex_Type = Integer32
_WfAtmAlcSarTrafficMgtIndex_Object = MibTableColumn
wfAtmAlcSarTrafficMgtIndex = _WfAtmAlcSarTrafficMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 2),
    _WfAtmAlcSarTrafficMgtIndex_Type()
)
wfAtmAlcSarTrafficMgtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarTrafficMgtIndex.setStatus("mandatory")


class _WfAtmAlcSarPeakCellRateEna_Type(Integer32):
    """Custom type wfAtmAlcSarPeakCellRateEna based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcSarPeakCellRateEna_Type.__name__ = "Integer32"
_WfAtmAlcSarPeakCellRateEna_Object = MibTableColumn
wfAtmAlcSarPeakCellRateEna = _WfAtmAlcSarPeakCellRateEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 3),
    _WfAtmAlcSarPeakCellRateEna_Type()
)
wfAtmAlcSarPeakCellRateEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarPeakCellRateEna.setStatus("mandatory")


class _WfAtmAlcSarAvgCellRateEna_Type(Integer32):
    """Custom type wfAtmAlcSarAvgCellRateEna based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcSarAvgCellRateEna_Type.__name__ = "Integer32"
_WfAtmAlcSarAvgCellRateEna_Object = MibTableColumn
wfAtmAlcSarAvgCellRateEna = _WfAtmAlcSarAvgCellRateEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 4),
    _WfAtmAlcSarAvgCellRateEna_Type()
)
wfAtmAlcSarAvgCellRateEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarAvgCellRateEna.setStatus("mandatory")


class _WfAtmAlcSarPeakCellRate_Type(Integer32):
    """Custom type wfAtmAlcSarPeakCellRate based on Integer32"""
    defaultValue = 365566

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            365566
        )
    )
    namedValues = NamedValues(
        ("default", 365566)
    )


_WfAtmAlcSarPeakCellRate_Type.__name__ = "Integer32"
_WfAtmAlcSarPeakCellRate_Object = MibTableColumn
wfAtmAlcSarPeakCellRate = _WfAtmAlcSarPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 5),
    _WfAtmAlcSarPeakCellRate_Type()
)
wfAtmAlcSarPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarPeakCellRate.setStatus("mandatory")


class _WfAtmAlcSarAvgCellRate_Type(Integer32):
    """Custom type wfAtmAlcSarAvgCellRate based on Integer32"""
    defaultValue = 365566

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            365566
        )
    )
    namedValues = NamedValues(
        ("default", 365566)
    )


_WfAtmAlcSarAvgCellRate_Type.__name__ = "Integer32"
_WfAtmAlcSarAvgCellRate_Object = MibTableColumn
wfAtmAlcSarAvgCellRate = _WfAtmAlcSarAvgCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 6),
    _WfAtmAlcSarAvgCellRate_Type()
)
wfAtmAlcSarAvgCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarAvgCellRate.setStatus("mandatory")


class _WfAtmAlcSarMaxBurstSize_Type(Integer32):
    """Custom type wfAtmAlcSarMaxBurstSize based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("default", 40)
    )


_WfAtmAlcSarMaxBurstSize_Type.__name__ = "Integer32"
_WfAtmAlcSarMaxBurstSize_Object = MibTableColumn
wfAtmAlcSarMaxBurstSize = _WfAtmAlcSarMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 9, 1, 7),
    _WfAtmAlcSarMaxBurstSize_Type()
)
wfAtmAlcSarMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcSarMaxBurstSize.setStatus("mandatory")
_WfAtmAlcSarRateQueueTable_Object = MibTable
wfAtmAlcSarRateQueueTable = _WfAtmAlcSarRateQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10)
)
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueTable.setStatus("mandatory")
_WfAtmAlcSarRateQueueEntry_Object = MibTableRow
wfAtmAlcSarRateQueueEntry = _WfAtmAlcSarRateQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1)
)
wfAtmAlcSarRateQueueEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcSarRateQueueIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcSarRateQueueNumber"),
)
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueEntry.setStatus("mandatory")
_WfAtmAlcSarRateQueueIndex_Type = Integer32
_WfAtmAlcSarRateQueueIndex_Object = MibTableColumn
wfAtmAlcSarRateQueueIndex = _WfAtmAlcSarRateQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1, 1),
    _WfAtmAlcSarRateQueueIndex_Type()
)
wfAtmAlcSarRateQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueIndex.setStatus("mandatory")


class _WfAtmAlcSarRateQueueNumber_Type(Integer32):
    """Custom type wfAtmAlcSarRateQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WfAtmAlcSarRateQueueNumber_Type.__name__ = "Integer32"
_WfAtmAlcSarRateQueueNumber_Object = MibTableColumn
wfAtmAlcSarRateQueueNumber = _WfAtmAlcSarRateQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1, 2),
    _WfAtmAlcSarRateQueueNumber_Type()
)
wfAtmAlcSarRateQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueNumber.setStatus("mandatory")


class _WfAtmAlcSarRateQueueState_Type(Integer32):
    """Custom type wfAtmAlcSarRateQueueState based on Integer32"""
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


_WfAtmAlcSarRateQueueState_Type.__name__ = "Integer32"
_WfAtmAlcSarRateQueueState_Object = MibTableColumn
wfAtmAlcSarRateQueueState = _WfAtmAlcSarRateQueueState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1, 3),
    _WfAtmAlcSarRateQueueState_Type()
)
wfAtmAlcSarRateQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueState.setStatus("mandatory")
_WfAtmAlcSarRateQueuePcr_Type = Integer32
_WfAtmAlcSarRateQueuePcr_Object = MibTableColumn
wfAtmAlcSarRateQueuePcr = _WfAtmAlcSarRateQueuePcr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1, 4),
    _WfAtmAlcSarRateQueuePcr_Type()
)
wfAtmAlcSarRateQueuePcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueuePcr.setStatus("mandatory")
_WfAtmAlcSarRateQueueVcs_Type = Integer32
_WfAtmAlcSarRateQueueVcs_Object = MibTableColumn
wfAtmAlcSarRateQueueVcs = _WfAtmAlcSarRateQueueVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1, 5),
    _WfAtmAlcSarRateQueueVcs_Type()
)
wfAtmAlcSarRateQueueVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueVcs.setStatus("mandatory")


class _WfAtmAlcSarRateQueueDef_Type(Integer32):
    """Custom type wfAtmAlcSarRateQueueDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicit", 2),
          ("implicit", 1))
    )


_WfAtmAlcSarRateQueueDef_Type.__name__ = "Integer32"
_WfAtmAlcSarRateQueueDef_Object = MibTableColumn
wfAtmAlcSarRateQueueDef = _WfAtmAlcSarRateQueueDef_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 10, 1, 6),
    _WfAtmAlcSarRateQueueDef_Type()
)
wfAtmAlcSarRateQueueDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcSarRateQueueDef.setStatus("mandatory")
_WfAtmAlcFrmConfTable_Object = MibTable
wfAtmAlcFrmConfTable = _WfAtmAlcFrmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11)
)
if mibBuilder.loadTexts:
    wfAtmAlcFrmConfTable.setStatus("mandatory")
_WfAtmAlcFrmConfEntry_Object = MibTableRow
wfAtmAlcFrmConfEntry = _WfAtmAlcFrmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1)
)
wfAtmAlcFrmConfEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmAlcFrmConfIndex"),
)
if mibBuilder.loadTexts:
    wfAtmAlcFrmConfEntry.setStatus("mandatory")


class _WfAtmAlcFrmConfDelete_Type(Integer32):
    """Custom type wfAtmAlcFrmConfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmAlcFrmConfDelete_Type.__name__ = "Integer32"
_WfAtmAlcFrmConfDelete_Object = MibTableColumn
wfAtmAlcFrmConfDelete = _WfAtmAlcFrmConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 1),
    _WfAtmAlcFrmConfDelete_Type()
)
wfAtmAlcFrmConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmConfDelete.setStatus("mandatory")
_WfAtmAlcFrmConfIndex_Type = Integer32
_WfAtmAlcFrmConfIndex_Object = MibTableColumn
wfAtmAlcFrmConfIndex = _WfAtmAlcFrmConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 2),
    _WfAtmAlcFrmConfIndex_Type()
)
wfAtmAlcFrmConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmAlcFrmConfIndex.setStatus("mandatory")


class _WfAtmAlcFrmGenEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmGenEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmGenEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenEnable_Object = MibTableColumn
wfAtmAlcFrmGenEnable = _WfAtmAlcFrmGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 3),
    _WfAtmAlcFrmGenEnable_Type()
)
wfAtmAlcFrmGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenEnable.setStatus("mandatory")


class _WfAtmAlcFrmGenFramingMode_Type(Integer32):
    """Custom type wfAtmAlcFrmGenFramingMode based on Integer32"""
    defaultValue = 3

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
        *(("cell", 1),
          ("ds3", 4),
          ("ds3nonplcp", 7),
          ("e3", 5),
          ("sdh", 2),
          ("sonet", 3),
          ("sonetsts1", 6))
    )


_WfAtmAlcFrmGenFramingMode_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenFramingMode_Object = MibTableColumn
wfAtmAlcFrmGenFramingMode = _WfAtmAlcFrmGenFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 4),
    _WfAtmAlcFrmGenFramingMode_Type()
)
wfAtmAlcFrmGenFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenFramingMode.setStatus("mandatory")


class _WfAtmAlcFrmGenScramblerEna_Type(Integer32):
    """Custom type wfAtmAlcFrmGenScramblerEna based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmGenScramblerEna_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenScramblerEna_Object = MibTableColumn
wfAtmAlcFrmGenScramblerEna = _WfAtmAlcFrmGenScramblerEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 5),
    _WfAtmAlcFrmGenScramblerEna_Type()
)
wfAtmAlcFrmGenScramblerEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenScramblerEna.setStatus("mandatory")


class _WfAtmAlcFrmGenDescrambleEna_Type(Integer32):
    """Custom type wfAtmAlcFrmGenDescrambleEna based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmGenDescrambleEna_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenDescrambleEna_Object = MibTableColumn
wfAtmAlcFrmGenDescrambleEna = _WfAtmAlcFrmGenDescrambleEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 6),
    _WfAtmAlcFrmGenDescrambleEna_Type()
)
wfAtmAlcFrmGenDescrambleEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenDescrambleEna.setStatus("mandatory")


class _WfAtmAlcFrmGenLoopback_Type(Integer32):
    """Custom type wfAtmAlcFrmGenLoopback based on Integer32"""
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


_WfAtmAlcFrmGenLoopback_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenLoopback_Object = MibTableColumn
wfAtmAlcFrmGenLoopback = _WfAtmAlcFrmGenLoopback_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 7),
    _WfAtmAlcFrmGenLoopback_Type()
)
wfAtmAlcFrmGenLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenLoopback.setStatus("mandatory")


class _WfAtmAlcFrmGenSyncFoundCnt_Type(Integer32):
    """Custom type wfAtmAlcFrmGenSyncFoundCnt based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfAtmAlcFrmGenSyncFoundCnt_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenSyncFoundCnt_Object = MibTableColumn
wfAtmAlcFrmGenSyncFoundCnt = _WfAtmAlcFrmGenSyncFoundCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 8),
    _WfAtmAlcFrmGenSyncFoundCnt_Type()
)
wfAtmAlcFrmGenSyncFoundCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenSyncFoundCnt.setStatus("mandatory")


class _WfAtmAlcFrmGenSyncLostCnt_Type(Integer32):
    """Custom type wfAtmAlcFrmGenSyncLostCnt based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfAtmAlcFrmGenSyncLostCnt_Type.__name__ = "Integer32"
_WfAtmAlcFrmGenSyncLostCnt_Object = MibTableColumn
wfAtmAlcFrmGenSyncLostCnt = _WfAtmAlcFrmGenSyncLostCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 9),
    _WfAtmAlcFrmGenSyncLostCnt_Type()
)
wfAtmAlcFrmGenSyncLostCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmGenSyncLostCnt.setStatus("mandatory")


class _WfAtmAlcFrmRcvCellEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvCellEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmRcvCellEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvCellEnable_Object = MibTableColumn
wfAtmAlcFrmRcvCellEnable = _WfAtmAlcFrmRcvCellEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 10),
    _WfAtmAlcFrmRcvCellEnable_Type()
)
wfAtmAlcFrmRcvCellEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvCellEnable.setStatus("mandatory")


class _WfAtmAlcFrmRcvOamCrcCheck_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvOamCrcCheck based on Integer32"""
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


_WfAtmAlcFrmRcvOamCrcCheck_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvOamCrcCheck_Object = MibTableColumn
wfAtmAlcFrmRcvOamCrcCheck = _WfAtmAlcFrmRcvOamCrcCheck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 11),
    _WfAtmAlcFrmRcvOamCrcCheck_Type()
)
wfAtmAlcFrmRcvOamCrcCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvOamCrcCheck.setStatus("mandatory")


class _WfAtmAlcFrmRcvOamCrcGen_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvOamCrcGen based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmRcvOamCrcGen_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvOamCrcGen_Object = MibTableColumn
wfAtmAlcFrmRcvOamCrcGen = _WfAtmAlcFrmRcvOamCrcGen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 12),
    _WfAtmAlcFrmRcvOamCrcGen_Type()
)
wfAtmAlcFrmRcvOamCrcGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvOamCrcGen.setStatus("mandatory")


class _WfAtmAlcFrmRcvCellInsPrio_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvCellInsPrio based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insert", 2),
          ("user", 1))
    )


_WfAtmAlcFrmRcvCellInsPrio_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvCellInsPrio_Object = MibTableColumn
wfAtmAlcFrmRcvCellInsPrio = _WfAtmAlcFrmRcvCellInsPrio_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 13),
    _WfAtmAlcFrmRcvCellInsPrio_Type()
)
wfAtmAlcFrmRcvCellInsPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvCellInsPrio.setStatus("mandatory")


class _WfAtmAlcFrmRcvInsertPcr_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvInsertPcr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("default", 4)
    )


_WfAtmAlcFrmRcvInsertPcr_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvInsertPcr_Object = MibTableColumn
wfAtmAlcFrmRcvInsertPcr = _WfAtmAlcFrmRcvInsertPcr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 14),
    _WfAtmAlcFrmRcvInsertPcr_Type()
)
wfAtmAlcFrmRcvInsertPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvInsertPcr.setStatus("mandatory")


class _WfAtmAlcFrmRcvGfcIgnore_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvGfcIgnore based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vpi12", 1),
          ("vpi8", 2))
    )


_WfAtmAlcFrmRcvGfcIgnore_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvGfcIgnore_Object = MibTableColumn
wfAtmAlcFrmRcvGfcIgnore = _WfAtmAlcFrmRcvGfcIgnore_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 15),
    _WfAtmAlcFrmRcvGfcIgnore_Type()
)
wfAtmAlcFrmRcvGfcIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvGfcIgnore.setStatus("mandatory")


class _WfAtmAlcFrmRcvDescrambleCtl_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDescrambleCtl based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmRcvDescrambleCtl_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDescrambleCtl_Object = MibTableColumn
wfAtmAlcFrmRcvDescrambleCtl = _WfAtmAlcFrmRcvDescrambleCtl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 16),
    _WfAtmAlcFrmRcvDescrambleCtl_Type()
)
wfAtmAlcFrmRcvDescrambleCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDescrambleCtl.setStatus("mandatory")


class _WfAtmAlcFrmRcvHecRcvMask_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvHecRcvMask based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmRcvHecRcvMask_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvHecRcvMask_Object = MibTableColumn
wfAtmAlcFrmRcvHecRcvMask = _WfAtmAlcFrmRcvHecRcvMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 17),
    _WfAtmAlcFrmRcvHecRcvMask_Type()
)
wfAtmAlcFrmRcvHecRcvMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvHecRcvMask.setStatus("mandatory")


class _WfAtmAlcFrmRcvErrCorrectEna_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvErrCorrectEna based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmRcvErrCorrectEna_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvErrCorrectEna_Object = MibTableColumn
wfAtmAlcFrmRcvErrCorrectEna = _WfAtmAlcFrmRcvErrCorrectEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 18),
    _WfAtmAlcFrmRcvErrCorrectEna_Type()
)
wfAtmAlcFrmRcvErrCorrectEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvErrCorrectEna.setStatus("mandatory")


class _WfAtmAlcFrmRcvByteAlignment_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvByteAlignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("align", 2),
          ("nonalign", 1))
    )


_WfAtmAlcFrmRcvByteAlignment_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvByteAlignment_Object = MibTableColumn
wfAtmAlcFrmRcvByteAlignment = _WfAtmAlcFrmRcvByteAlignment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 19),
    _WfAtmAlcFrmRcvByteAlignment_Type()
)
wfAtmAlcFrmRcvByteAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvByteAlignment.setStatus("mandatory")


class _WfAtmAlcFrmRcvCellSyncFound_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvCellSyncFound based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfAtmAlcFrmRcvCellSyncFound_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvCellSyncFound_Object = MibTableColumn
wfAtmAlcFrmRcvCellSyncFound = _WfAtmAlcFrmRcvCellSyncFound_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 20),
    _WfAtmAlcFrmRcvCellSyncFound_Type()
)
wfAtmAlcFrmRcvCellSyncFound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvCellSyncFound.setStatus("mandatory")


class _WfAtmAlcFrmRcvCellSyncLost_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvCellSyncLost based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfAtmAlcFrmRcvCellSyncLost_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvCellSyncLost_Object = MibTableColumn
wfAtmAlcFrmRcvCellSyncLost = _WfAtmAlcFrmRcvCellSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 21),
    _WfAtmAlcFrmRcvCellSyncLost_Type()
)
wfAtmAlcFrmRcvCellSyncLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvCellSyncLost.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtUserCell_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtUserCell based on Integer32"""
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
        *(("defined", 2),
          ("disabled", 1),
          ("invalid", 4),
          ("undefined", 3))
    )


_WfAtmAlcFrmRcvExtUserCell_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtUserCell_Object = MibTableColumn
wfAtmAlcFrmRcvExtUserCell = _WfAtmAlcFrmRcvExtUserCell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 22),
    _WfAtmAlcFrmRcvExtUserCell_Type()
)
wfAtmAlcFrmRcvExtUserCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtUserCell.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtMetaSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtMetaSig based on Integer32"""
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


_WfAtmAlcFrmRcvExtMetaSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtMetaSig_Object = MibTableColumn
wfAtmAlcFrmRcvExtMetaSig = _WfAtmAlcFrmRcvExtMetaSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 23),
    _WfAtmAlcFrmRcvExtMetaSig_Type()
)
wfAtmAlcFrmRcvExtMetaSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtMetaSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtBcastSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtBcastSig based on Integer32"""
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


_WfAtmAlcFrmRcvExtBcastSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtBcastSig_Object = MibTableColumn
wfAtmAlcFrmRcvExtBcastSig = _WfAtmAlcFrmRcvExtBcastSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 24),
    _WfAtmAlcFrmRcvExtBcastSig_Type()
)
wfAtmAlcFrmRcvExtBcastSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtBcastSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtPointSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtPointSig based on Integer32"""
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


_WfAtmAlcFrmRcvExtPointSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtPointSig_Object = MibTableColumn
wfAtmAlcFrmRcvExtPointSig = _WfAtmAlcFrmRcvExtPointSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 25),
    _WfAtmAlcFrmRcvExtPointSig_Type()
)
wfAtmAlcFrmRcvExtPointSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtPointSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtIlmiSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtIlmiSig based on Integer32"""
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


_WfAtmAlcFrmRcvExtIlmiSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtIlmiSig_Object = MibTableColumn
wfAtmAlcFrmRcvExtIlmiSig = _WfAtmAlcFrmRcvExtIlmiSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 26),
    _WfAtmAlcFrmRcvExtIlmiSig_Type()
)
wfAtmAlcFrmRcvExtIlmiSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtIlmiSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtF4F5PrfMan_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtF4F5PrfMan based on Integer32"""
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


_WfAtmAlcFrmRcvExtF4F5PrfMan_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtF4F5PrfMan_Object = MibTableColumn
wfAtmAlcFrmRcvExtF4F5PrfMan = _WfAtmAlcFrmRcvExtF4F5PrfMan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 27),
    _WfAtmAlcFrmRcvExtF4F5PrfMan_Type()
)
wfAtmAlcFrmRcvExtF4F5PrfMan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtF4F5PrfMan.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtF1F3PlOam_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtF1F3PlOam based on Integer32"""
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


_WfAtmAlcFrmRcvExtF1F3PlOam_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtF1F3PlOam_Object = MibTableColumn
wfAtmAlcFrmRcvExtF1F3PlOam = _WfAtmAlcFrmRcvExtF1F3PlOam_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 28),
    _WfAtmAlcFrmRcvExtF1F3PlOam_Type()
)
wfAtmAlcFrmRcvExtF1F3PlOam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtF1F3PlOam.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtF4Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtF4Segment based on Integer32"""
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


_WfAtmAlcFrmRcvExtF4Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtF4Segment_Object = MibTableColumn
wfAtmAlcFrmRcvExtF4Segment = _WfAtmAlcFrmRcvExtF4Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 29),
    _WfAtmAlcFrmRcvExtF4Segment_Type()
)
wfAtmAlcFrmRcvExtF4Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtF4Segment.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtF4EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtF4EndEnd based on Integer32"""
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


_WfAtmAlcFrmRcvExtF4EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtF4EndEnd_Object = MibTableColumn
wfAtmAlcFrmRcvExtF4EndEnd = _WfAtmAlcFrmRcvExtF4EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 30),
    _WfAtmAlcFrmRcvExtF4EndEnd_Type()
)
wfAtmAlcFrmRcvExtF4EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtF4EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtF5Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtF5Segment based on Integer32"""
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


_WfAtmAlcFrmRcvExtF5Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtF5Segment_Object = MibTableColumn
wfAtmAlcFrmRcvExtF5Segment = _WfAtmAlcFrmRcvExtF5Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 31),
    _WfAtmAlcFrmRcvExtF5Segment_Type()
)
wfAtmAlcFrmRcvExtF5Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtF5Segment.setStatus("mandatory")


class _WfAtmAlcFrmRcvExtF5EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvExtF5EndEnd based on Integer32"""
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


_WfAtmAlcFrmRcvExtF5EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvExtF5EndEnd_Object = MibTableColumn
wfAtmAlcFrmRcvExtF5EndEnd = _WfAtmAlcFrmRcvExtF5EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 32),
    _WfAtmAlcFrmRcvExtF5EndEnd_Type()
)
wfAtmAlcFrmRcvExtF5EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvExtF5EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisUserCell_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisUserCell based on Integer32"""
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
        *(("defined", 2),
          ("disabled", 1),
          ("invalid", 4),
          ("undefined", 3))
    )


_WfAtmAlcFrmRcvDisUserCell_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisUserCell_Object = MibTableColumn
wfAtmAlcFrmRcvDisUserCell = _WfAtmAlcFrmRcvDisUserCell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 33),
    _WfAtmAlcFrmRcvDisUserCell_Type()
)
wfAtmAlcFrmRcvDisUserCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisUserCell.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisMetaSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisMetaSig based on Integer32"""
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


_WfAtmAlcFrmRcvDisMetaSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisMetaSig_Object = MibTableColumn
wfAtmAlcFrmRcvDisMetaSig = _WfAtmAlcFrmRcvDisMetaSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 34),
    _WfAtmAlcFrmRcvDisMetaSig_Type()
)
wfAtmAlcFrmRcvDisMetaSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisMetaSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisBcastSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisBcastSig based on Integer32"""
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


_WfAtmAlcFrmRcvDisBcastSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisBcastSig_Object = MibTableColumn
wfAtmAlcFrmRcvDisBcastSig = _WfAtmAlcFrmRcvDisBcastSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 35),
    _WfAtmAlcFrmRcvDisBcastSig_Type()
)
wfAtmAlcFrmRcvDisBcastSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisBcastSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisPointSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisPointSig based on Integer32"""
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


_WfAtmAlcFrmRcvDisPointSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisPointSig_Object = MibTableColumn
wfAtmAlcFrmRcvDisPointSig = _WfAtmAlcFrmRcvDisPointSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 36),
    _WfAtmAlcFrmRcvDisPointSig_Type()
)
wfAtmAlcFrmRcvDisPointSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisPointSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisIlmiSig_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisIlmiSig based on Integer32"""
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


_WfAtmAlcFrmRcvDisIlmiSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisIlmiSig_Object = MibTableColumn
wfAtmAlcFrmRcvDisIlmiSig = _WfAtmAlcFrmRcvDisIlmiSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 37),
    _WfAtmAlcFrmRcvDisIlmiSig_Type()
)
wfAtmAlcFrmRcvDisIlmiSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisIlmiSig.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisUnassCell_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisUnassCell based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmRcvDisUnassCell_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisUnassCell_Object = MibTableColumn
wfAtmAlcFrmRcvDisUnassCell = _WfAtmAlcFrmRcvDisUnassCell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 38),
    _WfAtmAlcFrmRcvDisUnassCell_Type()
)
wfAtmAlcFrmRcvDisUnassCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisUnassCell.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisF4Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisF4Segment based on Integer32"""
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


_WfAtmAlcFrmRcvDisF4Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisF4Segment_Object = MibTableColumn
wfAtmAlcFrmRcvDisF4Segment = _WfAtmAlcFrmRcvDisF4Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 39),
    _WfAtmAlcFrmRcvDisF4Segment_Type()
)
wfAtmAlcFrmRcvDisF4Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisF4Segment.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisF4EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisF4EndEnd based on Integer32"""
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


_WfAtmAlcFrmRcvDisF4EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisF4EndEnd_Object = MibTableColumn
wfAtmAlcFrmRcvDisF4EndEnd = _WfAtmAlcFrmRcvDisF4EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 40),
    _WfAtmAlcFrmRcvDisF4EndEnd_Type()
)
wfAtmAlcFrmRcvDisF4EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisF4EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisF5Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisF5Segment based on Integer32"""
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


_WfAtmAlcFrmRcvDisF5Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisF5Segment_Object = MibTableColumn
wfAtmAlcFrmRcvDisF5Segment = _WfAtmAlcFrmRcvDisF5Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 41),
    _WfAtmAlcFrmRcvDisF5Segment_Type()
)
wfAtmAlcFrmRcvDisF5Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisF5Segment.setStatus("mandatory")


class _WfAtmAlcFrmRcvDisF5EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmRcvDisF5EndEnd based on Integer32"""
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


_WfAtmAlcFrmRcvDisF5EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmRcvDisF5EndEnd_Object = MibTableColumn
wfAtmAlcFrmRcvDisF5EndEnd = _WfAtmAlcFrmRcvDisF5EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 42),
    _WfAtmAlcFrmRcvDisF5EndEnd_Type()
)
wfAtmAlcFrmRcvDisF5EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmRcvDisF5EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmXmtCellEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtCellEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmXmtCellEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtCellEnable_Object = MibTableColumn
wfAtmAlcFrmXmtCellEnable = _WfAtmAlcFrmXmtCellEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 43),
    _WfAtmAlcFrmXmtCellEnable_Type()
)
wfAtmAlcFrmXmtCellEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtCellEnable.setStatus("mandatory")


class _WfAtmAlcFrmXmtOamCrcCheck_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtOamCrcCheck based on Integer32"""
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


_WfAtmAlcFrmXmtOamCrcCheck_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtOamCrcCheck_Object = MibTableColumn
wfAtmAlcFrmXmtOamCrcCheck = _WfAtmAlcFrmXmtOamCrcCheck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 44),
    _WfAtmAlcFrmXmtOamCrcCheck_Type()
)
wfAtmAlcFrmXmtOamCrcCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtOamCrcCheck.setStatus("mandatory")


class _WfAtmAlcFrmXmtOamCrcGen_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtOamCrcGen based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmXmtOamCrcGen_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtOamCrcGen_Object = MibTableColumn
wfAtmAlcFrmXmtOamCrcGen = _WfAtmAlcFrmXmtOamCrcGen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 45),
    _WfAtmAlcFrmXmtOamCrcGen_Type()
)
wfAtmAlcFrmXmtOamCrcGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtOamCrcGen.setStatus("mandatory")


class _WfAtmAlcFrmXmtCellInsPrio_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtCellInsPrio based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insert", 2),
          ("user", 1))
    )


_WfAtmAlcFrmXmtCellInsPrio_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtCellInsPrio_Object = MibTableColumn
wfAtmAlcFrmXmtCellInsPrio = _WfAtmAlcFrmXmtCellInsPrio_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 46),
    _WfAtmAlcFrmXmtCellInsPrio_Type()
)
wfAtmAlcFrmXmtCellInsPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtCellInsPrio.setStatus("mandatory")


class _WfAtmAlcFrmXmtInsertPcr_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtInsertPcr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("default", 4)
    )


_WfAtmAlcFrmXmtInsertPcr_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtInsertPcr_Object = MibTableColumn
wfAtmAlcFrmXmtInsertPcr = _WfAtmAlcFrmXmtInsertPcr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 47),
    _WfAtmAlcFrmXmtInsertPcr_Type()
)
wfAtmAlcFrmXmtInsertPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtInsertPcr.setStatus("mandatory")


class _WfAtmAlcFrmXmtGfcIgnore_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtGfcIgnore based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vpi12", 1),
          ("vpi8", 2))
    )


_WfAtmAlcFrmXmtGfcIgnore_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtGfcIgnore_Object = MibTableColumn
wfAtmAlcFrmXmtGfcIgnore = _WfAtmAlcFrmXmtGfcIgnore_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 48),
    _WfAtmAlcFrmXmtGfcIgnore_Type()
)
wfAtmAlcFrmXmtGfcIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtGfcIgnore.setStatus("mandatory")


class _WfAtmAlcFrmXmtCellDecouple_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtCellDecouple based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassign", 2))
    )


_WfAtmAlcFrmXmtCellDecouple_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtCellDecouple_Object = MibTableColumn
wfAtmAlcFrmXmtCellDecouple = _WfAtmAlcFrmXmtCellDecouple_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 49),
    _WfAtmAlcFrmXmtCellDecouple_Type()
)
wfAtmAlcFrmXmtCellDecouple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtCellDecouple.setStatus("mandatory")


class _WfAtmAlcFrmXmtScrambleCtl_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtScrambleCtl based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmXmtScrambleCtl_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtScrambleCtl_Object = MibTableColumn
wfAtmAlcFrmXmtScrambleCtl = _WfAtmAlcFrmXmtScrambleCtl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 50),
    _WfAtmAlcFrmXmtScrambleCtl_Type()
)
wfAtmAlcFrmXmtScrambleCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtScrambleCtl.setStatus("mandatory")


class _WfAtmAlcFrmXmtHecXmtMask_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtHecXmtMask based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmXmtHecXmtMask_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtHecXmtMask_Object = MibTableColumn
wfAtmAlcFrmXmtHecXmtMask = _WfAtmAlcFrmXmtHecXmtMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 51),
    _WfAtmAlcFrmXmtHecXmtMask_Type()
)
wfAtmAlcFrmXmtHecXmtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtHecXmtMask.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtUserCell_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtUserCell based on Integer32"""
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
        *(("defined", 2),
          ("disabled", 1),
          ("invalid", 4),
          ("undefined", 3))
    )


_WfAtmAlcFrmXmtExtUserCell_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtUserCell_Object = MibTableColumn
wfAtmAlcFrmXmtExtUserCell = _WfAtmAlcFrmXmtExtUserCell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 52),
    _WfAtmAlcFrmXmtExtUserCell_Type()
)
wfAtmAlcFrmXmtExtUserCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtUserCell.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtMetaSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtMetaSig based on Integer32"""
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


_WfAtmAlcFrmXmtExtMetaSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtMetaSig_Object = MibTableColumn
wfAtmAlcFrmXmtExtMetaSig = _WfAtmAlcFrmXmtExtMetaSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 53),
    _WfAtmAlcFrmXmtExtMetaSig_Type()
)
wfAtmAlcFrmXmtExtMetaSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtMetaSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtBcastSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtBcastSig based on Integer32"""
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


_WfAtmAlcFrmXmtExtBcastSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtBcastSig_Object = MibTableColumn
wfAtmAlcFrmXmtExtBcastSig = _WfAtmAlcFrmXmtExtBcastSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 54),
    _WfAtmAlcFrmXmtExtBcastSig_Type()
)
wfAtmAlcFrmXmtExtBcastSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtBcastSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtPointSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtPointSig based on Integer32"""
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


_WfAtmAlcFrmXmtExtPointSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtPointSig_Object = MibTableColumn
wfAtmAlcFrmXmtExtPointSig = _WfAtmAlcFrmXmtExtPointSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 55),
    _WfAtmAlcFrmXmtExtPointSig_Type()
)
wfAtmAlcFrmXmtExtPointSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtPointSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtIlmiSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtIlmiSig based on Integer32"""
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


_WfAtmAlcFrmXmtExtIlmiSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtIlmiSig_Object = MibTableColumn
wfAtmAlcFrmXmtExtIlmiSig = _WfAtmAlcFrmXmtExtIlmiSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 56),
    _WfAtmAlcFrmXmtExtIlmiSig_Type()
)
wfAtmAlcFrmXmtExtIlmiSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtIlmiSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtF4F5PrfMan_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtF4F5PrfMan based on Integer32"""
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


_WfAtmAlcFrmXmtExtF4F5PrfMan_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtF4F5PrfMan_Object = MibTableColumn
wfAtmAlcFrmXmtExtF4F5PrfMan = _WfAtmAlcFrmXmtExtF4F5PrfMan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 57),
    _WfAtmAlcFrmXmtExtF4F5PrfMan_Type()
)
wfAtmAlcFrmXmtExtF4F5PrfMan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtF4F5PrfMan.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtF4Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtF4Segment based on Integer32"""
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


_WfAtmAlcFrmXmtExtF4Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtF4Segment_Object = MibTableColumn
wfAtmAlcFrmXmtExtF4Segment = _WfAtmAlcFrmXmtExtF4Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 58),
    _WfAtmAlcFrmXmtExtF4Segment_Type()
)
wfAtmAlcFrmXmtExtF4Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtF4Segment.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtF4EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtF4EndEnd based on Integer32"""
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


_WfAtmAlcFrmXmtExtF4EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtF4EndEnd_Object = MibTableColumn
wfAtmAlcFrmXmtExtF4EndEnd = _WfAtmAlcFrmXmtExtF4EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 59),
    _WfAtmAlcFrmXmtExtF4EndEnd_Type()
)
wfAtmAlcFrmXmtExtF4EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtF4EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtF5Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtF5Segment based on Integer32"""
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


_WfAtmAlcFrmXmtExtF5Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtF5Segment_Object = MibTableColumn
wfAtmAlcFrmXmtExtF5Segment = _WfAtmAlcFrmXmtExtF5Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 60),
    _WfAtmAlcFrmXmtExtF5Segment_Type()
)
wfAtmAlcFrmXmtExtF5Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtF5Segment.setStatus("mandatory")


class _WfAtmAlcFrmXmtExtF5EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtExtF5EndEnd based on Integer32"""
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


_WfAtmAlcFrmXmtExtF5EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtExtF5EndEnd_Object = MibTableColumn
wfAtmAlcFrmXmtExtF5EndEnd = _WfAtmAlcFrmXmtExtF5EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 61),
    _WfAtmAlcFrmXmtExtF5EndEnd_Type()
)
wfAtmAlcFrmXmtExtF5EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtExtF5EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisUserCell_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisUserCell based on Integer32"""
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
        *(("defined", 2),
          ("disabled", 1),
          ("invalid", 4),
          ("undefined", 3))
    )


_WfAtmAlcFrmXmtDisUserCell_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisUserCell_Object = MibTableColumn
wfAtmAlcFrmXmtDisUserCell = _WfAtmAlcFrmXmtDisUserCell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 62),
    _WfAtmAlcFrmXmtDisUserCell_Type()
)
wfAtmAlcFrmXmtDisUserCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisUserCell.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisMetaSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisMetaSig based on Integer32"""
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


_WfAtmAlcFrmXmtDisMetaSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisMetaSig_Object = MibTableColumn
wfAtmAlcFrmXmtDisMetaSig = _WfAtmAlcFrmXmtDisMetaSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 63),
    _WfAtmAlcFrmXmtDisMetaSig_Type()
)
wfAtmAlcFrmXmtDisMetaSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisMetaSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisBcastSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisBcastSig based on Integer32"""
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


_WfAtmAlcFrmXmtDisBcastSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisBcastSig_Object = MibTableColumn
wfAtmAlcFrmXmtDisBcastSig = _WfAtmAlcFrmXmtDisBcastSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 64),
    _WfAtmAlcFrmXmtDisBcastSig_Type()
)
wfAtmAlcFrmXmtDisBcastSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisBcastSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisPointSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisPointSig based on Integer32"""
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


_WfAtmAlcFrmXmtDisPointSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisPointSig_Object = MibTableColumn
wfAtmAlcFrmXmtDisPointSig = _WfAtmAlcFrmXmtDisPointSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 65),
    _WfAtmAlcFrmXmtDisPointSig_Type()
)
wfAtmAlcFrmXmtDisPointSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisPointSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisIlmiSig_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisIlmiSig based on Integer32"""
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


_WfAtmAlcFrmXmtDisIlmiSig_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisIlmiSig_Object = MibTableColumn
wfAtmAlcFrmXmtDisIlmiSig = _WfAtmAlcFrmXmtDisIlmiSig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 66),
    _WfAtmAlcFrmXmtDisIlmiSig_Type()
)
wfAtmAlcFrmXmtDisIlmiSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisIlmiSig.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisUnassCell_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisUnassCell based on Integer32"""
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


_WfAtmAlcFrmXmtDisUnassCell_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisUnassCell_Object = MibTableColumn
wfAtmAlcFrmXmtDisUnassCell = _WfAtmAlcFrmXmtDisUnassCell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 67),
    _WfAtmAlcFrmXmtDisUnassCell_Type()
)
wfAtmAlcFrmXmtDisUnassCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisUnassCell.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisF4Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisF4Segment based on Integer32"""
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


_WfAtmAlcFrmXmtDisF4Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisF4Segment_Object = MibTableColumn
wfAtmAlcFrmXmtDisF4Segment = _WfAtmAlcFrmXmtDisF4Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 68),
    _WfAtmAlcFrmXmtDisF4Segment_Type()
)
wfAtmAlcFrmXmtDisF4Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisF4Segment.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisF4EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisF4EndEnd based on Integer32"""
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


_WfAtmAlcFrmXmtDisF4EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisF4EndEnd_Object = MibTableColumn
wfAtmAlcFrmXmtDisF4EndEnd = _WfAtmAlcFrmXmtDisF4EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 69),
    _WfAtmAlcFrmXmtDisF4EndEnd_Type()
)
wfAtmAlcFrmXmtDisF4EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisF4EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisF5Segment_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisF5Segment based on Integer32"""
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


_WfAtmAlcFrmXmtDisF5Segment_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisF5Segment_Object = MibTableColumn
wfAtmAlcFrmXmtDisF5Segment = _WfAtmAlcFrmXmtDisF5Segment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 70),
    _WfAtmAlcFrmXmtDisF5Segment_Type()
)
wfAtmAlcFrmXmtDisF5Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisF5Segment.setStatus("mandatory")


class _WfAtmAlcFrmXmtDisF5EndEnd_Type(Integer32):
    """Custom type wfAtmAlcFrmXmtDisF5EndEnd based on Integer32"""
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


_WfAtmAlcFrmXmtDisF5EndEnd_Type.__name__ = "Integer32"
_WfAtmAlcFrmXmtDisF5EndEnd_Object = MibTableColumn
wfAtmAlcFrmXmtDisF5EndEnd = _WfAtmAlcFrmXmtDisF5EndEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 71),
    _WfAtmAlcFrmXmtDisF5EndEnd_Type()
)
wfAtmAlcFrmXmtDisF5EndEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmXmtDisF5EndEnd.setStatus("mandatory")


class _WfAtmAlcFrmOamEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmOamEnable based on Integer32"""
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


_WfAtmAlcFrmOamEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamEnable_Object = MibTableColumn
wfAtmAlcFrmOamEnable = _WfAtmAlcFrmOamEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 72),
    _WfAtmAlcFrmOamEnable_Type()
)
wfAtmAlcFrmOamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamEnable.setStatus("mandatory")


class _WfAtmAlcFrmOamInvertBip_Type(Integer32):
    """Custom type wfAtmAlcFrmOamInvertBip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert", 2),
          ("normal", 1))
    )


_WfAtmAlcFrmOamInvertBip_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamInvertBip_Object = MibTableColumn
wfAtmAlcFrmOamInvertBip = _WfAtmAlcFrmOamInvertBip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 73),
    _WfAtmAlcFrmOamInvertBip_Type()
)
wfAtmAlcFrmOamInvertBip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamInvertBip.setStatus("mandatory")


class _WfAtmAlcFrmOamTxPathFerf_Type(Integer32):
    """Custom type wfAtmAlcFrmOamTxPathFerf based on Integer32"""
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
        *(("auto", 2),
          ("clear", 1),
          ("set", 3))
    )


_WfAtmAlcFrmOamTxPathFerf_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamTxPathFerf_Object = MibTableColumn
wfAtmAlcFrmOamTxPathFerf = _WfAtmAlcFrmOamTxPathFerf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 74),
    _WfAtmAlcFrmOamTxPathFerf_Type()
)
wfAtmAlcFrmOamTxPathFerf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamTxPathFerf.setStatus("mandatory")


class _WfAtmAlcFrmOamTxSectionFerf_Type(Integer32):
    """Custom type wfAtmAlcFrmOamTxSectionFerf based on Integer32"""
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
        *(("auto", 2),
          ("clear", 1),
          ("set", 3))
    )


_WfAtmAlcFrmOamTxSectionFerf_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamTxSectionFerf_Object = MibTableColumn
wfAtmAlcFrmOamTxSectionFerf = _WfAtmAlcFrmOamTxSectionFerf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 75),
    _WfAtmAlcFrmOamTxSectionFerf_Type()
)
wfAtmAlcFrmOamTxSectionFerf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamTxSectionFerf.setStatus("mandatory")


class _WfAtmAlcFrmOamTxPathAis_Type(Integer32):
    """Custom type wfAtmAlcFrmOamTxPathAis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_WfAtmAlcFrmOamTxPathAis_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamTxPathAis_Object = MibTableColumn
wfAtmAlcFrmOamTxPathAis = _WfAtmAlcFrmOamTxPathAis_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 76),
    _WfAtmAlcFrmOamTxPathAis_Type()
)
wfAtmAlcFrmOamTxPathAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamTxPathAis.setStatus("mandatory")


class _WfAtmAlcFrmOamTxSectionAis_Type(Integer32):
    """Custom type wfAtmAlcFrmOamTxSectionAis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_WfAtmAlcFrmOamTxSectionAis_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamTxSectionAis_Object = MibTableColumn
wfAtmAlcFrmOamTxSectionAis = _WfAtmAlcFrmOamTxSectionAis_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 77),
    _WfAtmAlcFrmOamTxSectionAis_Type()
)
wfAtmAlcFrmOamTxSectionAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamTxSectionAis.setStatus("mandatory")


class _WfAtmAlcFrmOamTxPathFebe_Type(Integer32):
    """Custom type wfAtmAlcFrmOamTxPathFebe based on Integer32"""
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


_WfAtmAlcFrmOamTxPathFebe_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamTxPathFebe_Object = MibTableColumn
wfAtmAlcFrmOamTxPathFebe = _WfAtmAlcFrmOamTxPathFebe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 78),
    _WfAtmAlcFrmOamTxPathFebe_Type()
)
wfAtmAlcFrmOamTxPathFebe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamTxPathFebe.setStatus("mandatory")


class _WfAtmAlcFrmOamTxSectionFebe_Type(Integer32):
    """Custom type wfAtmAlcFrmOamTxSectionFebe based on Integer32"""
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


_WfAtmAlcFrmOamTxSectionFebe_Type.__name__ = "Integer32"
_WfAtmAlcFrmOamTxSectionFebe_Object = MibTableColumn
wfAtmAlcFrmOamTxSectionFebe = _WfAtmAlcFrmOamTxSectionFebe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 79),
    _WfAtmAlcFrmOamTxSectionFebe_Type()
)
wfAtmAlcFrmOamTxSectionFebe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmOamTxSectionFebe.setStatus("mandatory")


class _WfAtmAlcFrmStatsSwEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsSwEnable based on Integer32"""
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


_WfAtmAlcFrmStatsSwEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsSwEnable_Object = MibTableColumn
wfAtmAlcFrmStatsSwEnable = _WfAtmAlcFrmStatsSwEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 80),
    _WfAtmAlcFrmStatsSwEnable_Type()
)
wfAtmAlcFrmStatsSwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsSwEnable.setStatus("mandatory")


class _WfAtmAlcFrmStatsMode_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsMode based on Integer32"""
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
        *(("disabled", 1),
          ("header", 2),
          ("header16", 3),
          ("header32", 4))
    )


_WfAtmAlcFrmStatsMode_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsMode_Object = MibTableColumn
wfAtmAlcFrmStatsMode = _WfAtmAlcFrmStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 81),
    _WfAtmAlcFrmStatsMode_Type()
)
wfAtmAlcFrmStatsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsMode.setStatus("mandatory")


class _WfAtmAlcFrmStatsReceive_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsReceive based on Integer32"""
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


_WfAtmAlcFrmStatsReceive_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsReceive_Object = MibTableColumn
wfAtmAlcFrmStatsReceive = _WfAtmAlcFrmStatsReceive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 82),
    _WfAtmAlcFrmStatsReceive_Type()
)
wfAtmAlcFrmStatsReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsReceive.setStatus("mandatory")


class _WfAtmAlcFrmStatsTransmit_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsTransmit based on Integer32"""
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


_WfAtmAlcFrmStatsTransmit_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsTransmit_Object = MibTableColumn
wfAtmAlcFrmStatsTransmit = _WfAtmAlcFrmStatsTransmit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 83),
    _WfAtmAlcFrmStatsTransmit_Type()
)
wfAtmAlcFrmStatsTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsTransmit.setStatus("mandatory")


class _WfAtmAlcFrmStatsMask_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsMask based on Integer32"""
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
        *(("disabled", 1),
          ("hmask", 2),
          ("invalid", 3),
          ("lmask", 4))
    )


_WfAtmAlcFrmStatsMask_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsMask_Object = MibTableColumn
wfAtmAlcFrmStatsMask = _WfAtmAlcFrmStatsMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 84),
    _WfAtmAlcFrmStatsMask_Type()
)
wfAtmAlcFrmStatsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsMask.setStatus("mandatory")
_WfAtmAlcFrmStatsTimeout_Type = Integer32
_WfAtmAlcFrmStatsTimeout_Object = MibTableColumn
wfAtmAlcFrmStatsTimeout = _WfAtmAlcFrmStatsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 85),
    _WfAtmAlcFrmStatsTimeout_Type()
)
wfAtmAlcFrmStatsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsTimeout.setStatus("mandatory")


class _WfAtmAlcFrmStatsTimerEna_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsTimerEna based on Integer32"""
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


_WfAtmAlcFrmStatsTimerEna_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsTimerEna_Object = MibTableColumn
wfAtmAlcFrmStatsTimerEna = _WfAtmAlcFrmStatsTimerEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 86),
    _WfAtmAlcFrmStatsTimerEna_Type()
)
wfAtmAlcFrmStatsTimerEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsTimerEna.setStatus("mandatory")


class _WfAtmAlcFrmStatsOflowEna_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsOflowEna based on Integer32"""
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


_WfAtmAlcFrmStatsOflowEna_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsOflowEna_Object = MibTableColumn
wfAtmAlcFrmStatsOflowEna = _WfAtmAlcFrmStatsOflowEna_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 87),
    _WfAtmAlcFrmStatsOflowEna_Type()
)
wfAtmAlcFrmStatsOflowEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsOflowEna.setStatus("mandatory")


class _WfAtmAlcFrmStatsForceDma_Type(Integer32):
    """Custom type wfAtmAlcFrmStatsForceDma based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dma", 2),
          ("other", 1))
    )


_WfAtmAlcFrmStatsForceDma_Type.__name__ = "Integer32"
_WfAtmAlcFrmStatsForceDma_Object = MibTableColumn
wfAtmAlcFrmStatsForceDma = _WfAtmAlcFrmStatsForceDma_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 88),
    _WfAtmAlcFrmStatsForceDma_Type()
)
wfAtmAlcFrmStatsForceDma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmStatsForceDma.setStatus("mandatory")


class _WfAtmAlcFrmCsiEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmCsiEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiEnable_Object = MibTableColumn
wfAtmAlcFrmCsiEnable = _WfAtmAlcFrmCsiEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 89),
    _WfAtmAlcFrmCsiEnable_Type()
)
wfAtmAlcFrmCsiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiEnable.setStatus("mandatory")


class _WfAtmAlcFrmCsiLoop_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiLoop based on Integer32"""
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


_WfAtmAlcFrmCsiLoop_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiLoop_Object = MibTableColumn
wfAtmAlcFrmCsiLoop = _WfAtmAlcFrmCsiLoop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 90),
    _WfAtmAlcFrmCsiLoop_Type()
)
wfAtmAlcFrmCsiLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiLoop.setStatus("mandatory")


class _WfAtmAlcFrmCsiRcvAtcEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRcvAtcEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmCsiRcvAtcEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRcvAtcEnable_Object = MibTableColumn
wfAtmAlcFrmCsiRcvAtcEnable = _WfAtmAlcFrmCsiRcvAtcEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 91),
    _WfAtmAlcFrmCsiRcvAtcEnable_Type()
)
wfAtmAlcFrmCsiRcvAtcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRcvAtcEnable.setStatus("mandatory")


class _WfAtmAlcFrmCsiRcvAte_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRcvAte based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_WfAtmAlcFrmCsiRcvAte_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRcvAte_Object = MibTableColumn
wfAtmAlcFrmCsiRcvAte = _WfAtmAlcFrmCsiRcvAte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 92),
    _WfAtmAlcFrmCsiRcvAte_Type()
)
wfAtmAlcFrmCsiRcvAte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRcvAte.setStatus("mandatory")


class _WfAtmAlcFrmCsiRcvClpBitOpt_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRcvClpBitOpt based on Integer32"""
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
        *(("force0", 3),
          ("force1", 4),
          ("header", 1),
          ("xlat", 2))
    )


_WfAtmAlcFrmCsiRcvClpBitOpt_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRcvClpBitOpt_Object = MibTableColumn
wfAtmAlcFrmCsiRcvClpBitOpt = _WfAtmAlcFrmCsiRcvClpBitOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 93),
    _WfAtmAlcFrmCsiRcvClpBitOpt_Type()
)
wfAtmAlcFrmCsiRcvClpBitOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRcvClpBitOpt.setStatus("mandatory")


class _WfAtmAlcFrmCsiRcvCongBitOpt_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRcvCongBitOpt based on Integer32"""
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
        *(("force0", 3),
          ("force1", 4),
          ("header", 1),
          ("xlat", 2))
    )


_WfAtmAlcFrmCsiRcvCongBitOpt_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRcvCongBitOpt_Object = MibTableColumn
wfAtmAlcFrmCsiRcvCongBitOpt = _WfAtmAlcFrmCsiRcvCongBitOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 94),
    _WfAtmAlcFrmCsiRcvCongBitOpt_Type()
)
wfAtmAlcFrmCsiRcvCongBitOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRcvCongBitOpt.setStatus("mandatory")


class _WfAtmAlcFrmCsiRoutingTag_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRoutingTag based on Integer32"""
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
        *(("tag0", 1),
          ("tag1", 2),
          ("tag2", 3),
          ("tag3", 4))
    )


_WfAtmAlcFrmCsiRoutingTag_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRoutingTag_Object = MibTableColumn
wfAtmAlcFrmCsiRoutingTag = _WfAtmAlcFrmCsiRoutingTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 95),
    _WfAtmAlcFrmCsiRoutingTag_Type()
)
wfAtmAlcFrmCsiRoutingTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRoutingTag.setStatus("mandatory")


class _WfAtmAlcFrmCsiXmtAtcEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiXmtAtcEnable based on Integer32"""
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


_WfAtmAlcFrmCsiXmtAtcEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiXmtAtcEnable_Object = MibTableColumn
wfAtmAlcFrmCsiXmtAtcEnable = _WfAtmAlcFrmCsiXmtAtcEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 96),
    _WfAtmAlcFrmCsiXmtAtcEnable_Type()
)
wfAtmAlcFrmCsiXmtAtcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiXmtAtcEnable.setStatus("mandatory")


class _WfAtmAlcFrmCsiXmtAte_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiXmtAte based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_WfAtmAlcFrmCsiXmtAte_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiXmtAte_Object = MibTableColumn
wfAtmAlcFrmCsiXmtAte = _WfAtmAlcFrmCsiXmtAte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 97),
    _WfAtmAlcFrmCsiXmtAte_Type()
)
wfAtmAlcFrmCsiXmtAte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiXmtAte.setStatus("mandatory")


class _WfAtmAlcFrmCsiXmtClpBitOpt_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiXmtClpBitOpt based on Integer32"""
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
        *(("force0", 3),
          ("force1", 4),
          ("header", 1),
          ("xlat", 2))
    )


_WfAtmAlcFrmCsiXmtClpBitOpt_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiXmtClpBitOpt_Object = MibTableColumn
wfAtmAlcFrmCsiXmtClpBitOpt = _WfAtmAlcFrmCsiXmtClpBitOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 98),
    _WfAtmAlcFrmCsiXmtClpBitOpt_Type()
)
wfAtmAlcFrmCsiXmtClpBitOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiXmtClpBitOpt.setStatus("mandatory")


class _WfAtmAlcFrmCsiXmtCongBitOpt_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiXmtCongBitOpt based on Integer32"""
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
        *(("force0", 3),
          ("force1", 4),
          ("header", 1),
          ("xlat", 2))
    )


_WfAtmAlcFrmCsiXmtCongBitOpt_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiXmtCongBitOpt_Object = MibTableColumn
wfAtmAlcFrmCsiXmtCongBitOpt = _WfAtmAlcFrmCsiXmtCongBitOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 99),
    _WfAtmAlcFrmCsiXmtCongBitOpt_Type()
)
wfAtmAlcFrmCsiXmtCongBitOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiXmtCongBitOpt.setStatus("mandatory")


class _WfAtmAlcFrmCsiOmitHec_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiOmitHec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cell52byte", 2),
          ("cell53byte", 1))
    )


_WfAtmAlcFrmCsiOmitHec_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiOmitHec_Object = MibTableColumn
wfAtmAlcFrmCsiOmitHec = _WfAtmAlcFrmCsiOmitHec_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 100),
    _WfAtmAlcFrmCsiOmitHec_Type()
)
wfAtmAlcFrmCsiOmitHec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiOmitHec.setStatus("mandatory")


class _WfAtmAlcFrmCsiRcvHecEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRcvHecEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmCsiRcvHecEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRcvHecEnable_Object = MibTableColumn
wfAtmAlcFrmCsiRcvHecEnable = _WfAtmAlcFrmCsiRcvHecEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 101),
    _WfAtmAlcFrmCsiRcvHecEnable_Type()
)
wfAtmAlcFrmCsiRcvHecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRcvHecEnable.setStatus("mandatory")


class _WfAtmAlcFrmCsiRcvHecMask_Type(Integer32):
    """Custom type wfAtmAlcFrmCsiRcvHecMask based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmCsiRcvHecMask_Type.__name__ = "Integer32"
_WfAtmAlcFrmCsiRcvHecMask_Object = MibTableColumn
wfAtmAlcFrmCsiRcvHecMask = _WfAtmAlcFrmCsiRcvHecMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 102),
    _WfAtmAlcFrmCsiRcvHecMask_Type()
)
wfAtmAlcFrmCsiRcvHecMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmCsiRcvHecMask.setStatus("mandatory")


class _WfAtmAlcFrmDmaChan0Enable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaChan0Enable based on Integer32"""
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


_WfAtmAlcFrmDmaChan0Enable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaChan0Enable_Object = MibTableColumn
wfAtmAlcFrmDmaChan0Enable = _WfAtmAlcFrmDmaChan0Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 103),
    _WfAtmAlcFrmDmaChan0Enable_Type()
)
wfAtmAlcFrmDmaChan0Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaChan0Enable.setStatus("mandatory")


class _WfAtmAlcFrmDmaChan1Enable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaChan1Enable based on Integer32"""
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


_WfAtmAlcFrmDmaChan1Enable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaChan1Enable_Object = MibTableColumn
wfAtmAlcFrmDmaChan1Enable = _WfAtmAlcFrmDmaChan1Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 104),
    _WfAtmAlcFrmDmaChan1Enable_Type()
)
wfAtmAlcFrmDmaChan1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaChan1Enable.setStatus("mandatory")


class _WfAtmAlcFrmDmaChan2Enable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaChan2Enable based on Integer32"""
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


_WfAtmAlcFrmDmaChan2Enable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaChan2Enable_Object = MibTableColumn
wfAtmAlcFrmDmaChan2Enable = _WfAtmAlcFrmDmaChan2Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 105),
    _WfAtmAlcFrmDmaChan2Enable_Type()
)
wfAtmAlcFrmDmaChan2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaChan2Enable.setStatus("mandatory")


class _WfAtmAlcFrmDmaChan3Enable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaChan3Enable based on Integer32"""
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


_WfAtmAlcFrmDmaChan3Enable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaChan3Enable_Object = MibTableColumn
wfAtmAlcFrmDmaChan3Enable = _WfAtmAlcFrmDmaChan3Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 106),
    _WfAtmAlcFrmDmaChan3Enable_Type()
)
wfAtmAlcFrmDmaChan3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaChan3Enable.setStatus("mandatory")


class _WfAtmAlcFrmDmaChan4Enable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaChan4Enable based on Integer32"""
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


_WfAtmAlcFrmDmaChan4Enable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaChan4Enable_Object = MibTableColumn
wfAtmAlcFrmDmaChan4Enable = _WfAtmAlcFrmDmaChan4Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 107),
    _WfAtmAlcFrmDmaChan4Enable_Type()
)
wfAtmAlcFrmDmaChan4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaChan4Enable.setStatus("mandatory")


class _WfAtmAlcFrmDmaChan5Enable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaChan5Enable based on Integer32"""
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


_WfAtmAlcFrmDmaChan5Enable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaChan5Enable_Object = MibTableColumn
wfAtmAlcFrmDmaChan5Enable = _WfAtmAlcFrmDmaChan5Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 108),
    _WfAtmAlcFrmDmaChan5Enable_Type()
)
wfAtmAlcFrmDmaChan5Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaChan5Enable.setStatus("mandatory")


class _WfAtmAlcFrmDmaEnable_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaEnable based on Integer32"""
    defaultValue = 1

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


_WfAtmAlcFrmDmaEnable_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaEnable_Object = MibTableColumn
wfAtmAlcFrmDmaEnable = _WfAtmAlcFrmDmaEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 109),
    _WfAtmAlcFrmDmaEnable_Type()
)
wfAtmAlcFrmDmaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaEnable.setStatus("mandatory")


class _WfAtmAlcFrmDmaStop_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaStop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notstopped", 1),
          ("stopped", 2))
    )


_WfAtmAlcFrmDmaStop_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaStop_Object = MibTableColumn
wfAtmAlcFrmDmaStop = _WfAtmAlcFrmDmaStop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 110),
    _WfAtmAlcFrmDmaStop_Type()
)
wfAtmAlcFrmDmaStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaStop.setStatus("mandatory")


class _WfAtmAlcFrmDmaPrioritySel_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaPrioritySel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chan0prio", 1),
          ("chan5prio", 2))
    )


_WfAtmAlcFrmDmaPrioritySel_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaPrioritySel_Object = MibTableColumn
wfAtmAlcFrmDmaPrioritySel = _WfAtmAlcFrmDmaPrioritySel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 111),
    _WfAtmAlcFrmDmaPrioritySel_Type()
)
wfAtmAlcFrmDmaPrioritySel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaPrioritySel.setStatus("mandatory")


class _WfAtmAlcFrmDmaFastXferMode_Type(Integer32):
    """Custom type wfAtmAlcFrmDmaFastXferMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descdma", 1),
          ("fastdma", 2))
    )


_WfAtmAlcFrmDmaFastXferMode_Type.__name__ = "Integer32"
_WfAtmAlcFrmDmaFastXferMode_Object = MibTableColumn
wfAtmAlcFrmDmaFastXferMode = _WfAtmAlcFrmDmaFastXferMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 2, 11, 1, 112),
    _WfAtmAlcFrmDmaFastXferMode_Type()
)
wfAtmAlcFrmDmaFastXferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcFrmDmaFastXferMode.setStatus("mandatory")
_WfAtmCellSwitchGroup_ObjectIdentity = ObjectIdentity
wfAtmCellSwitchGroup = _WfAtmCellSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3)
)
_WfAtmizerCfgTable_Object = MibTable
wfAtmizerCfgTable = _WfAtmizerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1)
)
if mibBuilder.loadTexts:
    wfAtmizerCfgTable.setStatus("mandatory")
_WfAtmizerCfgEntry_Object = MibTableRow
wfAtmizerCfgEntry = _WfAtmizerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1)
)
wfAtmizerCfgEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmizerCfgSlot"),
)
if mibBuilder.loadTexts:
    wfAtmizerCfgEntry.setStatus("mandatory")


class _WfAtmizerCfgSlot_Type(Integer32):
    """Custom type wfAtmizerCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfAtmizerCfgSlot_Type.__name__ = "Integer32"
_WfAtmizerCfgSlot_Object = MibTableColumn
wfAtmizerCfgSlot = _WfAtmizerCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 1),
    _WfAtmizerCfgSlot_Type()
)
wfAtmizerCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerCfgSlot.setStatus("mandatory")
_WfAtmizerCfgMaxVcl_Type = Integer32
_WfAtmizerCfgMaxVcl_Object = MibTableColumn
wfAtmizerCfgMaxVcl = _WfAtmizerCfgMaxVcl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 2),
    _WfAtmizerCfgMaxVcl_Type()
)
wfAtmizerCfgMaxVcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerCfgMaxVcl.setStatus("mandatory")
_WfAtmizerCfgCurrVcl_Type = Integer32
_WfAtmizerCfgCurrVcl_Object = MibTableColumn
wfAtmizerCfgCurrVcl = _WfAtmizerCfgCurrVcl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 3),
    _WfAtmizerCfgCurrVcl_Type()
)
wfAtmizerCfgCurrVcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerCfgCurrVcl.setStatus("mandatory")


class _WfAtmizerCfgRxQueueLenMax_Type(Integer32):
    """Custom type wfAtmizerCfgRxQueueLenMax based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            150
        )
    )
    namedValues = NamedValues(
        ("default", 150)
    )


_WfAtmizerCfgRxQueueLenMax_Type.__name__ = "Integer32"
_WfAtmizerCfgRxQueueLenMax_Object = MibTableColumn
wfAtmizerCfgRxQueueLenMax = _WfAtmizerCfgRxQueueLenMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 4),
    _WfAtmizerCfgRxQueueLenMax_Type()
)
wfAtmizerCfgRxQueueLenMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgRxQueueLenMax.setStatus("mandatory")


class _WfAtmizerCfgRxQueueTmoMax_Type(Integer32):
    """Custom type wfAtmizerCfgRxQueueTmoMax based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("default", 100)
    )


_WfAtmizerCfgRxQueueTmoMax_Type.__name__ = "Integer32"
_WfAtmizerCfgRxQueueTmoMax_Object = MibTableColumn
wfAtmizerCfgRxQueueTmoMax = _WfAtmizerCfgRxQueueTmoMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 5),
    _WfAtmizerCfgRxQueueTmoMax_Type()
)
wfAtmizerCfgRxQueueTmoMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgRxQueueTmoMax.setStatus("mandatory")
_WfAtmizerCfgRxBuffersMax_Type = Integer32
_WfAtmizerCfgRxBuffersMax_Object = MibTableColumn
wfAtmizerCfgRxBuffersMax = _WfAtmizerCfgRxBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 6),
    _WfAtmizerCfgRxBuffersMax_Type()
)
wfAtmizerCfgRxBuffersMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgRxBuffersMax.setStatus("mandatory")
_WfAtmizerCfgRxPagesMax_Type = Integer32
_WfAtmizerCfgRxPagesMax_Object = MibTableColumn
wfAtmizerCfgRxPagesMax = _WfAtmizerCfgRxPagesMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 7),
    _WfAtmizerCfgRxPagesMax_Type()
)
wfAtmizerCfgRxPagesMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgRxPagesMax.setStatus("mandatory")
_WfAtmizerCfgTxBuffersMax_Type = Integer32
_WfAtmizerCfgTxBuffersMax_Object = MibTableColumn
wfAtmizerCfgTxBuffersMax = _WfAtmizerCfgTxBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 8),
    _WfAtmizerCfgTxBuffersMax_Type()
)
wfAtmizerCfgTxBuffersMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgTxBuffersMax.setStatus("mandatory")
_WfAtmizerCfgTxPagesMax_Type = Integer32
_WfAtmizerCfgTxPagesMax_Object = MibTableColumn
wfAtmizerCfgTxPagesMax = _WfAtmizerCfgTxPagesMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 9),
    _WfAtmizerCfgTxPagesMax_Type()
)
wfAtmizerCfgTxPagesMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgTxPagesMax.setStatus("mandatory")


class _WfAtmizerCfgTxPercentRsrcs_Type(Integer32):
    """Custom type wfAtmizerCfgTxPercentRsrcs based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50
        )
    )
    namedValues = NamedValues(
        ("default", 50)
    )


_WfAtmizerCfgTxPercentRsrcs_Type.__name__ = "Integer32"
_WfAtmizerCfgTxPercentRsrcs_Object = MibTableColumn
wfAtmizerCfgTxPercentRsrcs = _WfAtmizerCfgTxPercentRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 10),
    _WfAtmizerCfgTxPercentRsrcs_Type()
)
wfAtmizerCfgTxPercentRsrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgTxPercentRsrcs.setStatus("mandatory")


class _WfAtmizerCfgHeartbeatPeriod_Type(Integer32):
    """Custom type wfAtmizerCfgHeartbeatPeriod based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("default", 3)
    )


_WfAtmizerCfgHeartbeatPeriod_Type.__name__ = "Integer32"
_WfAtmizerCfgHeartbeatPeriod_Object = MibTableColumn
wfAtmizerCfgHeartbeatPeriod = _WfAtmizerCfgHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 11),
    _WfAtmizerCfgHeartbeatPeriod_Type()
)
wfAtmizerCfgHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgHeartbeatPeriod.setStatus("mandatory")
_WfAtmizerRxBuffersMax_Type = Integer32
_WfAtmizerRxBuffersMax_Object = MibTableColumn
wfAtmizerRxBuffersMax = _WfAtmizerRxBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 12),
    _WfAtmizerRxBuffersMax_Type()
)
wfAtmizerRxBuffersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerRxBuffersMax.setStatus("mandatory")
_WfAtmizerRxPagesMax_Type = Integer32
_WfAtmizerRxPagesMax_Object = MibTableColumn
wfAtmizerRxPagesMax = _WfAtmizerRxPagesMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 13),
    _WfAtmizerRxPagesMax_Type()
)
wfAtmizerRxPagesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerRxPagesMax.setStatus("mandatory")
_WfAtmizerTxBuffersMax_Type = Integer32
_WfAtmizerTxBuffersMax_Object = MibTableColumn
wfAtmizerTxBuffersMax = _WfAtmizerTxBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 14),
    _WfAtmizerTxBuffersMax_Type()
)
wfAtmizerTxBuffersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerTxBuffersMax.setStatus("mandatory")
_WfAtmizerTxPagesMax_Type = Integer32
_WfAtmizerTxPagesMax_Object = MibTableColumn
wfAtmizerTxPagesMax = _WfAtmizerTxPagesMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 15),
    _WfAtmizerTxPagesMax_Type()
)
wfAtmizerTxPagesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerTxPagesMax.setStatus("mandatory")
_WfAtmizerTxPercentRsrcs_Type = Integer32
_WfAtmizerTxPercentRsrcs_Object = MibTableColumn
wfAtmizerTxPercentRsrcs = _WfAtmizerTxPercentRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 16),
    _WfAtmizerTxPercentRsrcs_Type()
)
wfAtmizerTxPercentRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerTxPercentRsrcs.setStatus("mandatory")


class _WfAtmizerTxPerVcClipEnable_Type(Integer32):
    """Custom type wfAtmizerTxPerVcClipEnable based on Integer32"""
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


_WfAtmizerTxPerVcClipEnable_Type.__name__ = "Integer32"
_WfAtmizerTxPerVcClipEnable_Object = MibTableColumn
wfAtmizerTxPerVcClipEnable = _WfAtmizerTxPerVcClipEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 17),
    _WfAtmizerTxPerVcClipEnable_Type()
)
wfAtmizerTxPerVcClipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerTxPerVcClipEnable.setStatus("mandatory")
_WfAtmizerCfgTxVcBuffersMax_Type = Integer32
_WfAtmizerCfgTxVcBuffersMax_Object = MibTableColumn
wfAtmizerCfgTxVcBuffersMax = _WfAtmizerCfgTxVcBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 18),
    _WfAtmizerCfgTxVcBuffersMax_Type()
)
wfAtmizerCfgTxVcBuffersMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerCfgTxVcBuffersMax.setStatus("mandatory")
_WfAtmizerTxVcBuffersMax_Type = Integer32
_WfAtmizerTxVcBuffersMax_Object = MibTableColumn
wfAtmizerTxVcBuffersMax = _WfAtmizerTxVcBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 1, 1, 19),
    _WfAtmizerTxVcBuffersMax_Type()
)
wfAtmizerTxVcBuffersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerTxVcBuffersMax.setStatus("mandatory")
_WfAtmizerDrvCfgTable_Object = MibTable
wfAtmizerDrvCfgTable = _WfAtmizerDrvCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2)
)
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgTable.setStatus("mandatory")
_WfAtmizerDrvCfgEntry_Object = MibTableRow
wfAtmizerDrvCfgEntry = _WfAtmizerDrvCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1)
)
wfAtmizerDrvCfgEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmizerDrvCfgSlot"),
    (0, "Wellfleet-ATM-MIB", "wfAtmizerDrvCfgPort"),
)
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgEntry.setStatus("mandatory")


class _WfAtmizerDrvCfgDelete_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfAtmizerDrvCfgDelete_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDelete_Object = MibTableColumn
wfAtmizerDrvCfgDelete = _WfAtmizerDrvCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 1),
    _WfAtmizerDrvCfgDelete_Type()
)
wfAtmizerDrvCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDelete.setStatus("mandatory")


class _WfAtmizerDrvCfgEnable_Type(Integer32):
    """Custom type wfAtmizerDrvCfgEnable based on Integer32"""
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


_WfAtmizerDrvCfgEnable_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgEnable_Object = MibTableColumn
wfAtmizerDrvCfgEnable = _WfAtmizerDrvCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 2),
    _WfAtmizerDrvCfgEnable_Type()
)
wfAtmizerDrvCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgEnable.setStatus("mandatory")


class _WfAtmizerDrvCfgState_Type(Integer32):
    """Custom type wfAtmizerDrvCfgState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("notpresent", 20),
          ("up", 1))
    )


_WfAtmizerDrvCfgState_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgState_Object = MibTableColumn
wfAtmizerDrvCfgState = _WfAtmizerDrvCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 3),
    _WfAtmizerDrvCfgState_Type()
)
wfAtmizerDrvCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgState.setStatus("mandatory")


class _WfAtmizerDrvCfgSlot_Type(Integer32):
    """Custom type wfAtmizerDrvCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfAtmizerDrvCfgSlot_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgSlot_Object = MibTableColumn
wfAtmizerDrvCfgSlot = _WfAtmizerDrvCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 4),
    _WfAtmizerDrvCfgSlot_Type()
)
wfAtmizerDrvCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgSlot.setStatus("mandatory")


class _WfAtmizerDrvCfgPort_Type(Integer32):
    """Custom type wfAtmizerDrvCfgPort based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfAtmizerDrvCfgPort_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgPort_Object = MibTableColumn
wfAtmizerDrvCfgPort = _WfAtmizerDrvCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 5),
    _WfAtmizerDrvCfgPort_Type()
)
wfAtmizerDrvCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgPort.setStatus("mandatory")


class _WfAtmizerDrvCfgCct_Type(Integer32):
    """Custom type wfAtmizerDrvCfgCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfAtmizerDrvCfgCct_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgCct_Object = MibTableColumn
wfAtmizerDrvCfgCct = _WfAtmizerDrvCfgCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 6),
    _WfAtmizerDrvCfgCct_Type()
)
wfAtmizerDrvCfgCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgCct.setStatus("mandatory")
_WfAtmizerDrvCfgLineNumber_Type = Integer32
_WfAtmizerDrvCfgLineNumber_Object = MibTableColumn
wfAtmizerDrvCfgLineNumber = _WfAtmizerDrvCfgLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 7),
    _WfAtmizerDrvCfgLineNumber_Type()
)
wfAtmizerDrvCfgLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgLineNumber.setStatus("mandatory")


class _WfAtmizerDrvCfgType_Type(Integer32):
    """Custom type wfAtmizerDrvCfgType based on Integer32"""
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
        *(("ds1", 4),
          ("ds3", 2),
          ("e1", 5),
          ("e3", 3),
          ("sonet", 1))
    )


_WfAtmizerDrvCfgType_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgType_Object = MibTableColumn
wfAtmizerDrvCfgType = _WfAtmizerDrvCfgType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 8),
    _WfAtmizerDrvCfgType_Type()
)
wfAtmizerDrvCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgType.setStatus("mandatory")


class _WfAtmizerDrvCfgMtu_Type(Integer32):
    """Custom type wfAtmizerDrvCfgMtu based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9188),
    )


_WfAtmizerDrvCfgMtu_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgMtu_Object = MibTableColumn
wfAtmizerDrvCfgMtu = _WfAtmizerDrvCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 9),
    _WfAtmizerDrvCfgMtu_Type()
)
wfAtmizerDrvCfgMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgMtu.setStatus("mandatory")


class _WfAtmizerDrvCfgSpeed_Type(Integer32):
    """Custom type wfAtmizerDrvCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1544000,
              2048000,
              34368000,
              44736000,
              100000000,
              140000000,
              155520000,
              622080000)
        )
    )
    namedValues = NamedValues(
        *(("speed100mb", 100000000),
          ("speed140mb", 140000000),
          ("speed155mb", 155520000),
          ("speed1p544mb", 1544000),
          ("speed2p048mb", 2048000),
          ("speed35mb", 34368000),
          ("speed45mb", 44736000),
          ("speed622mb", 622080000))
    )


_WfAtmizerDrvCfgSpeed_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgSpeed_Object = MibTableColumn
wfAtmizerDrvCfgSpeed = _WfAtmizerDrvCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 10),
    _WfAtmizerDrvCfgSpeed_Type()
)
wfAtmizerDrvCfgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgSpeed.setStatus("mandatory")


class _WfAtmizerDrvCfgDpNotify_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDpNotify based on Integer32"""
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


_WfAtmizerDrvCfgDpNotify_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDpNotify_Object = MibTableColumn
wfAtmizerDrvCfgDpNotify = _WfAtmizerDrvCfgDpNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 11),
    _WfAtmizerDrvCfgDpNotify_Type()
)
wfAtmizerDrvCfgDpNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDpNotify.setStatus("mandatory")


class _WfAtmizerDrvCfgDpNotifyTimeout_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDpNotifyTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WfAtmizerDrvCfgDpNotifyTimeout_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDpNotifyTimeout_Object = MibTableColumn
wfAtmizerDrvCfgDpNotifyTimeout = _WfAtmizerDrvCfgDpNotifyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 12),
    _WfAtmizerDrvCfgDpNotifyTimeout_Type()
)
wfAtmizerDrvCfgDpNotifyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDpNotifyTimeout.setStatus("mandatory")


class _WfAtmizerDrvCfgVcInactEnable_Type(Integer32):
    """Custom type wfAtmizerDrvCfgVcInactEnable based on Integer32"""
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


_WfAtmizerDrvCfgVcInactEnable_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgVcInactEnable_Object = MibTableColumn
wfAtmizerDrvCfgVcInactEnable = _WfAtmizerDrvCfgVcInactEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 13),
    _WfAtmizerDrvCfgVcInactEnable_Type()
)
wfAtmizerDrvCfgVcInactEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgVcInactEnable.setStatus("mandatory")


class _WfAtmizerDrvCfgVcInactTimeout_Type(Integer32):
    """Custom type wfAtmizerDrvCfgVcInactTimeout based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_WfAtmizerDrvCfgVcInactTimeout_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgVcInactTimeout_Object = MibTableColumn
wfAtmizerDrvCfgVcInactTimeout = _WfAtmizerDrvCfgVcInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 14),
    _WfAtmizerDrvCfgVcInactTimeout_Type()
)
wfAtmizerDrvCfgVcInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgVcInactTimeout.setStatus("mandatory")
_WfAtmizerDrvCfgMadrCt_Type = Integer32
_WfAtmizerDrvCfgMadrCt_Object = MibTableColumn
wfAtmizerDrvCfgMadrCt = _WfAtmizerDrvCfgMadrCt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 15),
    _WfAtmizerDrvCfgMadrCt_Type()
)
wfAtmizerDrvCfgMadrCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgMadrCt.setStatus("mandatory")
_WfAtmizerDrvCfgMadr_Type = OctetString
_WfAtmizerDrvCfgMadr_Object = MibTableColumn
wfAtmizerDrvCfgMadr = _WfAtmizerDrvCfgMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 16),
    _WfAtmizerDrvCfgMadr_Type()
)
wfAtmizerDrvCfgMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgMadr.setStatus("mandatory")


class _WfAtmizerDrvCfgFramingMode_Type(Integer32):
    """Custom type wfAtmizerDrvCfgFramingMode based on Integer32"""
    defaultValue = 2

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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("cbit", 3),
          ("cbitnofallback", 7),
          ("clearchannel", 8),
          ("e1adm", 10),
          ("e1plcp", 12),
          ("g751", 5),
          ("g832", 6),
          ("m23", 4),
          ("sdh", 1),
          ("sonet", 2),
          ("t1adm", 9),
          ("t1plcp", 11),
          ("t3cbitplcp", 13),
          ("t3m23plcp", 14))
    )


_WfAtmizerDrvCfgFramingMode_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgFramingMode_Object = MibTableColumn
wfAtmizerDrvCfgFramingMode = _WfAtmizerDrvCfgFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 17),
    _WfAtmizerDrvCfgFramingMode_Type()
)
wfAtmizerDrvCfgFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgFramingMode.setStatus("mandatory")


class _WfAtmizerDrvCfgClkSource_Type(Integer32):
    """Custom type wfAtmizerDrvCfgClkSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extrn", 2),
          ("intrn", 1))
    )


_WfAtmizerDrvCfgClkSource_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgClkSource_Object = MibTableColumn
wfAtmizerDrvCfgClkSource = _WfAtmizerDrvCfgClkSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 18),
    _WfAtmizerDrvCfgClkSource_Type()
)
wfAtmizerDrvCfgClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgClkSource.setStatus("mandatory")


class _WfAtmizerDrvCfgLogLevel_Type(Integer32):
    """Custom type wfAtmizerDrvCfgLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atmcdb2", 2),
          ("atmcdbg", 1),
          ("vcmsg", 4))
    )


_WfAtmizerDrvCfgLogLevel_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgLogLevel_Object = MibTableColumn
wfAtmizerDrvCfgLogLevel = _WfAtmizerDrvCfgLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 19),
    _WfAtmizerDrvCfgLogLevel_Type()
)
wfAtmizerDrvCfgLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgLogLevel.setStatus("mandatory")


class _WfAtmizerDrvCfgDsx3SendCode_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDsx3SendCode based on Integer32"""
    defaultValue = 1

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
        *(("line", 2),
          ("loop", 5),
          ("none", 1),
          ("pattern", 6),
          ("payload", 3),
          ("reset", 4))
    )


_WfAtmizerDrvCfgDsx3SendCode_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDsx3SendCode_Object = MibTableColumn
wfAtmizerDrvCfgDsx3SendCode = _WfAtmizerDrvCfgDsx3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 20),
    _WfAtmizerDrvCfgDsx3SendCode_Type()
)
wfAtmizerDrvCfgDsx3SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDsx3SendCode.setStatus("mandatory")


class _WfAtmizerDrvCfgDsx3LoopbackConfig_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDsx3LoopbackConfig based on Integer32"""
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
        *(("line", 3),
          ("none", 1),
          ("other", 4),
          ("payload", 2))
    )


_WfAtmizerDrvCfgDsx3LoopbackConfig_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDsx3LoopbackConfig_Object = MibTableColumn
wfAtmizerDrvCfgDsx3LoopbackConfig = _WfAtmizerDrvCfgDsx3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 21),
    _WfAtmizerDrvCfgDsx3LoopbackConfig_Type()
)
wfAtmizerDrvCfgDsx3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDsx3LoopbackConfig.setStatus("mandatory")


class _WfAtmizerDrvCfgDs3Scrambling_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDs3Scrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfAtmizerDrvCfgDs3Scrambling_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDs3Scrambling_Object = MibTableColumn
wfAtmizerDrvCfgDs3Scrambling = _WfAtmizerDrvCfgDs3Scrambling_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 22),
    _WfAtmizerDrvCfgDs3Scrambling_Type()
)
wfAtmizerDrvCfgDs3Scrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDs3Scrambling.setStatus("mandatory")


class _WfAtmizerDrvCfgDs3LineBuildOut_Type(Integer32):
    """Custom type wfAtmizerDrvCfgDs3LineBuildOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_WfAtmizerDrvCfgDs3LineBuildOut_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgDs3LineBuildOut_Object = MibTableColumn
wfAtmizerDrvCfgDs3LineBuildOut = _WfAtmizerDrvCfgDs3LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 23),
    _WfAtmizerDrvCfgDs3LineBuildOut_Type()
)
wfAtmizerDrvCfgDs3LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgDs3LineBuildOut.setStatus("mandatory")
_WfAtmizerDrvCfgModule_Type = Integer32
_WfAtmizerDrvCfgModule_Object = MibTableColumn
wfAtmizerDrvCfgModule = _WfAtmizerDrvCfgModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 24),
    _WfAtmizerDrvCfgModule_Type()
)
wfAtmizerDrvCfgModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgModule.setStatus("mandatory")
_WfAtmizerFramingMode_Type = Integer32
_WfAtmizerFramingMode_Object = MibTableColumn
wfAtmizerFramingMode = _WfAtmizerFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 25),
    _WfAtmizerFramingMode_Type()
)
wfAtmizerFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerFramingMode.setStatus("mandatory")


class _WfAtmizerDrvCfgIwfCct_Type(Integer32):
    """Custom type wfAtmizerDrvCfgIwfCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfAtmizerDrvCfgIwfCct_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgIwfCct_Object = MibTableColumn
wfAtmizerDrvCfgIwfCct = _WfAtmizerDrvCfgIwfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 26),
    _WfAtmizerDrvCfgIwfCct_Type()
)
wfAtmizerDrvCfgIwfCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgIwfCct.setStatus("mandatory")


class _WfAtmizerDrvCfgCcType_Type(Integer32):
    """Custom type wfAtmizerDrvCfgCcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atmCc", 4),
          ("mplsMlm", 2),
          ("none", 1))
    )


_WfAtmizerDrvCfgCcType_Type.__name__ = "Integer32"
_WfAtmizerDrvCfgCcType_Object = MibTableColumn
wfAtmizerDrvCfgCcType = _WfAtmizerDrvCfgCcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 27),
    _WfAtmizerDrvCfgCcType_Type()
)
wfAtmizerDrvCfgCcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgCcType.setStatus("mandatory")
_WfAtmizerDrvCfgMaxVcls_Type = Integer32
_WfAtmizerDrvCfgMaxVcls_Object = MibTableColumn
wfAtmizerDrvCfgMaxVcls = _WfAtmizerDrvCfgMaxVcls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 28),
    _WfAtmizerDrvCfgMaxVcls_Type()
)
wfAtmizerDrvCfgMaxVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgMaxVcls.setStatus("mandatory")
_WfAtmizerDrvCfgCurrVcls_Type = Integer32
_WfAtmizerDrvCfgCurrVcls_Object = MibTableColumn
wfAtmizerDrvCfgCurrVcls = _WfAtmizerDrvCfgCurrVcls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 29),
    _WfAtmizerDrvCfgCurrVcls_Type()
)
wfAtmizerDrvCfgCurrVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgCurrVcls.setStatus("mandatory")
_WfAtmizerDrvCfgScrSum_Type = Integer32
_WfAtmizerDrvCfgScrSum_Object = MibTableColumn
wfAtmizerDrvCfgScrSum = _WfAtmizerDrvCfgScrSum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 30),
    _WfAtmizerDrvCfgScrSum_Type()
)
wfAtmizerDrvCfgScrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgScrSum.setStatus("mandatory")


class _WfAtmizerDrvCfgExtRate_Type(Integer32):
    """Custom type wfAtmizerDrvCfgExtRate based on Integer32"""
    defaultValue = 0


_WfAtmizerDrvCfgExtRate_Object = MibTableColumn
wfAtmizerDrvCfgExtRate = _WfAtmizerDrvCfgExtRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 2, 1, 31),
    _WfAtmizerDrvCfgExtRate_Type()
)
wfAtmizerDrvCfgExtRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDrvCfgExtRate.setStatus("mandatory")
_WfAtmizerIntfStatsTable_Object = MibTable
wfAtmizerIntfStatsTable = _WfAtmizerIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3)
)
if mibBuilder.loadTexts:
    wfAtmizerIntfStatsTable.setStatus("mandatory")
_WfAtmizerIntfStatsEntry_Object = MibTableRow
wfAtmizerIntfStatsEntry = _WfAtmizerIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1)
)
wfAtmizerIntfStatsEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmizerIntfSlot"),
    (0, "Wellfleet-ATM-MIB", "wfAtmizerIntfPort"),
)
if mibBuilder.loadTexts:
    wfAtmizerIntfStatsEntry.setStatus("mandatory")


class _WfAtmizerIntfSlot_Type(Integer32):
    """Custom type wfAtmizerIntfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfAtmizerIntfSlot_Type.__name__ = "Integer32"
_WfAtmizerIntfSlot_Object = MibTableColumn
wfAtmizerIntfSlot = _WfAtmizerIntfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 1),
    _WfAtmizerIntfSlot_Type()
)
wfAtmizerIntfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfSlot.setStatus("mandatory")


class _WfAtmizerIntfPort_Type(Integer32):
    """Custom type wfAtmizerIntfPort based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfAtmizerIntfPort_Type.__name__ = "Integer32"
_WfAtmizerIntfPort_Object = MibTableColumn
wfAtmizerIntfPort = _WfAtmizerIntfPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 2),
    _WfAtmizerIntfPort_Type()
)
wfAtmizerIntfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfPort.setStatus("mandatory")
_WfAtmizerIntfLastChange_Type = TimeTicks
_WfAtmizerIntfLastChange_Object = MibTableColumn
wfAtmizerIntfLastChange = _WfAtmizerIntfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 3),
    _WfAtmizerIntfLastChange_Type()
)
wfAtmizerIntfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfLastChange.setStatus("mandatory")
_WfAtmizerIntfOutQLen_Type = Gauge32
_WfAtmizerIntfOutQLen_Object = MibTableColumn
wfAtmizerIntfOutQLen = _WfAtmizerIntfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 4),
    _WfAtmizerIntfOutQLen_Type()
)
wfAtmizerIntfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfOutQLen.setStatus("mandatory")


class _WfAtmizerIntfStatus_Type(Integer32):
    """Custom type wfAtmizerIntfStatus based on Integer32"""
    defaultValue = 4

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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_WfAtmizerIntfStatus_Type.__name__ = "Integer32"
_WfAtmizerIntfStatus_Object = MibTableColumn
wfAtmizerIntfStatus = _WfAtmizerIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 5),
    _WfAtmizerIntfStatus_Type()
)
wfAtmizerIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfStatus.setStatus("mandatory")
_WfAtmizerIntfIndex_Type = Integer32
_WfAtmizerIntfIndex_Object = MibTableColumn
wfAtmizerIntfIndex = _WfAtmizerIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 6),
    _WfAtmizerIntfIndex_Type()
)
wfAtmizerIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfIndex.setStatus("mandatory")
_WfAtmizerIntfOcdEvents_Type = Counter32
_WfAtmizerIntfOcdEvents_Object = MibTableColumn
wfAtmizerIntfOcdEvents = _WfAtmizerIntfOcdEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 7),
    _WfAtmizerIntfOcdEvents_Type()
)
wfAtmizerIntfOcdEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfOcdEvents.setStatus("mandatory")


class _WfAtmizerIntfTcAlarmState_Type(Integer32):
    """Custom type wfAtmizerIntfTcAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("no-alarm", 1))
    )


_WfAtmizerIntfTcAlarmState_Type.__name__ = "Integer32"
_WfAtmizerIntfTcAlarmState_Object = MibTableColumn
wfAtmizerIntfTcAlarmState = _WfAtmizerIntfTcAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 8),
    _WfAtmizerIntfTcAlarmState_Type()
)
wfAtmizerIntfTcAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTcAlarmState.setStatus("mandatory")
_WfAtmizerIntfRxPacketsOkWrap_Type = Counter32
_WfAtmizerIntfRxPacketsOkWrap_Object = MibTableColumn
wfAtmizerIntfRxPacketsOkWrap = _WfAtmizerIntfRxPacketsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 9),
    _WfAtmizerIntfRxPacketsOkWrap_Type()
)
wfAtmizerIntfRxPacketsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxPacketsOkWrap.setStatus("mandatory")
_WfAtmizerIntfRxPacketsOk_Type = Counter32
_WfAtmizerIntfRxPacketsOk_Object = MibTableColumn
wfAtmizerIntfRxPacketsOk = _WfAtmizerIntfRxPacketsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 10),
    _WfAtmizerIntfRxPacketsOk_Type()
)
wfAtmizerIntfRxPacketsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxPacketsOk.setStatus("mandatory")
_WfAtmizerIntfRxCellsOkWrap_Type = Counter32
_WfAtmizerIntfRxCellsOkWrap_Object = MibTableColumn
wfAtmizerIntfRxCellsOkWrap = _WfAtmizerIntfRxCellsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 11),
    _WfAtmizerIntfRxCellsOkWrap_Type()
)
wfAtmizerIntfRxCellsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxCellsOkWrap.setStatus("mandatory")
_WfAtmizerIntfRxCellsOk_Type = Counter32
_WfAtmizerIntfRxCellsOk_Object = MibTableColumn
wfAtmizerIntfRxCellsOk = _WfAtmizerIntfRxCellsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 12),
    _WfAtmizerIntfRxCellsOk_Type()
)
wfAtmizerIntfRxCellsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxCellsOk.setStatus("mandatory")
_WfAtmizerIntfRxOamCount_Type = Counter32
_WfAtmizerIntfRxOamCount_Object = MibTableColumn
wfAtmizerIntfRxOamCount = _WfAtmizerIntfRxOamCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 13),
    _WfAtmizerIntfRxOamCount_Type()
)
wfAtmizerIntfRxOamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxOamCount.setStatus("mandatory")
_WfAtmizerIntfRxFlowCtrlCount_Type = Counter32
_WfAtmizerIntfRxFlowCtrlCount_Object = MibTableColumn
wfAtmizerIntfRxFlowCtrlCount = _WfAtmizerIntfRxFlowCtrlCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 14),
    _WfAtmizerIntfRxFlowCtrlCount_Type()
)
wfAtmizerIntfRxFlowCtrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxFlowCtrlCount.setStatus("mandatory")
_WfAtmizerIntfRxInvalidHeaders_Type = Counter32
_WfAtmizerIntfRxInvalidHeaders_Object = MibTableColumn
wfAtmizerIntfRxInvalidHeaders = _WfAtmizerIntfRxInvalidHeaders_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 15),
    _WfAtmizerIntfRxInvalidHeaders_Type()
)
wfAtmizerIntfRxInvalidHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxInvalidHeaders.setStatus("mandatory")
_WfAtmizerIntfRxOverSizedSDUs_Type = Counter32
_WfAtmizerIntfRxOverSizedSDUs_Object = MibTableColumn
wfAtmizerIntfRxOverSizedSDUs = _WfAtmizerIntfRxOverSizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 16),
    _WfAtmizerIntfRxOverSizedSDUs_Type()
)
wfAtmizerIntfRxOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxOverSizedSDUs.setStatus("mandatory")
_WfAtmizerIntfRxCrcErrors_Type = Counter32
_WfAtmizerIntfRxCrcErrors_Object = MibTableColumn
wfAtmizerIntfRxCrcErrors = _WfAtmizerIntfRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 17),
    _WfAtmizerIntfRxCrcErrors_Type()
)
wfAtmizerIntfRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxCrcErrors.setStatus("mandatory")
_WfAtmizerIntfRxCrc10Errors_Type = Counter32
_WfAtmizerIntfRxCrc10Errors_Object = MibTableColumn
wfAtmizerIntfRxCrc10Errors = _WfAtmizerIntfRxCrc10Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 18),
    _WfAtmizerIntfRxCrc10Errors_Type()
)
wfAtmizerIntfRxCrc10Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxCrc10Errors.setStatus("mandatory")
_WfAtmizerIntfRxLackBufCredits_Type = Counter32
_WfAtmizerIntfRxLackBufCredits_Object = MibTableColumn
wfAtmizerIntfRxLackBufCredits = _WfAtmizerIntfRxLackBufCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 19),
    _WfAtmizerIntfRxLackBufCredits_Type()
)
wfAtmizerIntfRxLackBufCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxLackBufCredits.setStatus("mandatory")
_WfAtmizerIntfRxLackPageCredits_Type = Counter32
_WfAtmizerIntfRxLackPageCredits_Object = MibTableColumn
wfAtmizerIntfRxLackPageCredits = _WfAtmizerIntfRxLackPageCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 20),
    _WfAtmizerIntfRxLackPageCredits_Type()
)
wfAtmizerIntfRxLackPageCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxLackPageCredits.setStatus("mandatory")
_WfAtmizerIntfRxLackBufResc_Type = Counter32
_WfAtmizerIntfRxLackBufResc_Object = MibTableColumn
wfAtmizerIntfRxLackBufResc = _WfAtmizerIntfRxLackBufResc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 21),
    _WfAtmizerIntfRxLackBufResc_Type()
)
wfAtmizerIntfRxLackBufResc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxLackBufResc.setStatus("mandatory")
_WfAtmizerIntfRxLackPageResc_Type = Counter32
_WfAtmizerIntfRxLackPageResc_Object = MibTableColumn
wfAtmizerIntfRxLackPageResc = _WfAtmizerIntfRxLackPageResc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 22),
    _WfAtmizerIntfRxLackPageResc_Type()
)
wfAtmizerIntfRxLackPageResc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxLackPageResc.setStatus("mandatory")
_WfAtmizerIntfTxPacketsOkWrap_Type = Counter32
_WfAtmizerIntfTxPacketsOkWrap_Object = MibTableColumn
wfAtmizerIntfTxPacketsOkWrap = _WfAtmizerIntfTxPacketsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 23),
    _WfAtmizerIntfTxPacketsOkWrap_Type()
)
wfAtmizerIntfTxPacketsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxPacketsOkWrap.setStatus("mandatory")
_WfAtmizerIntfTxPacketsOk_Type = Counter32
_WfAtmizerIntfTxPacketsOk_Object = MibTableColumn
wfAtmizerIntfTxPacketsOk = _WfAtmizerIntfTxPacketsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 24),
    _WfAtmizerIntfTxPacketsOk_Type()
)
wfAtmizerIntfTxPacketsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxPacketsOk.setStatus("mandatory")
_WfAtmizerIntfTxCellsOkWrap_Type = Counter32
_WfAtmizerIntfTxCellsOkWrap_Object = MibTableColumn
wfAtmizerIntfTxCellsOkWrap = _WfAtmizerIntfTxCellsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 25),
    _WfAtmizerIntfTxCellsOkWrap_Type()
)
wfAtmizerIntfTxCellsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxCellsOkWrap.setStatus("mandatory")
_WfAtmizerIntfTxCellsOk_Type = Counter32
_WfAtmizerIntfTxCellsOk_Object = MibTableColumn
wfAtmizerIntfTxCellsOk = _WfAtmizerIntfTxCellsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 26),
    _WfAtmizerIntfTxCellsOk_Type()
)
wfAtmizerIntfTxCellsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxCellsOk.setStatus("mandatory")
_WfAtmizerIntfTxOamCount_Type = Counter32
_WfAtmizerIntfTxOamCount_Object = MibTableColumn
wfAtmizerIntfTxOamCount = _WfAtmizerIntfTxOamCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 27),
    _WfAtmizerIntfTxOamCount_Type()
)
wfAtmizerIntfTxOamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxOamCount.setStatus("mandatory")
_WfAtmizerIntfTxFlowCtrlCount_Type = Counter32
_WfAtmizerIntfTxFlowCtrlCount_Object = MibTableColumn
wfAtmizerIntfTxFlowCtrlCount = _WfAtmizerIntfTxFlowCtrlCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 28),
    _WfAtmizerIntfTxFlowCtrlCount_Type()
)
wfAtmizerIntfTxFlowCtrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxFlowCtrlCount.setStatus("mandatory")
_WfAtmizerIntfTxBadVcs_Type = Counter32
_WfAtmizerIntfTxBadVcs_Object = MibTableColumn
wfAtmizerIntfTxBadVcs = _WfAtmizerIntfTxBadVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 29),
    _WfAtmizerIntfTxBadVcs_Type()
)
wfAtmizerIntfTxBadVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxBadVcs.setStatus("mandatory")
_WfAtmizerIntfTxOverSizedSDUs_Type = Counter32
_WfAtmizerIntfTxOverSizedSDUs_Object = MibTableColumn
wfAtmizerIntfTxOverSizedSDUs = _WfAtmizerIntfTxOverSizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 30),
    _WfAtmizerIntfTxOverSizedSDUs_Type()
)
wfAtmizerIntfTxOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxOverSizedSDUs.setStatus("mandatory")
_WfAtmizerIntfTxLackBufCredits_Type = Counter32
_WfAtmizerIntfTxLackBufCredits_Object = MibTableColumn
wfAtmizerIntfTxLackBufCredits = _WfAtmizerIntfTxLackBufCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 31),
    _WfAtmizerIntfTxLackBufCredits_Type()
)
wfAtmizerIntfTxLackBufCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxLackBufCredits.setStatus("mandatory")
_WfAtmizerIntfTxLackPageCredits_Type = Counter32
_WfAtmizerIntfTxLackPageCredits_Object = MibTableColumn
wfAtmizerIntfTxLackPageCredits = _WfAtmizerIntfTxLackPageCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 32),
    _WfAtmizerIntfTxLackPageCredits_Type()
)
wfAtmizerIntfTxLackPageCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxLackPageCredits.setStatus("mandatory")
_WfAtmizerIntfTxDrvClipCount_Type = Counter32
_WfAtmizerIntfTxDrvClipCount_Object = MibTableColumn
wfAtmizerIntfTxDrvClipCount = _WfAtmizerIntfTxDrvClipCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 33),
    _WfAtmizerIntfTxDrvClipCount_Type()
)
wfAtmizerIntfTxDrvClipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxDrvClipCount.setStatus("mandatory")
_WfAtmizerIntfHecDetectedCount_Type = Counter32
_WfAtmizerIntfHecDetectedCount_Object = MibTableColumn
wfAtmizerIntfHecDetectedCount = _WfAtmizerIntfHecDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 34),
    _WfAtmizerIntfHecDetectedCount_Type()
)
wfAtmizerIntfHecDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfHecDetectedCount.setStatus("mandatory")
_WfAtmizerIntfHecCorrectedCount_Type = Counter32
_WfAtmizerIntfHecCorrectedCount_Object = MibTableColumn
wfAtmizerIntfHecCorrectedCount = _WfAtmizerIntfHecCorrectedCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 35),
    _WfAtmizerIntfHecCorrectedCount_Type()
)
wfAtmizerIntfHecCorrectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfHecCorrectedCount.setStatus("mandatory")
_WfAtmizerIntfRxOctets_Type = Counter32
_WfAtmizerIntfRxOctets_Object = MibTableColumn
wfAtmizerIntfRxOctets = _WfAtmizerIntfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 36),
    _WfAtmizerIntfRxOctets_Type()
)
wfAtmizerIntfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxOctets.setStatus("mandatory")
_WfAtmizerIntfTxOctets_Type = Counter32
_WfAtmizerIntfTxOctets_Object = MibTableColumn
wfAtmizerIntfTxOctets = _WfAtmizerIntfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 37),
    _WfAtmizerIntfTxOctets_Type()
)
wfAtmizerIntfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfTxOctets.setStatus("mandatory")
_WfAtmizerIntfRxUTOPIAErrors_Type = Counter32
_WfAtmizerIntfRxUTOPIAErrors_Object = MibTableColumn
wfAtmizerIntfRxUTOPIAErrors = _WfAtmizerIntfRxUTOPIAErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 38),
    _WfAtmizerIntfRxUTOPIAErrors_Type()
)
wfAtmizerIntfRxUTOPIAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxUTOPIAErrors.setStatus("mandatory")
_WfAtmizerIntfRxLengthErrors_Type = Counter32
_WfAtmizerIntfRxLengthErrors_Object = MibTableColumn
wfAtmizerIntfRxLengthErrors = _WfAtmizerIntfRxLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 39),
    _WfAtmizerIntfRxLengthErrors_Type()
)
wfAtmizerIntfRxLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxLengthErrors.setStatus("mandatory")
_WfAtmizerIntfRxAbortMessages_Type = Counter32
_WfAtmizerIntfRxAbortMessages_Object = MibTableColumn
wfAtmizerIntfRxAbortMessages = _WfAtmizerIntfRxAbortMessages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 40),
    _WfAtmizerIntfRxAbortMessages_Type()
)
wfAtmizerIntfRxAbortMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxAbortMessages.setStatus("mandatory")
_WfAtmizerIntfRxSequenceNumberErrors_Type = Counter32
_WfAtmizerIntfRxSequenceNumberErrors_Object = MibTableColumn
wfAtmizerIntfRxSequenceNumberErrors = _WfAtmizerIntfRxSequenceNumberErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 3, 1, 41),
    _WfAtmizerIntfRxSequenceNumberErrors_Type()
)
wfAtmizerIntfRxSequenceNumberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerIntfRxSequenceNumberErrors.setStatus("mandatory")
_WfAtmizerVclStatsTable_Object = MibTable
wfAtmizerVclStatsTable = _WfAtmizerVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4)
)
if mibBuilder.loadTexts:
    wfAtmizerVclStatsTable.setStatus("mandatory")
_WfAtmizerVclStatsEntry_Object = MibTableRow
wfAtmizerVclStatsEntry = _WfAtmizerVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1)
)
wfAtmizerVclStatsEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmizerVclIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmizerVclVpi"),
    (0, "Wellfleet-ATM-MIB", "wfAtmizerVclVci"),
)
if mibBuilder.loadTexts:
    wfAtmizerVclStatsEntry.setStatus("mandatory")
_WfAtmizerVclIndex_Type = Integer32
_WfAtmizerVclIndex_Object = MibTableColumn
wfAtmizerVclIndex = _WfAtmizerVclIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 1),
    _WfAtmizerVclIndex_Type()
)
wfAtmizerVclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclIndex.setStatus("mandatory")
_WfAtmizerVclVpi_Type = Integer32
_WfAtmizerVclVpi_Object = MibTableColumn
wfAtmizerVclVpi = _WfAtmizerVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 2),
    _WfAtmizerVclVpi_Type()
)
wfAtmizerVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclVpi.setStatus("mandatory")
_WfAtmizerVclVci_Type = Integer32
_WfAtmizerVclVci_Object = MibTableColumn
wfAtmizerVclVci = _WfAtmizerVclVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 3),
    _WfAtmizerVclVci_Type()
)
wfAtmizerVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclVci.setStatus("mandatory")
_WfAtmizerVclRxPacketsOkWrap_Type = Counter32
_WfAtmizerVclRxPacketsOkWrap_Object = MibTableColumn
wfAtmizerVclRxPacketsOkWrap = _WfAtmizerVclRxPacketsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 4),
    _WfAtmizerVclRxPacketsOkWrap_Type()
)
wfAtmizerVclRxPacketsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxPacketsOkWrap.setStatus("mandatory")
_WfAtmizerVclRxPacketsOk_Type = Counter32
_WfAtmizerVclRxPacketsOk_Object = MibTableColumn
wfAtmizerVclRxPacketsOk = _WfAtmizerVclRxPacketsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 5),
    _WfAtmizerVclRxPacketsOk_Type()
)
wfAtmizerVclRxPacketsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxPacketsOk.setStatus("mandatory")
_WfAtmizerVclRxCellsOkWrap_Type = Counter32
_WfAtmizerVclRxCellsOkWrap_Object = MibTableColumn
wfAtmizerVclRxCellsOkWrap = _WfAtmizerVclRxCellsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 6),
    _WfAtmizerVclRxCellsOkWrap_Type()
)
wfAtmizerVclRxCellsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxCellsOkWrap.setStatus("mandatory")
_WfAtmizerVclRxCellsOk_Type = Counter32
_WfAtmizerVclRxCellsOk_Object = MibTableColumn
wfAtmizerVclRxCellsOk = _WfAtmizerVclRxCellsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 7),
    _WfAtmizerVclRxCellsOk_Type()
)
wfAtmizerVclRxCellsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxCellsOk.setStatus("mandatory")
_WfAtmizerVclRxOamCount_Type = Counter32
_WfAtmizerVclRxOamCount_Object = MibTableColumn
wfAtmizerVclRxOamCount = _WfAtmizerVclRxOamCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 8),
    _WfAtmizerVclRxOamCount_Type()
)
wfAtmizerVclRxOamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxOamCount.setStatus("mandatory")
_WfAtmizerVclRxFlowCtrlCount_Type = Counter32
_WfAtmizerVclRxFlowCtrlCount_Object = MibTableColumn
wfAtmizerVclRxFlowCtrlCount = _WfAtmizerVclRxFlowCtrlCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 9),
    _WfAtmizerVclRxFlowCtrlCount_Type()
)
wfAtmizerVclRxFlowCtrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxFlowCtrlCount.setStatus("mandatory")
_WfAtmizerVclRxInvalidHeaders_Type = Counter32
_WfAtmizerVclRxInvalidHeaders_Object = MibTableColumn
wfAtmizerVclRxInvalidHeaders = _WfAtmizerVclRxInvalidHeaders_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 10),
    _WfAtmizerVclRxInvalidHeaders_Type()
)
wfAtmizerVclRxInvalidHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxInvalidHeaders.setStatus("mandatory")
_WfAtmizerVclRxOverSizedSDUs_Type = Counter32
_WfAtmizerVclRxOverSizedSDUs_Object = MibTableColumn
wfAtmizerVclRxOverSizedSDUs = _WfAtmizerVclRxOverSizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 11),
    _WfAtmizerVclRxOverSizedSDUs_Type()
)
wfAtmizerVclRxOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxOverSizedSDUs.setStatus("mandatory")
_WfAtmizerVclRxCrcErrors_Type = Counter32
_WfAtmizerVclRxCrcErrors_Object = MibTableColumn
wfAtmizerVclRxCrcErrors = _WfAtmizerVclRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 12),
    _WfAtmizerVclRxCrcErrors_Type()
)
wfAtmizerVclRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxCrcErrors.setStatus("mandatory")
_WfAtmizerVclRxCrc10Errors_Type = Counter32
_WfAtmizerVclRxCrc10Errors_Object = MibTableColumn
wfAtmizerVclRxCrc10Errors = _WfAtmizerVclRxCrc10Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 13),
    _WfAtmizerVclRxCrc10Errors_Type()
)
wfAtmizerVclRxCrc10Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxCrc10Errors.setStatus("mandatory")
_WfAtmizerVclRxLackBufCredits_Type = Counter32
_WfAtmizerVclRxLackBufCredits_Object = MibTableColumn
wfAtmizerVclRxLackBufCredits = _WfAtmizerVclRxLackBufCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 14),
    _WfAtmizerVclRxLackBufCredits_Type()
)
wfAtmizerVclRxLackBufCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxLackBufCredits.setStatus("mandatory")
_WfAtmizerVclRxLackPageCredits_Type = Counter32
_WfAtmizerVclRxLackPageCredits_Object = MibTableColumn
wfAtmizerVclRxLackPageCredits = _WfAtmizerVclRxLackPageCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 15),
    _WfAtmizerVclRxLackPageCredits_Type()
)
wfAtmizerVclRxLackPageCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxLackPageCredits.setStatus("mandatory")
_WfAtmizerVclRxLackBufResc_Type = Counter32
_WfAtmizerVclRxLackBufResc_Object = MibTableColumn
wfAtmizerVclRxLackBufResc = _WfAtmizerVclRxLackBufResc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 16),
    _WfAtmizerVclRxLackBufResc_Type()
)
wfAtmizerVclRxLackBufResc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxLackBufResc.setStatus("mandatory")
_WfAtmizerVclRxLackPageResc_Type = Counter32
_WfAtmizerVclRxLackPageResc_Object = MibTableColumn
wfAtmizerVclRxLackPageResc = _WfAtmizerVclRxLackPageResc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 17),
    _WfAtmizerVclRxLackPageResc_Type()
)
wfAtmizerVclRxLackPageResc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxLackPageResc.setStatus("mandatory")
_WfAtmizerVclTxPacketsOkWrap_Type = Counter32
_WfAtmizerVclTxPacketsOkWrap_Object = MibTableColumn
wfAtmizerVclTxPacketsOkWrap = _WfAtmizerVclTxPacketsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 18),
    _WfAtmizerVclTxPacketsOkWrap_Type()
)
wfAtmizerVclTxPacketsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxPacketsOkWrap.setStatus("mandatory")
_WfAtmizerVclTxPacketsOk_Type = Counter32
_WfAtmizerVclTxPacketsOk_Object = MibTableColumn
wfAtmizerVclTxPacketsOk = _WfAtmizerVclTxPacketsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 19),
    _WfAtmizerVclTxPacketsOk_Type()
)
wfAtmizerVclTxPacketsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxPacketsOk.setStatus("mandatory")
_WfAtmizerVclTxCellsOkWrap_Type = Counter32
_WfAtmizerVclTxCellsOkWrap_Object = MibTableColumn
wfAtmizerVclTxCellsOkWrap = _WfAtmizerVclTxCellsOkWrap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 20),
    _WfAtmizerVclTxCellsOkWrap_Type()
)
wfAtmizerVclTxCellsOkWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxCellsOkWrap.setStatus("mandatory")
_WfAtmizerVclTxCellsOk_Type = Counter32
_WfAtmizerVclTxCellsOk_Object = MibTableColumn
wfAtmizerVclTxCellsOk = _WfAtmizerVclTxCellsOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 21),
    _WfAtmizerVclTxCellsOk_Type()
)
wfAtmizerVclTxCellsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxCellsOk.setStatus("mandatory")
_WfAtmizerVclTxOamCount_Type = Counter32
_WfAtmizerVclTxOamCount_Object = MibTableColumn
wfAtmizerVclTxOamCount = _WfAtmizerVclTxOamCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 22),
    _WfAtmizerVclTxOamCount_Type()
)
wfAtmizerVclTxOamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxOamCount.setStatus("mandatory")
_WfAtmizerVclTxFlowCtrlCount_Type = Counter32
_WfAtmizerVclTxFlowCtrlCount_Object = MibTableColumn
wfAtmizerVclTxFlowCtrlCount = _WfAtmizerVclTxFlowCtrlCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 23),
    _WfAtmizerVclTxFlowCtrlCount_Type()
)
wfAtmizerVclTxFlowCtrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxFlowCtrlCount.setStatus("mandatory")
_WfAtmizerVclTxOverSizedSDUs_Type = Counter32
_WfAtmizerVclTxOverSizedSDUs_Object = MibTableColumn
wfAtmizerVclTxOverSizedSDUs = _WfAtmizerVclTxOverSizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 24),
    _WfAtmizerVclTxOverSizedSDUs_Type()
)
wfAtmizerVclTxOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxOverSizedSDUs.setStatus("mandatory")
_WfAtmizerVclTxLackBufCredits_Type = Counter32
_WfAtmizerVclTxLackBufCredits_Object = MibTableColumn
wfAtmizerVclTxLackBufCredits = _WfAtmizerVclTxLackBufCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 25),
    _WfAtmizerVclTxLackBufCredits_Type()
)
wfAtmizerVclTxLackBufCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxLackBufCredits.setStatus("mandatory")
_WfAtmizerVclTxLackPageCredits_Type = Counter32
_WfAtmizerVclTxLackPageCredits_Object = MibTableColumn
wfAtmizerVclTxLackPageCredits = _WfAtmizerVclTxLackPageCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 26),
    _WfAtmizerVclTxLackPageCredits_Type()
)
wfAtmizerVclTxLackPageCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxLackPageCredits.setStatus("mandatory")
_WfAtmizerVclRxOctets_Type = Counter32
_WfAtmizerVclRxOctets_Object = MibTableColumn
wfAtmizerVclRxOctets = _WfAtmizerVclRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 27),
    _WfAtmizerVclRxOctets_Type()
)
wfAtmizerVclRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxOctets.setStatus("mandatory")
_WfAtmizerVclTxOctets_Type = Counter32
_WfAtmizerVclTxOctets_Object = MibTableColumn
wfAtmizerVclTxOctets = _WfAtmizerVclTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 28),
    _WfAtmizerVclTxOctets_Type()
)
wfAtmizerVclTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxOctets.setStatus("mandatory")
_WfAtmizerVclTxClipFrames_Type = Counter32
_WfAtmizerVclTxClipFrames_Object = MibTableColumn
wfAtmizerVclTxClipFrames = _WfAtmizerVclTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 29),
    _WfAtmizerVclTxClipFrames_Type()
)
wfAtmizerVclTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclTxClipFrames.setStatus("mandatory")
_WfAtmizerVclRxLengthErrors_Type = Counter32
_WfAtmizerVclRxLengthErrors_Object = MibTableColumn
wfAtmizerVclRxLengthErrors = _WfAtmizerVclRxLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 30),
    _WfAtmizerVclRxLengthErrors_Type()
)
wfAtmizerVclRxLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxLengthErrors.setStatus("mandatory")
_WfAtmizerVclRxAbortMessages_Type = Counter32
_WfAtmizerVclRxAbortMessages_Object = MibTableColumn
wfAtmizerVclRxAbortMessages = _WfAtmizerVclRxAbortMessages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 31),
    _WfAtmizerVclRxAbortMessages_Type()
)
wfAtmizerVclRxAbortMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxAbortMessages.setStatus("mandatory")
_WfAtmizerVclRxSequenceNumberErrors_Type = Counter32
_WfAtmizerVclRxSequenceNumberErrors_Object = MibTableColumn
wfAtmizerVclRxSequenceNumberErrors = _WfAtmizerVclRxSequenceNumberErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 4, 1, 32),
    _WfAtmizerVclRxSequenceNumberErrors_Type()
)
wfAtmizerVclRxSequenceNumberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerVclRxSequenceNumberErrors.setStatus("mandatory")
_WfAtmizerDebugTable_Object = MibTable
wfAtmizerDebugTable = _WfAtmizerDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5)
)
if mibBuilder.loadTexts:
    wfAtmizerDebugTable.setStatus("mandatory")
_WfAtmizerDebugEntry_Object = MibTableRow
wfAtmizerDebugEntry = _WfAtmizerDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1)
)
wfAtmizerDebugEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmizerDebugSlot"),
)
if mibBuilder.loadTexts:
    wfAtmizerDebugEntry.setStatus("mandatory")


class _WfAtmizerDebugSlot_Type(Integer32):
    """Custom type wfAtmizerDebugSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfAtmizerDebugSlot_Type.__name__ = "Integer32"
_WfAtmizerDebugSlot_Object = MibTableColumn
wfAtmizerDebugSlot = _WfAtmizerDebugSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 1),
    _WfAtmizerDebugSlot_Type()
)
wfAtmizerDebugSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmizerDebugSlot.setStatus("mandatory")
_WfAtmizerDebugCmd_Type = Integer32
_WfAtmizerDebugCmd_Object = MibTableColumn
wfAtmizerDebugCmd = _WfAtmizerDebugCmd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 2),
    _WfAtmizerDebugCmd_Type()
)
wfAtmizerDebugCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugCmd.setStatus("mandatory")
_WfAtmizerDebugCmdSize_Type = Integer32
_WfAtmizerDebugCmdSize_Object = MibTableColumn
wfAtmizerDebugCmdSize = _WfAtmizerDebugCmdSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 3),
    _WfAtmizerDebugCmdSize_Type()
)
wfAtmizerDebugCmdSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugCmdSize.setStatus("mandatory")
_WfAtmizerDebugParam1_Type = Integer32
_WfAtmizerDebugParam1_Object = MibTableColumn
wfAtmizerDebugParam1 = _WfAtmizerDebugParam1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 4),
    _WfAtmizerDebugParam1_Type()
)
wfAtmizerDebugParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam1.setStatus("mandatory")
_WfAtmizerDebugParam2_Type = Integer32
_WfAtmizerDebugParam2_Object = MibTableColumn
wfAtmizerDebugParam2 = _WfAtmizerDebugParam2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 5),
    _WfAtmizerDebugParam2_Type()
)
wfAtmizerDebugParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam2.setStatus("mandatory")
_WfAtmizerDebugParam3_Type = Integer32
_WfAtmizerDebugParam3_Object = MibTableColumn
wfAtmizerDebugParam3 = _WfAtmizerDebugParam3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 6),
    _WfAtmizerDebugParam3_Type()
)
wfAtmizerDebugParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam3.setStatus("mandatory")
_WfAtmizerDebugParam4_Type = Integer32
_WfAtmizerDebugParam4_Object = MibTableColumn
wfAtmizerDebugParam4 = _WfAtmizerDebugParam4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 7),
    _WfAtmizerDebugParam4_Type()
)
wfAtmizerDebugParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam4.setStatus("mandatory")
_WfAtmizerDebugParam5_Type = Integer32
_WfAtmizerDebugParam5_Object = MibTableColumn
wfAtmizerDebugParam5 = _WfAtmizerDebugParam5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 8),
    _WfAtmizerDebugParam5_Type()
)
wfAtmizerDebugParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam5.setStatus("mandatory")
_WfAtmizerDebugParam6_Type = Integer32
_WfAtmizerDebugParam6_Object = MibTableColumn
wfAtmizerDebugParam6 = _WfAtmizerDebugParam6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 9),
    _WfAtmizerDebugParam6_Type()
)
wfAtmizerDebugParam6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam6.setStatus("mandatory")
_WfAtmizerDebugParam7_Type = Integer32
_WfAtmizerDebugParam7_Object = MibTableColumn
wfAtmizerDebugParam7 = _WfAtmizerDebugParam7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 10),
    _WfAtmizerDebugParam7_Type()
)
wfAtmizerDebugParam7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam7.setStatus("mandatory")
_WfAtmizerDebugParam8_Type = Integer32
_WfAtmizerDebugParam8_Object = MibTableColumn
wfAtmizerDebugParam8 = _WfAtmizerDebugParam8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 11),
    _WfAtmizerDebugParam8_Type()
)
wfAtmizerDebugParam8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam8.setStatus("mandatory")
_WfAtmizerDebugParam9_Type = Integer32
_WfAtmizerDebugParam9_Object = MibTableColumn
wfAtmizerDebugParam9 = _WfAtmizerDebugParam9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 12),
    _WfAtmizerDebugParam9_Type()
)
wfAtmizerDebugParam9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam9.setStatus("mandatory")
_WfAtmizerDebugParam10_Type = Integer32
_WfAtmizerDebugParam10_Object = MibTableColumn
wfAtmizerDebugParam10 = _WfAtmizerDebugParam10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 13),
    _WfAtmizerDebugParam10_Type()
)
wfAtmizerDebugParam10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugParam10.setStatus("mandatory")


class _WfAtmizerDebugRxDone_Type(Integer32):
    """Custom type wfAtmizerDebugRxDone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("err", 16),
          ("inprog", 1))
    )


_WfAtmizerDebugRxDone_Type.__name__ = "Integer32"
_WfAtmizerDebugRxDone_Object = MibTableColumn
wfAtmizerDebugRxDone = _WfAtmizerDebugRxDone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 14),
    _WfAtmizerDebugRxDone_Type()
)
wfAtmizerDebugRxDone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugRxDone.setStatus("mandatory")
_WfAtmizerDebugRxValue_Type = OctetString
_WfAtmizerDebugRxValue_Object = MibTableColumn
wfAtmizerDebugRxValue = _WfAtmizerDebugRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 15),
    _WfAtmizerDebugRxValue_Type()
)
wfAtmizerDebugRxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugRxValue.setStatus("mandatory")


class _WfAtmizerDebugTxDone_Type(Integer32):
    """Custom type wfAtmizerDebugTxDone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("err", 16),
          ("inprog", 1))
    )


_WfAtmizerDebugTxDone_Type.__name__ = "Integer32"
_WfAtmizerDebugTxDone_Object = MibTableColumn
wfAtmizerDebugTxDone = _WfAtmizerDebugTxDone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 16),
    _WfAtmizerDebugTxDone_Type()
)
wfAtmizerDebugTxDone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugTxDone.setStatus("mandatory")
_WfAtmizerDebugTxValue_Type = OctetString
_WfAtmizerDebugTxValue_Object = MibTableColumn
wfAtmizerDebugTxValue = _WfAtmizerDebugTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 3, 5, 1, 17),
    _WfAtmizerDebugTxValue_Type()
)
wfAtmizerDebugTxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerDebugTxValue.setStatus("mandatory")
_WfSonetMediumTable_Object = MibTable
wfSonetMediumTable = _WfSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1)
)
if mibBuilder.loadTexts:
    wfSonetMediumTable.setStatus("mandatory")
_WfSonetMediumEntry_Object = MibTableRow
wfSonetMediumEntry = _WfSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1)
)
wfSonetMediumEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetMediumIndex"),
)
if mibBuilder.loadTexts:
    wfSonetMediumEntry.setStatus("mandatory")
_WfSonetMediumIndex_Type = Integer32
_WfSonetMediumIndex_Object = MibTableColumn
wfSonetMediumIndex = _WfSonetMediumIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 1),
    _WfSonetMediumIndex_Type()
)
wfSonetMediumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumIndex.setStatus("mandatory")
_WfSonetMediumType_Type = Integer32
_WfSonetMediumType_Object = MibTableColumn
wfSonetMediumType = _WfSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 2),
    _WfSonetMediumType_Type()
)
wfSonetMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumType.setStatus("mandatory")
_WfSonetMediumTimeElapsed_Type = Integer32
_WfSonetMediumTimeElapsed_Object = MibTableColumn
wfSonetMediumTimeElapsed = _WfSonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 3),
    _WfSonetMediumTimeElapsed_Type()
)
wfSonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumTimeElapsed.setStatus("mandatory")
_WfSonetMediumValidIntervals_Type = Integer32
_WfSonetMediumValidIntervals_Object = MibTableColumn
wfSonetMediumValidIntervals = _WfSonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 4),
    _WfSonetMediumValidIntervals_Type()
)
wfSonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumValidIntervals.setStatus("mandatory")


class _WfSonetMediumLineCoding_Type(Integer32):
    """Custom type wfSonetMediumLineCoding based on Integer32"""
    defaultValue = 4

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
        *(("b3zs", 2),
          ("cmi", 3),
          ("nrz", 4),
          ("other", 1),
          ("rz", 5))
    )


_WfSonetMediumLineCoding_Type.__name__ = "Integer32"
_WfSonetMediumLineCoding_Object = MibTableColumn
wfSonetMediumLineCoding = _WfSonetMediumLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 5),
    _WfSonetMediumLineCoding_Type()
)
wfSonetMediumLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumLineCoding.setStatus("mandatory")


class _WfSonetMediumLineType_Type(Integer32):
    """Custom type wfSonetMediumLineType based on Integer32"""
    defaultValue = 2

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
        *(("coax", 5),
          ("longsinglemode", 3),
          ("multimode", 4),
          ("other", 1),
          ("shortsinglemode", 2),
          ("utp", 6))
    )


_WfSonetMediumLineType_Type.__name__ = "Integer32"
_WfSonetMediumLineType_Object = MibTableColumn
wfSonetMediumLineType = _WfSonetMediumLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 6),
    _WfSonetMediumLineType_Type()
)
wfSonetMediumLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumLineType.setStatus("mandatory")
_WfSonetMediumCircuitIdentifier_Type = DisplayString
_WfSonetMediumCircuitIdentifier_Object = MibTableColumn
wfSonetMediumCircuitIdentifier = _WfSonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 1, 1, 7),
    _WfSonetMediumCircuitIdentifier_Type()
)
wfSonetMediumCircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetMediumCircuitIdentifier.setStatus("mandatory")
_WfSonetSectionCurrentTable_Object = MibTable
wfSonetSectionCurrentTable = _WfSonetSectionCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2)
)
if mibBuilder.loadTexts:
    wfSonetSectionCurrentTable.setStatus("mandatory")
_WfSonetSectionCurrentEntry_Object = MibTableRow
wfSonetSectionCurrentEntry = _WfSonetSectionCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1)
)
wfSonetSectionCurrentEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetSectionCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfSonetSectionCurrentEntry.setStatus("mandatory")
_WfSonetSectionCurrentIndex_Type = Integer32
_WfSonetSectionCurrentIndex_Object = MibTableColumn
wfSonetSectionCurrentIndex = _WfSonetSectionCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1, 1),
    _WfSonetSectionCurrentIndex_Type()
)
wfSonetSectionCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionCurrentIndex.setStatus("mandatory")


class _WfSonetSectionCurrentStatus_Type(Integer32):
    """Custom type wfSonetSectionCurrentStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lof", 4),
          ("los", 2),
          ("nodefect", 1))
    )


_WfSonetSectionCurrentStatus_Type.__name__ = "Integer32"
_WfSonetSectionCurrentStatus_Object = MibTableColumn
wfSonetSectionCurrentStatus = _WfSonetSectionCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1, 2),
    _WfSonetSectionCurrentStatus_Type()
)
wfSonetSectionCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionCurrentStatus.setStatus("mandatory")
_WfSonetSectionCurrentESs_Type = Gauge32
_WfSonetSectionCurrentESs_Object = MibTableColumn
wfSonetSectionCurrentESs = _WfSonetSectionCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1, 3),
    _WfSonetSectionCurrentESs_Type()
)
wfSonetSectionCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionCurrentESs.setStatus("mandatory")
_WfSonetSectionCurrentSESs_Type = Gauge32
_WfSonetSectionCurrentSESs_Object = MibTableColumn
wfSonetSectionCurrentSESs = _WfSonetSectionCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1, 4),
    _WfSonetSectionCurrentSESs_Type()
)
wfSonetSectionCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionCurrentSESs.setStatus("mandatory")
_WfSonetSectionCurrentSEFSs_Type = Gauge32
_WfSonetSectionCurrentSEFSs_Object = MibTableColumn
wfSonetSectionCurrentSEFSs = _WfSonetSectionCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1, 5),
    _WfSonetSectionCurrentSEFSs_Type()
)
wfSonetSectionCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionCurrentSEFSs.setStatus("mandatory")
_WfSonetSectionCurrentCVs_Type = Gauge32
_WfSonetSectionCurrentCVs_Object = MibTableColumn
wfSonetSectionCurrentCVs = _WfSonetSectionCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 2, 1, 6),
    _WfSonetSectionCurrentCVs_Type()
)
wfSonetSectionCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionCurrentCVs.setStatus("mandatory")
_WfSonetSectionIntervalTable_Object = MibTable
wfSonetSectionIntervalTable = _WfSonetSectionIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3)
)
if mibBuilder.loadTexts:
    wfSonetSectionIntervalTable.setStatus("mandatory")
_WfSonetSectionIntervalEntry_Object = MibTableRow
wfSonetSectionIntervalEntry = _WfSonetSectionIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1)
)
wfSonetSectionIntervalEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetSectionIntervalIndex"),
    (0, "Wellfleet-ATM-MIB", "wfSonetSectionIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfSonetSectionIntervalEntry.setStatus("mandatory")
_WfSonetSectionIntervalIndex_Type = Integer32
_WfSonetSectionIntervalIndex_Object = MibTableColumn
wfSonetSectionIntervalIndex = _WfSonetSectionIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1, 1),
    _WfSonetSectionIntervalIndex_Type()
)
wfSonetSectionIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionIntervalIndex.setStatus("mandatory")
_WfSonetSectionIntervalNumber_Type = Integer32
_WfSonetSectionIntervalNumber_Object = MibTableColumn
wfSonetSectionIntervalNumber = _WfSonetSectionIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1, 2),
    _WfSonetSectionIntervalNumber_Type()
)
wfSonetSectionIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionIntervalNumber.setStatus("mandatory")
_WfSonetSectionIntervalESs_Type = Gauge32
_WfSonetSectionIntervalESs_Object = MibTableColumn
wfSonetSectionIntervalESs = _WfSonetSectionIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1, 3),
    _WfSonetSectionIntervalESs_Type()
)
wfSonetSectionIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionIntervalESs.setStatus("mandatory")
_WfSonetSectionIntervalSESs_Type = Gauge32
_WfSonetSectionIntervalSESs_Object = MibTableColumn
wfSonetSectionIntervalSESs = _WfSonetSectionIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1, 4),
    _WfSonetSectionIntervalSESs_Type()
)
wfSonetSectionIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionIntervalSESs.setStatus("mandatory")
_WfSonetSectionIntervalSEFSs_Type = Gauge32
_WfSonetSectionIntervalSEFSs_Object = MibTableColumn
wfSonetSectionIntervalSEFSs = _WfSonetSectionIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1, 5),
    _WfSonetSectionIntervalSEFSs_Type()
)
wfSonetSectionIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionIntervalSEFSs.setStatus("mandatory")
_WfSonetSectionIntervalCVs_Type = Gauge32
_WfSonetSectionIntervalCVs_Object = MibTableColumn
wfSonetSectionIntervalCVs = _WfSonetSectionIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 3, 1, 6),
    _WfSonetSectionIntervalCVs_Type()
)
wfSonetSectionIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetSectionIntervalCVs.setStatus("mandatory")
_WfSonetLineCurrentTable_Object = MibTable
wfSonetLineCurrentTable = _WfSonetLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4)
)
if mibBuilder.loadTexts:
    wfSonetLineCurrentTable.setStatus("mandatory")
_WfSonetLineCurrentEntry_Object = MibTableRow
wfSonetLineCurrentEntry = _WfSonetLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1)
)
wfSonetLineCurrentEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetLineCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfSonetLineCurrentEntry.setStatus("mandatory")
_WfSonetLineCurrentIndex_Type = Integer32
_WfSonetLineCurrentIndex_Object = MibTableColumn
wfSonetLineCurrentIndex = _WfSonetLineCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1, 1),
    _WfSonetLineCurrentIndex_Type()
)
wfSonetLineCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineCurrentIndex.setStatus("mandatory")


class _WfSonetLineCurrentStatus_Type(Integer32):
    """Custom type wfSonetLineCurrentStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("nodefect", 1),
          ("rdi", 4))
    )


_WfSonetLineCurrentStatus_Type.__name__ = "Integer32"
_WfSonetLineCurrentStatus_Object = MibTableColumn
wfSonetLineCurrentStatus = _WfSonetLineCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1, 2),
    _WfSonetLineCurrentStatus_Type()
)
wfSonetLineCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineCurrentStatus.setStatus("mandatory")
_WfSonetLineCurrentESs_Type = Gauge32
_WfSonetLineCurrentESs_Object = MibTableColumn
wfSonetLineCurrentESs = _WfSonetLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1, 3),
    _WfSonetLineCurrentESs_Type()
)
wfSonetLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineCurrentESs.setStatus("mandatory")
_WfSonetLineCurrentSESs_Type = Gauge32
_WfSonetLineCurrentSESs_Object = MibTableColumn
wfSonetLineCurrentSESs = _WfSonetLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1, 4),
    _WfSonetLineCurrentSESs_Type()
)
wfSonetLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineCurrentSESs.setStatus("mandatory")
_WfSonetLineCurrentCVs_Type = Gauge32
_WfSonetLineCurrentCVs_Object = MibTableColumn
wfSonetLineCurrentCVs = _WfSonetLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1, 5),
    _WfSonetLineCurrentCVs_Type()
)
wfSonetLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineCurrentCVs.setStatus("mandatory")
_WfSonetLineCurrentUASs_Type = Gauge32
_WfSonetLineCurrentUASs_Object = MibTableColumn
wfSonetLineCurrentUASs = _WfSonetLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 4, 1, 6),
    _WfSonetLineCurrentUASs_Type()
)
wfSonetLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineCurrentUASs.setStatus("mandatory")
_WfSonetLineIntervalTable_Object = MibTable
wfSonetLineIntervalTable = _WfSonetLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5)
)
if mibBuilder.loadTexts:
    wfSonetLineIntervalTable.setStatus("mandatory")
_WfSonetLineIntervalEntry_Object = MibTableRow
wfSonetLineIntervalEntry = _WfSonetLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1)
)
wfSonetLineIntervalEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetLineIntervalIndex"),
    (0, "Wellfleet-ATM-MIB", "wfSonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfSonetLineIntervalEntry.setStatus("mandatory")
_WfSonetLineIntervalIndex_Type = Integer32
_WfSonetLineIntervalIndex_Object = MibTableColumn
wfSonetLineIntervalIndex = _WfSonetLineIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1, 1),
    _WfSonetLineIntervalIndex_Type()
)
wfSonetLineIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineIntervalIndex.setStatus("mandatory")
_WfSonetLineIntervalNumber_Type = Integer32
_WfSonetLineIntervalNumber_Object = MibTableColumn
wfSonetLineIntervalNumber = _WfSonetLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1, 2),
    _WfSonetLineIntervalNumber_Type()
)
wfSonetLineIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineIntervalNumber.setStatus("mandatory")
_WfSonetLineIntervalESs_Type = Gauge32
_WfSonetLineIntervalESs_Object = MibTableColumn
wfSonetLineIntervalESs = _WfSonetLineIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1, 3),
    _WfSonetLineIntervalESs_Type()
)
wfSonetLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineIntervalESs.setStatus("mandatory")
_WfSonetLineIntervalSESs_Type = Gauge32
_WfSonetLineIntervalSESs_Object = MibTableColumn
wfSonetLineIntervalSESs = _WfSonetLineIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1, 4),
    _WfSonetLineIntervalSESs_Type()
)
wfSonetLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineIntervalSESs.setStatus("mandatory")
_WfSonetLineIntervalCVs_Type = Gauge32
_WfSonetLineIntervalCVs_Object = MibTableColumn
wfSonetLineIntervalCVs = _WfSonetLineIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1, 5),
    _WfSonetLineIntervalCVs_Type()
)
wfSonetLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineIntervalCVs.setStatus("mandatory")
_WfSonetLineIntervalUASs_Type = Gauge32
_WfSonetLineIntervalUASs_Object = MibTableColumn
wfSonetLineIntervalUASs = _WfSonetLineIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 5, 1, 6),
    _WfSonetLineIntervalUASs_Type()
)
wfSonetLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetLineIntervalUASs.setStatus("mandatory")
_WfSonetFarEndLineCurrentTable_Object = MibTable
wfSonetFarEndLineCurrentTable = _WfSonetFarEndLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6)
)
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentTable.setStatus("mandatory")
_WfSonetFarEndLineCurrentEntry_Object = MibTableRow
wfSonetFarEndLineCurrentEntry = _WfSonetFarEndLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6, 1)
)
wfSonetFarEndLineCurrentEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetFarEndLineCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentEntry.setStatus("mandatory")
_WfSonetFarEndLineCurrentIndex_Type = Integer32
_WfSonetFarEndLineCurrentIndex_Object = MibTableColumn
wfSonetFarEndLineCurrentIndex = _WfSonetFarEndLineCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6, 1, 1),
    _WfSonetFarEndLineCurrentIndex_Type()
)
wfSonetFarEndLineCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentIndex.setStatus("mandatory")
_WfSonetFarEndLineCurrentESs_Type = Gauge32
_WfSonetFarEndLineCurrentESs_Object = MibTableColumn
wfSonetFarEndLineCurrentESs = _WfSonetFarEndLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6, 1, 2),
    _WfSonetFarEndLineCurrentESs_Type()
)
wfSonetFarEndLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentESs.setStatus("mandatory")
_WfSonetFarEndLineCurrentSESs_Type = Gauge32
_WfSonetFarEndLineCurrentSESs_Object = MibTableColumn
wfSonetFarEndLineCurrentSESs = _WfSonetFarEndLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6, 1, 3),
    _WfSonetFarEndLineCurrentSESs_Type()
)
wfSonetFarEndLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentSESs.setStatus("mandatory")
_WfSonetFarEndLineCurrentCVs_Type = Gauge32
_WfSonetFarEndLineCurrentCVs_Object = MibTableColumn
wfSonetFarEndLineCurrentCVs = _WfSonetFarEndLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6, 1, 4),
    _WfSonetFarEndLineCurrentCVs_Type()
)
wfSonetFarEndLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentCVs.setStatus("mandatory")
_WfSonetFarEndLineCurrentUASs_Type = Gauge32
_WfSonetFarEndLineCurrentUASs_Object = MibTableColumn
wfSonetFarEndLineCurrentUASs = _WfSonetFarEndLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 6, 1, 5),
    _WfSonetFarEndLineCurrentUASs_Type()
)
wfSonetFarEndLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineCurrentUASs.setStatus("mandatory")
_WfSonetFarEndLineIntervalTable_Object = MibTable
wfSonetFarEndLineIntervalTable = _WfSonetFarEndLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7)
)
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalTable.setStatus("mandatory")
_WfSonetFarEndLineIntervalEntry_Object = MibTableRow
wfSonetFarEndLineIntervalEntry = _WfSonetFarEndLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1)
)
wfSonetFarEndLineIntervalEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetFarEndLineIntervalIndex"),
    (0, "Wellfleet-ATM-MIB", "wfSonetFarEndLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalEntry.setStatus("mandatory")
_WfSonetFarEndLineIntervalIndex_Type = Integer32
_WfSonetFarEndLineIntervalIndex_Object = MibTableColumn
wfSonetFarEndLineIntervalIndex = _WfSonetFarEndLineIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1, 1),
    _WfSonetFarEndLineIntervalIndex_Type()
)
wfSonetFarEndLineIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalIndex.setStatus("mandatory")
_WfSonetFarEndLineIntervalNumber_Type = Integer32
_WfSonetFarEndLineIntervalNumber_Object = MibTableColumn
wfSonetFarEndLineIntervalNumber = _WfSonetFarEndLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1, 2),
    _WfSonetFarEndLineIntervalNumber_Type()
)
wfSonetFarEndLineIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalNumber.setStatus("mandatory")
_WfSonetFarEndLineIntervalESs_Type = Gauge32
_WfSonetFarEndLineIntervalESs_Object = MibTableColumn
wfSonetFarEndLineIntervalESs = _WfSonetFarEndLineIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1, 3),
    _WfSonetFarEndLineIntervalESs_Type()
)
wfSonetFarEndLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalESs.setStatus("mandatory")
_WfSonetFarEndLineIntervalSESs_Type = Gauge32
_WfSonetFarEndLineIntervalSESs_Object = MibTableColumn
wfSonetFarEndLineIntervalSESs = _WfSonetFarEndLineIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1, 4),
    _WfSonetFarEndLineIntervalSESs_Type()
)
wfSonetFarEndLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalSESs.setStatus("mandatory")
_WfSonetFarEndLineIntervalCVs_Type = Gauge32
_WfSonetFarEndLineIntervalCVs_Object = MibTableColumn
wfSonetFarEndLineIntervalCVs = _WfSonetFarEndLineIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1, 5),
    _WfSonetFarEndLineIntervalCVs_Type()
)
wfSonetFarEndLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalCVs.setStatus("mandatory")
_WfSonetFarEndLineIntervalUASs_Type = Gauge32
_WfSonetFarEndLineIntervalUASs_Object = MibTableColumn
wfSonetFarEndLineIntervalUASs = _WfSonetFarEndLineIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 7, 1, 6),
    _WfSonetFarEndLineIntervalUASs_Type()
)
wfSonetFarEndLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndLineIntervalUASs.setStatus("mandatory")
_WfSonetPathCurrentTable_Object = MibTable
wfSonetPathCurrentTable = _WfSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8)
)
if mibBuilder.loadTexts:
    wfSonetPathCurrentTable.setStatus("mandatory")
_WfSonetPathCurrentEntry_Object = MibTableRow
wfSonetPathCurrentEntry = _WfSonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1)
)
wfSonetPathCurrentEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetPathCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfSonetPathCurrentEntry.setStatus("mandatory")
_WfSonetPathCurrentIndex_Type = Integer32
_WfSonetPathCurrentIndex_Object = MibTableColumn
wfSonetPathCurrentIndex = _WfSonetPathCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 1),
    _WfSonetPathCurrentIndex_Type()
)
wfSonetPathCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentIndex.setStatus("mandatory")


class _WfSonetPathCurrentWidth_Type(Integer32):
    """Custom type wfSonetPathCurrentWidth based on Integer32"""
    defaultValue = 2

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
        *(("sts1", 1),
          ("sts12cstm4", 3),
          ("sts24c", 4),
          ("sts3cstm1", 2),
          ("sts48cstm16", 5))
    )


_WfSonetPathCurrentWidth_Type.__name__ = "Integer32"
_WfSonetPathCurrentWidth_Object = MibTableColumn
wfSonetPathCurrentWidth = _WfSonetPathCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 2),
    _WfSonetPathCurrentWidth_Type()
)
wfSonetPathCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentWidth.setStatus("mandatory")


class _WfSonetPathCurrentStatus_Type(Integer32):
    """Custom type wfSonetPathCurrentStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("nodefect", 1),
          ("siglabelmis", 32),
          ("stsais", 4),
          ("stslop", 2),
          ("stsrdi", 8),
          ("unequipped", 16))
    )


_WfSonetPathCurrentStatus_Type.__name__ = "Integer32"
_WfSonetPathCurrentStatus_Object = MibTableColumn
wfSonetPathCurrentStatus = _WfSonetPathCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 3),
    _WfSonetPathCurrentStatus_Type()
)
wfSonetPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentStatus.setStatus("mandatory")
_WfSonetPathCurrentESs_Type = Gauge32
_WfSonetPathCurrentESs_Object = MibTableColumn
wfSonetPathCurrentESs = _WfSonetPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 4),
    _WfSonetPathCurrentESs_Type()
)
wfSonetPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentESs.setStatus("mandatory")
_WfSonetPathCurrentSESs_Type = Gauge32
_WfSonetPathCurrentSESs_Object = MibTableColumn
wfSonetPathCurrentSESs = _WfSonetPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 5),
    _WfSonetPathCurrentSESs_Type()
)
wfSonetPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentSESs.setStatus("mandatory")
_WfSonetPathCurrentCVs_Type = Gauge32
_WfSonetPathCurrentCVs_Object = MibTableColumn
wfSonetPathCurrentCVs = _WfSonetPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 6),
    _WfSonetPathCurrentCVs_Type()
)
wfSonetPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentCVs.setStatus("mandatory")
_WfSonetPathCurrentUASs_Type = Gauge32
_WfSonetPathCurrentUASs_Object = MibTableColumn
wfSonetPathCurrentUASs = _WfSonetPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 8, 1, 7),
    _WfSonetPathCurrentUASs_Type()
)
wfSonetPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathCurrentUASs.setStatus("mandatory")
_WfSonetPathIntervalTable_Object = MibTable
wfSonetPathIntervalTable = _WfSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9)
)
if mibBuilder.loadTexts:
    wfSonetPathIntervalTable.setStatus("mandatory")
_WfSonetPathIntervalEntry_Object = MibTableRow
wfSonetPathIntervalEntry = _WfSonetPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1)
)
wfSonetPathIntervalEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetPathIntervalIndex"),
    (0, "Wellfleet-ATM-MIB", "wfSonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfSonetPathIntervalEntry.setStatus("mandatory")
_WfSonetPathIntervalIndex_Type = Integer32
_WfSonetPathIntervalIndex_Object = MibTableColumn
wfSonetPathIntervalIndex = _WfSonetPathIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1, 1),
    _WfSonetPathIntervalIndex_Type()
)
wfSonetPathIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathIntervalIndex.setStatus("mandatory")
_WfSonetPathIntervalNumber_Type = Integer32
_WfSonetPathIntervalNumber_Object = MibTableColumn
wfSonetPathIntervalNumber = _WfSonetPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1, 2),
    _WfSonetPathIntervalNumber_Type()
)
wfSonetPathIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathIntervalNumber.setStatus("mandatory")
_WfSonetPathIntervalESs_Type = Gauge32
_WfSonetPathIntervalESs_Object = MibTableColumn
wfSonetPathIntervalESs = _WfSonetPathIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1, 3),
    _WfSonetPathIntervalESs_Type()
)
wfSonetPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathIntervalESs.setStatus("mandatory")
_WfSonetPathIntervalSESs_Type = Gauge32
_WfSonetPathIntervalSESs_Object = MibTableColumn
wfSonetPathIntervalSESs = _WfSonetPathIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1, 4),
    _WfSonetPathIntervalSESs_Type()
)
wfSonetPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathIntervalSESs.setStatus("mandatory")
_WfSonetPathIntervalCVs_Type = Gauge32
_WfSonetPathIntervalCVs_Object = MibTableColumn
wfSonetPathIntervalCVs = _WfSonetPathIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1, 5),
    _WfSonetPathIntervalCVs_Type()
)
wfSonetPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathIntervalCVs.setStatus("mandatory")
_WfSonetPathIntervalUASs_Type = Gauge32
_WfSonetPathIntervalUASs_Object = MibTableColumn
wfSonetPathIntervalUASs = _WfSonetPathIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 9, 1, 6),
    _WfSonetPathIntervalUASs_Type()
)
wfSonetPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetPathIntervalUASs.setStatus("mandatory")
_WfSonetFarEndPathCurrentTable_Object = MibTable
wfSonetFarEndPathCurrentTable = _WfSonetFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10)
)
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentTable.setStatus("mandatory")
_WfSonetFarEndPathCurrentEntry_Object = MibTableRow
wfSonetFarEndPathCurrentEntry = _WfSonetFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10, 1)
)
wfSonetFarEndPathCurrentEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetFarEndPathCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentEntry.setStatus("mandatory")
_WfSonetFarEndPathCurrentIndex_Type = Integer32
_WfSonetFarEndPathCurrentIndex_Object = MibTableColumn
wfSonetFarEndPathCurrentIndex = _WfSonetFarEndPathCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10, 1, 1),
    _WfSonetFarEndPathCurrentIndex_Type()
)
wfSonetFarEndPathCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentIndex.setStatus("mandatory")
_WfSonetFarEndPathCurrentESs_Type = Gauge32
_WfSonetFarEndPathCurrentESs_Object = MibTableColumn
wfSonetFarEndPathCurrentESs = _WfSonetFarEndPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10, 1, 2),
    _WfSonetFarEndPathCurrentESs_Type()
)
wfSonetFarEndPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentESs.setStatus("mandatory")
_WfSonetFarEndPathCurrentSESs_Type = Gauge32
_WfSonetFarEndPathCurrentSESs_Object = MibTableColumn
wfSonetFarEndPathCurrentSESs = _WfSonetFarEndPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10, 1, 3),
    _WfSonetFarEndPathCurrentSESs_Type()
)
wfSonetFarEndPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentSESs.setStatus("mandatory")
_WfSonetFarEndPathCurrentCVs_Type = Gauge32
_WfSonetFarEndPathCurrentCVs_Object = MibTableColumn
wfSonetFarEndPathCurrentCVs = _WfSonetFarEndPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10, 1, 4),
    _WfSonetFarEndPathCurrentCVs_Type()
)
wfSonetFarEndPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentCVs.setStatus("mandatory")
_WfSonetFarEndPathCurrentUASs_Type = Gauge32
_WfSonetFarEndPathCurrentUASs_Object = MibTableColumn
wfSonetFarEndPathCurrentUASs = _WfSonetFarEndPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 10, 1, 5),
    _WfSonetFarEndPathCurrentUASs_Type()
)
wfSonetFarEndPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathCurrentUASs.setStatus("mandatory")
_WfSonetFarEndPathIntervalTable_Object = MibTable
wfSonetFarEndPathIntervalTable = _WfSonetFarEndPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11)
)
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalTable.setStatus("mandatory")
_WfSonetFarEndPathIntervalEntry_Object = MibTableRow
wfSonetFarEndPathIntervalEntry = _WfSonetFarEndPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1)
)
wfSonetFarEndPathIntervalEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfSonetFarEndPathIntervalIndex"),
    (0, "Wellfleet-ATM-MIB", "wfSonetFarEndPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalEntry.setStatus("mandatory")
_WfSonetFarEndPathIntervalIndex_Type = Integer32
_WfSonetFarEndPathIntervalIndex_Object = MibTableColumn
wfSonetFarEndPathIntervalIndex = _WfSonetFarEndPathIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1, 1),
    _WfSonetFarEndPathIntervalIndex_Type()
)
wfSonetFarEndPathIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalIndex.setStatus("mandatory")
_WfSonetFarEndPathIntervalNumber_Type = Integer32
_WfSonetFarEndPathIntervalNumber_Object = MibTableColumn
wfSonetFarEndPathIntervalNumber = _WfSonetFarEndPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1, 2),
    _WfSonetFarEndPathIntervalNumber_Type()
)
wfSonetFarEndPathIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalNumber.setStatus("mandatory")
_WfSonetFarEndPathIntervalESs_Type = Gauge32
_WfSonetFarEndPathIntervalESs_Object = MibTableColumn
wfSonetFarEndPathIntervalESs = _WfSonetFarEndPathIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1, 3),
    _WfSonetFarEndPathIntervalESs_Type()
)
wfSonetFarEndPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalESs.setStatus("mandatory")
_WfSonetFarEndPathIntervalSESs_Type = Gauge32
_WfSonetFarEndPathIntervalSESs_Object = MibTableColumn
wfSonetFarEndPathIntervalSESs = _WfSonetFarEndPathIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1, 4),
    _WfSonetFarEndPathIntervalSESs_Type()
)
wfSonetFarEndPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalSESs.setStatus("mandatory")
_WfSonetFarEndPathIntervalCVs_Type = Gauge32
_WfSonetFarEndPathIntervalCVs_Object = MibTableColumn
wfSonetFarEndPathIntervalCVs = _WfSonetFarEndPathIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1, 5),
    _WfSonetFarEndPathIntervalCVs_Type()
)
wfSonetFarEndPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalCVs.setStatus("mandatory")
_WfSonetFarEndPathIntervalUASs_Type = Gauge32
_WfSonetFarEndPathIntervalUASs_Object = MibTableColumn
wfSonetFarEndPathIntervalUASs = _WfSonetFarEndPathIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 11, 1, 6),
    _WfSonetFarEndPathIntervalUASs_Type()
)
wfSonetFarEndPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSonetFarEndPathIntervalUASs.setStatus("mandatory")
_WfAtm_ObjectIdentity = ObjectIdentity
wfAtm = _WfAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 1)
)


class _WfAtmDelete_Type(Integer32):
    """Custom type wfAtmDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmDelete_Type.__name__ = "Integer32"
_WfAtmDelete_Object = MibScalar
wfAtmDelete = _WfAtmDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 1, 1),
    _WfAtmDelete_Type()
)
wfAtmDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmDelete.setStatus("mandatory")
_WfAtmInterfaceNumber_Type = Integer32
_WfAtmInterfaceNumber_Object = MibScalar
wfAtmInterfaceNumber = _WfAtmInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 1, 2),
    _WfAtmInterfaceNumber_Type()
)
wfAtmInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceNumber.setStatus("mandatory")


class _WfAtmOverallStatus_Type(Integer32):
    """Custom type wfAtmOverallStatus based on Integer32"""
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
        *(("healthy", 1),
          ("interfaceanomaly", 2),
          ("otheranomaly", 3))
    )


_WfAtmOverallStatus_Type.__name__ = "Integer32"
_WfAtmOverallStatus_Object = MibScalar
wfAtmOverallStatus = _WfAtmOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 1, 3),
    _WfAtmOverallStatus_Type()
)
wfAtmOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmOverallStatus.setStatus("mandatory")


class _WfAtmGlobalSigStkVersion_Type(Integer32):
    """Custom type wfAtmGlobalSigStkVersion based on Integer32"""
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
        *(("sym", 3),
          ("u30", 1),
          ("u31", 2),
          ("u40", 4))
    )


_WfAtmGlobalSigStkVersion_Type.__name__ = "Integer32"
_WfAtmGlobalSigStkVersion_Object = MibScalar
wfAtmGlobalSigStkVersion = _WfAtmGlobalSigStkVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 1, 4),
    _WfAtmGlobalSigStkVersion_Type()
)
wfAtmGlobalSigStkVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmGlobalSigStkVersion.setStatus("mandatory")
_WfAtmInterfaceTable_Object = MibTable
wfAtmInterfaceTable = _WfAtmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2)
)
if mibBuilder.loadTexts:
    wfAtmInterfaceTable.setStatus("mandatory")
_WfAtmInterfaceEntry_Object = MibTableRow
wfAtmInterfaceEntry = _WfAtmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1)
)
wfAtmInterfaceEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmInterfaceLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmInterfaceLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmInterfaceEntry.setStatus("mandatory")


class _WfAtmInterfaceDelete_Type(Integer32):
    """Custom type wfAtmInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmInterfaceDelete_Type.__name__ = "Integer32"
_WfAtmInterfaceDelete_Object = MibTableColumn
wfAtmInterfaceDelete = _WfAtmInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 1),
    _WfAtmInterfaceDelete_Type()
)
wfAtmInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceDelete.setStatus("mandatory")


class _WfAtmInterfaceDisable_Type(Integer32):
    """Custom type wfAtmInterfaceDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmInterfaceDisable_Type.__name__ = "Integer32"
_WfAtmInterfaceDisable_Object = MibTableColumn
wfAtmInterfaceDisable = _WfAtmInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 2),
    _WfAtmInterfaceDisable_Type()
)
wfAtmInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceDisable.setStatus("mandatory")


class _WfAtmInterfaceState_Type(Integer32):
    """Custom type wfAtmInterfaceState based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmInterfaceState_Type.__name__ = "Integer32"
_WfAtmInterfaceState_Object = MibTableColumn
wfAtmInterfaceState = _WfAtmInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 3),
    _WfAtmInterfaceState_Type()
)
wfAtmInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceState.setStatus("mandatory")
_WfAtmInterfaceCircuit_Type = Integer32
_WfAtmInterfaceCircuit_Object = MibTableColumn
wfAtmInterfaceCircuit = _WfAtmInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 4),
    _WfAtmInterfaceCircuit_Type()
)
wfAtmInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceCircuit.setStatus("mandatory")


class _WfAtmInterfaceMaxSupportedVCs_Type(Integer32):
    """Custom type wfAtmInterfaceMaxSupportedVCs based on Integer32"""
    defaultValue = 512


_WfAtmInterfaceMaxSupportedVCs_Object = MibTableColumn
wfAtmInterfaceMaxSupportedVCs = _WfAtmInterfaceMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 5),
    _WfAtmInterfaceMaxSupportedVCs_Type()
)
wfAtmInterfaceMaxSupportedVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceMaxSupportedVCs.setStatus("mandatory")
_WfAtmInterfaceVCsInUse_Type = Integer32
_WfAtmInterfaceVCsInUse_Object = MibTableColumn
wfAtmInterfaceVCsInUse = _WfAtmInterfaceVCsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 6),
    _WfAtmInterfaceVCsInUse_Type()
)
wfAtmInterfaceVCsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceVCsInUse.setStatus("mandatory")
_WfAtmInterfaceDescr_Type = DisplayString
_WfAtmInterfaceDescr_Object = MibTableColumn
wfAtmInterfaceDescr = _WfAtmInterfaceDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 7),
    _WfAtmInterfaceDescr_Type()
)
wfAtmInterfaceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceDescr.setStatus("mandatory")


class _WfAtmInterfaceType_Type(Integer32):
    """Custom type wfAtmInterfaceType based on Integer32"""
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
        *(("ds1", 2),
          ("ds3", 3),
          ("other", 1))
    )


_WfAtmInterfaceType_Type.__name__ = "Integer32"
_WfAtmInterfaceType_Object = MibTableColumn
wfAtmInterfaceType = _WfAtmInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 8),
    _WfAtmInterfaceType_Type()
)
wfAtmInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceType.setStatus("mandatory")
_WfAtmInterfaceLastChange_Type = TimeTicks
_WfAtmInterfaceLastChange_Object = MibTableColumn
wfAtmInterfaceLastChange = _WfAtmInterfaceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 9),
    _WfAtmInterfaceLastChange_Type()
)
wfAtmInterfaceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceLastChange.setStatus("mandatory")
_WfAtmInterfacePlcp_Type = ObjectIdentifier
_WfAtmInterfacePlcp_Object = MibTableColumn
wfAtmInterfacePlcp = _WfAtmInterfacePlcp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 10),
    _WfAtmInterfacePlcp_Type()
)
wfAtmInterfacePlcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfacePlcp.setStatus("mandatory")


class _WfAtmMpeNull_Type(Integer32):
    """Custom type wfAtmMpeNull based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mpe1294", 1),
          ("mpe1483", 3),
          ("null", 2))
    )


_WfAtmMpeNull_Type.__name__ = "Integer32"
_WfAtmMpeNull_Object = MibTableColumn
wfAtmMpeNull = _WfAtmMpeNull_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 11),
    _WfAtmMpeNull_Type()
)
wfAtmMpeNull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmMpeNull.setStatus("mandatory")


class _WfAtmCsNull_Type(Integer32):
    """Custom type wfAtmCsNull based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal34", 1),
          ("aal5", 3),
          ("null", 2))
    )


_WfAtmCsNull_Type.__name__ = "Integer32"
_WfAtmCsNull_Object = MibTableColumn
wfAtmCsNull = _WfAtmCsNull_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 12),
    _WfAtmCsNull_Type()
)
wfAtmCsNull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCsNull.setStatus("mandatory")


class _WfAtmInterfaceMulticast_Type(Integer32):
    """Custom type wfAtmInterfaceMulticast based on Integer32"""
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


_WfAtmInterfaceMulticast_Type.__name__ = "Integer32"
_WfAtmInterfaceMulticast_Object = MibTableColumn
wfAtmInterfaceMulticast = _WfAtmInterfaceMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 13),
    _WfAtmInterfaceMulticast_Type()
)
wfAtmInterfaceMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceMulticast.setStatus("mandatory")
_WfAtmDrops_Type = Counter32
_WfAtmDrops_Object = MibTableColumn
wfAtmDrops = _WfAtmDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 14),
    _WfAtmDrops_Type()
)
wfAtmDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDrops.setStatus("mandatory")


class _WfAtmInterfaceLmiDisable_Type(Integer32):
    """Custom type wfAtmInterfaceLmiDisable based on Integer32"""
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


_WfAtmInterfaceLmiDisable_Type.__name__ = "Integer32"
_WfAtmInterfaceLmiDisable_Object = MibTableColumn
wfAtmInterfaceLmiDisable = _WfAtmInterfaceLmiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 15),
    _WfAtmInterfaceLmiDisable_Type()
)
wfAtmInterfaceLmiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceLmiDisable.setStatus("mandatory")
_WfAtmInterfaceLineNumber_Type = Integer32
_WfAtmInterfaceLineNumber_Object = MibTableColumn
wfAtmInterfaceLineNumber = _WfAtmInterfaceLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 16),
    _WfAtmInterfaceLineNumber_Type()
)
wfAtmInterfaceLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceLineNumber.setStatus("mandatory")
_WfAtmInterfaceLLIndex_Type = Integer32
_WfAtmInterfaceLLIndex_Object = MibTableColumn
wfAtmInterfaceLLIndex = _WfAtmInterfaceLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 17),
    _WfAtmInterfaceLLIndex_Type()
)
wfAtmInterfaceLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceLLIndex.setStatus("mandatory")


class _WfAtmInterfaceDxiMode_Type(Integer32):
    """Custom type wfAtmInterfaceDxiMode based on Integer32"""
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
        *(("mode1a", 1),
          ("mode1b", 2),
          ("mode2", 3),
          ("modep2", 4))
    )


_WfAtmInterfaceDxiMode_Type.__name__ = "Integer32"
_WfAtmInterfaceDxiMode_Object = MibTableColumn
wfAtmInterfaceDxiMode = _WfAtmInterfaceDxiMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 18),
    _WfAtmInterfaceDxiMode_Type()
)
wfAtmInterfaceDxiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmInterfaceDxiMode.setStatus("mandatory")
_WfAtmUnknownVCPkts_Type = Counter32
_WfAtmUnknownVCPkts_Object = MibTableColumn
wfAtmUnknownVCPkts = _WfAtmUnknownVCPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 2, 1, 19),
    _WfAtmUnknownVCPkts_Type()
)
wfAtmUnknownVCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUnknownVCPkts.setStatus("mandatory")
_WfAtmLmiTable_Object = MibTable
wfAtmLmiTable = _WfAtmLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3)
)
if mibBuilder.loadTexts:
    wfAtmLmiTable.setStatus("mandatory")
_WfAtmLmiEntry_Object = MibTableRow
wfAtmLmiEntry = _WfAtmLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1)
)
wfAtmLmiEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmLmiLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmLmiLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmLmiEntry.setStatus("mandatory")


class _WfAtmLmiState_Type(Integer32):
    """Custom type wfAtmLmiState based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmLmiState_Type.__name__ = "Integer32"
_WfAtmLmiState_Object = MibTableColumn
wfAtmLmiState = _WfAtmLmiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 1),
    _WfAtmLmiState_Type()
)
wfAtmLmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiState.setStatus("mandatory")
_WfAtmLmiCircuit_Type = Integer32
_WfAtmLmiCircuit_Object = MibTableColumn
wfAtmLmiCircuit = _WfAtmLmiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 2),
    _WfAtmLmiCircuit_Type()
)
wfAtmLmiCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiCircuit.setStatus("mandatory")
_WfAtmLmiNoVCErrors_Type = Counter32
_WfAtmLmiNoVCErrors_Object = MibTableColumn
wfAtmLmiNoVCErrors = _WfAtmLmiNoVCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 3),
    _WfAtmLmiNoVCErrors_Type()
)
wfAtmLmiNoVCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiNoVCErrors.setStatus("mandatory")
_WfAtmLmiProxyRequests_Type = Counter32
_WfAtmLmiProxyRequests_Object = MibTableColumn
wfAtmLmiProxyRequests = _WfAtmLmiProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 4),
    _WfAtmLmiProxyRequests_Type()
)
wfAtmLmiProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiProxyRequests.setStatus("mandatory")
_WfAtmLmiCsuDsuResponses_Type = Counter32
_WfAtmLmiCsuDsuResponses_Object = MibTableColumn
wfAtmLmiCsuDsuResponses = _WfAtmLmiCsuDsuResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 5),
    _WfAtmLmiCsuDsuResponses_Type()
)
wfAtmLmiCsuDsuResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiCsuDsuResponses.setStatus("mandatory")
_WfAtmLmiCsuDsuTraps_Type = Counter32
_WfAtmLmiCsuDsuTraps_Object = MibTableColumn
wfAtmLmiCsuDsuTraps = _WfAtmLmiCsuDsuTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 6),
    _WfAtmLmiCsuDsuTraps_Type()
)
wfAtmLmiCsuDsuTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiCsuDsuTraps.setStatus("mandatory")
_WfAtmLmiOtherErrors_Type = Counter32
_WfAtmLmiOtherErrors_Object = MibTableColumn
wfAtmLmiOtherErrors = _WfAtmLmiOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 7),
    _WfAtmLmiOtherErrors_Type()
)
wfAtmLmiOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiOtherErrors.setStatus("mandatory")
_WfAtmLmiLineNumber_Type = Integer32
_WfAtmLmiLineNumber_Object = MibTableColumn
wfAtmLmiLineNumber = _WfAtmLmiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 8),
    _WfAtmLmiLineNumber_Type()
)
wfAtmLmiLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiLineNumber.setStatus("mandatory")
_WfAtmLmiLLIndex_Type = Integer32
_WfAtmLmiLLIndex_Object = MibTableColumn
wfAtmLmiLLIndex = _WfAtmLmiLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 3, 1, 9),
    _WfAtmLmiLLIndex_Type()
)
wfAtmLmiLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLmiLLIndex.setStatus("mandatory")
_WfAtmPlcpTable_Object = MibTable
wfAtmPlcpTable = _WfAtmPlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4)
)
if mibBuilder.loadTexts:
    wfAtmPlcpTable.setStatus("mandatory")
_WfAtmPlcpEntry_Object = MibTableRow
wfAtmPlcpEntry = _WfAtmPlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1)
)
wfAtmPlcpEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmPlcpLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmPlcpLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmPlcpEntry.setStatus("mandatory")
_WfAtmPlcpCct_Type = Integer32
_WfAtmPlcpCct_Object = MibTableColumn
wfAtmPlcpCct = _WfAtmPlcpCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 1),
    _WfAtmPlcpCct_Type()
)
wfAtmPlcpCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpCct.setStatus("mandatory")
_WfAtmPlcpPhysical_Type = ObjectIdentifier
_WfAtmPlcpPhysical_Object = MibTableColumn
wfAtmPlcpPhysical = _WfAtmPlcpPhysical_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 2),
    _WfAtmPlcpPhysical_Type()
)
wfAtmPlcpPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpPhysical.setStatus("mandatory")


class _WfAtmPlcpLof_Type(Integer32):
    """Custom type wfAtmPlcpLof based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfAtmPlcpLof_Type.__name__ = "Integer32"
_WfAtmPlcpLof_Object = MibTableColumn
wfAtmPlcpLof = _WfAtmPlcpLof_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 3),
    _WfAtmPlcpLof_Type()
)
wfAtmPlcpLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpLof.setStatus("mandatory")


class _WfAtmPlcpLofCFA_Type(Integer32):
    """Custom type wfAtmPlcpLofCFA based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfAtmPlcpLofCFA_Type.__name__ = "Integer32"
_WfAtmPlcpLofCFA_Object = MibTableColumn
wfAtmPlcpLofCFA = _WfAtmPlcpLofCFA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 4),
    _WfAtmPlcpLofCFA_Type()
)
wfAtmPlcpLofCFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpLofCFA.setStatus("mandatory")


class _WfAtmPlcpYellow_Type(Integer32):
    """Custom type wfAtmPlcpYellow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfAtmPlcpYellow_Type.__name__ = "Integer32"
_WfAtmPlcpYellow_Object = MibTableColumn
wfAtmPlcpYellow = _WfAtmPlcpYellow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 5),
    _WfAtmPlcpYellow_Type()
)
wfAtmPlcpYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpYellow.setStatus("mandatory")


class _WfAtmPlcpYellowCFA_Type(Integer32):
    """Custom type wfAtmPlcpYellowCFA based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfAtmPlcpYellowCFA_Type.__name__ = "Integer32"
_WfAtmPlcpYellowCFA_Object = MibTableColumn
wfAtmPlcpYellowCFA = _WfAtmPlcpYellowCFA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 6),
    _WfAtmPlcpYellowCFA_Type()
)
wfAtmPlcpYellowCFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpYellowCFA.setStatus("mandatory")


class _WfAtmPlcpStatus_Type(Integer32):
    """Custom type wfAtmPlcpStatus based on Integer32"""
    defaultValue = 3

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
        *(("connected", 1),
          ("down", 3),
          ("other", 4),
          ("outofframe", 5),
          ("up", 2))
    )


_WfAtmPlcpStatus_Type.__name__ = "Integer32"
_WfAtmPlcpStatus_Object = MibTableColumn
wfAtmPlcpStatus = _WfAtmPlcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 7),
    _WfAtmPlcpStatus_Type()
)
wfAtmPlcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpStatus.setStatus("mandatory")
_WfAtmPlcpSeconds_Type = Counter32
_WfAtmPlcpSeconds_Object = MibTableColumn
wfAtmPlcpSeconds = _WfAtmPlcpSeconds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 8),
    _WfAtmPlcpSeconds_Type()
)
wfAtmPlcpSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpSeconds.setStatus("mandatory")
_WfAtmPlcpBipErrors_Type = Counter32
_WfAtmPlcpBipErrors_Object = MibTableColumn
wfAtmPlcpBipErrors = _WfAtmPlcpBipErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 9),
    _WfAtmPlcpBipErrors_Type()
)
wfAtmPlcpBipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpBipErrors.setStatus("mandatory")
_WfAtmPlcpBipESecs_Type = Counter32
_WfAtmPlcpBipESecs_Object = MibTableColumn
wfAtmPlcpBipESecs = _WfAtmPlcpBipESecs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 10),
    _WfAtmPlcpBipESecs_Type()
)
wfAtmPlcpBipESecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpBipESecs.setStatus("mandatory")
_WfAtmPlcpBipSESecs_Type = Counter32
_WfAtmPlcpBipSESecs_Object = MibTableColumn
wfAtmPlcpBipSESecs = _WfAtmPlcpBipSESecs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 11),
    _WfAtmPlcpBipSESecs_Type()
)
wfAtmPlcpBipSESecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpBipSESecs.setStatus("mandatory")
_WfAtmPlcpFebes_Type = Counter32
_WfAtmPlcpFebes_Object = MibTableColumn
wfAtmPlcpFebes = _WfAtmPlcpFebes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 12),
    _WfAtmPlcpFebes_Type()
)
wfAtmPlcpFebes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpFebes.setStatus("mandatory")
_WfAtmPlcpFebeESecs_Type = Counter32
_WfAtmPlcpFebeESecs_Object = MibTableColumn
wfAtmPlcpFebeESecs = _WfAtmPlcpFebeESecs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 13),
    _WfAtmPlcpFebeESecs_Type()
)
wfAtmPlcpFebeESecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpFebeESecs.setStatus("mandatory")
_WfAtmPlcpFebeSESecs_Type = Counter32
_WfAtmPlcpFebeSESecs_Object = MibTableColumn
wfAtmPlcpFebeSESecs = _WfAtmPlcpFebeSESecs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 14),
    _WfAtmPlcpFebeSESecs_Type()
)
wfAtmPlcpFebeSESecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpFebeSESecs.setStatus("mandatory")
_WfAtmPlcpFrameErrors_Type = Counter32
_WfAtmPlcpFrameErrors_Object = MibTableColumn
wfAtmPlcpFrameErrors = _WfAtmPlcpFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 15),
    _WfAtmPlcpFrameErrors_Type()
)
wfAtmPlcpFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpFrameErrors.setStatus("mandatory")
_WfAtmPlcpSevereFrameErrors_Type = Counter32
_WfAtmPlcpSevereFrameErrors_Object = MibTableColumn
wfAtmPlcpSevereFrameErrors = _WfAtmPlcpSevereFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 16),
    _WfAtmPlcpSevereFrameErrors_Type()
)
wfAtmPlcpSevereFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpSevereFrameErrors.setStatus("mandatory")
_WfAtmPlcpSEFS_Type = Counter32
_WfAtmPlcpSEFS_Object = MibTableColumn
wfAtmPlcpSEFS = _WfAtmPlcpSEFS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 17),
    _WfAtmPlcpSEFS_Type()
)
wfAtmPlcpSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpSEFS.setStatus("mandatory")
_WfAtmPlcpUAS_Type = Counter32
_WfAtmPlcpUAS_Object = MibTableColumn
wfAtmPlcpUAS = _WfAtmPlcpUAS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 18),
    _WfAtmPlcpUAS_Type()
)
wfAtmPlcpUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpUAS.setStatus("mandatory")
_WfAtmPlcpLineNumber_Type = Integer32
_WfAtmPlcpLineNumber_Object = MibTableColumn
wfAtmPlcpLineNumber = _WfAtmPlcpLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 19),
    _WfAtmPlcpLineNumber_Type()
)
wfAtmPlcpLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpLineNumber.setStatus("mandatory")
_WfAtmPlcpLLIndex_Type = Integer32
_WfAtmPlcpLLIndex_Object = MibTableColumn
wfAtmPlcpLLIndex = _WfAtmPlcpLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 4, 1, 20),
    _WfAtmPlcpLLIndex_Type()
)
wfAtmPlcpLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPlcpLLIndex.setStatus("mandatory")
_WfAtmUniTable_Object = MibTable
wfAtmUniTable = _WfAtmUniTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5)
)
if mibBuilder.loadTexts:
    wfAtmUniTable.setStatus("mandatory")
_WfAtmUniEntry_Object = MibTableRow
wfAtmUniEntry = _WfAtmUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1)
)
wfAtmUniEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmUniLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmUniLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmUniEntry.setStatus("mandatory")
_WfAtmUniCct_Type = Integer32
_WfAtmUniCct_Object = MibTableColumn
wfAtmUniCct = _WfAtmUniCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1, 1),
    _WfAtmUniCct_Type()
)
wfAtmUniCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniCct.setStatus("mandatory")
_WfAtmUniPhysical_Type = ObjectIdentifier
_WfAtmUniPhysical_Object = MibTableColumn
wfAtmUniPhysical = _WfAtmUniPhysical_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1, 2),
    _WfAtmUniPhysical_Type()
)
wfAtmUniPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniPhysical.setStatus("mandatory")
_WfAtmUniAal_Type = ObjectIdentifier
_WfAtmUniAal_Object = MibTableColumn
wfAtmUniAal = _WfAtmUniAal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1, 3),
    _WfAtmUniAal_Type()
)
wfAtmUniAal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAal.setStatus("mandatory")
_WfAtmUniSeconds_Type = Counter32
_WfAtmUniSeconds_Object = MibTableColumn
wfAtmUniSeconds = _WfAtmUniSeconds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1, 4),
    _WfAtmUniSeconds_Type()
)
wfAtmUniSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniSeconds.setStatus("mandatory")
_WfAtmUniLineNumber_Type = Integer32
_WfAtmUniLineNumber_Object = MibTableColumn
wfAtmUniLineNumber = _WfAtmUniLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1, 5),
    _WfAtmUniLineNumber_Type()
)
wfAtmUniLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniLineNumber.setStatus("mandatory")
_WfAtmUniLLIndex_Type = Integer32
_WfAtmUniLLIndex_Object = MibTableColumn
wfAtmUniLLIndex = _WfAtmUniLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 5, 1, 6),
    _WfAtmUniLLIndex_Type()
)
wfAtmUniLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniLLIndex.setStatus("mandatory")
_WfAtmUniAtmTable_Object = MibTable
wfAtmUniAtmTable = _WfAtmUniAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6)
)
if mibBuilder.loadTexts:
    wfAtmUniAtmTable.setStatus("mandatory")
_WfAtmUniAtmEntry_Object = MibTableRow
wfAtmUniAtmEntry = _WfAtmUniAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1)
)
wfAtmUniAtmEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmUniAtmLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmUniAtmLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmUniAtmEntry.setStatus("mandatory")
_WfAtmUniAtmCct_Type = Integer32
_WfAtmUniAtmCct_Object = MibTableColumn
wfAtmUniAtmCct = _WfAtmUniAtmCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 1),
    _WfAtmUniAtmCct_Type()
)
wfAtmUniAtmCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmCct.setStatus("mandatory")
_WfAtmUniAtmNoBuffers_Type = Counter32
_WfAtmUniAtmNoBuffers_Object = MibTableColumn
wfAtmUniAtmNoBuffers = _WfAtmUniAtmNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 2),
    _WfAtmUniAtmNoBuffers_Type()
)
wfAtmUniAtmNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmNoBuffers.setStatus("mandatory")
_WfAtmUniAtmHECs_Type = Counter32
_WfAtmUniAtmHECs_Object = MibTableColumn
wfAtmUniAtmHECs = _WfAtmUniAtmHECs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 3),
    _WfAtmUniAtmHECs_Type()
)
wfAtmUniAtmHECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmHECs.setStatus("mandatory")
_WfAtmUniAtmCHECs_Type = Counter32
_WfAtmUniAtmCHECs_Object = MibTableColumn
wfAtmUniAtmCHECs = _WfAtmUniAtmCHECs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 4),
    _WfAtmUniAtmCHECs_Type()
)
wfAtmUniAtmCHECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmCHECs.setStatus("mandatory")
_WfAtmUniAtmNullCells_Type = Counter32
_WfAtmUniAtmNullCells_Object = MibTableColumn
wfAtmUniAtmNullCells = _WfAtmUniAtmNullCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 5),
    _WfAtmUniAtmNullCells_Type()
)
wfAtmUniAtmNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmNullCells.setStatus("mandatory")
_WfAtmUniAtmMisdeliveredCells_Type = Counter32
_WfAtmUniAtmMisdeliveredCells_Object = MibTableColumn
wfAtmUniAtmMisdeliveredCells = _WfAtmUniAtmMisdeliveredCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 6),
    _WfAtmUniAtmMisdeliveredCells_Type()
)
wfAtmUniAtmMisdeliveredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmMisdeliveredCells.setStatus("mandatory")
_WfAtmUniAtmReceives_Type = Counter32
_WfAtmUniAtmReceives_Object = MibTableColumn
wfAtmUniAtmReceives = _WfAtmUniAtmReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 7),
    _WfAtmUniAtmReceives_Type()
)
wfAtmUniAtmReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmReceives.setStatus("mandatory")
_WfAtmUniAtmTransmits_Type = Counter32
_WfAtmUniAtmTransmits_Object = MibTableColumn
wfAtmUniAtmTransmits = _WfAtmUniAtmTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 8),
    _WfAtmUniAtmTransmits_Type()
)
wfAtmUniAtmTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmTransmits.setStatus("mandatory")
_WfAtmUniAtmLineNumber_Type = Integer32
_WfAtmUniAtmLineNumber_Object = MibTableColumn
wfAtmUniAtmLineNumber = _WfAtmUniAtmLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 9),
    _WfAtmUniAtmLineNumber_Type()
)
wfAtmUniAtmLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmLineNumber.setStatus("mandatory")
_WfAtmUniAtmLLIndex_Type = Integer32
_WfAtmUniAtmLLIndex_Object = MibTableColumn
wfAtmUniAtmLLIndex = _WfAtmUniAtmLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 6, 1, 10),
    _WfAtmUniAtmLLIndex_Type()
)
wfAtmUniAtmLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmUniAtmLLIndex.setStatus("mandatory")
_WfAtmVbrTable_Object = MibTable
wfAtmVbrTable = _WfAtmVbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8)
)
if mibBuilder.loadTexts:
    wfAtmVbrTable.setStatus("mandatory")
_WfAtmVbrEntry_Object = MibTableRow
wfAtmVbrEntry = _WfAtmVbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1)
)
wfAtmVbrEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmVbrEntry.setStatus("mandatory")
_WfAtmVbrCct_Type = Integer32
_WfAtmVbrCct_Object = MibTableColumn
wfAtmVbrCct = _WfAtmVbrCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1, 1),
    _WfAtmVbrCct_Type()
)
wfAtmVbrCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCct.setStatus("mandatory")
_WfAtmVbrAtmUni_Type = ObjectIdentifier
_WfAtmVbrAtmUni_Object = MibTableColumn
wfAtmVbrAtmUni = _WfAtmVbrAtmUni_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1, 2),
    _WfAtmVbrAtmUni_Type()
)
wfAtmVbrAtmUni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrAtmUni.setStatus("mandatory")
_WfAtmVbrDxi_Type = ObjectIdentifier
_WfAtmVbrDxi_Object = MibTableColumn
wfAtmVbrDxi = _WfAtmVbrDxi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1, 3),
    _WfAtmVbrDxi_Type()
)
wfAtmVbrDxi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrDxi.setStatus("mandatory")
_WfAtmVbrSeconds_Type = Counter32
_WfAtmVbrSeconds_Object = MibTableColumn
wfAtmVbrSeconds = _WfAtmVbrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1, 4),
    _WfAtmVbrSeconds_Type()
)
wfAtmVbrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSeconds.setStatus("mandatory")
_WfAtmVbrLineNumber_Type = Integer32
_WfAtmVbrLineNumber_Object = MibTableColumn
wfAtmVbrLineNumber = _WfAtmVbrLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1, 5),
    _WfAtmVbrLineNumber_Type()
)
wfAtmVbrLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrLineNumber.setStatus("mandatory")
_WfAtmVbrLLIndex_Type = Integer32
_WfAtmVbrLLIndex_Object = MibTableColumn
wfAtmVbrLLIndex = _WfAtmVbrLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 8, 1, 6),
    _WfAtmVbrLLIndex_Type()
)
wfAtmVbrLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrLLIndex.setStatus("mandatory")
_WfAtmVbrSarTable_Object = MibTable
wfAtmVbrSarTable = _WfAtmVbrSarTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9)
)
if mibBuilder.loadTexts:
    wfAtmVbrSarTable.setStatus("mandatory")
_WfAtmVbrSarEntry_Object = MibTableRow
wfAtmVbrSarEntry = _WfAtmVbrSarEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1)
)
wfAtmVbrSarEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrSarLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrSarLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmVbrSarEntry.setStatus("mandatory")
_WfAtmVbrSarCct_Type = Integer32
_WfAtmVbrSarCct_Object = MibTableColumn
wfAtmVbrSarCct = _WfAtmVbrSarCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 1),
    _WfAtmVbrSarCct_Type()
)
wfAtmVbrSarCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarCct.setStatus("mandatory")


class _WfAtmVbrSarAssemblyTimer_Type(Integer32):
    """Custom type wfAtmVbrSarAssemblyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmVbrSarAssemblyTimer_Type.__name__ = "Integer32"
_WfAtmVbrSarAssemblyTimer_Object = MibTableColumn
wfAtmVbrSarAssemblyTimer = _WfAtmVbrSarAssemblyTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 2),
    _WfAtmVbrSarAssemblyTimer_Type()
)
wfAtmVbrSarAssemblyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarAssemblyTimer.setStatus("mandatory")
_WfAtmVbrSarCrc10Errors_Type = Counter32
_WfAtmVbrSarCrc10Errors_Object = MibTableColumn
wfAtmVbrSarCrc10Errors = _WfAtmVbrSarCrc10Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 3),
    _WfAtmVbrSarCrc10Errors_Type()
)
wfAtmVbrSarCrc10Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarCrc10Errors.setStatus("mandatory")
_WfAtmVbrSarCellMidErrors_Type = Counter32
_WfAtmVbrSarCellMidErrors_Object = MibTableColumn
wfAtmVbrSarCellMidErrors = _WfAtmVbrSarCellMidErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 4),
    _WfAtmVbrSarCellMidErrors_Type()
)
wfAtmVbrSarCellMidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarCellMidErrors.setStatus("mandatory")
_WfAtmVbrSarCsPduSizeTooBigErrors_Type = Counter32
_WfAtmVbrSarCsPduSizeTooBigErrors_Object = MibTableColumn
wfAtmVbrSarCsPduSizeTooBigErrors = _WfAtmVbrSarCsPduSizeTooBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 5),
    _WfAtmVbrSarCsPduSizeTooBigErrors_Type()
)
wfAtmVbrSarCsPduSizeTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarCsPduSizeTooBigErrors.setStatus("mandatory")
_WfAtmVbrSarNoBufferErrors_Type = Counter32
_WfAtmVbrSarNoBufferErrors_Object = MibTableColumn
wfAtmVbrSarNoBufferErrors = _WfAtmVbrSarNoBufferErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 6),
    _WfAtmVbrSarNoBufferErrors_Type()
)
wfAtmVbrSarNoBufferErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarNoBufferErrors.setStatus("mandatory")
_WfAtmVbrSarComNoProcessErrors_Type = Counter32
_WfAtmVbrSarComNoProcessErrors_Object = MibTableColumn
wfAtmVbrSarComNoProcessErrors = _WfAtmVbrSarComNoProcessErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 7),
    _WfAtmVbrSarComNoProcessErrors_Type()
)
wfAtmVbrSarComNoProcessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarComNoProcessErrors.setStatus("mandatory")
_WfAtmVbrSarEomNoProcessErrors_Type = Counter32
_WfAtmVbrSarEomNoProcessErrors_Object = MibTableColumn
wfAtmVbrSarEomNoProcessErrors = _WfAtmVbrSarEomNoProcessErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 8),
    _WfAtmVbrSarEomNoProcessErrors_Type()
)
wfAtmVbrSarEomNoProcessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarEomNoProcessErrors.setStatus("mandatory")
_WfAtmVbrSarCellSequenceErrors_Type = Counter32
_WfAtmVbrSarCellSequenceErrors_Object = MibTableColumn
wfAtmVbrSarCellSequenceErrors = _WfAtmVbrSarCellSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 9),
    _WfAtmVbrSarCellSequenceErrors_Type()
)
wfAtmVbrSarCellSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarCellSequenceErrors.setStatus("mandatory")
_WfAtmVbrSarCellLengthErrors_Type = Counter32
_WfAtmVbrSarCellLengthErrors_Object = MibTableColumn
wfAtmVbrSarCellLengthErrors = _WfAtmVbrSarCellLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 10),
    _WfAtmVbrSarCellLengthErrors_Type()
)
wfAtmVbrSarCellLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarCellLengthErrors.setStatus("mandatory")
_WfAtmVbrSarBomBeforeEomErrors_Type = Counter32
_WfAtmVbrSarBomBeforeEomErrors_Object = MibTableColumn
wfAtmVbrSarBomBeforeEomErrors = _WfAtmVbrSarBomBeforeEomErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 11),
    _WfAtmVbrSarBomBeforeEomErrors_Type()
)
wfAtmVbrSarBomBeforeEomErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarBomBeforeEomErrors.setStatus("mandatory")
_WfAtmVbrSarTimeouts_Type = Counter32
_WfAtmVbrSarTimeouts_Object = MibTableColumn
wfAtmVbrSarTimeouts = _WfAtmVbrSarTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 12),
    _WfAtmVbrSarTimeouts_Type()
)
wfAtmVbrSarTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarTimeouts.setStatus("mandatory")
_WfAtmVbrSarLengthExceeds_Type = Counter32
_WfAtmVbrSarLengthExceeds_Object = MibTableColumn
wfAtmVbrSarLengthExceeds = _WfAtmVbrSarLengthExceeds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 13),
    _WfAtmVbrSarLengthExceeds_Type()
)
wfAtmVbrSarLengthExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarLengthExceeds.setStatus("mandatory")
_WfAtmVbrSarReceives_Type = Counter32
_WfAtmVbrSarReceives_Object = MibTableColumn
wfAtmVbrSarReceives = _WfAtmVbrSarReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 14),
    _WfAtmVbrSarReceives_Type()
)
wfAtmVbrSarReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarReceives.setStatus("mandatory")
_WfAtmVbrSarTransmits_Type = Counter32
_WfAtmVbrSarTransmits_Object = MibTableColumn
wfAtmVbrSarTransmits = _WfAtmVbrSarTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 15),
    _WfAtmVbrSarTransmits_Type()
)
wfAtmVbrSarTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarTransmits.setStatus("mandatory")
_WfAtmVbrSarLineNumber_Type = Integer32
_WfAtmVbrSarLineNumber_Object = MibTableColumn
wfAtmVbrSarLineNumber = _WfAtmVbrSarLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 16),
    _WfAtmVbrSarLineNumber_Type()
)
wfAtmVbrSarLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarLineNumber.setStatus("mandatory")
_WfAtmVbrSarLLIndex_Type = Integer32
_WfAtmVbrSarLLIndex_Object = MibTableColumn
wfAtmVbrSarLLIndex = _WfAtmVbrSarLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 9, 1, 17),
    _WfAtmVbrSarLLIndex_Type()
)
wfAtmVbrSarLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrSarLLIndex.setStatus("mandatory")
_WfAtmVbrCsTable_Object = MibTable
wfAtmVbrCsTable = _WfAtmVbrCsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11)
)
if mibBuilder.loadTexts:
    wfAtmVbrCsTable.setStatus("mandatory")
_WfAtmVbrCsEntry_Object = MibTableRow
wfAtmVbrCsEntry = _WfAtmVbrCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1)
)
wfAtmVbrCsEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrCsLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrCsLLIndex"),
)
if mibBuilder.loadTexts:
    wfAtmVbrCsEntry.setStatus("mandatory")
_WfAtmVbrCsCct_Type = Integer32
_WfAtmVbrCsCct_Object = MibTableColumn
wfAtmVbrCsCct = _WfAtmVbrCsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 1),
    _WfAtmVbrCsCct_Type()
)
wfAtmVbrCsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsCct.setStatus("mandatory")
_WfAtmVbrCsBETagMismatches_Type = Counter32
_WfAtmVbrCsBETagMismatches_Object = MibTableColumn
wfAtmVbrCsBETagMismatches = _WfAtmVbrCsBETagMismatches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 2),
    _WfAtmVbrCsBETagMismatches_Type()
)
wfAtmVbrCsBETagMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsBETagMismatches.setStatus("mandatory")
_WfAtmVbrCsLengthMismatches_Type = Counter32
_WfAtmVbrCsLengthMismatches_Object = MibTableColumn
wfAtmVbrCsLengthMismatches = _WfAtmVbrCsLengthMismatches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 3),
    _WfAtmVbrCsLengthMismatches_Type()
)
wfAtmVbrCsLengthMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsLengthMismatches.setStatus("mandatory")
_WfAtmVbrCsMisdeliveredPdus_Type = Counter32
_WfAtmVbrCsMisdeliveredPdus_Object = MibTableColumn
wfAtmVbrCsMisdeliveredPdus = _WfAtmVbrCsMisdeliveredPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 4),
    _WfAtmVbrCsMisdeliveredPdus_Type()
)
wfAtmVbrCsMisdeliveredPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsMisdeliveredPdus.setStatus("mandatory")
_WfAtmVbrCsReceives_Type = Counter32
_WfAtmVbrCsReceives_Object = MibTableColumn
wfAtmVbrCsReceives = _WfAtmVbrCsReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 5),
    _WfAtmVbrCsReceives_Type()
)
wfAtmVbrCsReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsReceives.setStatus("mandatory")
_WfAtmVbrCsTransmits_Type = Counter32
_WfAtmVbrCsTransmits_Object = MibTableColumn
wfAtmVbrCsTransmits = _WfAtmVbrCsTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 6),
    _WfAtmVbrCsTransmits_Type()
)
wfAtmVbrCsTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsTransmits.setStatus("mandatory")
_WfAtmVbrCsLineNumber_Type = Integer32
_WfAtmVbrCsLineNumber_Object = MibTableColumn
wfAtmVbrCsLineNumber = _WfAtmVbrCsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 7),
    _WfAtmVbrCsLineNumber_Type()
)
wfAtmVbrCsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsLineNumber.setStatus("mandatory")
_WfAtmVbrCsLLIndex_Type = Integer32
_WfAtmVbrCsLLIndex_Object = MibTableColumn
wfAtmVbrCsLLIndex = _WfAtmVbrCsLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 11, 1, 8),
    _WfAtmVbrCsLLIndex_Type()
)
wfAtmVbrCsLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsLLIndex.setStatus("mandatory")
_WfAtmVbrCsVciTable_Object = MibTable
wfAtmVbrCsVciTable = _WfAtmVbrCsVciTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12)
)
if mibBuilder.loadTexts:
    wfAtmVbrCsVciTable.setStatus("mandatory")
_WfAtmVbrCsVciEntry_Object = MibTableRow
wfAtmVbrCsVciEntry = _WfAtmVbrCsVciEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1)
)
wfAtmVbrCsVciEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrCsVciLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrCsVciLLIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmVbrCsVciIndex"),
)
if mibBuilder.loadTexts:
    wfAtmVbrCsVciEntry.setStatus("mandatory")
_WfAtmVbrCsVciVbrCct_Type = Integer32
_WfAtmVbrCsVciVbrCct_Object = MibTableColumn
wfAtmVbrCsVciVbrCct = _WfAtmVbrCsVciVbrCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 1),
    _WfAtmVbrCsVciVbrCct_Type()
)
wfAtmVbrCsVciVbrCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciVbrCct.setStatus("mandatory")


class _WfAtmVbrCsVciIndex_Type(Integer32):
    """Custom type wfAtmVbrCsVciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_WfAtmVbrCsVciIndex_Type.__name__ = "Integer32"
_WfAtmVbrCsVciIndex_Object = MibTableColumn
wfAtmVbrCsVciIndex = _WfAtmVbrCsVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 2),
    _WfAtmVbrCsVciIndex_Type()
)
wfAtmVbrCsVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciIndex.setStatus("mandatory")
_WfAtmVbrCsVciBETagMismatches_Type = Counter32
_WfAtmVbrCsVciBETagMismatches_Object = MibTableColumn
wfAtmVbrCsVciBETagMismatches = _WfAtmVbrCsVciBETagMismatches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 3),
    _WfAtmVbrCsVciBETagMismatches_Type()
)
wfAtmVbrCsVciBETagMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciBETagMismatches.setStatus("mandatory")
_WfAtmVbrCsVciLengthMismatches_Type = Counter32
_WfAtmVbrCsVciLengthMismatches_Object = MibTableColumn
wfAtmVbrCsVciLengthMismatches = _WfAtmVbrCsVciLengthMismatches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 4),
    _WfAtmVbrCsVciLengthMismatches_Type()
)
wfAtmVbrCsVciLengthMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciLengthMismatches.setStatus("mandatory")
_WfAtmVbrCsVciMisdeliveredPdus_Type = Counter32
_WfAtmVbrCsVciMisdeliveredPdus_Object = MibTableColumn
wfAtmVbrCsVciMisdeliveredPdus = _WfAtmVbrCsVciMisdeliveredPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 5),
    _WfAtmVbrCsVciMisdeliveredPdus_Type()
)
wfAtmVbrCsVciMisdeliveredPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciMisdeliveredPdus.setStatus("mandatory")
_WfAtmVbrCsVciReceives_Type = Counter32
_WfAtmVbrCsVciReceives_Object = MibTableColumn
wfAtmVbrCsVciReceives = _WfAtmVbrCsVciReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 6),
    _WfAtmVbrCsVciReceives_Type()
)
wfAtmVbrCsVciReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciReceives.setStatus("mandatory")
_WfAtmVbrCsVciTransmits_Type = Counter32
_WfAtmVbrCsVciTransmits_Object = MibTableColumn
wfAtmVbrCsVciTransmits = _WfAtmVbrCsVciTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 7),
    _WfAtmVbrCsVciTransmits_Type()
)
wfAtmVbrCsVciTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciTransmits.setStatus("mandatory")
_WfAtmVbrCsVciOctetReceives_Type = Counter32
_WfAtmVbrCsVciOctetReceives_Object = MibTableColumn
wfAtmVbrCsVciOctetReceives = _WfAtmVbrCsVciOctetReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 8),
    _WfAtmVbrCsVciOctetReceives_Type()
)
wfAtmVbrCsVciOctetReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciOctetReceives.setStatus("mandatory")
_WfAtmVbrCsVciOctetTransmits_Type = Counter32
_WfAtmVbrCsVciOctetTransmits_Object = MibTableColumn
wfAtmVbrCsVciOctetTransmits = _WfAtmVbrCsVciOctetTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 9),
    _WfAtmVbrCsVciOctetTransmits_Type()
)
wfAtmVbrCsVciOctetTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciOctetTransmits.setStatus("mandatory")
_WfAtmVbrCsVciLineNumber_Type = Integer32
_WfAtmVbrCsVciLineNumber_Object = MibTableColumn
wfAtmVbrCsVciLineNumber = _WfAtmVbrCsVciLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 10),
    _WfAtmVbrCsVciLineNumber_Type()
)
wfAtmVbrCsVciLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciLineNumber.setStatus("mandatory")
_WfAtmVbrCsVciLLIndex_Type = Integer32
_WfAtmVbrCsVciLLIndex_Object = MibTableColumn
wfAtmVbrCsVciLLIndex = _WfAtmVbrCsVciLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 12, 1, 11),
    _WfAtmVbrCsVciLLIndex_Type()
)
wfAtmVbrCsVciLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmVbrCsVciLLIndex.setStatus("mandatory")
_WfAtmMpeTable_Object = MibTable
wfAtmMpeTable = _WfAtmMpeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13)
)
if mibBuilder.loadTexts:
    wfAtmMpeTable.setStatus("mandatory")
_WfAtmMpeEntry_Object = MibTableRow
wfAtmMpeEntry = _WfAtmMpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1)
)
wfAtmMpeEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    wfAtmMpeEntry.setStatus("mandatory")


class _WfAtmMpeIndex_Type(Integer32):
    """Custom type wfAtmMpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfAtmMpeIndex_Type.__name__ = "Integer32"
_WfAtmMpeIndex_Object = MibTableColumn
wfAtmMpeIndex = _WfAtmMpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 1),
    _WfAtmMpeIndex_Type()
)
wfAtmMpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeIndex.setStatus("mandatory")
_WfAtmMpeInvalidNlpids_Type = Counter32
_WfAtmMpeInvalidNlpids_Object = MibTableColumn
wfAtmMpeInvalidNlpids = _WfAtmMpeInvalidNlpids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 2),
    _WfAtmMpeInvalidNlpids_Type()
)
wfAtmMpeInvalidNlpids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeInvalidNlpids.setStatus("mandatory")
_WfAtmMpeInvalidPids_Type = Counter32
_WfAtmMpeInvalidPids_Object = MibTableColumn
wfAtmMpeInvalidPids = _WfAtmMpeInvalidPids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 3),
    _WfAtmMpeInvalidPids_Type()
)
wfAtmMpeInvalidPids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeInvalidPids.setStatus("mandatory")
_WfAtmMpeInvalidOuis_Type = Counter32
_WfAtmMpeInvalidOuis_Object = MibTableColumn
wfAtmMpeInvalidOuis = _WfAtmMpeInvalidOuis_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 4),
    _WfAtmMpeInvalidOuis_Type()
)
wfAtmMpeInvalidOuis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeInvalidOuis.setStatus("mandatory")
_WfAtmMpeMisdeliveredPdus_Type = Counter32
_WfAtmMpeMisdeliveredPdus_Object = MibTableColumn
wfAtmMpeMisdeliveredPdus = _WfAtmMpeMisdeliveredPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 5),
    _WfAtmMpeMisdeliveredPdus_Type()
)
wfAtmMpeMisdeliveredPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeMisdeliveredPdus.setStatus("mandatory")
_WfAtmMpeUnsupportedControlFields_Type = Counter32
_WfAtmMpeUnsupportedControlFields_Object = MibTableColumn
wfAtmMpeUnsupportedControlFields = _WfAtmMpeUnsupportedControlFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 6),
    _WfAtmMpeUnsupportedControlFields_Type()
)
wfAtmMpeUnsupportedControlFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeUnsupportedControlFields.setStatus("mandatory")
_WfAtmMpeInvalidSAP_Type = Counter32
_WfAtmMpeInvalidSAP_Object = MibTableColumn
wfAtmMpeInvalidSAP = _WfAtmMpeInvalidSAP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 13, 1, 7),
    _WfAtmMpeInvalidSAP_Type()
)
wfAtmMpeInvalidSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmMpeInvalidSAP.setStatus("mandatory")
_WfAtmPvcTable_Object = MibTable
wfAtmPvcTable = _WfAtmPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14)
)
if mibBuilder.loadTexts:
    wfAtmPvcTable.setStatus("mandatory")
_WfAtmPvcEntry_Object = MibTableRow
wfAtmPvcEntry = _WfAtmPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1)
)
wfAtmPvcEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmPvcLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmPvcLLIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmPvcVpi"),
    (0, "Wellfleet-ATM-MIB", "wfAtmPvcVci"),
)
if mibBuilder.loadTexts:
    wfAtmPvcEntry.setStatus("mandatory")


class _WfAtmPvcDelete_Type(Integer32):
    """Custom type wfAtmPvcDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmPvcDelete_Type.__name__ = "Integer32"
_WfAtmPvcDelete_Object = MibTableColumn
wfAtmPvcDelete = _WfAtmPvcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 1),
    _WfAtmPvcDelete_Type()
)
wfAtmPvcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcDelete.setStatus("mandatory")
_WfAtmPvcCct_Type = Integer32
_WfAtmPvcCct_Object = MibTableColumn
wfAtmPvcCct = _WfAtmPvcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 2),
    _WfAtmPvcCct_Type()
)
wfAtmPvcCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcCct.setStatus("mandatory")


class _WfAtmPvcVpi_Type(Integer32):
    """Custom type wfAtmPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAtmPvcVpi_Type.__name__ = "Integer32"
_WfAtmPvcVpi_Object = MibTableColumn
wfAtmPvcVpi = _WfAtmPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 3),
    _WfAtmPvcVpi_Type()
)
wfAtmPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcVpi.setStatus("mandatory")


class _WfAtmPvcVci_Type(Integer32):
    """Custom type wfAtmPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfAtmPvcVci_Type.__name__ = "Integer32"
_WfAtmPvcVci_Object = MibTableColumn
wfAtmPvcVci = _WfAtmPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 4),
    _WfAtmPvcVci_Type()
)
wfAtmPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcVci.setStatus("mandatory")
_WfAtmPvcReceives_Type = Counter32
_WfAtmPvcReceives_Object = MibTableColumn
wfAtmPvcReceives = _WfAtmPvcReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 5),
    _WfAtmPvcReceives_Type()
)
wfAtmPvcReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcReceives.setStatus("mandatory")
_WfAtmPvcTransmits_Type = Counter32
_WfAtmPvcTransmits_Object = MibTableColumn
wfAtmPvcTransmits = _WfAtmPvcTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 6),
    _WfAtmPvcTransmits_Type()
)
wfAtmPvcTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcTransmits.setStatus("mandatory")
_WfAtmPvcOctetReceives_Type = Counter32
_WfAtmPvcOctetReceives_Object = MibTableColumn
wfAtmPvcOctetReceives = _WfAtmPvcOctetReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 7),
    _WfAtmPvcOctetReceives_Type()
)
wfAtmPvcOctetReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcOctetReceives.setStatus("mandatory")
_WfAtmPvcOctetTransmits_Type = Counter32
_WfAtmPvcOctetTransmits_Object = MibTableColumn
wfAtmPvcOctetTransmits = _WfAtmPvcOctetTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 8),
    _WfAtmPvcOctetTransmits_Type()
)
wfAtmPvcOctetTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcOctetTransmits.setStatus("mandatory")


class _WfAtmPvcMode_Type(Integer32):
    """Custom type wfAtmPvcMode based on Integer32"""
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
        *(("direct", 3),
          ("groupaccess", 1),
          ("hybridaccess", 2))
    )


_WfAtmPvcMode_Type.__name__ = "Integer32"
_WfAtmPvcMode_Object = MibTableColumn
wfAtmPvcMode = _WfAtmPvcMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 9),
    _WfAtmPvcMode_Type()
)
wfAtmPvcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcMode.setStatus("mandatory")
_WfAtmPvcDirectAccessCct_Type = Integer32
_WfAtmPvcDirectAccessCct_Object = MibTableColumn
wfAtmPvcDirectAccessCct = _WfAtmPvcDirectAccessCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 10),
    _WfAtmPvcDirectAccessCct_Type()
)
wfAtmPvcDirectAccessCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcDirectAccessCct.setStatus("mandatory")


class _WfAtmPvcState_Type(Integer32):
    """Custom type wfAtmPvcState based on Integer32"""
    defaultValue = 4

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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAtmPvcState_Type.__name__ = "Integer32"
_WfAtmPvcState_Object = MibTableColumn
wfAtmPvcState = _WfAtmPvcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 11),
    _WfAtmPvcState_Type()
)
wfAtmPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcState.setStatus("mandatory")


class _WfAtmPvcMpeNull_Type(Integer32):
    """Custom type wfAtmPvcMpeNull based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mpe1294", 1),
          ("mpe1483", 3),
          ("null", 2))
    )


_WfAtmPvcMpeNull_Type.__name__ = "Integer32"
_WfAtmPvcMpeNull_Object = MibTableColumn
wfAtmPvcMpeNull = _WfAtmPvcMpeNull_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 12),
    _WfAtmPvcMpeNull_Type()
)
wfAtmPvcMpeNull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcMpeNull.setStatus("mandatory")


class _WfAtmPvcCsNull_Type(Integer32):
    """Custom type wfAtmPvcCsNull based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal34", 1),
          ("aal5", 3),
          ("null", 2))
    )


_WfAtmPvcCsNull_Type.__name__ = "Integer32"
_WfAtmPvcCsNull_Object = MibTableColumn
wfAtmPvcCsNull = _WfAtmPvcCsNull_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 13),
    _WfAtmPvcCsNull_Type()
)
wfAtmPvcCsNull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcCsNull.setStatus("mandatory")


class _WfAtmPvcDisable_Type(Integer32):
    """Custom type wfAtmPvcDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmPvcDisable_Type.__name__ = "Integer32"
_WfAtmPvcDisable_Object = MibTableColumn
wfAtmPvcDisable = _WfAtmPvcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 14),
    _WfAtmPvcDisable_Type()
)
wfAtmPvcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcDisable.setStatus("mandatory")
_WfAtmPvcDrops_Type = Counter32
_WfAtmPvcDrops_Object = MibTableColumn
wfAtmPvcDrops = _WfAtmPvcDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 15),
    _WfAtmPvcDrops_Type()
)
wfAtmPvcDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcDrops.setStatus("mandatory")


class _WfAtmPvcMulticast_Type(Integer32):
    """Custom type wfAtmPvcMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_WfAtmPvcMulticast_Type.__name__ = "Integer32"
_WfAtmPvcMulticast_Object = MibTableColumn
wfAtmPvcMulticast = _WfAtmPvcMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 16),
    _WfAtmPvcMulticast_Type()
)
wfAtmPvcMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmPvcMulticast.setStatus("mandatory")
_WfAtmPvcLineNumber_Type = Integer32
_WfAtmPvcLineNumber_Object = MibTableColumn
wfAtmPvcLineNumber = _WfAtmPvcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 17),
    _WfAtmPvcLineNumber_Type()
)
wfAtmPvcLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcLineNumber.setStatus("mandatory")
_WfAtmPvcLLIndex_Type = Integer32
_WfAtmPvcLLIndex_Object = MibTableColumn
wfAtmPvcLLIndex = _WfAtmPvcLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 14, 1, 18),
    _WfAtmPvcLLIndex_Type()
)
wfAtmPvcLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmPvcLLIndex.setStatus("mandatory")
_WfAtmDxiTable_Object = MibTable
wfAtmDxiTable = _WfAtmDxiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15)
)
if mibBuilder.loadTexts:
    wfAtmDxiTable.setStatus("mandatory")
_WfAtmDxiEntry_Object = MibTableRow
wfAtmDxiEntry = _WfAtmDxiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1)
)
wfAtmDxiEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiLLIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiComponent"),
)
if mibBuilder.loadTexts:
    wfAtmDxiEntry.setStatus("mandatory")
_WfAtmDxiCct_Type = Integer32
_WfAtmDxiCct_Object = MibTableColumn
wfAtmDxiCct = _WfAtmDxiCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 1),
    _WfAtmDxiCct_Type()
)
wfAtmDxiCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiCct.setStatus("mandatory")


class _WfAtmDxiComponent_Type(Integer32):
    """Custom type wfAtmDxiComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csudsu", 2),
          ("router", 1))
    )


_WfAtmDxiComponent_Type.__name__ = "Integer32"
_WfAtmDxiComponent_Object = MibTableColumn
wfAtmDxiComponent = _WfAtmDxiComponent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 2),
    _WfAtmDxiComponent_Type()
)
wfAtmDxiComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiComponent.setStatus("mandatory")
_WfAtmDxiMaxLmiPduLengthErrors_Type = Counter32
_WfAtmDxiMaxLmiPduLengthErrors_Object = MibTableColumn
wfAtmDxiMaxLmiPduLengthErrors = _WfAtmDxiMaxLmiPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 3),
    _WfAtmDxiMaxLmiPduLengthErrors_Type()
)
wfAtmDxiMaxLmiPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiMaxLmiPduLengthErrors.setStatus("mandatory")
_WfAtmDxiSeconds_Type = Counter32
_WfAtmDxiSeconds_Object = MibTableColumn
wfAtmDxiSeconds = _WfAtmDxiSeconds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 4),
    _WfAtmDxiSeconds_Type()
)
wfAtmDxiSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiSeconds.setStatus("mandatory")
_WfAtmDxiDiscardedFrames_Type = Counter32
_WfAtmDxiDiscardedFrames_Object = MibTableColumn
wfAtmDxiDiscardedFrames = _WfAtmDxiDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 5),
    _WfAtmDxiDiscardedFrames_Type()
)
wfAtmDxiDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDiscardedFrames.setStatus("mandatory")
_WfAtmDxiAbortedFrames_Type = Counter32
_WfAtmDxiAbortedFrames_Object = MibTableColumn
wfAtmDxiAbortedFrames = _WfAtmDxiAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 6),
    _WfAtmDxiAbortedFrames_Type()
)
wfAtmDxiAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiAbortedFrames.setStatus("mandatory")
_WfAtmDxiNonOctetAlignedFrames_Type = Counter32
_WfAtmDxiNonOctetAlignedFrames_Object = MibTableColumn
wfAtmDxiNonOctetAlignedFrames = _WfAtmDxiNonOctetAlignedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 7),
    _WfAtmDxiNonOctetAlignedFrames_Type()
)
wfAtmDxiNonOctetAlignedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiNonOctetAlignedFrames.setStatus("mandatory")
_WfAtmDxiTooLongFrames_Type = Counter32
_WfAtmDxiTooLongFrames_Object = MibTableColumn
wfAtmDxiTooLongFrames = _WfAtmDxiTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 8),
    _WfAtmDxiTooLongFrames_Type()
)
wfAtmDxiTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiTooLongFrames.setStatus("mandatory")
_WfAtmDxiTooShortFrames_Type = Counter32
_WfAtmDxiTooShortFrames_Object = MibTableColumn
wfAtmDxiTooShortFrames = _WfAtmDxiTooShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 9),
    _WfAtmDxiTooShortFrames_Type()
)
wfAtmDxiTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiTooShortFrames.setStatus("mandatory")
_WfAtmDxiFrameChecksumErrors_Type = Counter32
_WfAtmDxiFrameChecksumErrors_Object = MibTableColumn
wfAtmDxiFrameChecksumErrors = _WfAtmDxiFrameChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 10),
    _WfAtmDxiFrameChecksumErrors_Type()
)
wfAtmDxiFrameChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiFrameChecksumErrors.setStatus("mandatory")
_WfAtmDxiFrameHeaderErrors_Type = Counter32
_WfAtmDxiFrameHeaderErrors_Object = MibTableColumn
wfAtmDxiFrameHeaderErrors = _WfAtmDxiFrameHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 11),
    _WfAtmDxiFrameHeaderErrors_Type()
)
wfAtmDxiFrameHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiFrameHeaderErrors.setStatus("mandatory")
_WfAtmDxiValidFrameReceives_Type = Counter32
_WfAtmDxiValidFrameReceives_Object = MibTableColumn
wfAtmDxiValidFrameReceives = _WfAtmDxiValidFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 12),
    _WfAtmDxiValidFrameReceives_Type()
)
wfAtmDxiValidFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiValidFrameReceives.setStatus("mandatory")
_WfAtmDxiFrameTransmits_Type = Counter32
_WfAtmDxiFrameTransmits_Object = MibTableColumn
wfAtmDxiFrameTransmits = _WfAtmDxiFrameTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 13),
    _WfAtmDxiFrameTransmits_Type()
)
wfAtmDxiFrameTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiFrameTransmits.setStatus("mandatory")
_WfAtmDxiLineNumber_Type = Integer32
_WfAtmDxiLineNumber_Object = MibTableColumn
wfAtmDxiLineNumber = _WfAtmDxiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 14),
    _WfAtmDxiLineNumber_Type()
)
wfAtmDxiLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiLineNumber.setStatus("mandatory")
_WfAtmDxiLLIndex_Type = Integer32
_WfAtmDxiLLIndex_Object = MibTableColumn
wfAtmDxiLLIndex = _WfAtmDxiLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 15, 1, 15),
    _WfAtmDxiLLIndex_Type()
)
wfAtmDxiLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiLLIndex.setStatus("mandatory")
_WfAtmDxiDxiAddrTable_Object = MibTable
wfAtmDxiDxiAddrTable = _WfAtmDxiDxiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16)
)
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrTable.setStatus("mandatory")
_WfAtmDxiDxiAddrEntry_Object = MibTableRow
wfAtmDxiDxiAddrEntry = _WfAtmDxiDxiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1)
)
wfAtmDxiDxiAddrEntry.setIndexNames(
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiDxiAddrLineNumber"),
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiDxiAddrLLIndex"),
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiDxiAddrDxiComponent"),
    (0, "Wellfleet-ATM-MIB", "wfAtmDxiDxiAddrIndex"),
)
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrEntry.setStatus("mandatory")
_WfAtmDxiDxiAddrDxiCct_Type = Integer32
_WfAtmDxiDxiAddrDxiCct_Object = MibTableColumn
wfAtmDxiDxiAddrDxiCct = _WfAtmDxiDxiAddrDxiCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 1),
    _WfAtmDxiDxiAddrDxiCct_Type()
)
wfAtmDxiDxiAddrDxiCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrDxiCct.setStatus("mandatory")


class _WfAtmDxiDxiAddrDxiComponent_Type(Integer32):
    """Custom type wfAtmDxiDxiAddrDxiComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csudsu", 2),
          ("router", 1))
    )


_WfAtmDxiDxiAddrDxiComponent_Type.__name__ = "Integer32"
_WfAtmDxiDxiAddrDxiComponent_Object = MibTableColumn
wfAtmDxiDxiAddrDxiComponent = _WfAtmDxiDxiAddrDxiComponent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 2),
    _WfAtmDxiDxiAddrDxiComponent_Type()
)
wfAtmDxiDxiAddrDxiComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrDxiComponent.setStatus("mandatory")


class _WfAtmDxiDxiAddrIndex_Type(Integer32):
    """Custom type wfAtmDxiDxiAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_WfAtmDxiDxiAddrIndex_Type.__name__ = "Integer32"
_WfAtmDxiDxiAddrIndex_Object = MibTableColumn
wfAtmDxiDxiAddrIndex = _WfAtmDxiDxiAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 3),
    _WfAtmDxiDxiAddrIndex_Type()
)
wfAtmDxiDxiAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrIndex.setStatus("mandatory")
_WfAtmDxiDxiAddrAtmVbr_Type = ObjectIdentifier
_WfAtmDxiDxiAddrAtmVbr_Object = MibTableColumn
wfAtmDxiDxiAddrAtmVbr = _WfAtmDxiDxiAddrAtmVbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 4),
    _WfAtmDxiDxiAddrAtmVbr_Type()
)
wfAtmDxiDxiAddrAtmVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrAtmVbr.setStatus("mandatory")


class _WfAtmDxiDxiAddrVpiVci_Type(Integer32):
    """Custom type wfAtmDxiDxiAddrVpiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_WfAtmDxiDxiAddrVpiVci_Type.__name__ = "Integer32"
_WfAtmDxiDxiAddrVpiVci_Object = MibTableColumn
wfAtmDxiDxiAddrVpiVci = _WfAtmDxiDxiAddrVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 5),
    _WfAtmDxiDxiAddrVpiVci_Type()
)
wfAtmDxiDxiAddrVpiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrVpiVci.setStatus("mandatory")
_WfAtmDxiDxiAddrReceives_Type = Counter32
_WfAtmDxiDxiAddrReceives_Object = MibTableColumn
wfAtmDxiDxiAddrReceives = _WfAtmDxiDxiAddrReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 6),
    _WfAtmDxiDxiAddrReceives_Type()
)
wfAtmDxiDxiAddrReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrReceives.setStatus("mandatory")
_WfAtmDxiDxiAddrTransmits_Type = Counter32
_WfAtmDxiDxiAddrTransmits_Object = MibTableColumn
wfAtmDxiDxiAddrTransmits = _WfAtmDxiDxiAddrTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 7),
    _WfAtmDxiDxiAddrTransmits_Type()
)
wfAtmDxiDxiAddrTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrTransmits.setStatus("mandatory")
_WfAtmDxiDxiAddrLineNumber_Type = Integer32
_WfAtmDxiDxiAddrLineNumber_Object = MibTableColumn
wfAtmDxiDxiAddrLineNumber = _WfAtmDxiDxiAddrLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 8),
    _WfAtmDxiDxiAddrLineNumber_Type()
)
wfAtmDxiDxiAddrLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrLineNumber.setStatus("mandatory")
_WfAtmDxiDxiAddrLLIndex_Type = Integer32
_WfAtmDxiDxiAddrLLIndex_Object = MibTableColumn
wfAtmDxiDxiAddrLLIndex = _WfAtmDxiDxiAddrLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 16, 1, 9),
    _WfAtmDxiDxiAddrLLIndex_Type()
)
wfAtmDxiDxiAddrLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmDxiDxiAddrLLIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ATM-MIB",
    **{"wfAtmCommonGroup": wfAtmCommonGroup,
       "wfAtmInterfaceConfTable": wfAtmInterfaceConfTable,
       "wfAtmInterfaceConfEntry": wfAtmInterfaceConfEntry,
       "wfAtmInterfaceConfDelete": wfAtmInterfaceConfDelete,
       "wfAtmInterfaceConfIndex": wfAtmInterfaceConfIndex,
       "wfAtmInterfaceAdminStatus": wfAtmInterfaceAdminStatus,
       "wfAtmInterfaceOperStatus": wfAtmInterfaceOperStatus,
       "wfAtmInterfaceMaxVpcs": wfAtmInterfaceMaxVpcs,
       "wfAtmInterfaceMaxVccs": wfAtmInterfaceMaxVccs,
       "wfAtmInterfaceConfVpcs": wfAtmInterfaceConfVpcs,
       "wfAtmInterfaceConfVccs": wfAtmInterfaceConfVccs,
       "wfAtmInterfaceMaxActiveVpiBits": wfAtmInterfaceMaxActiveVpiBits,
       "wfAtmInterfaceMaxActiveVciBits": wfAtmInterfaceMaxActiveVciBits,
       "wfAtmInterfaceIlmiVpi": wfAtmInterfaceIlmiVpi,
       "wfAtmInterfaceIlmiVci": wfAtmInterfaceIlmiVci,
       "wfAtmInterfaceAddressType": wfAtmInterfaceAddressType,
       "wfAtmInterfaceCct": wfAtmInterfaceCct,
       "wfAtmInterfaceDrops": wfAtmInterfaceDrops,
       "wfAtmInterfaceSigEnable": wfAtmInterfaceSigEnable,
       "wfAtmInterfaceDebug": wfAtmInterfaceDebug,
       "wfAtmInterfaceUseHwMacAddr": wfAtmInterfaceUseHwMacAddr,
       "wfAtmInterfaceHwMacOverride": wfAtmInterfaceHwMacOverride,
       "wfAtmServicePqOverride": wfAtmServicePqOverride,
       "wfAtmServiceRecordTable": wfAtmServiceRecordTable,
       "wfAtmServiceRecordEntry": wfAtmServiceRecordEntry,
       "wfAtmServiceRecordDelete": wfAtmServiceRecordDelete,
       "wfAtmServiceRecordEnable": wfAtmServiceRecordEnable,
       "wfAtmServiceRecordIndex": wfAtmServiceRecordIndex,
       "wfAtmServiceRecordCct": wfAtmServiceRecordCct,
       "wfAtmServiceRecordAalEncapsType": wfAtmServiceRecordAalEncapsType,
       "wfAtmServiceRecordState": wfAtmServiceRecordState,
       "wfAtmServiceRecordVcType": wfAtmServiceRecordVcType,
       "wfAtmServiceRecordNetworkPrefix": wfAtmServiceRecordNetworkPrefix,
       "wfAtmServiceRecordUserSuffix": wfAtmServiceRecordUserSuffix,
       "wfAtmServiceRecordAtmAddress": wfAtmServiceRecordAtmAddress,
       "wfAtmServiceRecordFlag": wfAtmServiceRecordFlag,
       "wfAtmServiceRecordMtu": wfAtmServiceRecordMtu,
       "wfAtmServiceRecordLossPriorityPolicy": wfAtmServiceRecordLossPriorityPolicy,
       "wfAtmServiceRecordDebug": wfAtmServiceRecordDebug,
       "wfAtmServiceRecordName": wfAtmServiceRecordName,
       "wfAtmServiceRecordWanSvcRoutingMode": wfAtmServiceRecordWanSvcRoutingMode,
       "wfAtmVclConfTable": wfAtmVclConfTable,
       "wfAtmVclConfEntry": wfAtmVclConfEntry,
       "wfAtmVclConfDelete": wfAtmVclConfDelete,
       "wfAtmVclConfIndex": wfAtmVclConfIndex,
       "wfAtmVclConfVpi": wfAtmVclConfVpi,
       "wfAtmVclConfVci": wfAtmVclConfVci,
       "wfAtmVclAdminStatus": wfAtmVclAdminStatus,
       "wfAtmVclOperStatus": wfAtmVclOperStatus,
       "wfAtmVclLastChange": wfAtmVclLastChange,
       "wfAtmVclXmtPeakCellRate": wfAtmVclXmtPeakCellRate,
       "wfAtmVclXmtSustainableCellRate": wfAtmVclXmtSustainableCellRate,
       "wfAtmVclXmtBurstSize": wfAtmVclXmtBurstSize,
       "wfAtmVclXmtQosClass": wfAtmVclXmtQosClass,
       "wfAtmVclRcvPeakCellRate": wfAtmVclRcvPeakCellRate,
       "wfAtmVclRcvSustainableCellRate": wfAtmVclRcvSustainableCellRate,
       "wfAtmVclRcvBurstSize": wfAtmVclRcvBurstSize,
       "wfAtmVclRcvQosClass": wfAtmVclRcvQosClass,
       "wfAtmVclAalType": wfAtmVclAalType,
       "wfAtmVclAalCpcsTransmitSduSize": wfAtmVclAalCpcsTransmitSduSize,
       "wfAtmVclAalCpcsReceiveSduSize": wfAtmVclAalCpcsReceiveSduSize,
       "wfAtmVclAalEncapsType": wfAtmVclAalEncapsType,
       "wfAtmVclCongestionIndication": wfAtmVclCongestionIndication,
       "wfAtmVclCellLossPriority": wfAtmVclCellLossPriority,
       "wfAtmVclCct": wfAtmVclCct,
       "wfAtmVclDirectAccessCct": wfAtmVclDirectAccessCct,
       "wfAtmVclMulticast": wfAtmVclMulticast,
       "wfAtmVclMode": wfAtmVclMode,
       "wfAtmVclDrops": wfAtmVclDrops,
       "wfAtmVclVcIndex": wfAtmVclVcIndex,
       "wfAtmVclVcType": wfAtmVclVcType,
       "wfAtmVclXmtTagging": wfAtmVclXmtTagging,
       "wfAtmVclRcvTagging": wfAtmVclRcvTagging,
       "wfAtmVclOamLpbkEnable": wfAtmVclOamLpbkEnable,
       "wfAtmVclOamLpbkCellInterval": wfAtmVclOamLpbkCellInterval,
       "wfAtmVclOamLpbkThreshold1": wfAtmVclOamLpbkThreshold1,
       "wfAtmVclOamLpbkThreshold2": wfAtmVclOamLpbkThreshold2,
       "wfAtmVclOamAlarmEnable": wfAtmVclOamAlarmEnable,
       "wfAtmVclVcGroup": wfAtmVclVcGroup,
       "wfAtmVclServiceClass": wfAtmVclServiceClass,
       "wfAtmVclServiceCategory": wfAtmVclServiceCategory,
       "wfAtmVclVBRType": wfAtmVclVBRType,
       "wfAtmVclXmtMinimumCellRate": wfAtmVclXmtMinimumCellRate,
       "wfAtmVclXmtInitialCellRate": wfAtmVclXmtInitialCellRate,
       "wfAtmVclXmtRateIncreaseFactor": wfAtmVclXmtRateIncreaseFactor,
       "wfAtmVclXmtRateDecreaseFactor": wfAtmVclXmtRateDecreaseFactor,
       "wfAtmVclStatsTable": wfAtmVclStatsTable,
       "wfAtmVclStatsEntry": wfAtmVclStatsEntry,
       "wfAtmVclStatsIndex": wfAtmVclStatsIndex,
       "wfAtmVclStatsVpi": wfAtmVclStatsVpi,
       "wfAtmVclStatsVci": wfAtmVclStatsVci,
       "wfAtmVclStatsVcIndex": wfAtmVclStatsVcIndex,
       "wfAtmVclXmtCells": wfAtmVclXmtCells,
       "wfAtmVclRcvCells": wfAtmVclRcvCells,
       "wfAtmVclRcvSequenceNumErrs": wfAtmVclRcvSequenceNumErrs,
       "wfAtmVclRcvInvalidLenErrs": wfAtmVclRcvInvalidLenErrs,
       "wfAtmVclRcvMissingEomErrs": wfAtmVclRcvMissingEomErrs,
       "wfAtmVclRcvBufferOflowErrs": wfAtmVclRcvBufferOflowErrs,
       "wfAtmVclRcvMaxLenExceedErrs": wfAtmVclRcvMaxLenExceedErrs,
       "wfAtmVclRcvTrailerErrs": wfAtmVclRcvTrailerErrs,
       "wfAtmVclRcvAbortErrs": wfAtmVclRcvAbortErrs,
       "wfAtmVclRcvPacketLengthErrs": wfAtmVclRcvPacketLengthErrs,
       "wfAtmVclRcvReassemAbortErrs": wfAtmVclRcvReassemAbortErrs,
       "wfAtmVclRcvCrcErrs": wfAtmVclRcvCrcErrs,
       "wfAtmVclXmtOamCells": wfAtmVclXmtOamCells,
       "wfAtmVclRcvOamCells": wfAtmVclRcvOamCells,
       "wfAtmVclRcvOamCrcErrs": wfAtmVclRcvOamCrcErrs,
       "wfAtmSigTable": wfAtmSigTable,
       "wfAtmSigEntry": wfAtmSigEntry,
       "wfAtmSigDelete": wfAtmSigDelete,
       "wfAtmSigDisable": wfAtmSigDisable,
       "wfAtmSigLineNumber": wfAtmSigLineNumber,
       "wfAtmSigAtmCct": wfAtmSigAtmCct,
       "wfAtmSigState": wfAtmSigState,
       "wfAtmSigMaxServiceUsers": wfAtmSigMaxServiceUsers,
       "wfAtmSigMaxPtPtConnections": wfAtmSigMaxPtPtConnections,
       "wfAtmSigMaxPtMultConnections": wfAtmSigMaxPtMultConnections,
       "wfAtmSigMaxPartiesInMultConnect": wfAtmSigMaxPartiesInMultConnect,
       "wfAtmSigMaxRoutingRegistrations": wfAtmSigMaxRoutingRegistrations,
       "wfAtmSigMinBufferThreshold": wfAtmSigMinBufferThreshold,
       "wfAtmSigTimerResolution": wfAtmSigTimerResolution,
       "wfAtmSigVpi": wfAtmSigVpi,
       "wfAtmSigVci": wfAtmSigVci,
       "wfAtmSigStandard": wfAtmSigStandard,
       "wfAtmSigInterfaceType": wfAtmSigInterfaceType,
       "wfAtmSigMinVciPtPt": wfAtmSigMinVciPtPt,
       "wfAtmSigMaxVciPtPt": wfAtmSigMaxVciPtPt,
       "wfAtmSigMinVpiPtPt": wfAtmSigMinVpiPtPt,
       "wfAtmSigMaxVpiPtPt": wfAtmSigMaxVpiPtPt,
       "wfAtmSigMinVciPtMltPt": wfAtmSigMinVciPtMltPt,
       "wfAtmSigMaxVciPtMltPt": wfAtmSigMaxVciPtMltPt,
       "wfAtmSigMinVpiPtMltPt": wfAtmSigMinVpiPtMltPt,
       "wfAtmSigMaxVpiPtMltPt": wfAtmSigMaxVpiPtMltPt,
       "wfAtmSigT303": wfAtmSigT303,
       "wfAtmSigT308": wfAtmSigT308,
       "wfAtmSigT309": wfAtmSigT309,
       "wfAtmSigT310": wfAtmSigT310,
       "wfAtmSigT313": wfAtmSigT313,
       "wfAtmSigT316": wfAtmSigT316,
       "wfAtmSigT316c": wfAtmSigT316c,
       "wfAtmSigT322": wfAtmSigT322,
       "wfAtmSigTDisc": wfAtmSigTDisc,
       "wfAtmSigT398": wfAtmSigT398,
       "wfAtmSigT399": wfAtmSigT399,
       "wfAtmSigNumRst": wfAtmSigNumRst,
       "wfAtmSigNumStat": wfAtmSigNumStat,
       "wfAtmSigRestart": wfAtmSigRestart,
       "wfAtmSigDebug": wfAtmSigDebug,
       "wfAtmSigCallsSec": wfAtmSigCallsSec,
       "wfAtmSigT301": wfAtmSigT301,
       "wfAtmSigT304": wfAtmSigT304,
       "wfAtmSigT397": wfAtmSigT397,
       "wfAtmSscopTable": wfAtmSscopTable,
       "wfAtmSscopEntry": wfAtmSscopEntry,
       "wfAtmSscopDelete": wfAtmSscopDelete,
       "wfAtmSscopDisable": wfAtmSscopDisable,
       "wfAtmSscopLineNumber": wfAtmSscopLineNumber,
       "wfAtmSscopAtmCct": wfAtmSscopAtmCct,
       "wfAtmSscopState": wfAtmSscopState,
       "wfAtmSscopLowThreshold": wfAtmSscopLowThreshold,
       "wfAtmSscopUpThreshold": wfAtmSscopUpThreshold,
       "wfAtmSscopArbitration": wfAtmSscopArbitration,
       "wfAtmSscopPollTimer": wfAtmSscopPollTimer,
       "wfAtmSscopKeepAliveTimer": wfAtmSscopKeepAliveTimer,
       "wfAtmSscopNoResponseTimer": wfAtmSscopNoResponseTimer,
       "wfAtmSscopConnectControlTimer": wfAtmSscopConnectControlTimer,
       "wfAtmSscopMaxCc": wfAtmSscopMaxCc,
       "wfAtmSscopMaxPd": wfAtmSscopMaxPd,
       "wfAtmSscopMaxStat": wfAtmSscopMaxStat,
       "wfAtmSscopIdleTimer": wfAtmSscopIdleTimer,
       "wfAtmSscopStandard": wfAtmSscopStandard,
       "wfAtmSscopDebug": wfAtmSscopDebug,
       "wfAtmIlmiTable": wfAtmIlmiTable,
       "wfAtmIlmiEntry": wfAtmIlmiEntry,
       "wfAtmIlmiDelete": wfAtmIlmiDelete,
       "wfAtmIlmiDisable": wfAtmIlmiDisable,
       "wfAtmIlmiLineNumber": wfAtmIlmiLineNumber,
       "wfAtmIlmiAtmCct": wfAtmIlmiAtmCct,
       "wfAtmIlmiState": wfAtmIlmiState,
       "wfAtmIlmiLowThreshold": wfAtmIlmiLowThreshold,
       "wfAtmIlmiUpThreshold": wfAtmIlmiUpThreshold,
       "wfAtmIlmiVpi": wfAtmIlmiVpi,
       "wfAtmIlmiVci": wfAtmIlmiVci,
       "wfAtmIlmiInterfaceType": wfAtmIlmiInterfaceType,
       "wfAtmIlmiLocalPort": wfAtmIlmiLocalPort,
       "wfAtmIlmiRemotePort": wfAtmIlmiRemotePort,
       "wfAtmIlmiGetTimer": wfAtmIlmiGetTimer,
       "wfAtmIlmiGetRetryCnt": wfAtmIlmiGetRetryCnt,
       "wfAtmIlmiGetNextTimer": wfAtmIlmiGetNextTimer,
       "wfAtmIlmiGetNextRetryCnt": wfAtmIlmiGetNextRetryCnt,
       "wfAtmIlmiSetTimer": wfAtmIlmiSetTimer,
       "wfAtmIlmiSetRetryCnt": wfAtmIlmiSetRetryCnt,
       "wfAtmIlmiLocalOid": wfAtmIlmiLocalOid,
       "wfAtmIlmiDebug": wfAtmIlmiDebug,
       "wfAtmIlmiNetPrefixTimer": wfAtmIlmiNetPrefixTimer,
       "wfAtmNetPrefixTable": wfAtmNetPrefixTable,
       "wfAtmNetPrefixEntry": wfAtmNetPrefixEntry,
       "wfAtmNetPrefixPort": wfAtmNetPrefixPort,
       "wfAtmNetPrefixPrefix": wfAtmNetPrefixPrefix,
       "wfAtmNetPrefixStatus": wfAtmNetPrefixStatus,
       "wfAtmTableDebugTable": wfAtmTableDebugTable,
       "wfAtmTableDebugEntry": wfAtmTableDebugEntry,
       "wfAtmTableDebugDelete": wfAtmTableDebugDelete,
       "wfAtmTableDebugSlot": wfAtmTableDebugSlot,
       "wfAtmTableDebugType": wfAtmTableDebugType,
       "wfAtmVcGroupTable": wfAtmVcGroupTable,
       "wfAtmVcGroupEntry": wfAtmVcGroupEntry,
       "wfAtmVcGroupDelete": wfAtmVcGroupDelete,
       "wfAtmVcGroupCct": wfAtmVcGroupCct,
       "wfAtmVcGroupIndex": wfAtmVcGroupIndex,
       "wfAtmVcGroupName": wfAtmVcGroupName,
       "wfAtmSVCOptionsTable": wfAtmSVCOptionsTable,
       "wfAtmSVCOptionsEntry": wfAtmSVCOptionsEntry,
       "wfAtmSVCOptionsDelete": wfAtmSVCOptionsDelete,
       "wfAtmSVCOptionsDisable": wfAtmSVCOptionsDisable,
       "wfAtmSVCOptionsCct": wfAtmSVCOptionsCct,
       "wfAtmSVCOptionsIndex": wfAtmSVCOptionsIndex,
       "wfAtmSVCOptionsAdjHostAtmAddr": wfAtmSVCOptionsAdjHostAtmAddr,
       "wfAtmSVCOptionsXmtPeakCellRate": wfAtmSVCOptionsXmtPeakCellRate,
       "wfAtmSVCOptionsXmtSustCellRate": wfAtmSVCOptionsXmtSustCellRate,
       "wfAtmSVCOptionsRcvPeakCellRate": wfAtmSVCOptionsRcvPeakCellRate,
       "wfAtmSVCOptionsRcvSustCellRate": wfAtmSVCOptionsRcvSustCellRate,
       "wfAtmSVCOptionsName": wfAtmSVCOptionsName,
       "wfAtmLinkModuleGroup": wfAtmLinkModuleGroup,
       "wfAtmAlcDrvTable": wfAtmAlcDrvTable,
       "wfAtmAlcDrvEntry": wfAtmAlcDrvEntry,
       "wfAtmAlcDelete": wfAtmAlcDelete,
       "wfAtmAlcDisable": wfAtmAlcDisable,
       "wfAtmAlcState": wfAtmAlcState,
       "wfAtmAlcSlot": wfAtmAlcSlot,
       "wfAtmAlcPort": wfAtmAlcPort,
       "wfAtmAlcCct": wfAtmAlcCct,
       "wfAtmAlcLineNumber": wfAtmAlcLineNumber,
       "wfAtmAlcType": wfAtmAlcType,
       "wfAtmAlcMtu": wfAtmAlcMtu,
       "wfAtmAlcSpeed": wfAtmAlcSpeed,
       "wfAtmAlcLastChange": wfAtmAlcLastChange,
       "wfAtmAlcInterfaceStatus": wfAtmAlcInterfaceStatus,
       "wfAtmAlcInterfaceIndex": wfAtmAlcInterfaceIndex,
       "wfAtmAlcDpNotify": wfAtmAlcDpNotify,
       "wfAtmAlcDpNotifyTimeout": wfAtmAlcDpNotifyTimeout,
       "wfAtmAlcConfControlQSize": wfAtmAlcConfControlQSize,
       "wfAtmAlcConfIntqSize": wfAtmAlcConfIntqSize,
       "wfAtmAlcConfLogqSize": wfAtmAlcConfLogqSize,
       "wfAtmAlcConfNumXmtQueues": wfAtmAlcConfNumXmtQueues,
       "wfAtmAlcUseDebugger": wfAtmAlcUseDebugger,
       "wfAtmAlcConfXmtClipSlotMax": wfAtmAlcConfXmtClipSlotMax,
       "wfAtmAlcXmtClipSlotMax": wfAtmAlcXmtClipSlotMax,
       "wfAtmAlcConfXmtClipQueueMax": wfAtmAlcConfXmtClipQueueMax,
       "wfAtmAlcXmtClipQueueMax": wfAtmAlcXmtClipQueueMax,
       "wfAtmAlcConfXmtClipQueueMin": wfAtmAlcConfXmtClipQueueMin,
       "wfAtmAlcXmtClipQueueMin": wfAtmAlcXmtClipQueueMin,
       "wfAtmAlcXmtQueueBurst": wfAtmAlcXmtQueueBurst,
       "wfAtmAlcXmtPackets": wfAtmAlcXmtPackets,
       "wfAtmAlcXmtPacketClips": wfAtmAlcXmtPacketClips,
       "wfAtmAlcXmtOctets": wfAtmAlcXmtOctets,
       "wfAtmAlcOutQLen": wfAtmAlcOutQLen,
       "wfAtmAlcRcvPackets": wfAtmAlcRcvPackets,
       "wfAtmAlcRcvReplenMisses": wfAtmAlcRcvReplenMisses,
       "wfAtmAlcConfRcvBuffersMax": wfAtmAlcConfRcvBuffersMax,
       "wfAtmAlcRcvBuffersMax": wfAtmAlcRcvBuffersMax,
       "wfAtmAlcMadrCt": wfAtmAlcMadrCt,
       "wfAtmAlcMadr": wfAtmAlcMadr,
       "wfAtmAlcVcInactEnable": wfAtmAlcVcInactEnable,
       "wfAtmAlcXmtBadVcs": wfAtmAlcXmtBadVcs,
       "wfAtmAlcXmtqTable": wfAtmAlcXmtqTable,
       "wfAtmAlcXmtqEntry": wfAtmAlcXmtqEntry,
       "wfAtmAlcXmtqIndex": wfAtmAlcXmtqIndex,
       "wfAtmAlcXmtqNumber": wfAtmAlcXmtqNumber,
       "wfAtmAlcXmtqState": wfAtmAlcXmtqState,
       "wfAtmAlcXmtqStickyMask": wfAtmAlcXmtqStickyMask,
       "wfAtmAlcXmtqVcs": wfAtmAlcXmtqVcs,
       "wfAtmAlcXmtqOutQLen": wfAtmAlcXmtqOutQLen,
       "wfAtmAlcXmtqOctets": wfAtmAlcXmtqOctets,
       "wfAtmAlcXmtqPackets": wfAtmAlcXmtqPackets,
       "wfAtmAlcXmtqPacketClips": wfAtmAlcXmtqPacketClips,
       "wfAtmAlcCopConfTable": wfAtmAlcCopConfTable,
       "wfAtmAlcCopConfEntry": wfAtmAlcCopConfEntry,
       "wfAtmAlcCopConfDelete": wfAtmAlcCopConfDelete,
       "wfAtmAlcCopConfIndex": wfAtmAlcCopConfIndex,
       "wfAtmAlcCopBufSize": wfAtmAlcCopBufSize,
       "wfAtmAlcCopConfXmtBufs": wfAtmAlcCopConfXmtBufs,
       "wfAtmAlcCopConfRcvBufs": wfAtmAlcCopConfRcvBufs,
       "wfAtmAlcCopDmaHighWatermark": wfAtmAlcCopDmaHighWatermark,
       "wfAtmAlcCopDmaLowWatermark": wfAtmAlcCopDmaLowWatermark,
       "wfAtmAlcCopCacheControl": wfAtmAlcCopCacheControl,
       "wfAtmAlcCopHwModId": wfAtmAlcCopHwModId,
       "wfAtmAlcCopVcInactTimeout": wfAtmAlcCopVcInactTimeout,
       "wfAtmAlcCopHwTable": wfAtmAlcCopHwTable,
       "wfAtmAlcCopHwEntry": wfAtmAlcCopHwEntry,
       "wfAtmAlcCopHwIndex": wfAtmAlcCopHwIndex,
       "wfAtmAlcCopType": wfAtmAlcCopType,
       "wfAtmAlcCopPktMemSize": wfAtmAlcCopPktMemSize,
       "wfAtmAlcCopCtlMemSize": wfAtmAlcCopCtlMemSize,
       "wfAtmAlcCopInsMemSize": wfAtmAlcCopInsMemSize,
       "wfAtmAlcCopAlcClockSpeed": wfAtmAlcCopAlcClockSpeed,
       "wfAtmAlcCopAlcVersion": wfAtmAlcCopAlcVersion,
       "wfAtmAlcCopNtcVersion": wfAtmAlcCopNtcVersion,
       "wfAtmAlcCopAtcVersion": wfAtmAlcCopAtcVersion,
       "wfAtmAlcCopInfoTable": wfAtmAlcCopInfoTable,
       "wfAtmAlcCopInfoEntry": wfAtmAlcCopInfoEntry,
       "wfAtmAlcCopInfoIndex": wfAtmAlcCopInfoIndex,
       "wfAtmAlcCopState": wfAtmAlcCopState,
       "wfAtmAlcCopConfigState": wfAtmAlcCopConfigState,
       "wfAtmAlcCopTotalBufs": wfAtmAlcCopTotalBufs,
       "wfAtmAlcCopTotalXmtBufs": wfAtmAlcCopTotalXmtBufs,
       "wfAtmAlcCopTotalRcvBufs": wfAtmAlcCopTotalRcvBufs,
       "wfAtmAlcCopDataPathTable": wfAtmAlcCopDataPathTable,
       "wfAtmAlcCopDataPathEntry": wfAtmAlcCopDataPathEntry,
       "wfAtmAlcCopDataPathIndex": wfAtmAlcCopDataPathIndex,
       "wfAtmAlcCopXmtPackets": wfAtmAlcCopXmtPackets,
       "wfAtmAlcCopXmtBuffers": wfAtmAlcCopXmtBuffers,
       "wfAtmAlcCopXmtErrBuffers": wfAtmAlcCopXmtErrBuffers,
       "wfAtmAlcCopXmtCells": wfAtmAlcCopXmtCells,
       "wfAtmAlcCopXmtUnassCells": wfAtmAlcCopXmtUnassCells,
       "wfAtmAlcCopXmtIdleCells": wfAtmAlcCopXmtIdleCells,
       "wfAtmAlcCopXmtUserCells": wfAtmAlcCopXmtUserCells,
       "wfAtmAlcCopXmtOctets": wfAtmAlcCopXmtOctets,
       "wfAtmAlcCopRcvPackets": wfAtmAlcCopRcvPackets,
       "wfAtmAlcCopRcvClipPackets": wfAtmAlcCopRcvClipPackets,
       "wfAtmAlcCopRcvBuffers": wfAtmAlcCopRcvBuffers,
       "wfAtmAlcCopRcvErrBuffers": wfAtmAlcCopRcvErrBuffers,
       "wfAtmAlcCopRcvClipBuffers": wfAtmAlcCopRcvClipBuffers,
       "wfAtmAlcCopRcvSarDropBuffers": wfAtmAlcCopRcvSarDropBuffers,
       "wfAtmAlcCopRcvCells": wfAtmAlcCopRcvCells,
       "wfAtmAlcCopRcvDropCells": wfAtmAlcCopRcvDropCells,
       "wfAtmAlcCopRcvUnassCells": wfAtmAlcCopRcvUnassCells,
       "wfAtmAlcCopRcvIdleCells": wfAtmAlcCopRcvIdleCells,
       "wfAtmAlcCopRcvUserCells": wfAtmAlcCopRcvUserCells,
       "wfAtmAlcCopRcvSarDropCells": wfAtmAlcCopRcvSarDropCells,
       "wfAtmAlcCopRcvOctets": wfAtmAlcCopRcvOctets,
       "wfAtmAlcCopXmtOamCells": wfAtmAlcCopXmtOamCells,
       "wfAtmAlcCopRcvOamCells": wfAtmAlcCopRcvOamCells,
       "wfAtmAlcCopRcvOamCrcErrs": wfAtmAlcCopRcvOamCrcErrs,
       "wfAtmAlcCopErrorTable": wfAtmAlcCopErrorTable,
       "wfAtmAlcCopErrorEntry": wfAtmAlcCopErrorEntry,
       "wfAtmAlcCopErrorIndex": wfAtmAlcCopErrorIndex,
       "wfAtmAlcCopHecDetects": wfAtmAlcCopHecDetects,
       "wfAtmAlcCopHecCorrects": wfAtmAlcCopHecCorrects,
       "wfAtmAlcCopB2Febes": wfAtmAlcCopB2Febes,
       "wfAtmAlcCopB3Febes": wfAtmAlcCopB3Febes,
       "wfAtmAlcCopF1Febes": wfAtmAlcCopF1Febes,
       "wfAtmAlcCopF3Febes": wfAtmAlcCopF3Febes,
       "wfAtmAlcCopG1Febes": wfAtmAlcCopG1Febes,
       "wfAtmAlcCopDropIntqEvents": wfAtmAlcCopDropIntqEvents,
       "wfAtmAlcCopDropLogqEvents": wfAtmAlcCopDropLogqEvents,
       "wfAtmAlcCopDmaFifoOverruns": wfAtmAlcCopDmaFifoOverruns,
       "wfAtmAlcCopDmaFifoUnderruns": wfAtmAlcCopDmaFifoUnderruns,
       "wfAtmAlcCopLossSignals": wfAtmAlcCopLossSignals,
       "wfAtmAlcCopLossFrames": wfAtmAlcCopLossFrames,
       "wfAtmAlcCopLossPointers": wfAtmAlcCopLossPointers,
       "wfAtmAlcCopOutCellDelins": wfAtmAlcCopOutCellDelins,
       "wfAtmAlcCopInCellDelins": wfAtmAlcCopInCellDelins,
       "wfAtmAlcCopBufOverflows": wfAtmAlcCopBufOverflows,
       "wfAtmAlcCopXmtQueueFulls": wfAtmAlcCopXmtQueueFulls,
       "wfAtmAlcCopXmtAtes": wfAtmAlcCopXmtAtes,
       "wfAtmAlcCopRcvQueueEmptys": wfAtmAlcCopRcvQueueEmptys,
       "wfAtmAlcCopRcvWriteFails": wfAtmAlcCopRcvWriteFails,
       "wfAtmAlcCopRcvQueueFulls": wfAtmAlcCopRcvQueueFulls,
       "wfAtmAlcCopRcvAtes": wfAtmAlcCopRcvAtes,
       "wfAtmAlcSarConfTable": wfAtmAlcSarConfTable,
       "wfAtmAlcSarConfEntry": wfAtmAlcSarConfEntry,
       "wfAtmAlcSarConfDelete": wfAtmAlcSarConfDelete,
       "wfAtmAlcSarConfIndex": wfAtmAlcSarConfIndex,
       "wfAtmAlcSarDmaBurstLength": wfAtmAlcSarDmaBurstLength,
       "wfAtmAlcSarDmaModeBw": wfAtmAlcSarDmaModeBw,
       "wfAtmAlcSarDmaModeBmode": wfAtmAlcSarDmaModeBmode,
       "wfAtmAlcSarDmaModeOrder": wfAtmAlcSarDmaModeOrder,
       "wfAtmAlcSarDmaModeMmode": wfAtmAlcSarDmaModeMmode,
       "wfAtmAlcSarDmaModeCmode": wfAtmAlcSarDmaModeCmode,
       "wfAtmAlcSarDmaModeSync": wfAtmAlcSarDmaModeSync,
       "wfAtmAlcSarControlRif": wfAtmAlcSarControlRif,
       "wfAtmAlcSarControlLoop": wfAtmAlcSarControlLoop,
       "wfAtmAlcSarModeRtmr": wfAtmAlcSarModeRtmr,
       "wfAtmAlcSarModeRid": wfAtmAlcSarModeRid,
       "wfAtmAlcSarModeAal": wfAtmAlcSarModeAal,
       "wfAtmAlcSarModeDmask": wfAtmAlcSarModeDmask,
       "wfAtmAlcSarModeDchain": wfAtmAlcSarModeDchain,
       "wfAtmAlcSarModeSmode": wfAtmAlcSarModeSmode,
       "wfAtmAlcSarModeBchain": wfAtmAlcSarModeBchain,
       "wfAtmAlcSarModeHec": wfAtmAlcSarModeHec,
       "wfAtmAlcSarModeVpf": wfAtmAlcSarModeVpf,
       "wfAtmAlcSarModeBas": wfAtmAlcSarModeBas,
       "wfAtmAlcSarModeAm": wfAtmAlcSarModeAm,
       "wfAtmAlcSarModeTrtl": wfAtmAlcSarModeTrtl,
       "wfAtmAlcSarTimeoutCtrPeriod": wfAtmAlcSarTimeoutCtrPeriod,
       "wfAtmAlcSarTimeoutCtrInt": wfAtmAlcSarTimeoutCtrInt,
       "wfAtmAlcSarMaxReceivePktLen": wfAtmAlcSarMaxReceivePktLen,
       "wfAtmAlcSarTrafficMgtTable": wfAtmAlcSarTrafficMgtTable,
       "wfAtmAlcSarTrafficMgtEntry": wfAtmAlcSarTrafficMgtEntry,
       "wfAtmAlcSarTrafficMgtDelete": wfAtmAlcSarTrafficMgtDelete,
       "wfAtmAlcSarTrafficMgtIndex": wfAtmAlcSarTrafficMgtIndex,
       "wfAtmAlcSarPeakCellRateEna": wfAtmAlcSarPeakCellRateEna,
       "wfAtmAlcSarAvgCellRateEna": wfAtmAlcSarAvgCellRateEna,
       "wfAtmAlcSarPeakCellRate": wfAtmAlcSarPeakCellRate,
       "wfAtmAlcSarAvgCellRate": wfAtmAlcSarAvgCellRate,
       "wfAtmAlcSarMaxBurstSize": wfAtmAlcSarMaxBurstSize,
       "wfAtmAlcSarRateQueueTable": wfAtmAlcSarRateQueueTable,
       "wfAtmAlcSarRateQueueEntry": wfAtmAlcSarRateQueueEntry,
       "wfAtmAlcSarRateQueueIndex": wfAtmAlcSarRateQueueIndex,
       "wfAtmAlcSarRateQueueNumber": wfAtmAlcSarRateQueueNumber,
       "wfAtmAlcSarRateQueueState": wfAtmAlcSarRateQueueState,
       "wfAtmAlcSarRateQueuePcr": wfAtmAlcSarRateQueuePcr,
       "wfAtmAlcSarRateQueueVcs": wfAtmAlcSarRateQueueVcs,
       "wfAtmAlcSarRateQueueDef": wfAtmAlcSarRateQueueDef,
       "wfAtmAlcFrmConfTable": wfAtmAlcFrmConfTable,
       "wfAtmAlcFrmConfEntry": wfAtmAlcFrmConfEntry,
       "wfAtmAlcFrmConfDelete": wfAtmAlcFrmConfDelete,
       "wfAtmAlcFrmConfIndex": wfAtmAlcFrmConfIndex,
       "wfAtmAlcFrmGenEnable": wfAtmAlcFrmGenEnable,
       "wfAtmAlcFrmGenFramingMode": wfAtmAlcFrmGenFramingMode,
       "wfAtmAlcFrmGenScramblerEna": wfAtmAlcFrmGenScramblerEna,
       "wfAtmAlcFrmGenDescrambleEna": wfAtmAlcFrmGenDescrambleEna,
       "wfAtmAlcFrmGenLoopback": wfAtmAlcFrmGenLoopback,
       "wfAtmAlcFrmGenSyncFoundCnt": wfAtmAlcFrmGenSyncFoundCnt,
       "wfAtmAlcFrmGenSyncLostCnt": wfAtmAlcFrmGenSyncLostCnt,
       "wfAtmAlcFrmRcvCellEnable": wfAtmAlcFrmRcvCellEnable,
       "wfAtmAlcFrmRcvOamCrcCheck": wfAtmAlcFrmRcvOamCrcCheck,
       "wfAtmAlcFrmRcvOamCrcGen": wfAtmAlcFrmRcvOamCrcGen,
       "wfAtmAlcFrmRcvCellInsPrio": wfAtmAlcFrmRcvCellInsPrio,
       "wfAtmAlcFrmRcvInsertPcr": wfAtmAlcFrmRcvInsertPcr,
       "wfAtmAlcFrmRcvGfcIgnore": wfAtmAlcFrmRcvGfcIgnore,
       "wfAtmAlcFrmRcvDescrambleCtl": wfAtmAlcFrmRcvDescrambleCtl,
       "wfAtmAlcFrmRcvHecRcvMask": wfAtmAlcFrmRcvHecRcvMask,
       "wfAtmAlcFrmRcvErrCorrectEna": wfAtmAlcFrmRcvErrCorrectEna,
       "wfAtmAlcFrmRcvByteAlignment": wfAtmAlcFrmRcvByteAlignment,
       "wfAtmAlcFrmRcvCellSyncFound": wfAtmAlcFrmRcvCellSyncFound,
       "wfAtmAlcFrmRcvCellSyncLost": wfAtmAlcFrmRcvCellSyncLost,
       "wfAtmAlcFrmRcvExtUserCell": wfAtmAlcFrmRcvExtUserCell,
       "wfAtmAlcFrmRcvExtMetaSig": wfAtmAlcFrmRcvExtMetaSig,
       "wfAtmAlcFrmRcvExtBcastSig": wfAtmAlcFrmRcvExtBcastSig,
       "wfAtmAlcFrmRcvExtPointSig": wfAtmAlcFrmRcvExtPointSig,
       "wfAtmAlcFrmRcvExtIlmiSig": wfAtmAlcFrmRcvExtIlmiSig,
       "wfAtmAlcFrmRcvExtF4F5PrfMan": wfAtmAlcFrmRcvExtF4F5PrfMan,
       "wfAtmAlcFrmRcvExtF1F3PlOam": wfAtmAlcFrmRcvExtF1F3PlOam,
       "wfAtmAlcFrmRcvExtF4Segment": wfAtmAlcFrmRcvExtF4Segment,
       "wfAtmAlcFrmRcvExtF4EndEnd": wfAtmAlcFrmRcvExtF4EndEnd,
       "wfAtmAlcFrmRcvExtF5Segment": wfAtmAlcFrmRcvExtF5Segment,
       "wfAtmAlcFrmRcvExtF5EndEnd": wfAtmAlcFrmRcvExtF5EndEnd,
       "wfAtmAlcFrmRcvDisUserCell": wfAtmAlcFrmRcvDisUserCell,
       "wfAtmAlcFrmRcvDisMetaSig": wfAtmAlcFrmRcvDisMetaSig,
       "wfAtmAlcFrmRcvDisBcastSig": wfAtmAlcFrmRcvDisBcastSig,
       "wfAtmAlcFrmRcvDisPointSig": wfAtmAlcFrmRcvDisPointSig,
       "wfAtmAlcFrmRcvDisIlmiSig": wfAtmAlcFrmRcvDisIlmiSig,
       "wfAtmAlcFrmRcvDisUnassCell": wfAtmAlcFrmRcvDisUnassCell,
       "wfAtmAlcFrmRcvDisF4Segment": wfAtmAlcFrmRcvDisF4Segment,
       "wfAtmAlcFrmRcvDisF4EndEnd": wfAtmAlcFrmRcvDisF4EndEnd,
       "wfAtmAlcFrmRcvDisF5Segment": wfAtmAlcFrmRcvDisF5Segment,
       "wfAtmAlcFrmRcvDisF5EndEnd": wfAtmAlcFrmRcvDisF5EndEnd,
       "wfAtmAlcFrmXmtCellEnable": wfAtmAlcFrmXmtCellEnable,
       "wfAtmAlcFrmXmtOamCrcCheck": wfAtmAlcFrmXmtOamCrcCheck,
       "wfAtmAlcFrmXmtOamCrcGen": wfAtmAlcFrmXmtOamCrcGen,
       "wfAtmAlcFrmXmtCellInsPrio": wfAtmAlcFrmXmtCellInsPrio,
       "wfAtmAlcFrmXmtInsertPcr": wfAtmAlcFrmXmtInsertPcr,
       "wfAtmAlcFrmXmtGfcIgnore": wfAtmAlcFrmXmtGfcIgnore,
       "wfAtmAlcFrmXmtCellDecouple": wfAtmAlcFrmXmtCellDecouple,
       "wfAtmAlcFrmXmtScrambleCtl": wfAtmAlcFrmXmtScrambleCtl,
       "wfAtmAlcFrmXmtHecXmtMask": wfAtmAlcFrmXmtHecXmtMask,
       "wfAtmAlcFrmXmtExtUserCell": wfAtmAlcFrmXmtExtUserCell,
       "wfAtmAlcFrmXmtExtMetaSig": wfAtmAlcFrmXmtExtMetaSig,
       "wfAtmAlcFrmXmtExtBcastSig": wfAtmAlcFrmXmtExtBcastSig,
       "wfAtmAlcFrmXmtExtPointSig": wfAtmAlcFrmXmtExtPointSig,
       "wfAtmAlcFrmXmtExtIlmiSig": wfAtmAlcFrmXmtExtIlmiSig,
       "wfAtmAlcFrmXmtExtF4F5PrfMan": wfAtmAlcFrmXmtExtF4F5PrfMan,
       "wfAtmAlcFrmXmtExtF4Segment": wfAtmAlcFrmXmtExtF4Segment,
       "wfAtmAlcFrmXmtExtF4EndEnd": wfAtmAlcFrmXmtExtF4EndEnd,
       "wfAtmAlcFrmXmtExtF5Segment": wfAtmAlcFrmXmtExtF5Segment,
       "wfAtmAlcFrmXmtExtF5EndEnd": wfAtmAlcFrmXmtExtF5EndEnd,
       "wfAtmAlcFrmXmtDisUserCell": wfAtmAlcFrmXmtDisUserCell,
       "wfAtmAlcFrmXmtDisMetaSig": wfAtmAlcFrmXmtDisMetaSig,
       "wfAtmAlcFrmXmtDisBcastSig": wfAtmAlcFrmXmtDisBcastSig,
       "wfAtmAlcFrmXmtDisPointSig": wfAtmAlcFrmXmtDisPointSig,
       "wfAtmAlcFrmXmtDisIlmiSig": wfAtmAlcFrmXmtDisIlmiSig,
       "wfAtmAlcFrmXmtDisUnassCell": wfAtmAlcFrmXmtDisUnassCell,
       "wfAtmAlcFrmXmtDisF4Segment": wfAtmAlcFrmXmtDisF4Segment,
       "wfAtmAlcFrmXmtDisF4EndEnd": wfAtmAlcFrmXmtDisF4EndEnd,
       "wfAtmAlcFrmXmtDisF5Segment": wfAtmAlcFrmXmtDisF5Segment,
       "wfAtmAlcFrmXmtDisF5EndEnd": wfAtmAlcFrmXmtDisF5EndEnd,
       "wfAtmAlcFrmOamEnable": wfAtmAlcFrmOamEnable,
       "wfAtmAlcFrmOamInvertBip": wfAtmAlcFrmOamInvertBip,
       "wfAtmAlcFrmOamTxPathFerf": wfAtmAlcFrmOamTxPathFerf,
       "wfAtmAlcFrmOamTxSectionFerf": wfAtmAlcFrmOamTxSectionFerf,
       "wfAtmAlcFrmOamTxPathAis": wfAtmAlcFrmOamTxPathAis,
       "wfAtmAlcFrmOamTxSectionAis": wfAtmAlcFrmOamTxSectionAis,
       "wfAtmAlcFrmOamTxPathFebe": wfAtmAlcFrmOamTxPathFebe,
       "wfAtmAlcFrmOamTxSectionFebe": wfAtmAlcFrmOamTxSectionFebe,
       "wfAtmAlcFrmStatsSwEnable": wfAtmAlcFrmStatsSwEnable,
       "wfAtmAlcFrmStatsMode": wfAtmAlcFrmStatsMode,
       "wfAtmAlcFrmStatsReceive": wfAtmAlcFrmStatsReceive,
       "wfAtmAlcFrmStatsTransmit": wfAtmAlcFrmStatsTransmit,
       "wfAtmAlcFrmStatsMask": wfAtmAlcFrmStatsMask,
       "wfAtmAlcFrmStatsTimeout": wfAtmAlcFrmStatsTimeout,
       "wfAtmAlcFrmStatsTimerEna": wfAtmAlcFrmStatsTimerEna,
       "wfAtmAlcFrmStatsOflowEna": wfAtmAlcFrmStatsOflowEna,
       "wfAtmAlcFrmStatsForceDma": wfAtmAlcFrmStatsForceDma,
       "wfAtmAlcFrmCsiEnable": wfAtmAlcFrmCsiEnable,
       "wfAtmAlcFrmCsiLoop": wfAtmAlcFrmCsiLoop,
       "wfAtmAlcFrmCsiRcvAtcEnable": wfAtmAlcFrmCsiRcvAtcEnable,
       "wfAtmAlcFrmCsiRcvAte": wfAtmAlcFrmCsiRcvAte,
       "wfAtmAlcFrmCsiRcvClpBitOpt": wfAtmAlcFrmCsiRcvClpBitOpt,
       "wfAtmAlcFrmCsiRcvCongBitOpt": wfAtmAlcFrmCsiRcvCongBitOpt,
       "wfAtmAlcFrmCsiRoutingTag": wfAtmAlcFrmCsiRoutingTag,
       "wfAtmAlcFrmCsiXmtAtcEnable": wfAtmAlcFrmCsiXmtAtcEnable,
       "wfAtmAlcFrmCsiXmtAte": wfAtmAlcFrmCsiXmtAte,
       "wfAtmAlcFrmCsiXmtClpBitOpt": wfAtmAlcFrmCsiXmtClpBitOpt,
       "wfAtmAlcFrmCsiXmtCongBitOpt": wfAtmAlcFrmCsiXmtCongBitOpt,
       "wfAtmAlcFrmCsiOmitHec": wfAtmAlcFrmCsiOmitHec,
       "wfAtmAlcFrmCsiRcvHecEnable": wfAtmAlcFrmCsiRcvHecEnable,
       "wfAtmAlcFrmCsiRcvHecMask": wfAtmAlcFrmCsiRcvHecMask,
       "wfAtmAlcFrmDmaChan0Enable": wfAtmAlcFrmDmaChan0Enable,
       "wfAtmAlcFrmDmaChan1Enable": wfAtmAlcFrmDmaChan1Enable,
       "wfAtmAlcFrmDmaChan2Enable": wfAtmAlcFrmDmaChan2Enable,
       "wfAtmAlcFrmDmaChan3Enable": wfAtmAlcFrmDmaChan3Enable,
       "wfAtmAlcFrmDmaChan4Enable": wfAtmAlcFrmDmaChan4Enable,
       "wfAtmAlcFrmDmaChan5Enable": wfAtmAlcFrmDmaChan5Enable,
       "wfAtmAlcFrmDmaEnable": wfAtmAlcFrmDmaEnable,
       "wfAtmAlcFrmDmaStop": wfAtmAlcFrmDmaStop,
       "wfAtmAlcFrmDmaPrioritySel": wfAtmAlcFrmDmaPrioritySel,
       "wfAtmAlcFrmDmaFastXferMode": wfAtmAlcFrmDmaFastXferMode,
       "wfAtmCellSwitchGroup": wfAtmCellSwitchGroup,
       "wfAtmizerCfgTable": wfAtmizerCfgTable,
       "wfAtmizerCfgEntry": wfAtmizerCfgEntry,
       "wfAtmizerCfgSlot": wfAtmizerCfgSlot,
       "wfAtmizerCfgMaxVcl": wfAtmizerCfgMaxVcl,
       "wfAtmizerCfgCurrVcl": wfAtmizerCfgCurrVcl,
       "wfAtmizerCfgRxQueueLenMax": wfAtmizerCfgRxQueueLenMax,
       "wfAtmizerCfgRxQueueTmoMax": wfAtmizerCfgRxQueueTmoMax,
       "wfAtmizerCfgRxBuffersMax": wfAtmizerCfgRxBuffersMax,
       "wfAtmizerCfgRxPagesMax": wfAtmizerCfgRxPagesMax,
       "wfAtmizerCfgTxBuffersMax": wfAtmizerCfgTxBuffersMax,
       "wfAtmizerCfgTxPagesMax": wfAtmizerCfgTxPagesMax,
       "wfAtmizerCfgTxPercentRsrcs": wfAtmizerCfgTxPercentRsrcs,
       "wfAtmizerCfgHeartbeatPeriod": wfAtmizerCfgHeartbeatPeriod,
       "wfAtmizerRxBuffersMax": wfAtmizerRxBuffersMax,
       "wfAtmizerRxPagesMax": wfAtmizerRxPagesMax,
       "wfAtmizerTxBuffersMax": wfAtmizerTxBuffersMax,
       "wfAtmizerTxPagesMax": wfAtmizerTxPagesMax,
       "wfAtmizerTxPercentRsrcs": wfAtmizerTxPercentRsrcs,
       "wfAtmizerTxPerVcClipEnable": wfAtmizerTxPerVcClipEnable,
       "wfAtmizerCfgTxVcBuffersMax": wfAtmizerCfgTxVcBuffersMax,
       "wfAtmizerTxVcBuffersMax": wfAtmizerTxVcBuffersMax,
       "wfAtmizerDrvCfgTable": wfAtmizerDrvCfgTable,
       "wfAtmizerDrvCfgEntry": wfAtmizerDrvCfgEntry,
       "wfAtmizerDrvCfgDelete": wfAtmizerDrvCfgDelete,
       "wfAtmizerDrvCfgEnable": wfAtmizerDrvCfgEnable,
       "wfAtmizerDrvCfgState": wfAtmizerDrvCfgState,
       "wfAtmizerDrvCfgSlot": wfAtmizerDrvCfgSlot,
       "wfAtmizerDrvCfgPort": wfAtmizerDrvCfgPort,
       "wfAtmizerDrvCfgCct": wfAtmizerDrvCfgCct,
       "wfAtmizerDrvCfgLineNumber": wfAtmizerDrvCfgLineNumber,
       "wfAtmizerDrvCfgType": wfAtmizerDrvCfgType,
       "wfAtmizerDrvCfgMtu": wfAtmizerDrvCfgMtu,
       "wfAtmizerDrvCfgSpeed": wfAtmizerDrvCfgSpeed,
       "wfAtmizerDrvCfgDpNotify": wfAtmizerDrvCfgDpNotify,
       "wfAtmizerDrvCfgDpNotifyTimeout": wfAtmizerDrvCfgDpNotifyTimeout,
       "wfAtmizerDrvCfgVcInactEnable": wfAtmizerDrvCfgVcInactEnable,
       "wfAtmizerDrvCfgVcInactTimeout": wfAtmizerDrvCfgVcInactTimeout,
       "wfAtmizerDrvCfgMadrCt": wfAtmizerDrvCfgMadrCt,
       "wfAtmizerDrvCfgMadr": wfAtmizerDrvCfgMadr,
       "wfAtmizerDrvCfgFramingMode": wfAtmizerDrvCfgFramingMode,
       "wfAtmizerDrvCfgClkSource": wfAtmizerDrvCfgClkSource,
       "wfAtmizerDrvCfgLogLevel": wfAtmizerDrvCfgLogLevel,
       "wfAtmizerDrvCfgDsx3SendCode": wfAtmizerDrvCfgDsx3SendCode,
       "wfAtmizerDrvCfgDsx3LoopbackConfig": wfAtmizerDrvCfgDsx3LoopbackConfig,
       "wfAtmizerDrvCfgDs3Scrambling": wfAtmizerDrvCfgDs3Scrambling,
       "wfAtmizerDrvCfgDs3LineBuildOut": wfAtmizerDrvCfgDs3LineBuildOut,
       "wfAtmizerDrvCfgModule": wfAtmizerDrvCfgModule,
       "wfAtmizerFramingMode": wfAtmizerFramingMode,
       "wfAtmizerDrvCfgIwfCct": wfAtmizerDrvCfgIwfCct,
       "wfAtmizerDrvCfgCcType": wfAtmizerDrvCfgCcType,
       "wfAtmizerDrvCfgMaxVcls": wfAtmizerDrvCfgMaxVcls,
       "wfAtmizerDrvCfgCurrVcls": wfAtmizerDrvCfgCurrVcls,
       "wfAtmizerDrvCfgScrSum": wfAtmizerDrvCfgScrSum,
       "wfAtmizerDrvCfgExtRate": wfAtmizerDrvCfgExtRate,
       "wfAtmizerIntfStatsTable": wfAtmizerIntfStatsTable,
       "wfAtmizerIntfStatsEntry": wfAtmizerIntfStatsEntry,
       "wfAtmizerIntfSlot": wfAtmizerIntfSlot,
       "wfAtmizerIntfPort": wfAtmizerIntfPort,
       "wfAtmizerIntfLastChange": wfAtmizerIntfLastChange,
       "wfAtmizerIntfOutQLen": wfAtmizerIntfOutQLen,
       "wfAtmizerIntfStatus": wfAtmizerIntfStatus,
       "wfAtmizerIntfIndex": wfAtmizerIntfIndex,
       "wfAtmizerIntfOcdEvents": wfAtmizerIntfOcdEvents,
       "wfAtmizerIntfTcAlarmState": wfAtmizerIntfTcAlarmState,
       "wfAtmizerIntfRxPacketsOkWrap": wfAtmizerIntfRxPacketsOkWrap,
       "wfAtmizerIntfRxPacketsOk": wfAtmizerIntfRxPacketsOk,
       "wfAtmizerIntfRxCellsOkWrap": wfAtmizerIntfRxCellsOkWrap,
       "wfAtmizerIntfRxCellsOk": wfAtmizerIntfRxCellsOk,
       "wfAtmizerIntfRxOamCount": wfAtmizerIntfRxOamCount,
       "wfAtmizerIntfRxFlowCtrlCount": wfAtmizerIntfRxFlowCtrlCount,
       "wfAtmizerIntfRxInvalidHeaders": wfAtmizerIntfRxInvalidHeaders,
       "wfAtmizerIntfRxOverSizedSDUs": wfAtmizerIntfRxOverSizedSDUs,
       "wfAtmizerIntfRxCrcErrors": wfAtmizerIntfRxCrcErrors,
       "wfAtmizerIntfRxCrc10Errors": wfAtmizerIntfRxCrc10Errors,
       "wfAtmizerIntfRxLackBufCredits": wfAtmizerIntfRxLackBufCredits,
       "wfAtmizerIntfRxLackPageCredits": wfAtmizerIntfRxLackPageCredits,
       "wfAtmizerIntfRxLackBufResc": wfAtmizerIntfRxLackBufResc,
       "wfAtmizerIntfRxLackPageResc": wfAtmizerIntfRxLackPageResc,
       "wfAtmizerIntfTxPacketsOkWrap": wfAtmizerIntfTxPacketsOkWrap,
       "wfAtmizerIntfTxPacketsOk": wfAtmizerIntfTxPacketsOk,
       "wfAtmizerIntfTxCellsOkWrap": wfAtmizerIntfTxCellsOkWrap,
       "wfAtmizerIntfTxCellsOk": wfAtmizerIntfTxCellsOk,
       "wfAtmizerIntfTxOamCount": wfAtmizerIntfTxOamCount,
       "wfAtmizerIntfTxFlowCtrlCount": wfAtmizerIntfTxFlowCtrlCount,
       "wfAtmizerIntfTxBadVcs": wfAtmizerIntfTxBadVcs,
       "wfAtmizerIntfTxOverSizedSDUs": wfAtmizerIntfTxOverSizedSDUs,
       "wfAtmizerIntfTxLackBufCredits": wfAtmizerIntfTxLackBufCredits,
       "wfAtmizerIntfTxLackPageCredits": wfAtmizerIntfTxLackPageCredits,
       "wfAtmizerIntfTxDrvClipCount": wfAtmizerIntfTxDrvClipCount,
       "wfAtmizerIntfHecDetectedCount": wfAtmizerIntfHecDetectedCount,
       "wfAtmizerIntfHecCorrectedCount": wfAtmizerIntfHecCorrectedCount,
       "wfAtmizerIntfRxOctets": wfAtmizerIntfRxOctets,
       "wfAtmizerIntfTxOctets": wfAtmizerIntfTxOctets,
       "wfAtmizerIntfRxUTOPIAErrors": wfAtmizerIntfRxUTOPIAErrors,
       "wfAtmizerIntfRxLengthErrors": wfAtmizerIntfRxLengthErrors,
       "wfAtmizerIntfRxAbortMessages": wfAtmizerIntfRxAbortMessages,
       "wfAtmizerIntfRxSequenceNumberErrors": wfAtmizerIntfRxSequenceNumberErrors,
       "wfAtmizerVclStatsTable": wfAtmizerVclStatsTable,
       "wfAtmizerVclStatsEntry": wfAtmizerVclStatsEntry,
       "wfAtmizerVclIndex": wfAtmizerVclIndex,
       "wfAtmizerVclVpi": wfAtmizerVclVpi,
       "wfAtmizerVclVci": wfAtmizerVclVci,
       "wfAtmizerVclRxPacketsOkWrap": wfAtmizerVclRxPacketsOkWrap,
       "wfAtmizerVclRxPacketsOk": wfAtmizerVclRxPacketsOk,
       "wfAtmizerVclRxCellsOkWrap": wfAtmizerVclRxCellsOkWrap,
       "wfAtmizerVclRxCellsOk": wfAtmizerVclRxCellsOk,
       "wfAtmizerVclRxOamCount": wfAtmizerVclRxOamCount,
       "wfAtmizerVclRxFlowCtrlCount": wfAtmizerVclRxFlowCtrlCount,
       "wfAtmizerVclRxInvalidHeaders": wfAtmizerVclRxInvalidHeaders,
       "wfAtmizerVclRxOverSizedSDUs": wfAtmizerVclRxOverSizedSDUs,
       "wfAtmizerVclRxCrcErrors": wfAtmizerVclRxCrcErrors,
       "wfAtmizerVclRxCrc10Errors": wfAtmizerVclRxCrc10Errors,
       "wfAtmizerVclRxLackBufCredits": wfAtmizerVclRxLackBufCredits,
       "wfAtmizerVclRxLackPageCredits": wfAtmizerVclRxLackPageCredits,
       "wfAtmizerVclRxLackBufResc": wfAtmizerVclRxLackBufResc,
       "wfAtmizerVclRxLackPageResc": wfAtmizerVclRxLackPageResc,
       "wfAtmizerVclTxPacketsOkWrap": wfAtmizerVclTxPacketsOkWrap,
       "wfAtmizerVclTxPacketsOk": wfAtmizerVclTxPacketsOk,
       "wfAtmizerVclTxCellsOkWrap": wfAtmizerVclTxCellsOkWrap,
       "wfAtmizerVclTxCellsOk": wfAtmizerVclTxCellsOk,
       "wfAtmizerVclTxOamCount": wfAtmizerVclTxOamCount,
       "wfAtmizerVclTxFlowCtrlCount": wfAtmizerVclTxFlowCtrlCount,
       "wfAtmizerVclTxOverSizedSDUs": wfAtmizerVclTxOverSizedSDUs,
       "wfAtmizerVclTxLackBufCredits": wfAtmizerVclTxLackBufCredits,
       "wfAtmizerVclTxLackPageCredits": wfAtmizerVclTxLackPageCredits,
       "wfAtmizerVclRxOctets": wfAtmizerVclRxOctets,
       "wfAtmizerVclTxOctets": wfAtmizerVclTxOctets,
       "wfAtmizerVclTxClipFrames": wfAtmizerVclTxClipFrames,
       "wfAtmizerVclRxLengthErrors": wfAtmizerVclRxLengthErrors,
       "wfAtmizerVclRxAbortMessages": wfAtmizerVclRxAbortMessages,
       "wfAtmizerVclRxSequenceNumberErrors": wfAtmizerVclRxSequenceNumberErrors,
       "wfAtmizerDebugTable": wfAtmizerDebugTable,
       "wfAtmizerDebugEntry": wfAtmizerDebugEntry,
       "wfAtmizerDebugSlot": wfAtmizerDebugSlot,
       "wfAtmizerDebugCmd": wfAtmizerDebugCmd,
       "wfAtmizerDebugCmdSize": wfAtmizerDebugCmdSize,
       "wfAtmizerDebugParam1": wfAtmizerDebugParam1,
       "wfAtmizerDebugParam2": wfAtmizerDebugParam2,
       "wfAtmizerDebugParam3": wfAtmizerDebugParam3,
       "wfAtmizerDebugParam4": wfAtmizerDebugParam4,
       "wfAtmizerDebugParam5": wfAtmizerDebugParam5,
       "wfAtmizerDebugParam6": wfAtmizerDebugParam6,
       "wfAtmizerDebugParam7": wfAtmizerDebugParam7,
       "wfAtmizerDebugParam8": wfAtmizerDebugParam8,
       "wfAtmizerDebugParam9": wfAtmizerDebugParam9,
       "wfAtmizerDebugParam10": wfAtmizerDebugParam10,
       "wfAtmizerDebugRxDone": wfAtmizerDebugRxDone,
       "wfAtmizerDebugRxValue": wfAtmizerDebugRxValue,
       "wfAtmizerDebugTxDone": wfAtmizerDebugTxDone,
       "wfAtmizerDebugTxValue": wfAtmizerDebugTxValue,
       "wfSonetMediumTable": wfSonetMediumTable,
       "wfSonetMediumEntry": wfSonetMediumEntry,
       "wfSonetMediumIndex": wfSonetMediumIndex,
       "wfSonetMediumType": wfSonetMediumType,
       "wfSonetMediumTimeElapsed": wfSonetMediumTimeElapsed,
       "wfSonetMediumValidIntervals": wfSonetMediumValidIntervals,
       "wfSonetMediumLineCoding": wfSonetMediumLineCoding,
       "wfSonetMediumLineType": wfSonetMediumLineType,
       "wfSonetMediumCircuitIdentifier": wfSonetMediumCircuitIdentifier,
       "wfSonetSectionCurrentTable": wfSonetSectionCurrentTable,
       "wfSonetSectionCurrentEntry": wfSonetSectionCurrentEntry,
       "wfSonetSectionCurrentIndex": wfSonetSectionCurrentIndex,
       "wfSonetSectionCurrentStatus": wfSonetSectionCurrentStatus,
       "wfSonetSectionCurrentESs": wfSonetSectionCurrentESs,
       "wfSonetSectionCurrentSESs": wfSonetSectionCurrentSESs,
       "wfSonetSectionCurrentSEFSs": wfSonetSectionCurrentSEFSs,
       "wfSonetSectionCurrentCVs": wfSonetSectionCurrentCVs,
       "wfSonetSectionIntervalTable": wfSonetSectionIntervalTable,
       "wfSonetSectionIntervalEntry": wfSonetSectionIntervalEntry,
       "wfSonetSectionIntervalIndex": wfSonetSectionIntervalIndex,
       "wfSonetSectionIntervalNumber": wfSonetSectionIntervalNumber,
       "wfSonetSectionIntervalESs": wfSonetSectionIntervalESs,
       "wfSonetSectionIntervalSESs": wfSonetSectionIntervalSESs,
       "wfSonetSectionIntervalSEFSs": wfSonetSectionIntervalSEFSs,
       "wfSonetSectionIntervalCVs": wfSonetSectionIntervalCVs,
       "wfSonetLineCurrentTable": wfSonetLineCurrentTable,
       "wfSonetLineCurrentEntry": wfSonetLineCurrentEntry,
       "wfSonetLineCurrentIndex": wfSonetLineCurrentIndex,
       "wfSonetLineCurrentStatus": wfSonetLineCurrentStatus,
       "wfSonetLineCurrentESs": wfSonetLineCurrentESs,
       "wfSonetLineCurrentSESs": wfSonetLineCurrentSESs,
       "wfSonetLineCurrentCVs": wfSonetLineCurrentCVs,
       "wfSonetLineCurrentUASs": wfSonetLineCurrentUASs,
       "wfSonetLineIntervalTable": wfSonetLineIntervalTable,
       "wfSonetLineIntervalEntry": wfSonetLineIntervalEntry,
       "wfSonetLineIntervalIndex": wfSonetLineIntervalIndex,
       "wfSonetLineIntervalNumber": wfSonetLineIntervalNumber,
       "wfSonetLineIntervalESs": wfSonetLineIntervalESs,
       "wfSonetLineIntervalSESs": wfSonetLineIntervalSESs,
       "wfSonetLineIntervalCVs": wfSonetLineIntervalCVs,
       "wfSonetLineIntervalUASs": wfSonetLineIntervalUASs,
       "wfSonetFarEndLineCurrentTable": wfSonetFarEndLineCurrentTable,
       "wfSonetFarEndLineCurrentEntry": wfSonetFarEndLineCurrentEntry,
       "wfSonetFarEndLineCurrentIndex": wfSonetFarEndLineCurrentIndex,
       "wfSonetFarEndLineCurrentESs": wfSonetFarEndLineCurrentESs,
       "wfSonetFarEndLineCurrentSESs": wfSonetFarEndLineCurrentSESs,
       "wfSonetFarEndLineCurrentCVs": wfSonetFarEndLineCurrentCVs,
       "wfSonetFarEndLineCurrentUASs": wfSonetFarEndLineCurrentUASs,
       "wfSonetFarEndLineIntervalTable": wfSonetFarEndLineIntervalTable,
       "wfSonetFarEndLineIntervalEntry": wfSonetFarEndLineIntervalEntry,
       "wfSonetFarEndLineIntervalIndex": wfSonetFarEndLineIntervalIndex,
       "wfSonetFarEndLineIntervalNumber": wfSonetFarEndLineIntervalNumber,
       "wfSonetFarEndLineIntervalESs": wfSonetFarEndLineIntervalESs,
       "wfSonetFarEndLineIntervalSESs": wfSonetFarEndLineIntervalSESs,
       "wfSonetFarEndLineIntervalCVs": wfSonetFarEndLineIntervalCVs,
       "wfSonetFarEndLineIntervalUASs": wfSonetFarEndLineIntervalUASs,
       "wfSonetPathCurrentTable": wfSonetPathCurrentTable,
       "wfSonetPathCurrentEntry": wfSonetPathCurrentEntry,
       "wfSonetPathCurrentIndex": wfSonetPathCurrentIndex,
       "wfSonetPathCurrentWidth": wfSonetPathCurrentWidth,
       "wfSonetPathCurrentStatus": wfSonetPathCurrentStatus,
       "wfSonetPathCurrentESs": wfSonetPathCurrentESs,
       "wfSonetPathCurrentSESs": wfSonetPathCurrentSESs,
       "wfSonetPathCurrentCVs": wfSonetPathCurrentCVs,
       "wfSonetPathCurrentUASs": wfSonetPathCurrentUASs,
       "wfSonetPathIntervalTable": wfSonetPathIntervalTable,
       "wfSonetPathIntervalEntry": wfSonetPathIntervalEntry,
       "wfSonetPathIntervalIndex": wfSonetPathIntervalIndex,
       "wfSonetPathIntervalNumber": wfSonetPathIntervalNumber,
       "wfSonetPathIntervalESs": wfSonetPathIntervalESs,
       "wfSonetPathIntervalSESs": wfSonetPathIntervalSESs,
       "wfSonetPathIntervalCVs": wfSonetPathIntervalCVs,
       "wfSonetPathIntervalUASs": wfSonetPathIntervalUASs,
       "wfSonetFarEndPathCurrentTable": wfSonetFarEndPathCurrentTable,
       "wfSonetFarEndPathCurrentEntry": wfSonetFarEndPathCurrentEntry,
       "wfSonetFarEndPathCurrentIndex": wfSonetFarEndPathCurrentIndex,
       "wfSonetFarEndPathCurrentESs": wfSonetFarEndPathCurrentESs,
       "wfSonetFarEndPathCurrentSESs": wfSonetFarEndPathCurrentSESs,
       "wfSonetFarEndPathCurrentCVs": wfSonetFarEndPathCurrentCVs,
       "wfSonetFarEndPathCurrentUASs": wfSonetFarEndPathCurrentUASs,
       "wfSonetFarEndPathIntervalTable": wfSonetFarEndPathIntervalTable,
       "wfSonetFarEndPathIntervalEntry": wfSonetFarEndPathIntervalEntry,
       "wfSonetFarEndPathIntervalIndex": wfSonetFarEndPathIntervalIndex,
       "wfSonetFarEndPathIntervalNumber": wfSonetFarEndPathIntervalNumber,
       "wfSonetFarEndPathIntervalESs": wfSonetFarEndPathIntervalESs,
       "wfSonetFarEndPathIntervalSESs": wfSonetFarEndPathIntervalSESs,
       "wfSonetFarEndPathIntervalCVs": wfSonetFarEndPathIntervalCVs,
       "wfSonetFarEndPathIntervalUASs": wfSonetFarEndPathIntervalUASs,
       "wfAtm": wfAtm,
       "wfAtmDelete": wfAtmDelete,
       "wfAtmInterfaceNumber": wfAtmInterfaceNumber,
       "wfAtmOverallStatus": wfAtmOverallStatus,
       "wfAtmGlobalSigStkVersion": wfAtmGlobalSigStkVersion,
       "wfAtmInterfaceTable": wfAtmInterfaceTable,
       "wfAtmInterfaceEntry": wfAtmInterfaceEntry,
       "wfAtmInterfaceDelete": wfAtmInterfaceDelete,
       "wfAtmInterfaceDisable": wfAtmInterfaceDisable,
       "wfAtmInterfaceState": wfAtmInterfaceState,
       "wfAtmInterfaceCircuit": wfAtmInterfaceCircuit,
       "wfAtmInterfaceMaxSupportedVCs": wfAtmInterfaceMaxSupportedVCs,
       "wfAtmInterfaceVCsInUse": wfAtmInterfaceVCsInUse,
       "wfAtmInterfaceDescr": wfAtmInterfaceDescr,
       "wfAtmInterfaceType": wfAtmInterfaceType,
       "wfAtmInterfaceLastChange": wfAtmInterfaceLastChange,
       "wfAtmInterfacePlcp": wfAtmInterfacePlcp,
       "wfAtmMpeNull": wfAtmMpeNull,
       "wfAtmCsNull": wfAtmCsNull,
       "wfAtmInterfaceMulticast": wfAtmInterfaceMulticast,
       "wfAtmDrops": wfAtmDrops,
       "wfAtmInterfaceLmiDisable": wfAtmInterfaceLmiDisable,
       "wfAtmInterfaceLineNumber": wfAtmInterfaceLineNumber,
       "wfAtmInterfaceLLIndex": wfAtmInterfaceLLIndex,
       "wfAtmInterfaceDxiMode": wfAtmInterfaceDxiMode,
       "wfAtmUnknownVCPkts": wfAtmUnknownVCPkts,
       "wfAtmLmiTable": wfAtmLmiTable,
       "wfAtmLmiEntry": wfAtmLmiEntry,
       "wfAtmLmiState": wfAtmLmiState,
       "wfAtmLmiCircuit": wfAtmLmiCircuit,
       "wfAtmLmiNoVCErrors": wfAtmLmiNoVCErrors,
       "wfAtmLmiProxyRequests": wfAtmLmiProxyRequests,
       "wfAtmLmiCsuDsuResponses": wfAtmLmiCsuDsuResponses,
       "wfAtmLmiCsuDsuTraps": wfAtmLmiCsuDsuTraps,
       "wfAtmLmiOtherErrors": wfAtmLmiOtherErrors,
       "wfAtmLmiLineNumber": wfAtmLmiLineNumber,
       "wfAtmLmiLLIndex": wfAtmLmiLLIndex,
       "wfAtmPlcpTable": wfAtmPlcpTable,
       "wfAtmPlcpEntry": wfAtmPlcpEntry,
       "wfAtmPlcpCct": wfAtmPlcpCct,
       "wfAtmPlcpPhysical": wfAtmPlcpPhysical,
       "wfAtmPlcpLof": wfAtmPlcpLof,
       "wfAtmPlcpLofCFA": wfAtmPlcpLofCFA,
       "wfAtmPlcpYellow": wfAtmPlcpYellow,
       "wfAtmPlcpYellowCFA": wfAtmPlcpYellowCFA,
       "wfAtmPlcpStatus": wfAtmPlcpStatus,
       "wfAtmPlcpSeconds": wfAtmPlcpSeconds,
       "wfAtmPlcpBipErrors": wfAtmPlcpBipErrors,
       "wfAtmPlcpBipESecs": wfAtmPlcpBipESecs,
       "wfAtmPlcpBipSESecs": wfAtmPlcpBipSESecs,
       "wfAtmPlcpFebes": wfAtmPlcpFebes,
       "wfAtmPlcpFebeESecs": wfAtmPlcpFebeESecs,
       "wfAtmPlcpFebeSESecs": wfAtmPlcpFebeSESecs,
       "wfAtmPlcpFrameErrors": wfAtmPlcpFrameErrors,
       "wfAtmPlcpSevereFrameErrors": wfAtmPlcpSevereFrameErrors,
       "wfAtmPlcpSEFS": wfAtmPlcpSEFS,
       "wfAtmPlcpUAS": wfAtmPlcpUAS,
       "wfAtmPlcpLineNumber": wfAtmPlcpLineNumber,
       "wfAtmPlcpLLIndex": wfAtmPlcpLLIndex,
       "wfAtmUniTable": wfAtmUniTable,
       "wfAtmUniEntry": wfAtmUniEntry,
       "wfAtmUniCct": wfAtmUniCct,
       "wfAtmUniPhysical": wfAtmUniPhysical,
       "wfAtmUniAal": wfAtmUniAal,
       "wfAtmUniSeconds": wfAtmUniSeconds,
       "wfAtmUniLineNumber": wfAtmUniLineNumber,
       "wfAtmUniLLIndex": wfAtmUniLLIndex,
       "wfAtmUniAtmTable": wfAtmUniAtmTable,
       "wfAtmUniAtmEntry": wfAtmUniAtmEntry,
       "wfAtmUniAtmCct": wfAtmUniAtmCct,
       "wfAtmUniAtmNoBuffers": wfAtmUniAtmNoBuffers,
       "wfAtmUniAtmHECs": wfAtmUniAtmHECs,
       "wfAtmUniAtmCHECs": wfAtmUniAtmCHECs,
       "wfAtmUniAtmNullCells": wfAtmUniAtmNullCells,
       "wfAtmUniAtmMisdeliveredCells": wfAtmUniAtmMisdeliveredCells,
       "wfAtmUniAtmReceives": wfAtmUniAtmReceives,
       "wfAtmUniAtmTransmits": wfAtmUniAtmTransmits,
       "wfAtmUniAtmLineNumber": wfAtmUniAtmLineNumber,
       "wfAtmUniAtmLLIndex": wfAtmUniAtmLLIndex,
       "wfAtmVbrTable": wfAtmVbrTable,
       "wfAtmVbrEntry": wfAtmVbrEntry,
       "wfAtmVbrCct": wfAtmVbrCct,
       "wfAtmVbrAtmUni": wfAtmVbrAtmUni,
       "wfAtmVbrDxi": wfAtmVbrDxi,
       "wfAtmVbrSeconds": wfAtmVbrSeconds,
       "wfAtmVbrLineNumber": wfAtmVbrLineNumber,
       "wfAtmVbrLLIndex": wfAtmVbrLLIndex,
       "wfAtmVbrSarTable": wfAtmVbrSarTable,
       "wfAtmVbrSarEntry": wfAtmVbrSarEntry,
       "wfAtmVbrSarCct": wfAtmVbrSarCct,
       "wfAtmVbrSarAssemblyTimer": wfAtmVbrSarAssemblyTimer,
       "wfAtmVbrSarCrc10Errors": wfAtmVbrSarCrc10Errors,
       "wfAtmVbrSarCellMidErrors": wfAtmVbrSarCellMidErrors,
       "wfAtmVbrSarCsPduSizeTooBigErrors": wfAtmVbrSarCsPduSizeTooBigErrors,
       "wfAtmVbrSarNoBufferErrors": wfAtmVbrSarNoBufferErrors,
       "wfAtmVbrSarComNoProcessErrors": wfAtmVbrSarComNoProcessErrors,
       "wfAtmVbrSarEomNoProcessErrors": wfAtmVbrSarEomNoProcessErrors,
       "wfAtmVbrSarCellSequenceErrors": wfAtmVbrSarCellSequenceErrors,
       "wfAtmVbrSarCellLengthErrors": wfAtmVbrSarCellLengthErrors,
       "wfAtmVbrSarBomBeforeEomErrors": wfAtmVbrSarBomBeforeEomErrors,
       "wfAtmVbrSarTimeouts": wfAtmVbrSarTimeouts,
       "wfAtmVbrSarLengthExceeds": wfAtmVbrSarLengthExceeds,
       "wfAtmVbrSarReceives": wfAtmVbrSarReceives,
       "wfAtmVbrSarTransmits": wfAtmVbrSarTransmits,
       "wfAtmVbrSarLineNumber": wfAtmVbrSarLineNumber,
       "wfAtmVbrSarLLIndex": wfAtmVbrSarLLIndex,
       "wfAtmVbrCsTable": wfAtmVbrCsTable,
       "wfAtmVbrCsEntry": wfAtmVbrCsEntry,
       "wfAtmVbrCsCct": wfAtmVbrCsCct,
       "wfAtmVbrCsBETagMismatches": wfAtmVbrCsBETagMismatches,
       "wfAtmVbrCsLengthMismatches": wfAtmVbrCsLengthMismatches,
       "wfAtmVbrCsMisdeliveredPdus": wfAtmVbrCsMisdeliveredPdus,
       "wfAtmVbrCsReceives": wfAtmVbrCsReceives,
       "wfAtmVbrCsTransmits": wfAtmVbrCsTransmits,
       "wfAtmVbrCsLineNumber": wfAtmVbrCsLineNumber,
       "wfAtmVbrCsLLIndex": wfAtmVbrCsLLIndex,
       "wfAtmVbrCsVciTable": wfAtmVbrCsVciTable,
       "wfAtmVbrCsVciEntry": wfAtmVbrCsVciEntry,
       "wfAtmVbrCsVciVbrCct": wfAtmVbrCsVciVbrCct,
       "wfAtmVbrCsVciIndex": wfAtmVbrCsVciIndex,
       "wfAtmVbrCsVciBETagMismatches": wfAtmVbrCsVciBETagMismatches,
       "wfAtmVbrCsVciLengthMismatches": wfAtmVbrCsVciLengthMismatches,
       "wfAtmVbrCsVciMisdeliveredPdus": wfAtmVbrCsVciMisdeliveredPdus,
       "wfAtmVbrCsVciReceives": wfAtmVbrCsVciReceives,
       "wfAtmVbrCsVciTransmits": wfAtmVbrCsVciTransmits,
       "wfAtmVbrCsVciOctetReceives": wfAtmVbrCsVciOctetReceives,
       "wfAtmVbrCsVciOctetTransmits": wfAtmVbrCsVciOctetTransmits,
       "wfAtmVbrCsVciLineNumber": wfAtmVbrCsVciLineNumber,
       "wfAtmVbrCsVciLLIndex": wfAtmVbrCsVciLLIndex,
       "wfAtmMpeTable": wfAtmMpeTable,
       "wfAtmMpeEntry": wfAtmMpeEntry,
       "wfAtmMpeIndex": wfAtmMpeIndex,
       "wfAtmMpeInvalidNlpids": wfAtmMpeInvalidNlpids,
       "wfAtmMpeInvalidPids": wfAtmMpeInvalidPids,
       "wfAtmMpeInvalidOuis": wfAtmMpeInvalidOuis,
       "wfAtmMpeMisdeliveredPdus": wfAtmMpeMisdeliveredPdus,
       "wfAtmMpeUnsupportedControlFields": wfAtmMpeUnsupportedControlFields,
       "wfAtmMpeInvalidSAP": wfAtmMpeInvalidSAP,
       "wfAtmPvcTable": wfAtmPvcTable,
       "wfAtmPvcEntry": wfAtmPvcEntry,
       "wfAtmPvcDelete": wfAtmPvcDelete,
       "wfAtmPvcCct": wfAtmPvcCct,
       "wfAtmPvcVpi": wfAtmPvcVpi,
       "wfAtmPvcVci": wfAtmPvcVci,
       "wfAtmPvcReceives": wfAtmPvcReceives,
       "wfAtmPvcTransmits": wfAtmPvcTransmits,
       "wfAtmPvcOctetReceives": wfAtmPvcOctetReceives,
       "wfAtmPvcOctetTransmits": wfAtmPvcOctetTransmits,
       "wfAtmPvcMode": wfAtmPvcMode,
       "wfAtmPvcDirectAccessCct": wfAtmPvcDirectAccessCct,
       "wfAtmPvcState": wfAtmPvcState,
       "wfAtmPvcMpeNull": wfAtmPvcMpeNull,
       "wfAtmPvcCsNull": wfAtmPvcCsNull,
       "wfAtmPvcDisable": wfAtmPvcDisable,
       "wfAtmPvcDrops": wfAtmPvcDrops,
       "wfAtmPvcMulticast": wfAtmPvcMulticast,
       "wfAtmPvcLineNumber": wfAtmPvcLineNumber,
       "wfAtmPvcLLIndex": wfAtmPvcLLIndex,
       "wfAtmDxiTable": wfAtmDxiTable,
       "wfAtmDxiEntry": wfAtmDxiEntry,
       "wfAtmDxiCct": wfAtmDxiCct,
       "wfAtmDxiComponent": wfAtmDxiComponent,
       "wfAtmDxiMaxLmiPduLengthErrors": wfAtmDxiMaxLmiPduLengthErrors,
       "wfAtmDxiSeconds": wfAtmDxiSeconds,
       "wfAtmDxiDiscardedFrames": wfAtmDxiDiscardedFrames,
       "wfAtmDxiAbortedFrames": wfAtmDxiAbortedFrames,
       "wfAtmDxiNonOctetAlignedFrames": wfAtmDxiNonOctetAlignedFrames,
       "wfAtmDxiTooLongFrames": wfAtmDxiTooLongFrames,
       "wfAtmDxiTooShortFrames": wfAtmDxiTooShortFrames,
       "wfAtmDxiFrameChecksumErrors": wfAtmDxiFrameChecksumErrors,
       "wfAtmDxiFrameHeaderErrors": wfAtmDxiFrameHeaderErrors,
       "wfAtmDxiValidFrameReceives": wfAtmDxiValidFrameReceives,
       "wfAtmDxiFrameTransmits": wfAtmDxiFrameTransmits,
       "wfAtmDxiLineNumber": wfAtmDxiLineNumber,
       "wfAtmDxiLLIndex": wfAtmDxiLLIndex,
       "wfAtmDxiDxiAddrTable": wfAtmDxiDxiAddrTable,
       "wfAtmDxiDxiAddrEntry": wfAtmDxiDxiAddrEntry,
       "wfAtmDxiDxiAddrDxiCct": wfAtmDxiDxiAddrDxiCct,
       "wfAtmDxiDxiAddrDxiComponent": wfAtmDxiDxiAddrDxiComponent,
       "wfAtmDxiDxiAddrIndex": wfAtmDxiDxiAddrIndex,
       "wfAtmDxiDxiAddrAtmVbr": wfAtmDxiDxiAddrAtmVbr,
       "wfAtmDxiDxiAddrVpiVci": wfAtmDxiDxiAddrVpiVci,
       "wfAtmDxiDxiAddrReceives": wfAtmDxiDxiAddrReceives,
       "wfAtmDxiDxiAddrTransmits": wfAtmDxiDxiAddrTransmits,
       "wfAtmDxiDxiAddrLineNumber": wfAtmDxiDxiAddrLineNumber,
       "wfAtmDxiDxiAddrLLIndex": wfAtmDxiDxiAddrLLIndex}
)
