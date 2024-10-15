# SNMP MIB module (MICOM-MPANL-SIGNALING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-MPANL-SIGNALING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:45 2024
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

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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

_Micom_msm_ObjectIdentity = ObjectIdentity
micom_msm = _Micom_msm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1)
)
_McmMSMProfileCfgGroup_ObjectIdentity = ObjectIdentity
mcmMSMProfileCfgGroup = _McmMSMProfileCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1)
)


class _McmMSMProfileCfgGroupNodeID_Type(Integer32):
    """Custom type mcmMSMProfileCfgGroupNodeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmMSMProfileCfgGroupNodeID_Type.__name__ = "Integer32"
_McmMSMProfileCfgGroupNodeID_Object = MibScalar
mcmMSMProfileCfgGroupNodeID = _McmMSMProfileCfgGroupNodeID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1, 1),
    _McmMSMProfileCfgGroupNodeID_Type()
)
mcmMSMProfileCfgGroupNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMProfileCfgGroupNodeID.setStatus("mandatory")


class _McmMSMProfileCfgGroupCustomerID_Type(Integer32):
    """Custom type mcmMSMProfileCfgGroupCustomerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmMSMProfileCfgGroupCustomerID_Type.__name__ = "Integer32"
_McmMSMProfileCfgGroupCustomerID_Object = MibScalar
mcmMSMProfileCfgGroupCustomerID = _McmMSMProfileCfgGroupCustomerID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1, 2),
    _McmMSMProfileCfgGroupCustomerID_Type()
)
mcmMSMProfileCfgGroupCustomerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMProfileCfgGroupCustomerID.setStatus("mandatory")


class _McmMSMProfileCfgGroupDNAPrefix_Type(DisplayString):
    """Custom type mcmMSMProfileCfgGroupDNAPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_McmMSMProfileCfgGroupDNAPrefix_Type.__name__ = "DisplayString"
_McmMSMProfileCfgGroupDNAPrefix_Object = MibScalar
mcmMSMProfileCfgGroupDNAPrefix = _McmMSMProfileCfgGroupDNAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 1, 3),
    _McmMSMProfileCfgGroupDNAPrefix_Type()
)
mcmMSMProfileCfgGroupDNAPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMProfileCfgGroupDNAPrefix.setStatus("mandatory")
_NvmMSMProfileCfgGroup_ObjectIdentity = ObjectIdentity
nvmMSMProfileCfgGroup = _NvmMSMProfileCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2)
)


class _NvmMSMProfileCfgGroupNodeID_Type(Integer32):
    """Custom type nvmMSMProfileCfgGroupNodeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmMSMProfileCfgGroupNodeID_Type.__name__ = "Integer32"
_NvmMSMProfileCfgGroupNodeID_Object = MibScalar
nvmMSMProfileCfgGroupNodeID = _NvmMSMProfileCfgGroupNodeID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2, 1),
    _NvmMSMProfileCfgGroupNodeID_Type()
)
nvmMSMProfileCfgGroupNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMProfileCfgGroupNodeID.setStatus("mandatory")


class _NvmMSMProfileCfgGroupCustomerID_Type(Integer32):
    """Custom type nvmMSMProfileCfgGroupCustomerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmMSMProfileCfgGroupCustomerID_Type.__name__ = "Integer32"
_NvmMSMProfileCfgGroupCustomerID_Object = MibScalar
nvmMSMProfileCfgGroupCustomerID = _NvmMSMProfileCfgGroupCustomerID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2, 2),
    _NvmMSMProfileCfgGroupCustomerID_Type()
)
nvmMSMProfileCfgGroupCustomerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMProfileCfgGroupCustomerID.setStatus("mandatory")


class _NvmMSMProfileCfgGroupDNAPrefix_Type(DisplayString):
    """Custom type nvmMSMProfileCfgGroupDNAPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NvmMSMProfileCfgGroupDNAPrefix_Type.__name__ = "DisplayString"
_NvmMSMProfileCfgGroupDNAPrefix_Object = MibScalar
nvmMSMProfileCfgGroupDNAPrefix = _NvmMSMProfileCfgGroupDNAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 2, 3),
    _NvmMSMProfileCfgGroupDNAPrefix_Type()
)
nvmMSMProfileCfgGroupDNAPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMProfileCfgGroupDNAPrefix.setStatus("mandatory")
_McmMSMDTELinkCfgTable_Object = MibTable
mcmMSMDTELinkCfgTable = _McmMSMDTELinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3)
)
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgTable.setStatus("mandatory")
_McmMSMDTELinkCfgEntry_Object = MibTableRow
mcmMSMDTELinkCfgEntry = _McmMSMDTELinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1)
)
mcmMSMDTELinkCfgEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDTELinkCfgIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgEntry.setStatus("mandatory")


class _McmMSMDTELinkCfgIfIndex_Type(Integer32):
    """Custom type mcmMSMDTELinkCfgIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMDTELinkCfgIfIndex_Type.__name__ = "Integer32"
_McmMSMDTELinkCfgIfIndex_Object = MibTableColumn
mcmMSMDTELinkCfgIfIndex = _McmMSMDTELinkCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 1),
    _McmMSMDTELinkCfgIfIndex_Type()
)
mcmMSMDTELinkCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgIfIndex.setStatus("mandatory")


class _McmMSMDTELinkCfgMaxSubChannelRange_Type(Integer32):
    """Custom type mcmMSMDTELinkCfgMaxSubChannelRange based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 255),
    )


