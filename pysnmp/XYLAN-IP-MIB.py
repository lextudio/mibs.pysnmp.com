# SNMP MIB module (XYLAN-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:06 2024
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

(xylanIpArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanIpArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanIpFilterGroup_ObjectIdentity = ObjectIdentity
xylanIpFilterGroup = _XylanIpFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1)
)
_XylanIpRipFilterTable_Object = MibTable
xylanIpRipFilterTable = _XylanIpRipFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    xylanIpRipFilterTable.setStatus("mandatory")
_XylanIpRipFilterEntry_Object = MibTableRow
xylanIpRipFilterEntry = _XylanIpRipFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1)
)
xylanIpRipFilterEntry.setIndexNames(
    (0, "XYLAN-IP-MIB", "xylanIpRipFilterNum"),
)
if mibBuilder.loadTexts:
    xylanIpRipFilterEntry.setStatus("mandatory")
_XylanIpRipFilterNum_Type = Integer32
_XylanIpRipFilterNum_Object = MibTableColumn
xylanIpRipFilterNum = _XylanIpRipFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 1),
    _XylanIpRipFilterNum_Type()
)
xylanIpRipFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpRipFilterNum.setStatus("mandatory")


class _XylanIpRipFilterAdminState_Type(Integer32):
    """Custom type xylanIpRipFilterAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanIpRipFilterAdminState_Type.__name__ = "Integer32"
_XylanIpRipFilterAdminState_Object = MibTableColumn
xylanIpRipFilterAdminState = _XylanIpRipFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 2),
    _XylanIpRipFilterAdminState_Type()
)
xylanIpRipFilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterAdminState.setStatus("mandatory")


class _XylanIpRipFilterType_Type(Integer32):
    """Custom type xylanIpRipFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip-input", 2),
          ("rip-output", 1))
    )


_XylanIpRipFilterType_Type.__name__ = "Integer32"
_XylanIpRipFilterType_Object = MibTableColumn
xylanIpRipFilterType = _XylanIpRipFilterType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 3),
    _XylanIpRipFilterType_Type()
)
xylanIpRipFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterType.setStatus("mandatory")
_XylanIpRipFilterNet_Type = IpAddress
_XylanIpRipFilterNet_Object = MibTableColumn
xylanIpRipFilterNet = _XylanIpRipFilterNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 4),
    _XylanIpRipFilterNet_Type()
)
xylanIpRipFilterNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterNet.setStatus("mandatory")
_XylanIpRipFilterNetMask_Type = IpAddress
_XylanIpRipFilterNetMask_Object = MibTableColumn
xylanIpRipFilterNetMask = _XylanIpRipFilterNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 5),
    _XylanIpRipFilterNetMask_Type()
)
xylanIpRipFilterNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterNetMask.setStatus("mandatory")


class _XylanIpRipFilterMode_Type(Integer32):
    """Custom type xylanIpRipFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_XylanIpRipFilterMode_Type.__name__ = "Integer32"
_XylanIpRipFilterMode_Object = MibTableColumn
xylanIpRipFilterMode = _XylanIpRipFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 6),
    _XylanIpRipFilterMode_Type()
)
xylanIpRipFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterMode.setStatus("mandatory")
_XylanIpRipFilterGroupId_Type = Integer32
_XylanIpRipFilterGroupId_Object = MibTableColumn
xylanIpRipFilterGroupId = _XylanIpRipFilterGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 7),
    _XylanIpRipFilterGroupId_Type()
)
xylanIpRipFilterGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterGroupId.setStatus("mandatory")
_XylanIpRipFilterVlanId_Type = Integer32
_XylanIpRipFilterVlanId_Object = MibTableColumn
xylanIpRipFilterVlanId = _XylanIpRipFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 8),
    _XylanIpRipFilterVlanId_Type()
)
xylanIpRipFilterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterVlanId.setStatus("mandatory")


class _XylanIpRipFilterWanType_Type(Integer32):
    """Custom type xylanIpRipFilterWanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 2),
          ("not-used", 1),
          ("ppp", 3))
    )


_XylanIpRipFilterWanType_Type.__name__ = "Integer32"
_XylanIpRipFilterWanType_Object = MibTableColumn
xylanIpRipFilterWanType = _XylanIpRipFilterWanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 9),
    _XylanIpRipFilterWanType_Type()
)
xylanIpRipFilterWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterWanType.setStatus("mandatory")
_XylanIpRipFilterSlot_Type = Integer32
_XylanIpRipFilterSlot_Object = MibTableColumn
xylanIpRipFilterSlot = _XylanIpRipFilterSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 10),
    _XylanIpRipFilterSlot_Type()
)
xylanIpRipFilterSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterSlot.setStatus("mandatory")
_XylanIpRipFilterPort_Type = Integer32
_XylanIpRipFilterPort_Object = MibTableColumn
xylanIpRipFilterPort = _XylanIpRipFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 11),
    _XylanIpRipFilterPort_Type()
)
xylanIpRipFilterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterPort.setStatus("mandatory")
_XylanIpRipFilterVc_Type = Integer32
_XylanIpRipFilterVc_Object = MibTableColumn
xylanIpRipFilterVc = _XylanIpRipFilterVc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 12),
    _XylanIpRipFilterVc_Type()
)
xylanIpRipFilterVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterVc.setStatus("mandatory")
_XylanIpRipFilterPeerId_Type = Integer32
_XylanIpRipFilterPeerId_Object = MibTableColumn
xylanIpRipFilterPeerId = _XylanIpRipFilterPeerId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 1, 1, 1, 13),
    _XylanIpRipFilterPeerId_Type()
)
xylanIpRipFilterPeerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpRipFilterPeerId.setStatus("mandatory")
_XylanIpMiscGroup_ObjectIdentity = ObjectIdentity
xylanIpMiscGroup = _XylanIpMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2)
)
_XylanIpAssocMacTable_Object = MibTable
xylanIpAssocMacTable = _XylanIpAssocMacTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    xylanIpAssocMacTable.setStatus("mandatory")
_XylanIpAssocEntry_Object = MibTableRow
xylanIpAssocEntry = _XylanIpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1)
)
xylanIpAssocEntry.setIndexNames(
    (0, "XYLAN-IP-MIB", "xylanIpAssocAddr"),
)
if mibBuilder.loadTexts:
    xylanIpAssocEntry.setStatus("mandatory")
