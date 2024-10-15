# SNMP MIB module (DOCS-CABLE-DEVICE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-CABLE-DEVICE-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:32 2024
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

(docsDev,
 docsDevEvId,
 docsDevEvLevel,
 docsDevEvText,
 docsDevNotification,
 docsDevServerDhcp,
 docsDevServerTime,
 docsDevSwFilename,
 docsDevSwServer) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDev",
    "docsDevEvId",
    "docsDevEvLevel",
    "docsDevEvText",
    "docsDevNotification",
    "docsDevServerDhcp",
    "docsDevServerTime",
    "docsDevSwFilename",
    "docsDevSwServer")

(docsIfCmtsCmStatusDocsisMode,
 docsIfDocsisCapability,
 docsIfDocsisOperMode) = mibBuilder.importSymbols(
    "DOCS-IF-EXT-MIB",
    "docsIfCmtsCmStatusDocsisMode",
    "docsIfDocsisCapability",
    "docsIfDocsisOperMode")

(docsIfCmCmtsAddress,
 docsIfCmtsCmStatusMacAddress) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmCmtsAddress",
    "docsIfCmtsCmStatusMacAddress")

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

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

docsDevTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 69, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsDevTraps_ObjectIdentity = ObjectIdentity
docsDevTraps = _DocsDevTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1)
)
_DocsDevTrapControl_ObjectIdentity = ObjectIdentity
docsDevTrapControl = _DocsDevTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 1)
)


class _DocsDevCmTrapControl_Type(Bits):
    """Custom type docsDevCmTrapControl based on Bits"""
    namedValues = NamedValues(
        *(("cmBPKMTrap", 5),
          ("cmBpiInitTrap", 4),
          ("cmDCCAckFailTrap", 15),
          ("cmDCCReqFailTrap", 13),
          ("cmDCCRspFailTrap", 14),
          ("cmDHCPFailTrap", 7),
          ("cmDynServAckFailTrap", 3),
          ("cmDynServReqFailTrap", 1),
          ("cmDynServRspFailTrap", 2),
          ("cmDynamicSATrap", 6),
          ("cmInitTLVUnknownTrap", 0),
          ("cmSwUpgradeCVCTrap", 11),
          ("cmSwUpgradeFailTrap", 9),
          ("cmSwUpgradeInitTrap", 8),
          ("cmSwUpgradeSuccessTrap", 10),
          ("cmTODFailTrap", 12))
    )

_DocsDevCmTrapControl_Type.__name__ = "Bits"
_DocsDevCmTrapControl_Object = MibScalar
docsDevCmTrapControl = _DocsDevCmTrapControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 1, 1),
    _DocsDevCmTrapControl_Type()
)
docsDevCmTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCmTrapControl.setStatus("current")


class _DocsDevCmtsTrapControl_Type(Bits):
    """Custom type docsDevCmtsTrapControl based on Bits"""
    namedValues = NamedValues(
        *(("cmtsBPKMTrap", 7),
          ("cmtsBpiInitTrap", 6),
          ("cmtsDCCAckFailTrap", 11),
          ("cmtsDCCReqFailTrap", 9),
          ("cmtsDCCRspFailTrap", 10),
          ("cmtsDynServAckFailTrap", 5),
          ("cmtsDynServReqFailTrap", 3),
          ("cmtsDynServRspFailTrap", 4),
          ("cmtsDynamicSATrap", 8),
          ("cmtsInitRegAckFailTrap", 2),
          ("cmtsInitRegReqFailTrap", 0),
          ("cmtsInitRegRspFailTrap", 1))
    )

_DocsDevCmtsTrapControl_Type.__name__ = "Bits"
_DocsDevCmtsTrapControl_Object = MibScalar
docsDevCmtsTrapControl = _DocsDevCmtsTrapControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 1, 2),
    _DocsDevCmtsTrapControl_Type()
)
docsDevCmtsTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCmtsTrapControl.setStatus("current")
_DocsDevTrapConformance_ObjectIdentity = ObjectIdentity
docsDevTrapConformance = _DocsDevTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2)
)
_DocsDevCmTraps_ObjectIdentity = ObjectIdentity
docsDevCmTraps = _DocsDevCmTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0)
)
_DocsDevTrapGroups_ObjectIdentity = ObjectIdentity
docsDevTrapGroups = _DocsDevTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1)
)
_DocsDevTrapCompliances_ObjectIdentity = ObjectIdentity
docsDevTrapCompliances = _DocsDevTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 2)
)
_DocsDevCmtsTraps_ObjectIdentity = ObjectIdentity
docsDevCmtsTraps = _DocsDevCmtsTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0)
)

# Managed Objects groups

docsDevCmTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 1)
)
docsDevCmTrapControlGroup.setObjects(
    ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTrapControl")
)
if mibBuilder.loadTexts:
    docsDevCmTrapControlGroup.setStatus("current")

docsDevCmtsTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 3)
)
docsDevCmtsTrapControlGroup.setObjects(
    ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsTrapControl")
)
if mibBuilder.loadTexts:
    docsDevCmtsTrapControlGroup.setStatus("current")


# Notification objects

docsDevCmInitTLVUnknownTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 1)
)
docsDevCmInitTLVUnknownTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmInitTLVUnknownTrap.setStatus(
        "current"
    )

docsDevCmDynServReqFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 2)
)
docsDevCmDynServReqFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDynServReqFailTrap.setStatus(
        "current"
    )

docsDevCmDynServRspFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 3)
)
docsDevCmDynServRspFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDynServRspFailTrap.setStatus(
        "current"
    )

docsDevCmDynServAckFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 4)
)
docsDevCmDynServAckFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDynServAckFailTrap.setStatus(
        "current"
    )

docsDevCmBpiInitTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 5)
)
docsDevCmBpiInitTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmBpiInitTrap.setStatus(
        "current"
    )

docsDevCmBPKMTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 6)
)
docsDevCmBPKMTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmBPKMTrap.setStatus(
        "current"
    )

docsDevCmDynamicSATrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 7)
)
docsDevCmDynamicSATrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDynamicSATrap.setStatus(
        "current"
    )

docsDevCmDHCPFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 8)
)
docsDevCmDHCPFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcp"))
)
if mibBuilder.loadTexts:
    docsDevCmDHCPFailTrap.setStatus(
        "current"
    )

docsDevCmSwUpgradeInitTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 9)
)
docsDevCmSwUpgradeInitTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeInitTrap.setStatus(
        "current"
    )

docsDevCmSwUpgradeFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 10)
)
docsDevCmSwUpgradeFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeFailTrap.setStatus(
        "current"
    )

docsDevCmSwUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 11)
)
docsDevCmSwUpgradeSuccessTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeSuccessTrap.setStatus(
        "current"
    )

docsDevCmSwUpgradeCVCFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 12)
)
docsDevCmSwUpgradeCVCFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeCVCFailTrap.setStatus(
        "current"
    )

docsDevCmTODFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 13)
)
docsDevCmTODFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTime"))
)
if mibBuilder.loadTexts:
    docsDevCmTODFailTrap.setStatus(
        "current"
    )

docsDevCmDCCReqFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 14)
)
docsDevCmDCCReqFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDCCReqFailTrap.setStatus(
        "current"
    )

docsDevCmDCCRspFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 15)
)
docsDevCmDCCRspFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDCCRspFailTrap.setStatus(
        "current"
    )

docsDevCmDCCAckFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 16)
)
docsDevCmDCCAckFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmDCCAckFailTrap.setStatus(
        "current"
    )

docsDevCmtsInitRegReqFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 1)
)
docsDevCmtsInitRegReqFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsInitRegReqFailTrap.setStatus(
        "current"
    )

docsDevCmtsInitRegRspFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 2)
)
docsDevCmtsInitRegRspFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsInitRegRspFailTrap.setStatus(
        "current"
    )

docsDevCmtsInitRegAckFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 3)
)
docsDevCmtsInitRegAckFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsInitRegAckFailTrap.setStatus(
        "current"
    )

docsDevCmtsDynServReqFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 4)
)
docsDevCmtsDynServReqFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynServReqFailTrap.setStatus(
        "current"
    )

docsDevCmtsDynServRspFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 5)
)
docsDevCmtsDynServRspFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynServRspFailTrap.setStatus(
        "current"
    )

docsDevCmtsDynServAckFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 6)
)
docsDevCmtsDynServAckFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynServAckFailTrap.setStatus(
        "current"
    )

docsDevCmtsBpiInitTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 7)
)
docsDevCmtsBpiInitTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsBpiInitTrap.setStatus(
        "current"
    )

docsDevCmtsBPKMTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 8)
)
docsDevCmtsBPKMTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsBPKMTrap.setStatus(
        "current"
    )

docsDevCmtsDynamicSATrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 9)
)
docsDevCmtsDynamicSATrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynamicSATrap.setStatus(
        "current"
    )

docsDevCmtsDCCReqFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 10)
)
docsDevCmtsDCCReqFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDCCReqFailTrap.setStatus(
        "current"
    )

docsDevCmtsDCCRspFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 11)
)
docsDevCmtsDCCRspFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDCCRspFailTrap.setStatus(
        "current"
    )

docsDevCmtsDCCAckFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 12)
)
docsDevCmtsDCCAckFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDCCAckFailTrap.setStatus(
        "current"
    )


# Notifications groups

docsDevCmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 2)
)
docsDevCmNotificationGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmInitTLVUnknownTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServReqFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServRspFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServAckFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmBpiInitTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmBPKMTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynamicSATrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDHCPFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeInitTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeSuccessTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeCVCFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTODFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCReqFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCRspFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCAckFailTrap"))
)
if mibBuilder.loadTexts:
    docsDevCmNotificationGroup.setStatus(
        "current"
    )

docsDevCmtsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 4)
)
docsDevCmtsNotificationGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegReqFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegRspFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegAckFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServReqFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServRspFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServAckFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsBpiInitTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsBPKMTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynamicSATrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCReqFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCRspFailTrap"),
        ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCAckFailTrap"))
)
if mibBuilder.loadTexts:
    docsDevCmtsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

docsDevCmTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    docsDevCmTrapCompliance.setStatus(
        "current"
    )

docsDevCmtsTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    docsDevCmtsTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-CABLE-DEVICE-TRAP-MIB",
    **{"docsDevTraps": docsDevTraps,
       "docsDevTrapControl": docsDevTrapControl,
       "docsDevCmTrapControl": docsDevCmTrapControl,
       "docsDevCmtsTrapControl": docsDevCmtsTrapControl,
       "docsDevTrapConformance": docsDevTrapConformance,
       "docsDevCmTraps": docsDevCmTraps,
       "docsDevCmInitTLVUnknownTrap": docsDevCmInitTLVUnknownTrap,
       "docsDevCmDynServReqFailTrap": docsDevCmDynServReqFailTrap,
       "docsDevCmDynServRspFailTrap": docsDevCmDynServRspFailTrap,
       "docsDevCmDynServAckFailTrap": docsDevCmDynServAckFailTrap,
       "docsDevCmBpiInitTrap": docsDevCmBpiInitTrap,
       "docsDevCmBPKMTrap": docsDevCmBPKMTrap,
       "docsDevCmDynamicSATrap": docsDevCmDynamicSATrap,
       "docsDevCmDHCPFailTrap": docsDevCmDHCPFailTrap,
       "docsDevCmSwUpgradeInitTrap": docsDevCmSwUpgradeInitTrap,
       "docsDevCmSwUpgradeFailTrap": docsDevCmSwUpgradeFailTrap,
       "docsDevCmSwUpgradeSuccessTrap": docsDevCmSwUpgradeSuccessTrap,
       "docsDevCmSwUpgradeCVCFailTrap": docsDevCmSwUpgradeCVCFailTrap,
       "docsDevCmTODFailTrap": docsDevCmTODFailTrap,
       "docsDevCmDCCReqFailTrap": docsDevCmDCCReqFailTrap,
       "docsDevCmDCCRspFailTrap": docsDevCmDCCRspFailTrap,
       "docsDevCmDCCAckFailTrap": docsDevCmDCCAckFailTrap,
       "docsDevTrapGroups": docsDevTrapGroups,
       "docsDevCmTrapControlGroup": docsDevCmTrapControlGroup,
       "docsDevCmNotificationGroup": docsDevCmNotificationGroup,
       "docsDevCmtsTrapControlGroup": docsDevCmtsTrapControlGroup,
       "docsDevCmtsNotificationGroup": docsDevCmtsNotificationGroup,
       "docsDevTrapCompliances": docsDevTrapCompliances,
       "docsDevCmTrapCompliance": docsDevCmTrapCompliance,
       "docsDevCmtsTrapCompliance": docsDevCmtsTrapCompliance,
       "docsDevCmtsTraps": docsDevCmtsTraps,
       "docsDevCmtsInitRegReqFailTrap": docsDevCmtsInitRegReqFailTrap,
       "docsDevCmtsInitRegRspFailTrap": docsDevCmtsInitRegRspFailTrap,
       "docsDevCmtsInitRegAckFailTrap": docsDevCmtsInitRegAckFailTrap,
       "docsDevCmtsDynServReqFailTrap": docsDevCmtsDynServReqFailTrap,
       "docsDevCmtsDynServRspFailTrap": docsDevCmtsDynServRspFailTrap,
       "docsDevCmtsDynServAckFailTrap": docsDevCmtsDynServAckFailTrap,
       "docsDevCmtsBpiInitTrap": docsDevCmtsBpiInitTrap,
       "docsDevCmtsBPKMTrap": docsDevCmtsBPKMTrap,
       "docsDevCmtsDynamicSATrap": docsDevCmtsDynamicSATrap,
       "docsDevCmtsDCCReqFailTrap": docsDevCmtsDCCReqFailTrap,
       "docsDevCmtsDCCRspFailTrap": docsDevCmtsDCCRspFailTrap,
       "docsDevCmtsDCCAckFailTrap": docsDevCmtsDCCAckFailTrap,
       "docsDevTrapMIB": docsDevTrapMIB}
)