_McmMSMDTELinkCfgMaxSubChannelRange_Type.__name__ = "Integer32"
_McmMSMDTELinkCfgMaxSubChannelRange_Object = MibTableColumn
mcmMSMDTELinkCfgMaxSubChannelRange = _McmMSMDTELinkCfgMaxSubChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 2),
    _McmMSMDTELinkCfgMaxSubChannelRange_Type()
)
mcmMSMDTELinkCfgMaxSubChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgMaxSubChannelRange.setStatus("mandatory")


class _McmMSMDTELinkCfgDTEReceiverBW_Type(Integer32):
    """Custom type mcmMSMDTELinkCfgDTEReceiverBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 2048000),
    )


_McmMSMDTELinkCfgDTEReceiverBW_Type.__name__ = "Integer32"
_McmMSMDTELinkCfgDTEReceiverBW_Object = MibTableColumn
mcmMSMDTELinkCfgDTEReceiverBW = _McmMSMDTELinkCfgDTEReceiverBW_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 3),
    _McmMSMDTELinkCfgDTEReceiverBW_Type()
)
mcmMSMDTELinkCfgDTEReceiverBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgDTEReceiverBW.setStatus("mandatory")


class _McmMSMDTELinkCfgDCEReceiverBW_Type(Integer32):
    """Custom type mcmMSMDTELinkCfgDCEReceiverBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 2048000),
    )


_McmMSMDTELinkCfgDCEReceiverBW_Type.__name__ = "Integer32"
_McmMSMDTELinkCfgDCEReceiverBW_Object = MibTableColumn
mcmMSMDTELinkCfgDCEReceiverBW = _McmMSMDTELinkCfgDCEReceiverBW_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 4),
    _McmMSMDTELinkCfgDCEReceiverBW_Type()
)
mcmMSMDTELinkCfgDCEReceiverBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgDCEReceiverBW.setStatus("mandatory")


class _McmMSMDTELinkCfgDTEMaxFrameSize_Type(Integer32):
    """Custom type mcmMSMDTELinkCfgDTEMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 4100),
    )


_McmMSMDTELinkCfgDTEMaxFrameSize_Type.__name__ = "Integer32"
_McmMSMDTELinkCfgDTEMaxFrameSize_Object = MibTableColumn
mcmMSMDTELinkCfgDTEMaxFrameSize = _McmMSMDTELinkCfgDTEMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 5),
    _McmMSMDTELinkCfgDTEMaxFrameSize_Type()
)
mcmMSMDTELinkCfgDTEMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgDTEMaxFrameSize.setStatus("mandatory")


class _McmMSMDTELinkCfgDCEMaxFrameSize_Type(Integer32):
    """Custom type mcmMSMDTELinkCfgDCEMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 4100),
    )


_McmMSMDTELinkCfgDCEMaxFrameSize_Type.__name__ = "Integer32"
_McmMSMDTELinkCfgDCEMaxFrameSize_Object = MibTableColumn
mcmMSMDTELinkCfgDCEMaxFrameSize = _McmMSMDTELinkCfgDCEMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 3, 1, 6),
    _McmMSMDTELinkCfgDCEMaxFrameSize_Type()
)
mcmMSMDTELinkCfgDCEMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkCfgDCEMaxFrameSize.setStatus("mandatory")
_NvmMSMDTELinkCfgTable_Object = MibTable
nvmMSMDTELinkCfgTable = _NvmMSMDTELinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4)
)
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgTable.setStatus("mandatory")
_NvmMSMDTELinkCfgEntry_Object = MibTableRow
nvmMSMDTELinkCfgEntry = _NvmMSMDTELinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1)
)
nvmMSMDTELinkCfgEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "nvmMSMDTELinkCfgIfIndex"),
)
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgEntry.setStatus("mandatory")


class _NvmMSMDTELinkCfgIfIndex_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmMSMDTELinkCfgIfIndex_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgIfIndex_Object = MibTableColumn
nvmMSMDTELinkCfgIfIndex = _NvmMSMDTELinkCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 1),
    _NvmMSMDTELinkCfgIfIndex_Type()
)
nvmMSMDTELinkCfgIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgIfIndex.setStatus("mandatory")


class _NvmMSMDTELinkCfgMaxSubChannelRange_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgMaxSubChannelRange based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 255),
    )


_NvmMSMDTELinkCfgMaxSubChannelRange_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgMaxSubChannelRange_Object = MibTableColumn
nvmMSMDTELinkCfgMaxSubChannelRange = _NvmMSMDTELinkCfgMaxSubChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 2),
    _NvmMSMDTELinkCfgMaxSubChannelRange_Type()
)
nvmMSMDTELinkCfgMaxSubChannelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgMaxSubChannelRange.setStatus("mandatory")


class _NvmMSMDTELinkCfgDTEReceiverBW_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgDTEReceiverBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 2048000),
    )


_NvmMSMDTELinkCfgDTEReceiverBW_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgDTEReceiverBW_Object = MibTableColumn
nvmMSMDTELinkCfgDTEReceiverBW = _NvmMSMDTELinkCfgDTEReceiverBW_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 3),
    _NvmMSMDTELinkCfgDTEReceiverBW_Type()
)
nvmMSMDTELinkCfgDTEReceiverBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgDTEReceiverBW.setStatus("mandatory")


class _NvmMSMDTELinkCfgDCEReceiverBW_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgDCEReceiverBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 2048000),
    )


_NvmMSMDTELinkCfgDCEReceiverBW_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgDCEReceiverBW_Object = MibTableColumn
nvmMSMDTELinkCfgDCEReceiverBW = _NvmMSMDTELinkCfgDCEReceiverBW_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 4),
    _NvmMSMDTELinkCfgDCEReceiverBW_Type()
)
nvmMSMDTELinkCfgDCEReceiverBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgDCEReceiverBW.setStatus("mandatory")


class _NvmMSMDTELinkCfgDTEMaxFrameSize_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgDTEMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 4100),
    )


