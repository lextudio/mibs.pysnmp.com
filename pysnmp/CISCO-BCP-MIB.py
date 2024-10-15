# SNMP MIB module (CISCO-BCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:14 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoBcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 275)
)
ciscoBcpMIB.setRevisions(
        ("2004-08-31 00:00",
         "2002-08-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBcpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBcpMIBObjects = _CiscoBcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1)
)
_BcpOperTable_Object = MibTable
bcpOperTable = _BcpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 1)
)
if mibBuilder.loadTexts:
    bcpOperTable.setStatus("current")
_BcpOperEntry_Object = MibTableRow
bcpOperEntry = _BcpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 1, 1)
)
bcpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bcpOperEntry.setStatus("current")


class _BcpOperStatus_Type(Integer32):
    """Custom type bcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("listening", 3),
          ("open", 1))
    )


_BcpOperStatus_Type.__name__ = "Integer32"
_BcpOperStatus_Object = MibTableColumn
bcpOperStatus = _BcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 1, 1, 1),
    _BcpOperStatus_Type()
)
bcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcpOperStatus.setStatus("current")
_BcpConfigTable_Object = MibTable
bcpConfigTable = _BcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2)
)
if mibBuilder.loadTexts:
    bcpConfigTable.setStatus("current")
_BcpConfigEntry_Object = MibTableRow
bcpConfigEntry = _BcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1)
)
bcpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bcpConfigEntry.setStatus("current")


class _BcpConfigBridgeIdControl_Type(Integer32):
    """Custom type bcpConfigBridgeIdControl based on Integer32"""
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


_BcpConfigBridgeIdControl_Type.__name__ = "Integer32"
_BcpConfigBridgeIdControl_Object = MibTableColumn
bcpConfigBridgeIdControl = _BcpConfigBridgeIdControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 1),
    _BcpConfigBridgeIdControl_Type()
)
bcpConfigBridgeIdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigBridgeIdControl.setStatus("current")


class _BcpConfigBridgeId_Type(Unsigned32):
    """Custom type bcpConfigBridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BcpConfigBridgeId_Type.__name__ = "Unsigned32"
_BcpConfigBridgeId_Object = MibTableColumn
bcpConfigBridgeId = _BcpConfigBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 2),
    _BcpConfigBridgeId_Type()
)
bcpConfigBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigBridgeId.setStatus("current")


class _BcpConfigLineIdControl_Type(Integer32):
    """Custom type bcpConfigLineIdControl based on Integer32"""
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


_BcpConfigLineIdControl_Type.__name__ = "Integer32"
_BcpConfigLineIdControl_Object = MibTableColumn
bcpConfigLineIdControl = _BcpConfigLineIdControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 3),
    _BcpConfigLineIdControl_Type()
)
bcpConfigLineIdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigLineIdControl.setStatus("current")


class _BcpConfigLineId_Type(Unsigned32):
    """Custom type bcpConfigLineId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BcpConfigLineId_Type.__name__ = "Unsigned32"
_BcpConfigLineId_Object = MibTableColumn
bcpConfigLineId = _BcpConfigLineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 4),
    _BcpConfigLineId_Type()
)
bcpConfigLineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigLineId.setStatus("current")


class _BcpConfigMacSupport_Type(Integer32):
    """Custom type bcpConfigMacSupport based on Integer32"""
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


_BcpConfigMacSupport_Type.__name__ = "Integer32"
_BcpConfigMacSupport_Object = MibTableColumn
bcpConfigMacSupport = _BcpConfigMacSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 5),
    _BcpConfigMacSupport_Type()
)
bcpConfigMacSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigMacSupport.setStatus("current")


class _BcpConfigMacType_Type(Integer32):
    """Custom type bcpConfigMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("fddiCanonical", 12),
          ("fddiNonCanonical", 4),
          ("ieee802dot3Canonical", 1),
          ("ieee802dot4Canonical", 2),
          ("ieee802dot5Canonical", 11),
          ("ieee802dot5NonCanonical", 3))
    )


