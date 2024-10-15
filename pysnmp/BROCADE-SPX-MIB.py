# SNMP MIB module (BROCADE-SPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-SPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:33 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

brcdSPXMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40)
)
brcdSPXMIB.setRevisions(
        ("2015-05-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdSPXGlobalObjects_ObjectIdentity = ObjectIdentity
brcdSPXGlobalObjects = _BrcdSPXGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 1)
)


class _BrcdSPXGlobalConfigCBState_Type(Integer32):
    """Custom type brcdSPXGlobalConfigCBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 0))
    )


_BrcdSPXGlobalConfigCBState_Type.__name__ = "Integer32"
_BrcdSPXGlobalConfigCBState_Object = MibScalar
brcdSPXGlobalConfigCBState = _BrcdSPXGlobalConfigCBState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 1, 1),
    _BrcdSPXGlobalConfigCBState_Type()
)
brcdSPXGlobalConfigCBState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXGlobalConfigCBState.setStatus("current")


class _BrcdSPXGlobalConfigPEState_Type(Integer32):
    """Custom type brcdSPXGlobalConfigPEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 0))
    )


_BrcdSPXGlobalConfigPEState_Type.__name__ = "Integer32"
_BrcdSPXGlobalConfigPEState_Object = MibScalar
brcdSPXGlobalConfigPEState = _BrcdSPXGlobalConfigPEState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 1, 2),
    _BrcdSPXGlobalConfigPEState_Type()
)
brcdSPXGlobalConfigPEState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXGlobalConfigPEState.setStatus("current")
_BrcdSPXTableObjects_ObjectIdentity = ObjectIdentity
brcdSPXTableObjects = _BrcdSPXTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2)
)
_BrcdSPXConfigUnitTable_Object = MibTable
brcdSPXConfigUnitTable = _BrcdSPXConfigUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1)
)
if mibBuilder.loadTexts:
    brcdSPXConfigUnitTable.setStatus("current")
_BrcdSPXConfigUnitEntry_Object = MibTableRow
brcdSPXConfigUnitEntry = _BrcdSPXConfigUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1)
)
brcdSPXConfigUnitEntry.setIndexNames(
    (0, "BROCADE-SPX-MIB", "brcdSPXConfigUnitIndex"),
)
if mibBuilder.loadTexts:
    brcdSPXConfigUnitEntry.setStatus("current")
_BrcdSPXConfigUnitIndex_Type = Integer32
_BrcdSPXConfigUnitIndex_Object = MibTableColumn
brcdSPXConfigUnitIndex = _BrcdSPXConfigUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 1),
    _BrcdSPXConfigUnitIndex_Type()
)
brcdSPXConfigUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitIndex.setStatus("current")


class _BrcdSPXConfigUnitPEName_Type(DisplayString):
    """Custom type brcdSPXConfigUnitPEName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrcdSPXConfigUnitPEName_Type.__name__ = "DisplayString"
_BrcdSPXConfigUnitPEName_Object = MibTableColumn
brcdSPXConfigUnitPEName = _BrcdSPXConfigUnitPEName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 2),
    _BrcdSPXConfigUnitPEName_Type()
)
brcdSPXConfigUnitPEName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitPEName.setStatus("current")
_BrcdSPXConfigUnitPESPXPort1_Type = InterfaceIndexOrZero
_BrcdSPXConfigUnitPESPXPort1_Object = MibTableColumn
brcdSPXConfigUnitPESPXPort1 = _BrcdSPXConfigUnitPESPXPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 3),
    _BrcdSPXConfigUnitPESPXPort1_Type()
)
brcdSPXConfigUnitPESPXPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitPESPXPort1.setStatus("current")
_BrcdSPXConfigUnitPESPXPort2_Type = InterfaceIndexOrZero
_BrcdSPXConfigUnitPESPXPort2_Object = MibTableColumn
brcdSPXConfigUnitPESPXPort2 = _BrcdSPXConfigUnitPESPXPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 4),
    _BrcdSPXConfigUnitPESPXPort2_Type()
)
brcdSPXConfigUnitPESPXPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitPESPXPort2.setStatus("current")
_BrcdSPXConfigUnitPESPXLag1_Type = OctetString
_BrcdSPXConfigUnitPESPXLag1_Object = MibTableColumn
brcdSPXConfigUnitPESPXLag1 = _BrcdSPXConfigUnitPESPXLag1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 5),
    _BrcdSPXConfigUnitPESPXLag1_Type()
)
brcdSPXConfigUnitPESPXLag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitPESPXLag1.setStatus("current")
_BrcdSPXConfigUnitPESPXLag2_Type = OctetString
_BrcdSPXConfigUnitPESPXLag2_Object = MibTableColumn
brcdSPXConfigUnitPESPXLag2 = _BrcdSPXConfigUnitPESPXLag2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 6),
    _BrcdSPXConfigUnitPESPXLag2_Type()
)
brcdSPXConfigUnitPESPXLag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitPESPXLag2.setStatus("current")


class _BrcdSPXConfigUnitRowStatus_Type(Integer32):
    """Custom type brcdSPXConfigUnitRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_BrcdSPXConfigUnitRowStatus_Type.__name__ = "Integer32"