_NvmMSMDTELinkCfgDTEMaxFrameSize_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgDTEMaxFrameSize_Object = MibTableColumn
nvmMSMDTELinkCfgDTEMaxFrameSize = _NvmMSMDTELinkCfgDTEMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 5),
    _NvmMSMDTELinkCfgDTEMaxFrameSize_Type()
)
nvmMSMDTELinkCfgDTEMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgDTEMaxFrameSize.setStatus("mandatory")


class _NvmMSMDTELinkCfgDCEMaxFrameSize_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgDCEMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 4100),
    )


_NvmMSMDTELinkCfgDCEMaxFrameSize_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgDCEMaxFrameSize_Object = MibTableColumn
nvmMSMDTELinkCfgDCEMaxFrameSize = _NvmMSMDTELinkCfgDCEMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 6),
    _NvmMSMDTELinkCfgDCEMaxFrameSize_Type()
)
nvmMSMDTELinkCfgDCEMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgDCEMaxFrameSize.setStatus("mandatory")


class _NvmMSMDTELinkCfgEntryStatus_Type(Integer32):
    """Custom type nvmMSMDTELinkCfgEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("modify", 1)
    )


_NvmMSMDTELinkCfgEntryStatus_Type.__name__ = "Integer32"
_NvmMSMDTELinkCfgEntryStatus_Object = MibTableColumn
nvmMSMDTELinkCfgEntryStatus = _NvmMSMDTELinkCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 1, 4, 1, 7),
    _NvmMSMDTELinkCfgEntryStatus_Type()
)
nvmMSMDTELinkCfgEntryStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvmMSMDTELinkCfgEntryStatus.setStatus("obsolete")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2)
)
_McmMSMLAPFConnectionsCntrTable_Object = MibTable
mcmMSMLAPFConnectionsCntrTable = _McmMSMLAPFConnectionsCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1)
)
if mibBuilder.loadTexts:
    mcmMSMLAPFConnectionsCntrTable.setStatus("obsolete")
_McmMSMLAPFConnectionsCntrEntry_Object = MibTableRow
mcmMSMLAPFConnectionsCntrEntry = _McmMSMLAPFConnectionsCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1, 1)
)
mcmMSMLAPFConnectionsCntrEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMLAPFConnectionsCntrIndex"),
)
if mibBuilder.loadTexts:
    mcmMSMLAPFConnectionsCntrEntry.setStatus("obsolete")


class _McmMSMLAPFConnectionsCntrIndex_Type(Integer32):
    """Custom type mcmMSMLAPFConnectionsCntrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMLAPFConnectionsCntrIndex_Type.__name__ = "Integer32"
_McmMSMLAPFConnectionsCntrIndex_Object = MibTableColumn
mcmMSMLAPFConnectionsCntrIndex = _McmMSMLAPFConnectionsCntrIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1, 1, 1),
    _McmMSMLAPFConnectionsCntrIndex_Type()
)
mcmMSMLAPFConnectionsCntrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLAPFConnectionsCntrIndex.setStatus("obsolete")


class _McmMSMLAPFConnectionsCntrAction_Type(Integer32):
    """Custom type mcmMSMLAPFConnectionsCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmMSMLAPFConnectionsCntrAction_Type.__name__ = "Integer32"
_McmMSMLAPFConnectionsCntrAction_Object = MibTableColumn
mcmMSMLAPFConnectionsCntrAction = _McmMSMLAPFConnectionsCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 2, 1, 1, 2),
    _McmMSMLAPFConnectionsCntrAction_Type()
)
mcmMSMLAPFConnectionsCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmMSMLAPFConnectionsCntrAction.setStatus("obsolete")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3)
)
_McmMSMStatsLAPFConnTable_Object = MibTable
mcmMSMStatsLAPFConnTable = _McmMSMStatsLAPFConnTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1)
)
if mibBuilder.loadTexts:
    mcmMSMStatsLAPFConnTable.setStatus("mandatory")
_McmMSMStatsLAPFConnEntry_Object = MibTableRow
mcmMSMStatsLAPFConnEntry = _McmMSMStatsLAPFConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1)
)
mcmMSMStatsLAPFConnEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMStatsLAPFConnIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMSMStatsLAPFConnEntry.setStatus("mandatory")


class _McmMSMStatsLAPFConnIfIndex_Type(Integer32):
    """Custom type mcmMSMStatsLAPFConnIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMStatsLAPFConnIfIndex_Type.__name__ = "Integer32"