_BcpConfigMacType_Type.__name__ = "Integer32"
_BcpConfigMacType_Object = MibTableColumn
bcpConfigMacType = _BcpConfigMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 6),
    _BcpConfigMacType_Type()
)
bcpConfigMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigMacType.setStatus("current")


class _BcpConfigTinygram_Type(Integer32):
    """Custom type bcpConfigTinygram based on Integer32"""
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


_BcpConfigTinygram_Type.__name__ = "Integer32"
_BcpConfigTinygram_Object = MibTableColumn
bcpConfigTinygram = _BcpConfigTinygram_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 7),
    _BcpConfigTinygram_Type()
)
bcpConfigTinygram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigTinygram.setStatus("current")


class _BcpConfigMacAddressControl_Type(Integer32):
    """Custom type bcpConfigMacAddressControl based on Integer32"""
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


_BcpConfigMacAddressControl_Type.__name__ = "Integer32"
_BcpConfigMacAddressControl_Object = MibTableColumn
bcpConfigMacAddressControl = _BcpConfigMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 8),
    _BcpConfigMacAddressControl_Type()
)
bcpConfigMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigMacAddressControl.setStatus("current")


class _BcpConfigMacAddress_Type(DisplayString):
    """Custom type bcpConfigMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BcpConfigMacAddress_Type.__name__ = "DisplayString"
_BcpConfigMacAddress_Object = MibTableColumn
bcpConfigMacAddress = _BcpConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 9),
    _BcpConfigMacAddress_Type()
)
bcpConfigMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigMacAddress.setStatus("current")


class _BcpConfigSpanTreeControl_Type(Integer32):
    """Custom type bcpConfigSpanTreeControl based on Integer32"""
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


_BcpConfigSpanTreeControl_Type.__name__ = "Integer32"
_BcpConfigSpanTreeControl_Object = MibTableColumn
bcpConfigSpanTreeControl = _BcpConfigSpanTreeControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 10),
    _BcpConfigSpanTreeControl_Type()
)
bcpConfigSpanTreeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigSpanTreeControl.setStatus("current")


class _BcpConfigSpanTree_Type(Integer32):
    """Custom type bcpConfigSpanTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("decLanBridge100", 4),
          ("ibmSourceRoute", 3),
          ("ieee802dot1D", 1),
          ("ieee802dot1GExtended", 2),
          ("null", 0))
    )


_BcpConfigSpanTree_Type.__name__ = "Integer32"
_BcpConfigSpanTree_Object = MibTableColumn
bcpConfigSpanTree = _BcpConfigSpanTree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 11),
    _BcpConfigSpanTree_Type()
)
bcpConfigSpanTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigSpanTree.setStatus("current")


class _BcpConfigIeee802dot1qTagged_Type(Integer32):
    """Custom type bcpConfigIeee802dot1qTagged based on Integer32"""
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


_BcpConfigIeee802dot1qTagged_Type.__name__ = "Integer32"
_BcpConfigIeee802dot1qTagged_Object = MibTableColumn
bcpConfigIeee802dot1qTagged = _BcpConfigIeee802dot1qTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 12),
    _BcpConfigIeee802dot1qTagged_Type()
)
bcpConfigIeee802dot1qTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigIeee802dot1qTagged.setStatus("current")


class _BcpConfigMgmtInline_Type(Integer32):
    """Custom type bcpConfigMgmtInline based on Integer32"""
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


_BcpConfigMgmtInline_Type.__name__ = "Integer32"
_BcpConfigMgmtInline_Object = MibTableColumn
bcpConfigMgmtInline = _BcpConfigMgmtInline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 13),
    _BcpConfigMgmtInline_Type()
)
bcpConfigMgmtInline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigMgmtInline.setStatus("current")


class _BcpConfigBCPacketIndicator_Type(Integer32):
    """Custom type bcpConfigBCPacketIndicator based on Integer32"""
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


