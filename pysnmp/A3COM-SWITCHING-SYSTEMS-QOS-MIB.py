# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:52 2024
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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComQos_ObjectIdentity = ObjectIdentity
a3ComQos = _A3ComQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21)
)
_A3ComQosClass_ObjectIdentity = ObjectIdentity
a3ComQosClass = _A3ComQosClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1)
)
_A3ComQosGenClassTable_Object = MibTable
a3ComQosGenClassTable = _A3ComQosGenClassTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 1)
)
if mibBuilder.loadTexts:
    a3ComQosGenClassTable.setStatus("mandatory")
_A3ComQosGenClassEntry_Object = MibTableRow
a3ComQosGenClassEntry = _A3ComQosGenClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 1, 1)
)
a3ComQosGenClassEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosGenClassIndex"),
)
if mibBuilder.loadTexts:
    a3ComQosGenClassEntry.setStatus("mandatory")


class _A3ComQosGenClassIndex_Type(Integer32):
    """Custom type a3ComQosGenClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65532),
    )


_A3ComQosGenClassIndex_Type.__name__ = "Integer32"
_A3ComQosGenClassIndex_Object = MibTableColumn
a3ComQosGenClassIndex = _A3ComQosGenClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 1, 1, 1),
    _A3ComQosGenClassIndex_Type()
)
a3ComQosGenClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosGenClassIndex.setStatus("mandatory")


class _A3ComQosGenClassName_Type(DisplayString):
    """Custom type a3ComQosGenClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_A3ComQosGenClassName_Type.__name__ = "DisplayString"
_A3ComQosGenClassName_Object = MibTableColumn
a3ComQosGenClassName = _A3ComQosGenClassName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 1, 1, 2),
    _A3ComQosGenClassName_Type()
)
a3ComQosGenClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosGenClassName.setStatus("mandatory")
_A3ComQosGenClassControlId_Type = Integer32
_A3ComQosGenClassControlId_Object = MibTableColumn
a3ComQosGenClassControlId = _A3ComQosGenClassControlId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 1, 1, 3),
    _A3ComQosGenClassControlId_Type()
)
a3ComQosGenClassControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosGenClassControlId.setStatus("mandatory")
_A3ComQosFlowClassTable_Object = MibTable
a3ComQosFlowClassTable = _A3ComQosFlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2)
)
if mibBuilder.loadTexts:
    a3ComQosFlowClassTable.setStatus("mandatory")
_A3ComQosFlowClassEntry_Object = MibTableRow
a3ComQosFlowClassEntry = _A3ComQosFlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1)
)
a3ComQosFlowClassEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosFlowClassIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosFlowClassFilterIndex"),
)
if mibBuilder.loadTexts:
    a3ComQosFlowClassEntry.setStatus("mandatory")


class _A3ComQosFlowClassIndex_Type(Integer32):
    """Custom type a3ComQosFlowClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65532),
    )


_A3ComQosFlowClassIndex_Type.__name__ = "Integer32"
_A3ComQosFlowClassIndex_Object = MibTableColumn
a3ComQosFlowClassIndex = _A3ComQosFlowClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 1),
    _A3ComQosFlowClassIndex_Type()
)
a3ComQosFlowClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosFlowClassIndex.setStatus("mandatory")


class _A3ComQosFlowClassFilterIndex_Type(Integer32):
    """Custom type a3ComQosFlowClassFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_A3ComQosFlowClassFilterIndex_Type.__name__ = "Integer32"
_A3ComQosFlowClassFilterIndex_Object = MibTableColumn
a3ComQosFlowClassFilterIndex = _A3ComQosFlowClassFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 2),
    _A3ComQosFlowClassFilterIndex_Type()
)
a3ComQosFlowClassFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosFlowClassFilterIndex.setStatus("mandatory")


class _A3ComQosFlowClassCastType_Type(Integer32):
    """Custom type a3ComQosFlowClassCastType based on Integer32"""
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
        *(("both", 3),
          ("multicast", 2),
          ("unicast", 1))
    )


_A3ComQosFlowClassCastType_Type.__name__ = "Integer32"
_A3ComQosFlowClassCastType_Object = MibTableColumn
a3ComQosFlowClassCastType = _A3ComQosFlowClassCastType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 3),
    _A3ComQosFlowClassCastType_Type()
)
a3ComQosFlowClassCastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassCastType.setStatus("mandatory")


class _A3ComQosFlowClassIpProtoType_Type(Integer32):
    """Custom type a3ComQosFlowClassIpProtoType based on Integer32"""
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
        *(("both", 3),
          ("tcp", 2),
          ("udp", 1))
    )


_A3ComQosFlowClassIpProtoType_Type.__name__ = "Integer32"
_A3ComQosFlowClassIpProtoType_Object = MibTableColumn
a3ComQosFlowClassIpProtoType = _A3ComQosFlowClassIpProtoType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 4),
    _A3ComQosFlowClassIpProtoType_Type()
)
a3ComQosFlowClassIpProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassIpProtoType.setStatus("mandatory")
_A3ComQosFlowClassSrcAddr_Type = IpAddress
_A3ComQosFlowClassSrcAddr_Object = MibTableColumn
a3ComQosFlowClassSrcAddr = _A3ComQosFlowClassSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 5),
    _A3ComQosFlowClassSrcAddr_Type()
)
a3ComQosFlowClassSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassSrcAddr.setStatus("mandatory")
_A3ComQosFlowClassSrcSubnetMask_Type = IpAddress
_A3ComQosFlowClassSrcSubnetMask_Object = MibTableColumn
a3ComQosFlowClassSrcSubnetMask = _A3ComQosFlowClassSrcSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 6),
    _A3ComQosFlowClassSrcSubnetMask_Type()
)
a3ComQosFlowClassSrcSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassSrcSubnetMask.setStatus("mandatory")
_A3ComQosFlowClassDestAddr_Type = IpAddress
_A3ComQosFlowClassDestAddr_Object = MibTableColumn
a3ComQosFlowClassDestAddr = _A3ComQosFlowClassDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 7),
    _A3ComQosFlowClassDestAddr_Type()
)
a3ComQosFlowClassDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassDestAddr.setStatus("mandatory")
_A3ComQosFlowClassDestSubnetMask_Type = IpAddress
_A3ComQosFlowClassDestSubnetMask_Object = MibTableColumn
a3ComQosFlowClassDestSubnetMask = _A3ComQosFlowClassDestSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 8),
    _A3ComQosFlowClassDestSubnetMask_Type()
)
a3ComQosFlowClassDestSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassDestSubnetMask.setStatus("mandatory")