_McmMSMStatsLAPFConnIfIndex_Object = MibTableColumn
mcmMSMStatsLAPFConnIfIndex = _McmMSMStatsLAPFConnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 1),
    _McmMSMStatsLAPFConnIfIndex_Type()
)
mcmMSMStatsLAPFConnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsLAPFConnIfIndex.setStatus("mandatory")
_McmMSMStatsLAPFConnReestablished_Type = Counter32
_McmMSMStatsLAPFConnReestablished_Object = MibTableColumn
mcmMSMStatsLAPFConnReestablished = _McmMSMStatsLAPFConnReestablished_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 2),
    _McmMSMStatsLAPFConnReestablished_Type()
)
mcmMSMStatsLAPFConnReestablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsLAPFConnReestablished.setStatus("obsolete")
_McmMSMStatsLAPFConnEstablished_Type = Counter32
_McmMSMStatsLAPFConnEstablished_Object = MibTableColumn
mcmMSMStatsLAPFConnEstablished = _McmMSMStatsLAPFConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 3),
    _McmMSMStatsLAPFConnEstablished_Type()
)
mcmMSMStatsLAPFConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsLAPFConnEstablished.setStatus("mandatory")
_McmMSMStatsLAPFConnDisconnects_Type = Counter32
_McmMSMStatsLAPFConnDisconnects_Object = MibTableColumn
mcmMSMStatsLAPFConnDisconnects = _McmMSMStatsLAPFConnDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 4),
    _McmMSMStatsLAPFConnDisconnects_Type()
)
mcmMSMStatsLAPFConnDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsLAPFConnDisconnects.setStatus("mandatory")
_McmMSMStatsProfileTxCnt_Type = Counter32
_McmMSMStatsProfileTxCnt_Object = MibTableColumn
mcmMSMStatsProfileTxCnt = _McmMSMStatsProfileTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 5),
    _McmMSMStatsProfileTxCnt_Type()
)
mcmMSMStatsProfileTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsProfileTxCnt.setStatus("mandatory")
_McmMSMStatsProfileRxCnt_Type = Counter32
_McmMSMStatsProfileRxCnt_Object = MibTableColumn
mcmMSMStatsProfileRxCnt = _McmMSMStatsProfileRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 6),
    _McmMSMStatsProfileRxCnt_Type()
)
mcmMSMStatsProfileRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsProfileRxCnt.setStatus("mandatory")
_McmMSMStatsRestartReqTxCnt_Type = Counter32
_McmMSMStatsRestartReqTxCnt_Object = MibTableColumn
mcmMSMStatsRestartReqTxCnt = _McmMSMStatsRestartReqTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 7),
    _McmMSMStatsRestartReqTxCnt_Type()
)
mcmMSMStatsRestartReqTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsRestartReqTxCnt.setStatus("mandatory")
_McmMSMStatsRestartReqRxCnt_Type = Counter32
_McmMSMStatsRestartReqRxCnt_Object = MibTableColumn
mcmMSMStatsRestartReqRxCnt = _McmMSMStatsRestartReqRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 8),
    _McmMSMStatsRestartReqRxCnt_Type()
)
mcmMSMStatsRestartReqRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsRestartReqRxCnt.setStatus("mandatory")
_McmMSMStatsDnaAssociationCnt_Type = Counter32
_McmMSMStatsDnaAssociationCnt_Object = MibTableColumn
mcmMSMStatsDnaAssociationCnt = _McmMSMStatsDnaAssociationCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 9),
    _McmMSMStatsDnaAssociationCnt_Type()
)
mcmMSMStatsDnaAssociationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsDnaAssociationCnt.setStatus("mandatory")
_McmMSMStatsDnaDeassociationCnt_Type = Counter32
_McmMSMStatsDnaDeassociationCnt_Object = MibTableColumn
mcmMSMStatsDnaDeassociationCnt = _McmMSMStatsDnaDeassociationCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 10),
    _McmMSMStatsDnaDeassociationCnt_Type()
)
mcmMSMStatsDnaDeassociationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsDnaDeassociationCnt.setStatus("mandatory")
_McmMSMStatsPANLInfoElementsTxCnt_Type = Counter32
_McmMSMStatsPANLInfoElementsTxCnt_Object = MibTableColumn
mcmMSMStatsPANLInfoElementsTxCnt = _McmMSMStatsPANLInfoElementsTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 11),
    _McmMSMStatsPANLInfoElementsTxCnt_Type()
)
mcmMSMStatsPANLInfoElementsTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsPANLInfoElementsTxCnt.setStatus("mandatory")
_McmMSMStatsPANLInfoElementsRxCnt_Type = Counter32
_McmMSMStatsPANLInfoElementsRxCnt_Object = MibTableColumn
mcmMSMStatsPANLInfoElementsRxCnt = _McmMSMStatsPANLInfoElementsRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 1, 1, 12),
    _McmMSMStatsPANLInfoElementsRxCnt_Type()
)
mcmMSMStatsPANLInfoElementsRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMStatsPANLInfoElementsRxCnt.setStatus("mandatory")
_McmMSMDTELinkStatsTable_Object = MibTable
mcmMSMDTELinkStatsTable = _McmMSMDTELinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2)
)
if mibBuilder.loadTexts:
    mcmMSMDTELinkStatsTable.setStatus("deprecated")
_McmMSMDTELinkStatsEntry_Object = MibTableRow
mcmMSMDTELinkStatsEntry = _McmMSMDTELinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1)
)
mcmMSMDTELinkStatsEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDTELinkStatsIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMSMDTELinkStatsEntry.setStatus("deprecated")


class _McmMSMDTELinkStatsIfIndex_Type(Integer32):
    """Custom type mcmMSMDTELinkStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMDTELinkStatsIfIndex_Type.__name__ = "Integer32"
_McmMSMDTELinkStatsIfIndex_Object = MibTableColumn
mcmMSMDTELinkStatsIfIndex = _McmMSMDTELinkStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 1),
    _McmMSMDTELinkStatsIfIndex_Type()
)
mcmMSMDTELinkStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkStatsIfIndex.setStatus("deprecated")


class _McmMSMDTELinkStatsStatus_Type(Integer32):
    """Custom type mcmMSMDTELinkStatsStatus based on Integer32"""
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


_McmMSMDTELinkStatsStatus_Type.__name__ = "Integer32"
_McmMSMDTELinkStatsStatus_Object = MibTableColumn
mcmMSMDTELinkStatsStatus = _McmMSMDTELinkStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 2),
    _McmMSMDTELinkStatsStatus_Type()
)
mcmMSMDTELinkStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkStatsStatus.setStatus("deprecated")


class _McmMSMDTELinkStatsLocalCompName_Type(DisplayString):
    """Custom type mcmMSMDTELinkStatsLocalCompName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_McmMSMDTELinkStatsLocalCompName_Type.__name__ = "DisplayString"