_BcpConfigBCPacketIndicator_Type.__name__ = "Integer32"
_BcpConfigBCPacketIndicator_Object = MibTableColumn
bcpConfigBCPacketIndicator = _BcpConfigBCPacketIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 1, 2, 1, 14),
    _BcpConfigBCPacketIndicator_Type()
)
bcpConfigBCPacketIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcpConfigBCPacketIndicator.setStatus("current")
_CBcpMIBConformance_ObjectIdentity = ObjectIdentity
cBcpMIBConformance = _CBcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 3)
)
_CBcpMIBCompliances_ObjectIdentity = ObjectIdentity
cBcpMIBCompliances = _CBcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 3, 1)
)
_CBcpMIBGroups_ObjectIdentity = ObjectIdentity
cBcpMIBGroups = _CBcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 3, 2)
)

# Managed Objects groups

cBcpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 3, 2, 1)
)
cBcpMIBGroup.setObjects(
      *(("CISCO-BCP-MIB", "bcpOperStatus"),
        ("CISCO-BCP-MIB", "bcpConfigBridgeIdControl"),
        ("CISCO-BCP-MIB", "bcpConfigBridgeId"),
        ("CISCO-BCP-MIB", "bcpConfigLineIdControl"),
        ("CISCO-BCP-MIB", "bcpConfigLineId"),
        ("CISCO-BCP-MIB", "bcpConfigMacSupport"),
        ("CISCO-BCP-MIB", "bcpConfigMacType"),
        ("CISCO-BCP-MIB", "bcpConfigTinygram"),
        ("CISCO-BCP-MIB", "bcpConfigMacAddressControl"),
        ("CISCO-BCP-MIB", "bcpConfigMacAddress"),
        ("CISCO-BCP-MIB", "bcpConfigSpanTreeControl"),
        ("CISCO-BCP-MIB", "bcpConfigSpanTree"),
        ("CISCO-BCP-MIB", "bcpConfigIeee802dot1qTagged"),
        ("CISCO-BCP-MIB", "bcpConfigMgmtInline"),
        ("CISCO-BCP-MIB", "bcpConfigBCPacketIndicator"))
)
if mibBuilder.loadTexts:
    cBcpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cBcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 275, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cBcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BCP-MIB",
    **{"ciscoBcpMIB": ciscoBcpMIB,
       "ciscoBcpMIBObjects": ciscoBcpMIBObjects,
       "bcpOperTable": bcpOperTable,
       "bcpOperEntry": bcpOperEntry,
       "bcpOperStatus": bcpOperStatus,
       "bcpConfigTable": bcpConfigTable,
       "bcpConfigEntry": bcpConfigEntry,
       "bcpConfigBridgeIdControl": bcpConfigBridgeIdControl,
       "bcpConfigBridgeId": bcpConfigBridgeId,
       "bcpConfigLineIdControl": bcpConfigLineIdControl,
       "bcpConfigLineId": bcpConfigLineId,
       "bcpConfigMacSupport": bcpConfigMacSupport,
       "bcpConfigMacType": bcpConfigMacType,
       "bcpConfigTinygram": bcpConfigTinygram,
       "bcpConfigMacAddressControl": bcpConfigMacAddressControl,
       "bcpConfigMacAddress": bcpConfigMacAddress,
       "bcpConfigSpanTreeControl": bcpConfigSpanTreeControl,
       "bcpConfigSpanTree": bcpConfigSpanTree,
       "bcpConfigIeee802dot1qTagged": bcpConfigIeee802dot1qTagged,
       "bcpConfigMgmtInline": bcpConfigMgmtInline,
       "bcpConfigBCPacketIndicator": bcpConfigBCPacketIndicator,
       "cBcpMIBConformance": cBcpMIBConformance,
       "cBcpMIBCompliances": cBcpMIBCompliances,
       "cBcpMIBCompliance": cBcpMIBCompliance,
       "cBcpMIBGroups": cBcpMIBGroups,
       "cBcpMIBGroup": cBcpMIBGroup}
)