class _A3ComQosFlowClassPortStart_Type(Integer32):
    """Custom type a3ComQosFlowClassPortStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComQosFlowClassPortStart_Type.__name__ = "Integer32"
_A3ComQosFlowClassPortStart_Object = MibTableColumn
a3ComQosFlowClassPortStart = _A3ComQosFlowClassPortStart_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 9),
    _A3ComQosFlowClassPortStart_Type()
)
a3ComQosFlowClassPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassPortStart.setStatus("mandatory")


class _A3ComQosFlowClassPortEnd_Type(Integer32):
    """Custom type a3ComQosFlowClassPortEnd based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComQosFlowClassPortEnd_Type.__name__ = "Integer32"
_A3ComQosFlowClassPortEnd_Object = MibTableColumn
a3ComQosFlowClassPortEnd = _A3ComQosFlowClassPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 10),
    _A3ComQosFlowClassPortEnd_Type()
)
a3ComQosFlowClassPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassPortEnd.setStatus("mandatory")
_A3ComQosFlowClassRowStatus_Type = RowStatus
_A3ComQosFlowClassRowStatus_Object = MibTableColumn
a3ComQosFlowClassRowStatus = _A3ComQosFlowClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 2, 1, 11),
    _A3ComQosFlowClassRowStatus_Type()
)
a3ComQosFlowClassRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosFlowClassRowStatus.setStatus("mandatory")
_A3ComQosNonFlowClassTable_Object = MibTable
a3ComQosNonFlowClassTable = _A3ComQosNonFlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3)
)
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassTable.setStatus("mandatory")
_A3ComQosNonFlowClassEntry_Object = MibTableRow
a3ComQosNonFlowClassEntry = _A3ComQosNonFlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1)
)
a3ComQosNonFlowClassEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosNonFlowClassIndex"),
)
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassEntry.setStatus("mandatory")


class _A3ComQosNonFlowClassIndex_Type(Integer32):
    """Custom type a3ComQosNonFlowClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65532),
    )


_A3ComQosNonFlowClassIndex_Type.__name__ = "Integer32"
_A3ComQosNonFlowClassIndex_Object = MibTableColumn
a3ComQosNonFlowClassIndex = _A3ComQosNonFlowClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 1),
    _A3ComQosNonFlowClassIndex_Type()
)
a3ComQosNonFlowClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassIndex.setStatus("mandatory")


class _A3ComQosNonFlowClassCastType_Type(OctetString):
    """Custom type a3ComQosNonFlowClassCastType based on OctetString"""
    defaultHexValue = "07"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_A3ComQosNonFlowClassCastType_Type.__name__ = "OctetString"
_A3ComQosNonFlowClassCastType_Object = MibTableColumn
a3ComQosNonFlowClassCastType = _A3ComQosNonFlowClassCastType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 2),
    _A3ComQosNonFlowClassCastType_Type()
)
a3ComQosNonFlowClassCastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassCastType.setStatus("mandatory")


class _A3ComQosNonFlowClassProtos_Type(OctetString):
    """Custom type a3ComQosNonFlowClassProtos based on OctetString"""
    defaultHexValue = "f"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_A3ComQosNonFlowClassProtos_Type.__name__ = "OctetString"
_A3ComQosNonFlowClassProtos_Object = MibTableColumn
a3ComQosNonFlowClassProtos = _A3ComQosNonFlowClassProtos_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 3),
    _A3ComQosNonFlowClassProtos_Type()
)
a3ComQosNonFlowClassProtos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassProtos.setStatus("mandatory")


class _A3ComQosNonFlowClass8021pTags_Type(OctetString):
    """Custom type a3ComQosNonFlowClass8021pTags based on OctetString"""
    defaultHexValue = "ff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_A3ComQosNonFlowClass8021pTags_Type.__name__ = "OctetString"
_A3ComQosNonFlowClass8021pTags_Object = MibTableColumn
a3ComQosNonFlowClass8021pTags = _A3ComQosNonFlowClass8021pTags_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 4),
    _A3ComQosNonFlowClass8021pTags_Type()
)
a3ComQosNonFlowClass8021pTags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClass8021pTags.setStatus("mandatory")
_A3ComQosNonFlowClassRowStatus_Type = RowStatus
_A3ComQosNonFlowClassRowStatus_Object = MibTableColumn
a3ComQosNonFlowClassRowStatus = _A3ComQosNonFlowClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 5),
    _A3ComQosNonFlowClassRowStatus_Type()
)
a3ComQosNonFlowClassRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassRowStatus.setStatus("mandatory")


class _A3ComQosNonFlowClassProtoDescriptor_Type(Integer32):
    """Custom type a3ComQosNonFlowClassProtoDescriptor based on Integer32"""
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
        *(("dsap-ssap", 3),
          ("ethertype", 2),
          ("name", 1))
    )


_A3ComQosNonFlowClassProtoDescriptor_Type.__name__ = "Integer32"
_A3ComQosNonFlowClassProtoDescriptor_Object = MibTableColumn
a3ComQosNonFlowClassProtoDescriptor = _A3ComQosNonFlowClassProtoDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 6),
    _A3ComQosNonFlowClassProtoDescriptor_Type()
)
a3ComQosNonFlowClassProtoDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassProtoDescriptor.setStatus("mandatory")


class _A3ComQosNonFlowClassCustomProto_Type(OctetString):
    """Custom type a3ComQosNonFlowClassCustomProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_A3ComQosNonFlowClassCustomProto_Type.__name__ = "OctetString"