_McmMSMDTELinkStatsLocalCompName_Object = MibTableColumn
mcmMSMDTELinkStatsLocalCompName = _McmMSMDTELinkStatsLocalCompName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 3),
    _McmMSMDTELinkStatsLocalCompName_Type()
)
mcmMSMDTELinkStatsLocalCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkStatsLocalCompName.setStatus("deprecated")


class _McmMSMDTELinkStatsRemoteCompName_Type(DisplayString):
    """Custom type mcmMSMDTELinkStatsRemoteCompName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_McmMSMDTELinkStatsRemoteCompName_Type.__name__ = "DisplayString"
_McmMSMDTELinkStatsRemoteCompName_Object = MibTableColumn
mcmMSMDTELinkStatsRemoteCompName = _McmMSMDTELinkStatsRemoteCompName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 3, 2, 1, 4),
    _McmMSMDTELinkStatsRemoteCompName_Type()
)
mcmMSMDTELinkStatsRemoteCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDTELinkStatsRemoteCompName.setStatus("deprecated")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4)
)
_McmMSMLinkStatusTable_Object = MibTable
mcmMSMLinkStatusTable = _McmMSMLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1)
)
if mibBuilder.loadTexts:
    mcmMSMLinkStatusTable.setStatus("mandatory")
_McmMSMLinkStatusEntry_Object = MibTableRow
mcmMSMLinkStatusEntry = _McmMSMLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1)
)
mcmMSMLinkStatusEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMSMLinkStatusEntry.setStatus("mandatory")


class _McmMSMLinkStatusIfIndex_Type(Integer32):
    """Custom type mcmMSMLinkStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMLinkStatusIfIndex_Type.__name__ = "Integer32"
_McmMSMLinkStatusIfIndex_Object = MibTableColumn
mcmMSMLinkStatusIfIndex = _McmMSMLinkStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 1),
    _McmMSMLinkStatusIfIndex_Type()
)
mcmMSMLinkStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusIfIndex.setStatus("mandatory")


class _McmMSMLinkStatusInterfaceType_Type(Integer32):
    """Custom type mcmMSMLinkStatusInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_McmMSMLinkStatusInterfaceType_Type.__name__ = "Integer32"
_McmMSMLinkStatusInterfaceType_Object = MibTableColumn
mcmMSMLinkStatusInterfaceType = _McmMSMLinkStatusInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 2),
    _McmMSMLinkStatusInterfaceType_Type()
)
mcmMSMLinkStatusInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusInterfaceType.setStatus("mandatory")


class _McmMSMLinkStatusLAPFStatus_Type(Integer32):
    """Custom type mcmMSMLinkStatusLAPFStatus based on Integer32"""
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


_McmMSMLinkStatusLAPFStatus_Type.__name__ = "Integer32"
_McmMSMLinkStatusLAPFStatus_Object = MibTableColumn
mcmMSMLinkStatusLAPFStatus = _McmMSMLinkStatusLAPFStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 3),
    _McmMSMLinkStatusLAPFStatus_Type()
)
mcmMSMLinkStatusLAPFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusLAPFStatus.setStatus("mandatory")


class _McmMSMLinkStatusLocalCompName_Type(DisplayString):
    """Custom type mcmMSMLinkStatusLocalCompName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_McmMSMLinkStatusLocalCompName_Type.__name__ = "DisplayString"
_McmMSMLinkStatusLocalCompName_Object = MibTableColumn
mcmMSMLinkStatusLocalCompName = _McmMSMLinkStatusLocalCompName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 4),
    _McmMSMLinkStatusLocalCompName_Type()
)
mcmMSMLinkStatusLocalCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusLocalCompName.setStatus("mandatory")


class _McmMSMLinkStatusRemoteCompName_Type(DisplayString):
    """Custom type mcmMSMLinkStatusRemoteCompName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_McmMSMLinkStatusRemoteCompName_Type.__name__ = "DisplayString"
_McmMSMLinkStatusRemoteCompName_Object = MibTableColumn
mcmMSMLinkStatusRemoteCompName = _McmMSMLinkStatusRemoteCompName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 5),
    _McmMSMLinkStatusRemoteCompName_Type()
)
mcmMSMLinkStatusRemoteCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusRemoteCompName.setStatus("mandatory")


class _McmMSMLinkStatusRemoteGenCfgType_Type(Integer32):
    """Custom type mcmMSMLinkStatusRemoteGenCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("micomAccessDevice", 1),
          ("nortelAccessDevice", 2),
          ("passportSwitch", 3))
    )


_McmMSMLinkStatusRemoteGenCfgType_Type.__name__ = "Integer32"
_McmMSMLinkStatusRemoteGenCfgType_Object = MibTableColumn
mcmMSMLinkStatusRemoteGenCfgType = _McmMSMLinkStatusRemoteGenCfgType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 6),
    _McmMSMLinkStatusRemoteGenCfgType_Type()
)
mcmMSMLinkStatusRemoteGenCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusRemoteGenCfgType.setStatus("mandatory")


class _McmMSMLinkStatusPANLStatus_Type(Integer32):
    """Custom type mcmMSMLinkStatusPANLStatus based on Integer32"""
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
        *(("down", 1),
          ("incompatible", 4),
          ("restart", 3),
          ("up", 2))
    )