_BrcdSPXConfigUnitRowStatus_Object = MibTableColumn
brcdSPXConfigUnitRowStatus = _BrcdSPXConfigUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 7),
    _BrcdSPXConfigUnitRowStatus_Type()
)
brcdSPXConfigUnitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitRowStatus.setStatus("current")
_BrcdSPXConfigUnitType_Type = DisplayString
_BrcdSPXConfigUnitType_Object = MibTableColumn
brcdSPXConfigUnitType = _BrcdSPXConfigUnitType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 8),
    _BrcdSPXConfigUnitType_Type()
)
brcdSPXConfigUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitType.setStatus("current")


class _BrcdSPXConfigUnitState_Type(Integer32):
    """Custom type brcdSPXConfigUnitState based on Integer32"""
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
        *(("empty", 4),
          ("local", 1),
          ("remote", 2),
          ("reserved", 3))
    )


_BrcdSPXConfigUnitState_Type.__name__ = "Integer32"
_BrcdSPXConfigUnitState_Object = MibTableColumn
brcdSPXConfigUnitState = _BrcdSPXConfigUnitState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 9),
    _BrcdSPXConfigUnitState_Type()
)
brcdSPXConfigUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXConfigUnitState.setStatus("current")
_BrcdSPXOperUnitTable_Object = MibTable
brcdSPXOperUnitTable = _BrcdSPXOperUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2)
)
if mibBuilder.loadTexts:
    brcdSPXOperUnitTable.setStatus("current")
_BrcdSPXOperUnitEntry_Object = MibTableRow
brcdSPXOperUnitEntry = _BrcdSPXOperUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1)
)
brcdSPXOperUnitEntry.setIndexNames(
    (0, "BROCADE-SPX-MIB", "brcdSPXOperUnitIndex"),
)
if mibBuilder.loadTexts:
    brcdSPXOperUnitEntry.setStatus("current")
_BrcdSPXOperUnitIndex_Type = Integer32
_BrcdSPXOperUnitIndex_Object = MibTableColumn
brcdSPXOperUnitIndex = _BrcdSPXOperUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 1),
    _BrcdSPXOperUnitIndex_Type()
)
brcdSPXOperUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSPXOperUnitIndex.setStatus("current")
_BrcdSPXOperUnitType_Type = DisplayString
_BrcdSPXOperUnitType_Object = MibTableColumn
brcdSPXOperUnitType = _BrcdSPXOperUnitType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 2),
    _BrcdSPXOperUnitType_Type()
)
brcdSPXOperUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitType.setStatus("current")


class _BrcdSPXOperUnitRole_Type(Integer32):
    """Custom type brcdSPXOperUnitRole based on Integer32"""
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
        *(("active", 2),
          ("member", 4),
          ("other", 1),
          ("spx-pe", 6),
          ("standalone", 5),
          ("standby", 3))
    )


_BrcdSPXOperUnitRole_Type.__name__ = "Integer32"
_BrcdSPXOperUnitRole_Object = MibTableColumn
brcdSPXOperUnitRole = _BrcdSPXOperUnitRole_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 3),
    _BrcdSPXOperUnitRole_Type()
)
brcdSPXOperUnitRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitRole.setStatus("current")
_BrcdSPXOperUnitMac_Type = MacAddress
_BrcdSPXOperUnitMac_Object = MibTableColumn
brcdSPXOperUnitMac = _BrcdSPXOperUnitMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 4),
    _BrcdSPXOperUnitMac_Type()
)
brcdSPXOperUnitMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitMac.setStatus("current")