_A3ComQosNonFlowClassCustomProto_Object = MibTableColumn
a3ComQosNonFlowClassCustomProto = _A3ComQosNonFlowClassCustomProto_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 1, 3, 1, 7),
    _A3ComQosNonFlowClassCustomProto_Type()
)
a3ComQosNonFlowClassCustomProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosNonFlowClassCustomProto.setStatus("mandatory")
_A3ComQosCtrl_ObjectIdentity = ObjectIdentity
a3ComQosCtrl = _A3ComQosCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2)
)
_A3ComQosCtrlTable_Object = MibTable
a3ComQosCtrlTable = _A3ComQosCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComQosCtrlTable.setStatus("mandatory")
_A3ComQosCtrlEntry_Object = MibTableRow
a3ComQosCtrlEntry = _A3ComQosCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1)
)
a3ComQosCtrlEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosCtrlIndex"),
)
if mibBuilder.loadTexts:
    a3ComQosCtrlEntry.setStatus("mandatory")


class _A3ComQosCtrlIndex_Type(Integer32):
    """Custom type a3ComQosCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65532),
    )


_A3ComQosCtrlIndex_Type.__name__ = "Integer32"
_A3ComQosCtrlIndex_Object = MibTableColumn
a3ComQosCtrlIndex = _A3ComQosCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 1),
    _A3ComQosCtrlIndex_Type()
)
a3ComQosCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosCtrlIndex.setStatus("mandatory")


class _A3ComQosCtrlName_Type(DisplayString):
    """Custom type a3ComQosCtrlName based on DisplayString"""
    defaultHexValue = "00"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_A3ComQosCtrlName_Type.__name__ = "DisplayString"
_A3ComQosCtrlName_Object = MibTableColumn
a3ComQosCtrlName = _A3ComQosCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 2),
    _A3ComQosCtrlName_Type()
)
a3ComQosCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlName.setStatus("mandatory")


class _A3ComQosCtrlServiceLevel_Type(Integer32):
    """Custom type a3ComQosCtrlServiceLevel based on Integer32"""
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
        *(("bestEffort", 2),
          ("drop", 4),
          ("highPriority", 1),
          ("lowPriority", 3))
    )


_A3ComQosCtrlServiceLevel_Type.__name__ = "Integer32"
_A3ComQosCtrlServiceLevel_Object = MibTableColumn
a3ComQosCtrlServiceLevel = _A3ComQosCtrlServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 3),
    _A3ComQosCtrlServiceLevel_Type()
)
a3ComQosCtrlServiceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlServiceLevel.setStatus("mandatory")


class _A3ComQosCtrlConformPktsLossEligible_Type(Integer32):
    """Custom type a3ComQosCtrlConformPktsLossEligible based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("nonEligible", 2))
    )


_A3ComQosCtrlConformPktsLossEligible_Type.__name__ = "Integer32"
_A3ComQosCtrlConformPktsLossEligible_Object = MibTableColumn
a3ComQosCtrlConformPktsLossEligible = _A3ComQosCtrlConformPktsLossEligible_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 4),
    _A3ComQosCtrlConformPktsLossEligible_Type()
)
a3ComQosCtrlConformPktsLossEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlConformPktsLossEligible.setStatus("mandatory")


class _A3ComQosCtrlExcessPktsServiceLevel_Type(Integer32):
    """Custom type a3ComQosCtrlExcessPktsServiceLevel based on Integer32"""
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
        *(("bestEffort", 2),
          ("drop", 4),
          ("highPriority", 1),
          ("lowPriority", 3))
    )


_A3ComQosCtrlExcessPktsServiceLevel_Type.__name__ = "Integer32"
_A3ComQosCtrlExcessPktsServiceLevel_Object = MibTableColumn
a3ComQosCtrlExcessPktsServiceLevel = _A3ComQosCtrlExcessPktsServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 5),
    _A3ComQosCtrlExcessPktsServiceLevel_Type()
)
a3ComQosCtrlExcessPktsServiceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlExcessPktsServiceLevel.setStatus("mandatory")


class _A3ComQosCtrlExcessPktsLossEligible_Type(Integer32):
    """Custom type a3ComQosCtrlExcessPktsLossEligible based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("nonEligible", 2))
    )


_A3ComQosCtrlExcessPktsLossEligible_Type.__name__ = "Integer32"
_A3ComQosCtrlExcessPktsLossEligible_Object = MibTableColumn
a3ComQosCtrlExcessPktsLossEligible = _A3ComQosCtrlExcessPktsLossEligible_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 6),
    _A3ComQosCtrlExcessPktsLossEligible_Type()
)
a3ComQosCtrlExcessPktsLossEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlExcessPktsLossEligible.setStatus("mandatory")


class _A3ComQosCtrl8021pTag_Type(Integer32):
    """Custom type a3ComQosCtrl8021pTag based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021pTag0", 2),
          ("ieee8021pTag1", 3),
          ("ieee8021pTag2", 4),
          ("ieee8021pTag3", 5),
          ("ieee8021pTag4", 6),
          ("ieee8021pTag5", 7),
          ("ieee8021pTag6", 8),
          ("ieee8021pTag7", 9),
          ("none", 1))
    )


_A3ComQosCtrl8021pTag_Type.__name__ = "Integer32"
_A3ComQosCtrl8021pTag_Object = MibTableColumn
a3ComQosCtrl8021pTag = _A3ComQosCtrl8021pTag_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 7),
    _A3ComQosCtrl8021pTag_Type()
)
a3ComQosCtrl8021pTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrl8021pTag.setStatus("mandatory")


class _A3ComQosCtrlRateLimitType_Type(Integer32):
    """Custom type a3ComQosCtrlRateLimitType based on Integer32"""
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
        *(("aggregate", 3),
          ("none", 1),
          ("receivePort", 2))
    )