_McmMSMLinkStatusPANLStatus_Type.__name__ = "Integer32"
_McmMSMLinkStatusPANLStatus_Object = MibTableColumn
mcmMSMLinkStatusPANLStatus = _McmMSMLinkStatusPANLStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 1, 1, 7),
    _McmMSMLinkStatusPANLStatus_Type()
)
mcmMSMLinkStatusPANLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMLinkStatusPANLStatus.setStatus("mandatory")
_McmMSMDCELinkStatusTable_Object = MibTable
mcmMSMDCELinkStatusTable = _McmMSMDCELinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2)
)
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusTable.setStatus("mandatory")
_McmMSMDCELinkStatusEntry_Object = MibTableRow
mcmMSMDCELinkStatusEntry = _McmMSMDCELinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1)
)
mcmMSMDCELinkStatusEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDCELinkStatusIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusEntry.setStatus("mandatory")


class _McmMSMDCELinkStatusIfIndex_Type(Integer32):
    """Custom type mcmMSMDCELinkStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMDCELinkStatusIfIndex_Type.__name__ = "Integer32"
_McmMSMDCELinkStatusIfIndex_Object = MibTableColumn
mcmMSMDCELinkStatusIfIndex = _McmMSMDCELinkStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 1),
    _McmMSMDCELinkStatusIfIndex_Type()
)
mcmMSMDCELinkStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusIfIndex.setStatus("mandatory")


class _McmMSMDCELinkStatusRemoteNodeId_Type(Integer32):
    """Custom type mcmMSMDCELinkStatusRemoteNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmMSMDCELinkStatusRemoteNodeId_Type.__name__ = "Integer32"
_McmMSMDCELinkStatusRemoteNodeId_Object = MibTableColumn
mcmMSMDCELinkStatusRemoteNodeId = _McmMSMDCELinkStatusRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 2),
    _McmMSMDCELinkStatusRemoteNodeId_Type()
)
mcmMSMDCELinkStatusRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusRemoteNodeId.setStatus("mandatory")


class _McmMSMDCELinkStatusRemoteCustId_Type(Integer32):
    """Custom type mcmMSMDCELinkStatusRemoteCustId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmMSMDCELinkStatusRemoteCustId_Type.__name__ = "Integer32"
_McmMSMDCELinkStatusRemoteCustId_Object = MibTableColumn
mcmMSMDCELinkStatusRemoteCustId = _McmMSMDCELinkStatusRemoteCustId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 3),
    _McmMSMDCELinkStatusRemoteCustId_Type()
)
mcmMSMDCELinkStatusRemoteCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusRemoteCustId.setStatus("mandatory")


class _McmMSMDCELinkStatusRemoteRxBw_Type(Integer32):
    """Custom type mcmMSMDCELinkStatusRemoteRxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1600, 2048000),
    )


_McmMSMDCELinkStatusRemoteRxBw_Type.__name__ = "Integer32"
_McmMSMDCELinkStatusRemoteRxBw_Object = MibTableColumn
mcmMSMDCELinkStatusRemoteRxBw = _McmMSMDCELinkStatusRemoteRxBw_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 4),
    _McmMSMDCELinkStatusRemoteRxBw_Type()
)
mcmMSMDCELinkStatusRemoteRxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusRemoteRxBw.setStatus("mandatory")


class _McmMSMDCELinkStatusRemoteMaxFrameSize_Type(Integer32):
    """Custom type mcmMSMDCELinkStatusRemoteMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 4100),
    )


_McmMSMDCELinkStatusRemoteMaxFrameSize_Type.__name__ = "Integer32"
_McmMSMDCELinkStatusRemoteMaxFrameSize_Object = MibTableColumn
mcmMSMDCELinkStatusRemoteMaxFrameSize = _McmMSMDCELinkStatusRemoteMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 5),
    _McmMSMDCELinkStatusRemoteMaxFrameSize_Type()
)
mcmMSMDCELinkStatusRemoteMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusRemoteMaxFrameSize.setStatus("mandatory")


class _McmMSMDCELinkStatusRemoteDLCIRange_Type(Integer32):
    """Custom type mcmMSMDCELinkStatusRemoteDLCIRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 255),
    )


_McmMSMDCELinkStatusRemoteDLCIRange_Type.__name__ = "Integer32"
_McmMSMDCELinkStatusRemoteDLCIRange_Object = MibTableColumn
mcmMSMDCELinkStatusRemoteDLCIRange = _McmMSMDCELinkStatusRemoteDLCIRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 2, 1, 6),
    _McmMSMDCELinkStatusRemoteDLCIRange_Type()
)
mcmMSMDCELinkStatusRemoteDLCIRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDCELinkStatusRemoteDLCIRange.setStatus("mandatory")
_McmMSMDNAStatusTable_Object = MibTable
mcmMSMDNAStatusTable = _McmMSMDNAStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3)
)
if mibBuilder.loadTexts:
    mcmMSMDNAStatusTable.setStatus("mandatory")
_McmMSMDNAStatusEntry_Object = MibTableRow
mcmMSMDNAStatusEntry = _McmMSMDNAStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1)
)
mcmMSMDNAStatusEntry.setIndexNames(
    (0, "MICOM-MPANL-SIGNALING-MIB", "mcmMSMDNAStatusPrefixNumber"),
)
if mibBuilder.loadTexts:
    mcmMSMDNAStatusEntry.setStatus("mandatory")


class _McmMSMDNAStatusPrefixNumber_Type(DisplayString):
    """Custom type mcmMSMDNAStatusPrefixNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_McmMSMDNAStatusPrefixNumber_Type.__name__ = "DisplayString"
_McmMSMDNAStatusPrefixNumber_Object = MibTableColumn
mcmMSMDNAStatusPrefixNumber = _McmMSMDNAStatusPrefixNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1, 1),
    _McmMSMDNAStatusPrefixNumber_Type()
)
mcmMSMDNAStatusPrefixNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDNAStatusPrefixNumber.setStatus("mandatory")


class _McmMSMDNAStatusIfIndex_Type(Integer32):
    """Custom type mcmMSMDNAStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMSMDNAStatusIfIndex_Type.__name__ = "Integer32"
