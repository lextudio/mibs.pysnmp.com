# SNMP MIB module (V-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/V-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:58 2024
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

(dot1dBasePort,
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBridge")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

vBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 17, 13)
)
vBridgeMIB.setRevisions(
        ("2001-07-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VBridgeMIBObjects_ObjectIdentity = ObjectIdentity
vBridgeMIBObjects = _VBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 13, 1)
)
_Dot1vProtocol_ObjectIdentity = ObjectIdentity
dot1vProtocol = _Dot1vProtocol_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1)
)
_Dot1vProtocolGroupTable_Object = MibTable
dot1vProtocolGroupTable = _Dot1vProtocolGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1vProtocolGroupTable.setStatus("current")
_Dot1vProtocolGroupEntry_Object = MibTableRow
dot1vProtocolGroupEntry = _Dot1vProtocolGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 1, 1)
)
dot1vProtocolGroupEntry.setIndexNames(
    (0, "V-BRIDGE-MIB", "dot1vProtocolTemplateFrameType"),
    (0, "V-BRIDGE-MIB", "dot1vProtocolTemplateProtocolValue"),
)
if mibBuilder.loadTexts:
    dot1vProtocolGroupEntry.setStatus("current")


class _Dot1vProtocolTemplateFrameType_Type(Integer32):
    """Custom type dot1vProtocolTemplateFrameType based on Integer32"""
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
        *(("ethernet", 1),
          ("llcOther", 5),
          ("rfc1042", 2),
          ("snap8021H", 3),
          ("snapOther", 4))
    )


_Dot1vProtocolTemplateFrameType_Type.__name__ = "Integer32"
_Dot1vProtocolTemplateFrameType_Object = MibTableColumn
dot1vProtocolTemplateFrameType = _Dot1vProtocolTemplateFrameType_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 1, 1, 1),
    _Dot1vProtocolTemplateFrameType_Type()
)
dot1vProtocolTemplateFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1vProtocolTemplateFrameType.setStatus("current")


class _Dot1vProtocolTemplateProtocolValue_Type(OctetString):
    """Custom type dot1vProtocolTemplateProtocolValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(5, 5),
    )


_Dot1vProtocolTemplateProtocolValue_Type.__name__ = "OctetString"
_Dot1vProtocolTemplateProtocolValue_Object = MibTableColumn
dot1vProtocolTemplateProtocolValue = _Dot1vProtocolTemplateProtocolValue_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 1, 1, 2),
    _Dot1vProtocolTemplateProtocolValue_Type()
)
dot1vProtocolTemplateProtocolValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1vProtocolTemplateProtocolValue.setStatus("current")


class _Dot1vProtocolGroupId_Type(Integer32):
    """Custom type dot1vProtocolGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dot1vProtocolGroupId_Type.__name__ = "Integer32"
_Dot1vProtocolGroupId_Object = MibTableColumn
dot1vProtocolGroupId = _Dot1vProtocolGroupId_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 1, 1, 3),
    _Dot1vProtocolGroupId_Type()
)
dot1vProtocolGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1vProtocolGroupId.setStatus("current")
_Dot1vProtocolPortTable_Object = MibTable
dot1vProtocolPortTable = _Dot1vProtocolPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot1vProtocolPortTable.setStatus("current")
_Dot1vProtocolPortEntry_Object = MibTableRow
dot1vProtocolPortEntry = _Dot1vProtocolPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 2, 1)
)
dot1vProtocolPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "V-BRIDGE-MIB", "dot1vProtocolPortGroupId"),
)
if mibBuilder.loadTexts:
    dot1vProtocolPortEntry.setStatus("current")


class _Dot1vProtocolPortGroupId_Type(Integer32):
    """Custom type dot1vProtocolPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot1vProtocolPortGroupId_Type.__name__ = "Integer32"
_Dot1vProtocolPortGroupId_Object = MibTableColumn
dot1vProtocolPortGroupId = _Dot1vProtocolPortGroupId_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 2, 1, 1),
    _Dot1vProtocolPortGroupId_Type()
)
dot1vProtocolPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1vProtocolPortGroupId.setStatus("current")


class _Dot1vProtocolPortGroupVid_Type(Integer32):
    """Custom type dot1vProtocolPortGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1vProtocolPortGroupVid_Type.__name__ = "Integer32"
_Dot1vProtocolPortGroupVid_Object = MibTableColumn
dot1vProtocolPortGroupVid = _Dot1vProtocolPortGroupVid_Object(
    (1, 3, 6, 1, 2, 1, 17, 13, 1, 1, 2, 1, 2),
    _Dot1vProtocolPortGroupVid_Type()
)
dot1vProtocolPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1vProtocolPortGroupVid.setStatus("current")
_VBridgeConformance_ObjectIdentity = ObjectIdentity
vBridgeConformance = _VBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 13, 2)
)
_VBridgeGroups_ObjectIdentity = ObjectIdentity
vBridgeGroups = _VBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 13, 2, 1)
)
_VBridgeCompliances_ObjectIdentity = ObjectIdentity
vBridgeCompliances = _VBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 13, 2, 2)
)

# Managed Objects groups

vBridgeDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 13, 2, 1, 1)
)
vBridgeDeviceGroup.setObjects(
    ("V-BRIDGE-MIB", "dot1vProtocolGroupId")
)
if mibBuilder.loadTexts:
    vBridgeDeviceGroup.setStatus("current")

vBridgePortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 13, 2, 1, 2)
)
vBridgePortGroup.setObjects(
    ("V-BRIDGE-MIB", "dot1vProtocolPortGroupVid")
)
if mibBuilder.loadTexts:
    vBridgePortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "V-BRIDGE-MIB",
    **{"vBridgeMIB": vBridgeMIB,
       "vBridgeMIBObjects": vBridgeMIBObjects,
       "dot1vProtocol": dot1vProtocol,
       "dot1vProtocolGroupTable": dot1vProtocolGroupTable,
       "dot1vProtocolGroupEntry": dot1vProtocolGroupEntry,
       "dot1vProtocolTemplateFrameType": dot1vProtocolTemplateFrameType,
       "dot1vProtocolTemplateProtocolValue": dot1vProtocolTemplateProtocolValue,
       "dot1vProtocolGroupId": dot1vProtocolGroupId,
       "dot1vProtocolPortTable": dot1vProtocolPortTable,
       "dot1vProtocolPortEntry": dot1vProtocolPortEntry,
       "dot1vProtocolPortGroupId": dot1vProtocolPortGroupId,
       "dot1vProtocolPortGroupVid": dot1vProtocolPortGroupVid,
       "vBridgeConformance": vBridgeConformance,
       "vBridgeGroups": vBridgeGroups,
       "vBridgeDeviceGroup": vBridgeDeviceGroup,
       "vBridgePortGroup": vBridgePortGroup,
       "vBridgeCompliances": vBridgeCompliances,
       "vBridgeCompliance": vBridgeCompliance}
)