_A3ComQosCtrlRateLimitType_Type.__name__ = "Integer32"
_A3ComQosCtrlRateLimitType_Object = MibTableColumn
a3ComQosCtrlRateLimitType = _A3ComQosCtrlRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 8),
    _A3ComQosCtrlRateLimitType_Type()
)
a3ComQosCtrlRateLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitType.setStatus("mandatory")
_A3ComQosCtrlRowStatus_Type = RowStatus
_A3ComQosCtrlRowStatus_Object = MibTableColumn
a3ComQosCtrlRowStatus = _A3ComQosCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 1, 1, 9),
    _A3ComQosCtrlRowStatus_Type()
)
a3ComQosCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlRowStatus.setStatus("mandatory")
_A3ComQosCtrlRateLimitTable_Object = MibTable
a3ComQosCtrlRateLimitTable = _A3ComQosCtrlRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitTable.setStatus("mandatory")
_A3ComQosCtrlRateLimitEntry_Object = MibTableRow
a3ComQosCtrlRateLimitEntry = _A3ComQosCtrlRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1)
)
a3ComQosCtrlRateLimitEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosCtrlRateLimitCtrlIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosCtrlRateLimitIndex"),
)
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitEntry.setStatus("mandatory")


class _A3ComQosCtrlRateLimitCtrlIndex_Type(Integer32):
    """Custom type a3ComQosCtrlRateLimitCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65532),
    )


_A3ComQosCtrlRateLimitCtrlIndex_Type.__name__ = "Integer32"
_A3ComQosCtrlRateLimitCtrlIndex_Object = MibTableColumn
a3ComQosCtrlRateLimitCtrlIndex = _A3ComQosCtrlRateLimitCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1, 1),
    _A3ComQosCtrlRateLimitCtrlIndex_Type()
)
a3ComQosCtrlRateLimitCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitCtrlIndex.setStatus("mandatory")


class _A3ComQosCtrlRateLimitIndex_Type(Integer32):
    """Custom type a3ComQosCtrlRateLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_A3ComQosCtrlRateLimitIndex_Type.__name__ = "Integer32"
_A3ComQosCtrlRateLimitIndex_Object = MibTableColumn
a3ComQosCtrlRateLimitIndex = _A3ComQosCtrlRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1, 2),
    _A3ComQosCtrlRateLimitIndex_Type()
)
a3ComQosCtrlRateLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitIndex.setStatus("mandatory")


class _A3ComQosCtrlRateLimitPercent_Type(Integer32):
    """Custom type a3ComQosCtrlRateLimitPercent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_A3ComQosCtrlRateLimitPercent_Type.__name__ = "Integer32"
_A3ComQosCtrlRateLimitPercent_Object = MibTableColumn
a3ComQosCtrlRateLimitPercent = _A3ComQosCtrlRateLimitPercent_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1, 3),
    _A3ComQosCtrlRateLimitPercent_Type()
)
a3ComQosCtrlRateLimitPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitPercent.setStatus("mandatory")


class _A3ComQosCtrlRateLimitKbps_Type(Integer32):
    """Custom type a3ComQosCtrlRateLimitKbps based on Integer32"""
    defaultValue = -1


_A3ComQosCtrlRateLimitKbps_Object = MibTableColumn
a3ComQosCtrlRateLimitKbps = _A3ComQosCtrlRateLimitKbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1, 4),
    _A3ComQosCtrlRateLimitKbps_Type()
)
a3ComQosCtrlRateLimitKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitKbps.setStatus("mandatory")


class _A3ComQosCtrlRateLimitPorts_Type(OctetString):
    """Custom type a3ComQosCtrlRateLimitPorts based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_A3ComQosCtrlRateLimitPorts_Type.__name__ = "OctetString"
_A3ComQosCtrlRateLimitPorts_Object = MibTableColumn
a3ComQosCtrlRateLimitPorts = _A3ComQosCtrlRateLimitPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1, 5),
    _A3ComQosCtrlRateLimitPorts_Type()
)
a3ComQosCtrlRateLimitPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitPorts.setStatus("mandatory")
_A3ComQosCtrlRateLimitRowStatus_Type = RowStatus
_A3ComQosCtrlRateLimitRowStatus_Object = MibTableColumn
a3ComQosCtrlRateLimitRowStatus = _A3ComQosCtrlRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 2, 2, 1, 6),
    _A3ComQosCtrlRateLimitRowStatus_Type()
)
a3ComQosCtrlRateLimitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosCtrlRateLimitRowStatus.setStatus("mandatory")
_A3ComQosRsvp_ObjectIdentity = ObjectIdentity
a3ComQosRsvp = _A3ComQosRsvp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3)
)


class _A3ComQosRsvpStatus_Type(Integer32):
    """Custom type a3ComQosRsvpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsvpDisabled", 2),
          ("rsvpEnabled", 1))
    )


_A3ComQosRsvpStatus_Type.__name__ = "Integer32"
_A3ComQosRsvpStatus_Object = MibScalar
a3ComQosRsvpStatus = _A3ComQosRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 1),
    _A3ComQosRsvpStatus_Type()
)
a3ComQosRsvpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpStatus.setStatus("mandatory")


class _A3ComQosRsvpMaxTotalResvdBandwidth_Type(Integer32):
    """Custom type a3ComQosRsvpMaxTotalResvdBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_A3ComQosRsvpMaxTotalResvdBandwidth_Type.__name__ = "Integer32"
_A3ComQosRsvpMaxTotalResvdBandwidth_Object = MibScalar
a3ComQosRsvpMaxTotalResvdBandwidth = _A3ComQosRsvpMaxTotalResvdBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 2),
    _A3ComQosRsvpMaxTotalResvdBandwidth_Type()
)
a3ComQosRsvpMaxTotalResvdBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpMaxTotalResvdBandwidth.setStatus("mandatory")