class _BrcdSPXOperUnitPriority_Type(Integer32):
    """Custom type brcdSPXOperUnitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrcdSPXOperUnitPriority_Type.__name__ = "Integer32"
_BrcdSPXOperUnitPriority_Object = MibTableColumn
brcdSPXOperUnitPriority = _BrcdSPXOperUnitPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 5),
    _BrcdSPXOperUnitPriority_Type()
)
brcdSPXOperUnitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitPriority.setStatus("current")


class _BrcdSPXOperUnitState_Type(Integer32):
    """Custom type brcdSPXOperUnitState based on Integer32"""
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
        *(("empty", 4),
          ("local", 1),
          ("remote", 2),
          ("reserved", 3))
    )


_BrcdSPXOperUnitState_Type.__name__ = "Integer32"
_BrcdSPXOperUnitState_Object = MibTableColumn
brcdSPXOperUnitState = _BrcdSPXOperUnitState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 6),
    _BrcdSPXOperUnitState_Type()
)
brcdSPXOperUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitState.setStatus("current")


class _BrcdSPXOperUnitDescription_Type(DisplayString):
    """Custom type brcdSPXOperUnitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BrcdSPXOperUnitDescription_Type.__name__ = "DisplayString"
_BrcdSPXOperUnitDescription_Object = MibTableColumn
brcdSPXOperUnitDescription = _BrcdSPXOperUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 7),
    _BrcdSPXOperUnitDescription_Type()
)
brcdSPXOperUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitDescription.setStatus("current")


class _BrcdSPXOperUnitImgVer_Type(DisplayString):
    """Custom type brcdSPXOperUnitImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrcdSPXOperUnitImgVer_Type.__name__ = "DisplayString"
_BrcdSPXOperUnitImgVer_Object = MibTableColumn
brcdSPXOperUnitImgVer = _BrcdSPXOperUnitImgVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 8),
    _BrcdSPXOperUnitImgVer_Type()
)
brcdSPXOperUnitImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitImgVer.setStatus("current")


class _BrcdSPXOperUnitBuildlVer_Type(DisplayString):
    """Custom type brcdSPXOperUnitBuildlVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrcdSPXOperUnitBuildlVer_Type.__name__ = "DisplayString"
_BrcdSPXOperUnitBuildlVer_Object = MibTableColumn
brcdSPXOperUnitBuildlVer = _BrcdSPXOperUnitBuildlVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 9),
    _BrcdSPXOperUnitBuildlVer_Type()
)
brcdSPXOperUnitBuildlVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXOperUnitBuildlVer.setStatus("current")
_BrcdSPXCBSPXPortTable_Object = MibTable
brcdSPXCBSPXPortTable = _BrcdSPXCBSPXPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3)
)
if mibBuilder.loadTexts:
    brcdSPXCBSPXPortTable.setStatus("current")
_BrcdSPXCBSPXPortEntry_Object = MibTableRow
brcdSPXCBSPXPortEntry = _BrcdSPXCBSPXPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1)
)
brcdSPXCBSPXPortEntry.setIndexNames(
    (0, "BROCADE-SPX-MIB", "brcdSPXCBSPXPortPort"),
)
if mibBuilder.loadTexts:
    brcdSPXCBSPXPortEntry.setStatus("current")
_BrcdSPXCBSPXPortPort_Type = InterfaceIndexOrZero
_BrcdSPXCBSPXPortPort_Object = MibTableColumn
brcdSPXCBSPXPortPort = _BrcdSPXCBSPXPortPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1, 1),
    _BrcdSPXCBSPXPortPort_Type()
)
brcdSPXCBSPXPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSPXCBSPXPortPort.setStatus("current")


class _BrcdSPXCBSPXPortPEGroup_Type(DisplayString):
    """Custom type brcdSPXCBSPXPortPEGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrcdSPXCBSPXPortPEGroup_Type.__name__ = "DisplayString"
_BrcdSPXCBSPXPortPEGroup_Object = MibTableColumn
brcdSPXCBSPXPortPEGroup = _BrcdSPXCBSPXPortPEGroup_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1, 2),
    _BrcdSPXCBSPXPortPEGroup_Type()
)
brcdSPXCBSPXPortPEGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXCBSPXPortPEGroup.setStatus("current")


class _BrcdSPXCBSPXPortRowStatus_Type(Integer32):
    """Custom type brcdSPXCBSPXPortRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_BrcdSPXCBSPXPortRowStatus_Type.__name__ = "Integer32"
_BrcdSPXCBSPXPortRowStatus_Object = MibTableColumn
brcdSPXCBSPXPortRowStatus = _BrcdSPXCBSPXPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1, 3),
    _BrcdSPXCBSPXPortRowStatus_Type()
)
brcdSPXCBSPXPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXCBSPXPortRowStatus.setStatus("current")
_BrcdSPXCBSPXLagTable_Object = MibTable
brcdSPXCBSPXLagTable = _BrcdSPXCBSPXLagTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4)
)
if mibBuilder.loadTexts:
    brcdSPXCBSPXLagTable.setStatus("current")