_McmMSMDNAStatusIfIndex_Object = MibTableColumn
mcmMSMDNAStatusIfIndex = _McmMSMDNAStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1, 2),
    _McmMSMDNAStatusIfIndex_Type()
)
mcmMSMDNAStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDNAStatusIfIndex.setStatus("mandatory")


class _McmMSMDNAStatusAssociation_Type(Integer32):
    """Custom type mcmMSMDNAStatusAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("associatedDNA", 1),
          ("deassociatedDNA", 2))
    )


_McmMSMDNAStatusAssociation_Type.__name__ = "Integer32"
_McmMSMDNAStatusAssociation_Object = MibTableColumn
mcmMSMDNAStatusAssociation = _McmMSMDNAStatusAssociation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 4, 3, 1, 3),
    _McmMSMDNAStatusAssociation_Type()
)
mcmMSMDNAStatusAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMSMDNAStatusAssociation.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmMSMProfileReceivedFromPassport = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 0, 1)
)
mcmMSMProfileReceivedFromPassport.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMDTELinkStatsRemoteCompName"))
)
if mibBuilder.loadTexts:
    mcmMSMProfileReceivedFromPassport.setStatus(
        ""
    )

mcmMpanlInterfaceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 0, 2)
)
mcmMpanlInterfaceLinkUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"))
)
if mibBuilder.loadTexts:
    mcmMpanlInterfaceLinkUp.setStatus(
        ""
    )

mcmMpanlInterfaceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 0, 3)
)
mcmMpanlInterfaceLinkDown.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"))
)
if mibBuilder.loadTexts:
    mcmMpanlInterfaceLinkDown.setStatus(
        ""
    )

mcmMpanlPrefixDNAhasNotBeenConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 0, 4)
)
mcmMpanlPrefixDNAhasNotBeenConfigured.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmMpanlPrefixDNAhasNotBeenConfigured.setStatus(
        ""
    )

mcmMpanlPrefixDNAChangedWithoutDeassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 0, 5)
)
mcmMpanlPrefixDNAChangedWithoutDeassociation.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMDNAStatusPrefixNumber"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMDNAStatusIfIndex"))
)
if mibBuilder.loadTexts:
    mcmMpanlPrefixDNAChangedWithoutDeassociation.setStatus(
        ""
    )

mcmMpanlIncompatibleType = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 19, 0, 6)
)
mcmMpanlIncompatibleType.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusIfIndex"),
        ("MICOM-MPANL-SIGNALING-MIB", "mcmMSMLinkStatusRemoteGenCfgType"))
)
if mibBuilder.loadTexts:
    mcmMpanlIncompatibleType.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-MPANL-SIGNALING-MIB",
    **{"micom-msm": micom_msm,
       "mcmMSMProfileReceivedFromPassport": mcmMSMProfileReceivedFromPassport,
       "mcmMpanlInterfaceLinkUp": mcmMpanlInterfaceLinkUp,
       "mcmMpanlInterfaceLinkDown": mcmMpanlInterfaceLinkDown,
       "mcmMpanlPrefixDNAhasNotBeenConfigured": mcmMpanlPrefixDNAhasNotBeenConfigured,
       "mcmMpanlPrefixDNAChangedWithoutDeassociation": mcmMpanlPrefixDNAChangedWithoutDeassociation,
       "mcmMpanlIncompatibleType": mcmMpanlIncompatibleType,
       "configuration": configuration,
       "mcmMSMProfileCfgGroup": mcmMSMProfileCfgGroup,
       "mcmMSMProfileCfgGroupNodeID": mcmMSMProfileCfgGroupNodeID,
       "mcmMSMProfileCfgGroupCustomerID": mcmMSMProfileCfgGroupCustomerID,
       "mcmMSMProfileCfgGroupDNAPrefix": mcmMSMProfileCfgGroupDNAPrefix,
       "nvmMSMProfileCfgGroup": nvmMSMProfileCfgGroup,
       "nvmMSMProfileCfgGroupNodeID": nvmMSMProfileCfgGroupNodeID,
       "nvmMSMProfileCfgGroupCustomerID": nvmMSMProfileCfgGroupCustomerID,
       "nvmMSMProfileCfgGroupDNAPrefix": nvmMSMProfileCfgGroupDNAPrefix,
       "mcmMSMDTELinkCfgTable": mcmMSMDTELinkCfgTable,
       "mcmMSMDTELinkCfgEntry": mcmMSMDTELinkCfgEntry,
       "mcmMSMDTELinkCfgIfIndex": mcmMSMDTELinkCfgIfIndex,
       "mcmMSMDTELinkCfgMaxSubChannelRange": mcmMSMDTELinkCfgMaxSubChannelRange,
       "mcmMSMDTELinkCfgDTEReceiverBW": mcmMSMDTELinkCfgDTEReceiverBW,
       "mcmMSMDTELinkCfgDCEReceiverBW": mcmMSMDTELinkCfgDCEReceiverBW,
       "mcmMSMDTELinkCfgDTEMaxFrameSize": mcmMSMDTELinkCfgDTEMaxFrameSize,
       "mcmMSMDTELinkCfgDCEMaxFrameSize": mcmMSMDTELinkCfgDCEMaxFrameSize,
       "nvmMSMDTELinkCfgTable": nvmMSMDTELinkCfgTable,
       "nvmMSMDTELinkCfgEntry": nvmMSMDTELinkCfgEntry,
       "nvmMSMDTELinkCfgIfIndex": nvmMSMDTELinkCfgIfIndex,
       "nvmMSMDTELinkCfgMaxSubChannelRange": nvmMSMDTELinkCfgMaxSubChannelRange,
       "nvmMSMDTELinkCfgDTEReceiverBW": nvmMSMDTELinkCfgDTEReceiverBW,
       "nvmMSMDTELinkCfgDCEReceiverBW": nvmMSMDTELinkCfgDCEReceiverBW,
       "nvmMSMDTELinkCfgDTEMaxFrameSize": nvmMSMDTELinkCfgDTEMaxFrameSize,
       "nvmMSMDTELinkCfgDCEMaxFrameSize": nvmMSMDTELinkCfgDCEMaxFrameSize,
       "nvmMSMDTELinkCfgEntryStatus": nvmMSMDTELinkCfgEntryStatus,
       "control": control,
       "mcmMSMLAPFConnectionsCntrTable": mcmMSMLAPFConnectionsCntrTable,
       "mcmMSMLAPFConnectionsCntrEntry": mcmMSMLAPFConnectionsCntrEntry,
       "mcmMSMLAPFConnectionsCntrIndex": mcmMSMLAPFConnectionsCntrIndex,
       "mcmMSMLAPFConnectionsCntrAction": mcmMSMLAPFConnectionsCntrAction,
       "statistics": statistics,
       "mcmMSMStatsLAPFConnTable": mcmMSMStatsLAPFConnTable,
       "mcmMSMStatsLAPFConnEntry": mcmMSMStatsLAPFConnEntry,
       "mcmMSMStatsLAPFConnIfIndex": mcmMSMStatsLAPFConnIfIndex,
       "mcmMSMStatsLAPFConnReestablished": mcmMSMStatsLAPFConnReestablished,
       "mcmMSMStatsLAPFConnEstablished": mcmMSMStatsLAPFConnEstablished,
       "mcmMSMStatsLAPFConnDisconnects": mcmMSMStatsLAPFConnDisconnects,
       "mcmMSMStatsProfileTxCnt": mcmMSMStatsProfileTxCnt,
       "mcmMSMStatsProfileRxCnt": mcmMSMStatsProfileRxCnt,
       "mcmMSMStatsRestartReqTxCnt": mcmMSMStatsRestartReqTxCnt,
       "mcmMSMStatsRestartReqRxCnt": mcmMSMStatsRestartReqRxCnt,
       "mcmMSMStatsDnaAssociationCnt": mcmMSMStatsDnaAssociationCnt,
       "mcmMSMStatsDnaDeassociationCnt": mcmMSMStatsDnaDeassociationCnt,
       "mcmMSMStatsPANLInfoElementsTxCnt": mcmMSMStatsPANLInfoElementsTxCnt,
       "mcmMSMStatsPANLInfoElementsRxCnt": mcmMSMStatsPANLInfoElementsRxCnt,
       "mcmMSMDTELinkStatsTable": mcmMSMDTELinkStatsTable,
       "mcmMSMDTELinkStatsEntry": mcmMSMDTELinkStatsEntry,
       "mcmMSMDTELinkStatsIfIndex": mcmMSMDTELinkStatsIfIndex,
       "mcmMSMDTELinkStatsStatus": mcmMSMDTELinkStatsStatus,
       "mcmMSMDTELinkStatsLocalCompName": mcmMSMDTELinkStatsLocalCompName,
       "mcmMSMDTELinkStatsRemoteCompName": mcmMSMDTELinkStatsRemoteCompName,
       "status": status,
       "mcmMSMLinkStatusTable": mcmMSMLinkStatusTable,
       "mcmMSMLinkStatusEntry": mcmMSMLinkStatusEntry,
       "mcmMSMLinkStatusIfIndex": mcmMSMLinkStatusIfIndex,
       "mcmMSMLinkStatusInterfaceType": mcmMSMLinkStatusInterfaceType,
       "mcmMSMLinkStatusLAPFStatus": mcmMSMLinkStatusLAPFStatus,
       "mcmMSMLinkStatusLocalCompName": mcmMSMLinkStatusLocalCompName,
       "mcmMSMLinkStatusRemoteCompName": mcmMSMLinkStatusRemoteCompName,
       "mcmMSMLinkStatusRemoteGenCfgType": mcmMSMLinkStatusRemoteGenCfgType,
       "mcmMSMLinkStatusPANLStatus": mcmMSMLinkStatusPANLStatus,
       "mcmMSMDCELinkStatusTable": mcmMSMDCELinkStatusTable,
       "mcmMSMDCELinkStatusEntry": mcmMSMDCELinkStatusEntry,
       "mcmMSMDCELinkStatusIfIndex": mcmMSMDCELinkStatusIfIndex,
       "mcmMSMDCELinkStatusRemoteNodeId": mcmMSMDCELinkStatusRemoteNodeId,
       "mcmMSMDCELinkStatusRemoteCustId": mcmMSMDCELinkStatusRemoteCustId,
       "mcmMSMDCELinkStatusRemoteRxBw": mcmMSMDCELinkStatusRemoteRxBw,
       "mcmMSMDCELinkStatusRemoteMaxFrameSize": mcmMSMDCELinkStatusRemoteMaxFrameSize,
       "mcmMSMDCELinkStatusRemoteDLCIRange": mcmMSMDCELinkStatusRemoteDLCIRange,
       "mcmMSMDNAStatusTable": mcmMSMDNAStatusTable,
       "mcmMSMDNAStatusEntry": mcmMSMDNAStatusEntry,
       "mcmMSMDNAStatusPrefixNumber": mcmMSMDNAStatusPrefixNumber,
       "mcmMSMDNAStatusIfIndex": mcmMSMDNAStatusIfIndex,
       "mcmMSMDNAStatusAssociation": mcmMSMDNAStatusAssociation}
)