class _A3ComQosRsvpMaxPerResvBandwidth_Type(Integer32):
    """Custom type a3ComQosRsvpMaxPerResvBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_A3ComQosRsvpMaxPerResvBandwidth_Type.__name__ = "Integer32"
_A3ComQosRsvpMaxPerResvBandwidth_Object = MibScalar
a3ComQosRsvpMaxPerResvBandwidth = _A3ComQosRsvpMaxPerResvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 3),
    _A3ComQosRsvpMaxPerResvBandwidth_Type()
)
a3ComQosRsvpMaxPerResvBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpMaxPerResvBandwidth.setStatus("mandatory")


class _A3ComQosRsvpPolicy_Type(Integer32):
    """Custom type a3ComQosRsvpPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("edge", 1),
          ("never", 3))
    )


_A3ComQosRsvpPolicy_Type.__name__ = "Integer32"
_A3ComQosRsvpPolicy_Object = MibScalar
a3ComQosRsvpPolicy = _A3ComQosRsvpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 4),
    _A3ComQosRsvpPolicy_Type()
)
a3ComQosRsvpPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpPolicy.setStatus("mandatory")


class _A3ComQosRsvpExcessTrafficPolicy_Type(Integer32):
    """Custom type a3ComQosRsvpExcessTrafficPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("lowPriority", 2))
    )


_A3ComQosRsvpExcessTrafficPolicy_Type.__name__ = "Integer32"
_A3ComQosRsvpExcessTrafficPolicy_Object = MibScalar
a3ComQosRsvpExcessTrafficPolicy = _A3ComQosRsvpExcessTrafficPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 5),
    _A3ComQosRsvpExcessTrafficPolicy_Type()
)
a3ComQosRsvpExcessTrafficPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpExcessTrafficPolicy.setStatus("mandatory")


class _A3ComQosRsvpExcessPktsLossEligible_Type(Integer32):
    """Custom type a3ComQosRsvpExcessPktsLossEligible based on Integer32"""
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


_A3ComQosRsvpExcessPktsLossEligible_Type.__name__ = "Integer32"
_A3ComQosRsvpExcessPktsLossEligible_Object = MibScalar
a3ComQosRsvpExcessPktsLossEligible = _A3ComQosRsvpExcessPktsLossEligible_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 6),
    _A3ComQosRsvpExcessPktsLossEligible_Type()
)
a3ComQosRsvpExcessPktsLossEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpExcessPktsLossEligible.setStatus("mandatory")


class _A3ComQosRsvpAuthentication_Type(Integer32):
    """Custom type a3ComQosRsvpAuthentication based on Integer32"""
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


_A3ComQosRsvpAuthentication_Type.__name__ = "Integer32"
_A3ComQosRsvpAuthentication_Object = MibScalar
a3ComQosRsvpAuthentication = _A3ComQosRsvpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 7),
    _A3ComQosRsvpAuthentication_Type()
)
a3ComQosRsvpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpAuthentication.setStatus("mandatory")


class _A3ComQosRsvpMd5Key_Type(OctetString):
    """Custom type a3ComQosRsvpMd5Key based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_A3ComQosRsvpMd5Key_Type.__name__ = "OctetString"
_A3ComQosRsvpMd5Key_Object = MibScalar
a3ComQosRsvpMd5Key = _A3ComQosRsvpMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 3, 8),
    _A3ComQosRsvpMd5Key_Type()
)
a3ComQosRsvpMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosRsvpMd5Key.setStatus("mandatory")
_A3ComQosStats_ObjectIdentity = ObjectIdentity
a3ComQosStats = _A3ComQosStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4)
)


class _A3ComQosStatsInterval_Type(Integer32):
    """Custom type a3ComQosStatsInterval based on Integer32"""
    defaultValue = 1


_A3ComQosStatsInterval_Object = MibScalar
a3ComQosStatsInterval = _A3ComQosStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 1),
    _A3ComQosStatsInterval_Type()
)
a3ComQosStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosStatsInterval.setStatus("mandatory")
_A3ComQosXmtStatsTable_Object = MibTable
a3ComQosXmtStatsTable = _A3ComQosXmtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2)
)
if mibBuilder.loadTexts:
    a3ComQosXmtStatsTable.setStatus("mandatory")
_A3ComQosXmtStatsEntry_Object = MibTableRow
a3ComQosXmtStatsEntry = _A3ComQosXmtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1)
)
a3ComQosXmtStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosXmtStatsQindex"),
)
if mibBuilder.loadTexts:
    a3ComQosXmtStatsEntry.setStatus("mandatory")


class _A3ComQosXmtStatsQindex_Type(Integer32):
    """Custom type a3ComQosXmtStatsQindex based on Integer32"""
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
        *(("bestEffort", 3),
          ("highPriority", 2),
          ("lowPriority", 4),
          ("reserved", 1))
    )