_BrcdSPXCBSPXLagEntry_Object = MibTableRow
brcdSPXCBSPXLagEntry = _BrcdSPXCBSPXLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1)
)
brcdSPXCBSPXLagEntry.setIndexNames(
    (0, "BROCADE-SPX-MIB", "brcdSPXCBSPXLagPrimaryPort"),
)
if mibBuilder.loadTexts:
    brcdSPXCBSPXLagEntry.setStatus("current")
_BrcdSPXCBSPXLagPrimaryPort_Type = InterfaceIndexOrZero
_BrcdSPXCBSPXLagPrimaryPort_Object = MibTableColumn
brcdSPXCBSPXLagPrimaryPort = _BrcdSPXCBSPXLagPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 1),
    _BrcdSPXCBSPXLagPrimaryPort_Type()
)
brcdSPXCBSPXLagPrimaryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSPXCBSPXLagPrimaryPort.setStatus("current")
_BrcdSPXCBSPXLagLagIflist_Type = OctetString
_BrcdSPXCBSPXLagLagIflist_Object = MibTableColumn
brcdSPXCBSPXLagLagIflist = _BrcdSPXCBSPXLagLagIflist_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 2),
    _BrcdSPXCBSPXLagLagIflist_Type()
)
brcdSPXCBSPXLagLagIflist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXCBSPXLagLagIflist.setStatus("current")


class _BrcdSPXCBSPXLagPEGroup_Type(DisplayString):
    """Custom type brcdSPXCBSPXLagPEGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrcdSPXCBSPXLagPEGroup_Type.__name__ = "DisplayString"
_BrcdSPXCBSPXLagPEGroup_Object = MibTableColumn
brcdSPXCBSPXLagPEGroup = _BrcdSPXCBSPXLagPEGroup_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 3),
    _BrcdSPXCBSPXLagPEGroup_Type()
)
brcdSPXCBSPXLagPEGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXCBSPXLagPEGroup.setStatus("current")


class _BrcdSPXCBSPXLagRowStatus_Type(Integer32):
    """Custom type brcdSPXCBSPXLagRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_BrcdSPXCBSPXLagRowStatus_Type.__name__ = "Integer32"
_BrcdSPXCBSPXLagRowStatus_Object = MibTableColumn
brcdSPXCBSPXLagRowStatus = _BrcdSPXCBSPXLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 4),
    _BrcdSPXCBSPXLagRowStatus_Type()
)
brcdSPXCBSPXLagRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSPXCBSPXLagRowStatus.setStatus("current")
_BrcdSPXPEGroupTable_Object = MibTable
brcdSPXPEGroupTable = _BrcdSPXPEGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5)
)
if mibBuilder.loadTexts:
    brcdSPXPEGroupTable.setStatus("current")
_BrcdSPXPEGroupEntry_Object = MibTableRow
brcdSPXPEGroupEntry = _BrcdSPXPEGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1)
)
brcdSPXPEGroupEntry.setIndexNames(
    (0, "BROCADE-SPX-MIB", "brcdSPXPEGroupCBSPXPort"),
)
if mibBuilder.loadTexts:
    brcdSPXPEGroupEntry.setStatus("current")