_XylanIpAssocAddr_Type = IpAddress
_XylanIpAssocAddr_Object = MibTableColumn
xylanIpAssocAddr = _XylanIpAssocAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 1),
    _XylanIpAssocAddr_Type()
)
xylanIpAssocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocAddr.setStatus("mandatory")
_XylanIpAssocMac_Type = OctetString
_XylanIpAssocMac_Object = MibTableColumn
xylanIpAssocMac = _XylanIpAssocMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 2),
    _XylanIpAssocMac_Type()
)
xylanIpAssocMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocMac.setStatus("mandatory")
_XylanIpAssocSlot_Type = Integer32
_XylanIpAssocSlot_Object = MibTableColumn
xylanIpAssocSlot = _XylanIpAssocSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 3),
    _XylanIpAssocSlot_Type()
)
xylanIpAssocSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocSlot.setStatus("mandatory")
_XylanIpAssocIntf_Type = Integer32
_XylanIpAssocIntf_Object = MibTableColumn
xylanIpAssocIntf = _XylanIpAssocIntf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 4),
    _XylanIpAssocIntf_Type()
)
xylanIpAssocIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocIntf.setStatus("mandatory")
_XylanIpAssocDupMac_Type = OctetString
_XylanIpAssocDupMac_Object = MibTableColumn
xylanIpAssocDupMac = _XylanIpAssocDupMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 5),
    _XylanIpAssocDupMac_Type()
)
xylanIpAssocDupMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocDupMac.setStatus("mandatory")
_XylanIpAssocDupSlot_Type = Integer32
_XylanIpAssocDupSlot_Object = MibTableColumn
xylanIpAssocDupSlot = _XylanIpAssocDupSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 6),
    _XylanIpAssocDupSlot_Type()
)
xylanIpAssocDupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocDupSlot.setStatus("mandatory")
_XylanIpAssocDupIntf_Type = Integer32
_XylanIpAssocDupIntf_Object = MibTableColumn
xylanIpAssocDupIntf = _XylanIpAssocDupIntf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 13, 2, 1, 1, 7),
    _XylanIpAssocDupIntf_Type()
)
xylanIpAssocDupIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpAssocDupIntf.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-IP-MIB",
    **{"xylanIpFilterGroup": xylanIpFilterGroup,
       "xylanIpRipFilterTable": xylanIpRipFilterTable,
       "xylanIpRipFilterEntry": xylanIpRipFilterEntry,
       "xylanIpRipFilterNum": xylanIpRipFilterNum,
       "xylanIpRipFilterAdminState": xylanIpRipFilterAdminState,
       "xylanIpRipFilterType": xylanIpRipFilterType,
       "xylanIpRipFilterNet": xylanIpRipFilterNet,
       "xylanIpRipFilterNetMask": xylanIpRipFilterNetMask,
       "xylanIpRipFilterMode": xylanIpRipFilterMode,
       "xylanIpRipFilterGroupId": xylanIpRipFilterGroupId,
       "xylanIpRipFilterVlanId": xylanIpRipFilterVlanId,
       "xylanIpRipFilterWanType": xylanIpRipFilterWanType,
       "xylanIpRipFilterSlot": xylanIpRipFilterSlot,
       "xylanIpRipFilterPort": xylanIpRipFilterPort,
       "xylanIpRipFilterVc": xylanIpRipFilterVc,
       "xylanIpRipFilterPeerId": xylanIpRipFilterPeerId,
       "xylanIpMiscGroup": xylanIpMiscGroup,
       "xylanIpAssocMacTable": xylanIpAssocMacTable,
       "xylanIpAssocEntry": xylanIpAssocEntry,
       "xylanIpAssocAddr": xylanIpAssocAddr,
       "xylanIpAssocMac": xylanIpAssocMac,
       "xylanIpAssocSlot": xylanIpAssocSlot,
       "xylanIpAssocIntf": xylanIpAssocIntf,
       "xylanIpAssocDupMac": xylanIpAssocDupMac,
       "xylanIpAssocDupSlot": xylanIpAssocDupSlot,
       "xylanIpAssocDupIntf": xylanIpAssocDupIntf}
)