_A3ComQosXmtStatsQindex_Type.__name__ = "Integer32"
_A3ComQosXmtStatsQindex_Object = MibTableColumn
a3ComQosXmtStatsQindex = _A3ComQosXmtStatsQindex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1, 1),
    _A3ComQosXmtStatsQindex_Type()
)
a3ComQosXmtStatsQindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtStatsQindex.setStatus("mandatory")
_A3ComQosXmtStatsLowLossPkts_Type = Gauge32
_A3ComQosXmtStatsLowLossPkts_Object = MibTableColumn
a3ComQosXmtStatsLowLossPkts = _A3ComQosXmtStatsLowLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1, 2),
    _A3ComQosXmtStatsLowLossPkts_Type()
)
a3ComQosXmtStatsLowLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtStatsLowLossPkts.setStatus("mandatory")
_A3ComQosXmtStatsLowLossDelayedPkts_Type = Gauge32
_A3ComQosXmtStatsLowLossDelayedPkts_Object = MibTableColumn
a3ComQosXmtStatsLowLossDelayedPkts = _A3ComQosXmtStatsLowLossDelayedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1, 3),
    _A3ComQosXmtStatsLowLossDelayedPkts_Type()
)
a3ComQosXmtStatsLowLossDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtStatsLowLossDelayedPkts.setStatus("mandatory")
_A3ComQosXmtStatsLowLossDiscardedPkts_Type = Gauge32
_A3ComQosXmtStatsLowLossDiscardedPkts_Object = MibTableColumn
a3ComQosXmtStatsLowLossDiscardedPkts = _A3ComQosXmtStatsLowLossDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1, 4),
    _A3ComQosXmtStatsLowLossDiscardedPkts_Type()
)
a3ComQosXmtStatsLowLossDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtStatsLowLossDiscardedPkts.setStatus("mandatory")
_A3ComQosXmtStatsHighLossPkts_Type = Gauge32
_A3ComQosXmtStatsHighLossPkts_Object = MibTableColumn
a3ComQosXmtStatsHighLossPkts = _A3ComQosXmtStatsHighLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1, 5),
    _A3ComQosXmtStatsHighLossPkts_Type()
)
a3ComQosXmtStatsHighLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtStatsHighLossPkts.setStatus("mandatory")
_A3ComQosXmtStatsHighLossDiscardedPkts_Type = Gauge32
_A3ComQosXmtStatsHighLossDiscardedPkts_Object = MibTableColumn
a3ComQosXmtStatsHighLossDiscardedPkts = _A3ComQosXmtStatsHighLossDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 2, 1, 6),
    _A3ComQosXmtStatsHighLossDiscardedPkts_Type()
)
a3ComQosXmtStatsHighLossDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtStatsHighLossDiscardedPkts.setStatus("mandatory")
_A3ComQosXmtHmStatsTable_Object = MibTable
a3ComQosXmtHmStatsTable = _A3ComQosXmtHmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3)
)
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsTable.setStatus("mandatory")
_A3ComQosXmtHmStatsEntry_Object = MibTableRow
a3ComQosXmtHmStatsEntry = _A3ComQosXmtHmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1)
)
a3ComQosXmtHmStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosXmtHmStatsQindex"),
)
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsEntry.setStatus("mandatory")


class _A3ComQosXmtHmStatsQindex_Type(Integer32):
    """Custom type a3ComQosXmtHmStatsQindex based on Integer32"""
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
        *(("bestEffort", 3),
          ("highPriority", 2),
          ("lowPriority", 4),
          ("reserved", 1))
    )


_A3ComQosXmtHmStatsQindex_Type.__name__ = "Integer32"
_A3ComQosXmtHmStatsQindex_Object = MibTableColumn
a3ComQosXmtHmStatsQindex = _A3ComQosXmtHmStatsQindex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1, 1),
    _A3ComQosXmtHmStatsQindex_Type()
)
a3ComQosXmtHmStatsQindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsQindex.setStatus("mandatory")
_A3ComQosXmtHmStatsLowLossPkts_Type = Gauge32
_A3ComQosXmtHmStatsLowLossPkts_Object = MibTableColumn
a3ComQosXmtHmStatsLowLossPkts = _A3ComQosXmtHmStatsLowLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1, 2),
    _A3ComQosXmtHmStatsLowLossPkts_Type()
)
a3ComQosXmtHmStatsLowLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsLowLossPkts.setStatus("mandatory")
_A3ComQosXmtHmStatsLowLossDelayedPkts_Type = Gauge32
_A3ComQosXmtHmStatsLowLossDelayedPkts_Object = MibTableColumn
a3ComQosXmtHmStatsLowLossDelayedPkts = _A3ComQosXmtHmStatsLowLossDelayedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1, 3),
    _A3ComQosXmtHmStatsLowLossDelayedPkts_Type()
)
a3ComQosXmtHmStatsLowLossDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsLowLossDelayedPkts.setStatus("mandatory")
_A3ComQosXmtHmStatsLowLossDiscardedPkts_Type = Gauge32
_A3ComQosXmtHmStatsLowLossDiscardedPkts_Object = MibTableColumn
a3ComQosXmtHmStatsLowLossDiscardedPkts = _A3ComQosXmtHmStatsLowLossDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1, 4),
    _A3ComQosXmtHmStatsLowLossDiscardedPkts_Type()
)
a3ComQosXmtHmStatsLowLossDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsLowLossDiscardedPkts.setStatus("mandatory")
_A3ComQosXmtHmStatsHighLossPkts_Type = Gauge32
_A3ComQosXmtHmStatsHighLossPkts_Object = MibTableColumn
a3ComQosXmtHmStatsHighLossPkts = _A3ComQosXmtHmStatsHighLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1, 5),
    _A3ComQosXmtHmStatsHighLossPkts_Type()
)
a3ComQosXmtHmStatsHighLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsHighLossPkts.setStatus("mandatory")
_A3ComQosXmtHmStatsHighLossDiscardedPkts_Type = Gauge32
_A3ComQosXmtHmStatsHighLossDiscardedPkts_Object = MibTableColumn
a3ComQosXmtHmStatsHighLossDiscardedPkts = _A3ComQosXmtHmStatsHighLossDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 3, 1, 6),
    _A3ComQosXmtHmStatsHighLossDiscardedPkts_Type()
)
a3ComQosXmtHmStatsHighLossDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosXmtHmStatsHighLossDiscardedPkts.setStatus("mandatory")
_A3ComQosRcvStatsTable_Object = MibTable
a3ComQosRcvStatsTable = _A3ComQosRcvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 4)
)
if mibBuilder.loadTexts:
    a3ComQosRcvStatsTable.setStatus("mandatory")