_BrcdSPXPEGroupCBSPXPort_Type = InterfaceIndexOrZero
_BrcdSPXPEGroupCBSPXPort_Object = MibTableColumn
brcdSPXPEGroupCBSPXPort = _BrcdSPXPEGroupCBSPXPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 1),
    _BrcdSPXPEGroupCBSPXPort_Type()
)
brcdSPXPEGroupCBSPXPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSPXPEGroupCBSPXPort.setStatus("current")
_BrcdSPXPEGroupPEGroup_Type = DisplayString
_BrcdSPXPEGroupPEGroup_Object = MibTableColumn
brcdSPXPEGroupPEGroup = _BrcdSPXPEGroupPEGroup_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 2),
    _BrcdSPXPEGroupPEGroup_Type()
)
brcdSPXPEGroupPEGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXPEGroupPEGroup.setStatus("current")
_BrcdSPXPEGroupPEIdList_Type = DisplayString
_BrcdSPXPEGroupPEIdList_Object = MibTableColumn
brcdSPXPEGroupPEIdList = _BrcdSPXPEGroupPEIdList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 3),
    _BrcdSPXPEGroupPEIdList_Type()
)
brcdSPXPEGroupPEIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXPEGroupPEIdList.setStatus("current")
_BrcdSPXPEGroupCBSPXEndPort_Type = InterfaceIndexOrZero
_BrcdSPXPEGroupCBSPXEndPort_Object = MibTableColumn
brcdSPXPEGroupCBSPXEndPort = _BrcdSPXPEGroupCBSPXEndPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 4),
    _BrcdSPXPEGroupCBSPXEndPort_Type()
)
brcdSPXPEGroupCBSPXEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSPXPEGroupCBSPXEndPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-SPX-MIB",
    **{"brcdSPXMIB": brcdSPXMIB,
       "brcdSPXGlobalObjects": brcdSPXGlobalObjects,
       "brcdSPXGlobalConfigCBState": brcdSPXGlobalConfigCBState,
       "brcdSPXGlobalConfigPEState": brcdSPXGlobalConfigPEState,
       "brcdSPXTableObjects": brcdSPXTableObjects,
       "brcdSPXConfigUnitTable": brcdSPXConfigUnitTable,
       "brcdSPXConfigUnitEntry": brcdSPXConfigUnitEntry,
       "brcdSPXConfigUnitIndex": brcdSPXConfigUnitIndex,
       "brcdSPXConfigUnitPEName": brcdSPXConfigUnitPEName,
       "brcdSPXConfigUnitPESPXPort1": brcdSPXConfigUnitPESPXPort1,
       "brcdSPXConfigUnitPESPXPort2": brcdSPXConfigUnitPESPXPort2,
       "brcdSPXConfigUnitPESPXLag1": brcdSPXConfigUnitPESPXLag1,
       "brcdSPXConfigUnitPESPXLag2": brcdSPXConfigUnitPESPXLag2,
       "brcdSPXConfigUnitRowStatus": brcdSPXConfigUnitRowStatus,
       "brcdSPXConfigUnitType": brcdSPXConfigUnitType,
       "brcdSPXConfigUnitState": brcdSPXConfigUnitState,
       "brcdSPXOperUnitTable": brcdSPXOperUnitTable,
       "brcdSPXOperUnitEntry": brcdSPXOperUnitEntry,
       "brcdSPXOperUnitIndex": brcdSPXOperUnitIndex,
       "brcdSPXOperUnitType": brcdSPXOperUnitType,
       "brcdSPXOperUnitRole": brcdSPXOperUnitRole,
       "brcdSPXOperUnitMac": brcdSPXOperUnitMac,
       "brcdSPXOperUnitPriority": brcdSPXOperUnitPriority,
       "brcdSPXOperUnitState": brcdSPXOperUnitState,
       "brcdSPXOperUnitDescription": brcdSPXOperUnitDescription,
       "brcdSPXOperUnitImgVer": brcdSPXOperUnitImgVer,
       "brcdSPXOperUnitBuildlVer": brcdSPXOperUnitBuildlVer,
       "brcdSPXCBSPXPortTable": brcdSPXCBSPXPortTable,
       "brcdSPXCBSPXPortEntry": brcdSPXCBSPXPortEntry,
       "brcdSPXCBSPXPortPort": brcdSPXCBSPXPortPort,
       "brcdSPXCBSPXPortPEGroup": brcdSPXCBSPXPortPEGroup,
       "brcdSPXCBSPXPortRowStatus": brcdSPXCBSPXPortRowStatus,
       "brcdSPXCBSPXLagTable": brcdSPXCBSPXLagTable,
       "brcdSPXCBSPXLagEntry": brcdSPXCBSPXLagEntry,
       "brcdSPXCBSPXLagPrimaryPort": brcdSPXCBSPXLagPrimaryPort,
       "brcdSPXCBSPXLagLagIflist": brcdSPXCBSPXLagLagIflist,
       "brcdSPXCBSPXLagPEGroup": brcdSPXCBSPXLagPEGroup,
       "brcdSPXCBSPXLagRowStatus": brcdSPXCBSPXLagRowStatus,
       "brcdSPXPEGroupTable": brcdSPXPEGroupTable,
       "brcdSPXPEGroupEntry": brcdSPXPEGroupEntry,
       "brcdSPXPEGroupCBSPXPort": brcdSPXPEGroupCBSPXPort,
       "brcdSPXPEGroupPEGroup": brcdSPXPEGroupPEGroup,
       "brcdSPXPEGroupPEIdList": brcdSPXPEGroupPEIdList,
       "brcdSPXPEGroupCBSPXEndPort": brcdSPXPEGroupCBSPXEndPort}
)