_A3ComQosRcvStatsEntry_Object = MibTableRow
a3ComQosRcvStatsEntry = _A3ComQosRcvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 4, 1)
)
a3ComQosRcvStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    a3ComQosRcvStatsEntry.setStatus("mandatory")
_A3ComQosRcvStatsConformBytesTotal_Type = Gauge32
_A3ComQosRcvStatsConformBytesTotal_Object = MibTableColumn
a3ComQosRcvStatsConformBytesTotal = _A3ComQosRcvStatsConformBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 4, 1, 1),
    _A3ComQosRcvStatsConformBytesTotal_Type()
)
a3ComQosRcvStatsConformBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosRcvStatsConformBytesTotal.setStatus("mandatory")
_A3ComQosRcvStatsNonConformBytesForFlows_Type = Gauge32
_A3ComQosRcvStatsNonConformBytesForFlows_Object = MibTableColumn
a3ComQosRcvStatsNonConformBytesForFlows = _A3ComQosRcvStatsNonConformBytesForFlows_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 4, 1, 2),
    _A3ComQosRcvStatsNonConformBytesForFlows_Type()
)
a3ComQosRcvStatsNonConformBytesForFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosRcvStatsNonConformBytesForFlows.setStatus("mandatory")
_A3ComQosRcvStatsNonConformBytesForNonFlows_Type = Gauge32
_A3ComQosRcvStatsNonConformBytesForNonFlows_Object = MibTableColumn
a3ComQosRcvStatsNonConformBytesForNonFlows = _A3ComQosRcvStatsNonConformBytesForNonFlows_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 4, 1, 3),
    _A3ComQosRcvStatsNonConformBytesForNonFlows_Type()
)
a3ComQosRcvStatsNonConformBytesForNonFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosRcvStatsNonConformBytesForNonFlows.setStatus("mandatory")
_A3ComQosRcvStatsDroppedPkts_Type = Gauge32
_A3ComQosRcvStatsDroppedPkts_Object = MibTableColumn
a3ComQosRcvStatsDroppedPkts = _A3ComQosRcvStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 4, 4, 1, 4),
    _A3ComQosRcvStatsDroppedPkts_Type()
)
a3ComQosRcvStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQosRcvStatsDroppedPkts.setStatus("mandatory")
_A3ComQosMisc_ObjectIdentity = ObjectIdentity
a3ComQosMisc = _A3ComQosMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 5)
)


class _A3ComQosBandwidthRatio_Type(Integer32):
    """Custom type a3ComQosBandwidthRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_A3ComQosBandwidthRatio_Type.__name__ = "Integer32"
_A3ComQosBandwidthRatio_Object = MibScalar
a3ComQosBandwidthRatio = _A3ComQosBandwidthRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 5, 1),
    _A3ComQosBandwidthRatio_Type()
)
a3ComQosBandwidthRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosBandwidthRatio.setStatus("mandatory")


class _A3ComQosExcessTrafficClassTag_Type(Integer32):
    """Custom type a3ComQosExcessTrafficClassTag based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021pTag0", 2),
          ("ieee8021pTag1", 3),
          ("ieee8021pTag2", 4),
          ("ieee8021pTag3", 5),
          ("ieee8021pTag4", 6),
          ("ieee8021pTag5", 7),
          ("ieee8021pTag6", 8),
          ("ieee8021pTag7", 9),
          ("none", 1))
    )


_A3ComQosExcessTrafficClassTag_Type.__name__ = "Integer32"
_A3ComQosExcessTrafficClassTag_Object = MibScalar
a3ComQosExcessTrafficClassTag = _A3ComQosExcessTrafficClassTag_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 21, 5, 2),
    _A3ComQosExcessTrafficClassTag_Type()
)
a3ComQosExcessTrafficClassTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQosExcessTrafficClassTag.setStatus("mandatory")

# Managed Objects groups


# Notification objects

a3ComQosFlowClassIntrudingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 88)
)
a3ComQosFlowClassIntrudingEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosFlowClassIndex"),
        ("A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosFlowClassIpProtoType"),
        ("A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosFlowClassSrcAddr"),
        ("A3COM-SWITCHING-SYSTEMS-QOS-MIB", "a3ComQosFlowClassDestAddr"))
)
if mibBuilder.loadTexts:
    a3ComQosFlowClassIntrudingEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-QOS-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComQosFlowClassIntrudingEvent": a3ComQosFlowClassIntrudingEvent,
       "a3ComQos": a3ComQos,
       "a3ComQosClass": a3ComQosClass,
       "a3ComQosGenClassTable": a3ComQosGenClassTable,
       "a3ComQosGenClassEntry": a3ComQosGenClassEntry,
       "a3ComQosGenClassIndex": a3ComQosGenClassIndex,
       "a3ComQosGenClassName": a3ComQosGenClassName,
       "a3ComQosGenClassControlId": a3ComQosGenClassControlId,
       "a3ComQosFlowClassTable": a3ComQosFlowClassTable,
       "a3ComQosFlowClassEntry": a3ComQosFlowClassEntry,
       "a3ComQosFlowClassIndex": a3ComQosFlowClassIndex,
       "a3ComQosFlowClassFilterIndex": a3ComQosFlowClassFilterIndex,
       "a3ComQosFlowClassCastType": a3ComQosFlowClassCastType,
       "a3ComQosFlowClassIpProtoType": a3ComQosFlowClassIpProtoType,
       "a3ComQosFlowClassSrcAddr": a3ComQosFlowClassSrcAddr,
       "a3ComQosFlowClassSrcSubnetMask": a3ComQosFlowClassSrcSubnetMask,
       "a3ComQosFlowClassDestAddr": a3ComQosFlowClassDestAddr,
       "a3ComQosFlowClassDestSubnetMask": a3ComQosFlowClassDestSubnetMask,
       "a3ComQosFlowClassPortStart": a3ComQosFlowClassPortStart,
       "a3ComQosFlowClassPortEnd": a3ComQosFlowClassPortEnd,
       "a3ComQosFlowClassRowStatus": a3ComQosFlowClassRowStatus,
       "a3ComQosNonFlowClassTable": a3ComQosNonFlowClassTable,
       "a3ComQosNonFlowClassEntry": a3ComQosNonFlowClassEntry,
       "a3ComQosNonFlowClassIndex": a3ComQosNonFlowClassIndex,
       "a3ComQosNonFlowClassCastType": a3ComQosNonFlowClassCastType,
       "a3ComQosNonFlowClassProtos": a3ComQosNonFlowClassProtos,
       "a3ComQosNonFlowClass8021pTags": a3ComQosNonFlowClass8021pTags,
       "a3ComQosNonFlowClassRowStatus": a3ComQosNonFlowClassRowStatus,
       "a3ComQosNonFlowClassProtoDescriptor": a3ComQosNonFlowClassProtoDescriptor,
       "a3ComQosNonFlowClassCustomProto": a3ComQosNonFlowClassCustomProto,
       "a3ComQosCtrl": a3ComQosCtrl,
       "a3ComQosCtrlTable": a3ComQosCtrlTable,
       "a3ComQosCtrlEntry": a3ComQosCtrlEntry,
       "a3ComQosCtrlIndex": a3ComQosCtrlIndex,
       "a3ComQosCtrlName": a3ComQosCtrlName,
       "a3ComQosCtrlServiceLevel": a3ComQosCtrlServiceLevel,
       "a3ComQosCtrlConformPktsLossEligible": a3ComQosCtrlConformPktsLossEligible,
       "a3ComQosCtrlExcessPktsServiceLevel": a3ComQosCtrlExcessPktsServiceLevel,
       "a3ComQosCtrlExcessPktsLossEligible": a3ComQosCtrlExcessPktsLossEligible,
       "a3ComQosCtrl8021pTag": a3ComQosCtrl8021pTag,
       "a3ComQosCtrlRateLimitType": a3ComQosCtrlRateLimitType,
       "a3ComQosCtrlRowStatus": a3ComQosCtrlRowStatus,
       "a3ComQosCtrlRateLimitTable": a3ComQosCtrlRateLimitTable,
       "a3ComQosCtrlRateLimitEntry": a3ComQosCtrlRateLimitEntry,
       "a3ComQosCtrlRateLimitCtrlIndex": a3ComQosCtrlRateLimitCtrlIndex,
       "a3ComQosCtrlRateLimitIndex": a3ComQosCtrlRateLimitIndex,
       "a3ComQosCtrlRateLimitPercent": a3ComQosCtrlRateLimitPercent,
       "a3ComQosCtrlRateLimitKbps": a3ComQosCtrlRateLimitKbps,
       "a3ComQosCtrlRateLimitPorts": a3ComQosCtrlRateLimitPorts,
       "a3ComQosCtrlRateLimitRowStatus": a3ComQosCtrlRateLimitRowStatus,
       "a3ComQosRsvp": a3ComQosRsvp,
       "a3ComQosRsvpStatus": a3ComQosRsvpStatus,
       "a3ComQosRsvpMaxTotalResvdBandwidth": a3ComQosRsvpMaxTotalResvdBandwidth,
       "a3ComQosRsvpMaxPerResvBandwidth": a3ComQosRsvpMaxPerResvBandwidth,
       "a3ComQosRsvpPolicy": a3ComQosRsvpPolicy,
       "a3ComQosRsvpExcessTrafficPolicy": a3ComQosRsvpExcessTrafficPolicy,
       "a3ComQosRsvpExcessPktsLossEligible": a3ComQosRsvpExcessPktsLossEligible,
       "a3ComQosRsvpAuthentication": a3ComQosRsvpAuthentication,
       "a3ComQosRsvpMd5Key": a3ComQosRsvpMd5Key,
       "a3ComQosStats": a3ComQosStats,
       "a3ComQosStatsInterval": a3ComQosStatsInterval,
       "a3ComQosXmtStatsTable": a3ComQosXmtStatsTable,
       "a3ComQosXmtStatsEntry": a3ComQosXmtStatsEntry,
       "a3ComQosXmtStatsQindex": a3ComQosXmtStatsQindex,
       "a3ComQosXmtStatsLowLossPkts": a3ComQosXmtStatsLowLossPkts,
       "a3ComQosXmtStatsLowLossDelayedPkts": a3ComQosXmtStatsLowLossDelayedPkts,
       "a3ComQosXmtStatsLowLossDiscardedPkts": a3ComQosXmtStatsLowLossDiscardedPkts,
       "a3ComQosXmtStatsHighLossPkts": a3ComQosXmtStatsHighLossPkts,
       "a3ComQosXmtStatsHighLossDiscardedPkts": a3ComQosXmtStatsHighLossDiscardedPkts,
       "a3ComQosXmtHmStatsTable": a3ComQosXmtHmStatsTable,
       "a3ComQosXmtHmStatsEntry": a3ComQosXmtHmStatsEntry,
       "a3ComQosXmtHmStatsQindex": a3ComQosXmtHmStatsQindex,
       "a3ComQosXmtHmStatsLowLossPkts": a3ComQosXmtHmStatsLowLossPkts,
       "a3ComQosXmtHmStatsLowLossDelayedPkts": a3ComQosXmtHmStatsLowLossDelayedPkts,
       "a3ComQosXmtHmStatsLowLossDiscardedPkts": a3ComQosXmtHmStatsLowLossDiscardedPkts,
       "a3ComQosXmtHmStatsHighLossPkts": a3ComQosXmtHmStatsHighLossPkts,
       "a3ComQosXmtHmStatsHighLossDiscardedPkts": a3ComQosXmtHmStatsHighLossDiscardedPkts,
       "a3ComQosRcvStatsTable": a3ComQosRcvStatsTable,
       "a3ComQosRcvStatsEntry": a3ComQosRcvStatsEntry,
       "a3ComQosRcvStatsConformBytesTotal": a3ComQosRcvStatsConformBytesTotal,
       "a3ComQosRcvStatsNonConformBytesForFlows": a3ComQosRcvStatsNonConformBytesForFlows,
       "a3ComQosRcvStatsNonConformBytesForNonFlows": a3ComQosRcvStatsNonConformBytesForNonFlows,
       "a3ComQosRcvStatsDroppedPkts": a3ComQosRcvStatsDroppedPkts,
       "a3ComQosMisc": a3ComQosMisc,
       "a3ComQosBandwidthRatio": a3ComQosBandwidthRatio,
       "a3ComQosExcessTrafficClassTag": a3ComQosExcessTrafficClassTag}
)
