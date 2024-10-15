# SNMP MIB module (DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:37 2024
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

(docsDevEvId,
 docsDevEvLevel,
 docsDevEvText,
 docsDevServerDhcp,
 docsDevServerTime,
 docsDevSwFilename,
 docsDevSwServer) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLevel",
    "docsDevEvText",
    "docsDevServerDhcp",
    "docsDevServerTime",
    "docsDevSwFilename",
    "docsDevSwServer")

(docsIfCmCmtsAddress,
 docsIfCmStatusDocsisOperMode,
 docsIfCmStatusModulationType,
 docsIfCmtsCmStatusDocsisRegMode,
 docsIfCmtsCmStatusMacAddress,
 docsIfCmtsCmStatusModulationType,
 docsIfDocsisBaseCapability) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmCmtsAddress",
    "docsIfCmStatusDocsisOperMode",
    "docsIfCmStatusModulationType",
    "docsIfCmtsCmStatusDocsisRegMode",
    "docsIfCmtsCmStatusMacAddress",
    "docsIfCmtsCmStatusModulationType",
    "docsIfDocsisBaseCapability")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

docsDevNotifMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 132)
)
docsDevNotifMIB.setRevisions(
        ("2006-05-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsDevNotifControl_ObjectIdentity = ObjectIdentity
docsDevNotifControl = _DocsDevNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 132, 1)
)


class _DocsDevCmNotifControl_Type(Bits):
    """Custom type docsDevCmNotifControl based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cmBPKMNotif", 5),
          ("cmBpiInitNotif", 4),
          ("cmDCCAckFailNotif", 15),
          ("cmDCCReqFailNotif", 13),
          ("cmDCCRspFailNotif", 14),
          ("cmDHCPFailNotif", 7),
          ("cmDynServAckFailNotif", 3),
          ("cmDynServReqFailNotif", 1),
          ("cmDynServRspFailNotif", 2),
          ("cmDynamicSANotif", 6),
          ("cmInitTLVUnknownNotif", 0),
          ("cmSwUpgradeCVCNotif", 11),
          ("cmSwUpgradeFailNotif", 9),
          ("cmSwUpgradeInitNotif", 8),
          ("cmSwUpgradeSuccessNotif", 10),
          ("cmTODFailNotif", 12))
    )

_DocsDevCmNotifControl_Type.__name__ = "Bits"
_DocsDevCmNotifControl_Object = MibScalar
docsDevCmNotifControl = _DocsDevCmNotifControl_Object(
    (1, 3, 6, 1, 2, 1, 132, 1, 1),
    _DocsDevCmNotifControl_Type()
)
docsDevCmNotifControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCmNotifControl.setStatus("current")


class _DocsDevCmtsNotifControl_Type(Bits):
    """Custom type docsDevCmtsNotifControl based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cmtsBPKMNotif", 7),
          ("cmtsBpiInitNotif", 6),
          ("cmtsDCCAckFailNotif", 11),
          ("cmtsDCCReqFailNotif", 9),
          ("cmtsDCCRspFailNotif", 10),
          ("cmtsDynServAckFailNotif", 5),
          ("cmtsDynServReqFailNotif", 3),
          ("cmtsDynServRspFailNotif", 4),
          ("cmtsDynamicSANotif", 8),
          ("cmtsInitRegAckFailNotif", 2),
          ("cmtsInitRegReqFailNotif", 0),
          ("cmtsInitRegRspFailNotif", 1))
    )

_DocsDevCmtsNotifControl_Type.__name__ = "Bits"
_DocsDevCmtsNotifControl_Object = MibScalar
docsDevCmtsNotifControl = _DocsDevCmtsNotifControl_Object(
    (1, 3, 6, 1, 2, 1, 132, 1, 2),
    _DocsDevCmtsNotifControl_Type()
)
docsDevCmtsNotifControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCmtsNotifControl.setStatus("current")
_DocsDevCmNotifs_ObjectIdentity = ObjectIdentity
docsDevCmNotifs = _DocsDevCmNotifs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 132, 2, 0)
)
_DocsDevCmtsNotifs_ObjectIdentity = ObjectIdentity
docsDevCmtsNotifs = _DocsDevCmtsNotifs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 132, 3, 0)
)
_DocsDevNotifConformance_ObjectIdentity = ObjectIdentity
docsDevNotifConformance = _DocsDevNotifConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 132, 4)
)
_DocsDevNotifGroups_ObjectIdentity = ObjectIdentity
docsDevNotifGroups = _DocsDevNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 132, 4, 1)
)
_DocsDevNotifCompliances_ObjectIdentity = ObjectIdentity
docsDevNotifCompliances = _DocsDevNotifCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 132, 4, 2)
)

# Managed Objects groups

docsDevCmNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 132, 4, 1, 1)
)
docsDevCmNotifControlGroup.setObjects(
    ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmNotifControl")
)
if mibBuilder.loadTexts:
    docsDevCmNotifControlGroup.setStatus("current")

docsDevCmtsNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 132, 4, 1, 3)
)
docsDevCmtsNotifControlGroup.setObjects(
    ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsNotifControl")
)
if mibBuilder.loadTexts:
    docsDevCmtsNotifControlGroup.setStatus("current")


# Notification objects

docsDevCmInitTLVUnknownNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 1)
)
docsDevCmInitTLVUnknownNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmInitTLVUnknownNotif.setStatus(
        "current"
    )

docsDevCmDynServReqFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 2)
)
docsDevCmDynServReqFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDynServReqFailNotif.setStatus(
        "current"
    )

docsDevCmDynServRspFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 3)
)
docsDevCmDynServRspFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDynServRspFailNotif.setStatus(
        "current"
    )

docsDevCmDynServAckFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 4)
)
docsDevCmDynServAckFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDynServAckFailNotif.setStatus(
        "current"
    )

docsDevCmBpiInitNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 5)
)
docsDevCmBpiInitNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmBpiInitNotif.setStatus(
        "current"
    )

docsDevCmBPKMNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 6)
)
docsDevCmBPKMNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmBPKMNotif.setStatus(
        "current"
    )

docsDevCmDynamicSANotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 7)
)
docsDevCmDynamicSANotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDynamicSANotif.setStatus(
        "current"
    )

docsDevCmDHCPFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 8)
)
docsDevCmDHCPFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcp"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDHCPFailNotif.setStatus(
        "current"
    )

docsDevCmSwUpgradeInitNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 9)
)
docsDevCmSwUpgradeInitNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeInitNotif.setStatus(
        "current"
    )

docsDevCmSwUpgradeFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 10)
)
docsDevCmSwUpgradeFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeFailNotif.setStatus(
        "current"
    )

docsDevCmSwUpgradeSuccessNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 11)
)
docsDevCmSwUpgradeSuccessNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeSuccessNotif.setStatus(
        "current"
    )

docsDevCmSwUpgradeCVCFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 12)
)
docsDevCmSwUpgradeCVCFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmSwUpgradeCVCFailNotif.setStatus(
        "current"
    )

docsDevCmTODFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 13)
)
docsDevCmTODFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTime"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmTODFailNotif.setStatus(
        "current"
    )

docsDevCmDCCReqFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 14)
)
docsDevCmDCCReqFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDCCReqFailNotif.setStatus(
        "current"
    )

docsDevCmDCCRspFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 15)
)
docsDevCmDCCRspFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDCCRspFailNotif.setStatus(
        "current"
    )

docsDevCmDCCAckFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 2, 0, 16)
)
docsDevCmDCCAckFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmDCCAckFailNotif.setStatus(
        "current"
    )

docsDevCmtsInitRegReqFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 1)
)
docsDevCmtsInitRegReqFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsInitRegReqFailNotif.setStatus(
        "current"
    )

docsDevCmtsInitRegRspFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 2)
)
docsDevCmtsInitRegRspFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsInitRegRspFailNotif.setStatus(
        "current"
    )

docsDevCmtsInitRegAckFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 3)
)
docsDevCmtsInitRegAckFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsInitRegAckFailNotif.setStatus(
        "current"
    )

docsDevCmtsDynServReqFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 4)
)
docsDevCmtsDynServReqFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynServReqFailNotif.setStatus(
        "current"
    )

docsDevCmtsDynServRspFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 5)
)
docsDevCmtsDynServRspFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynServRspFailNotif.setStatus(
        "current"
    )

docsDevCmtsDynServAckFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 6)
)
docsDevCmtsDynServAckFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynServAckFailNotif.setStatus(
        "current"
    )

docsDevCmtsBpiInitNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 7)
)
docsDevCmtsBpiInitNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsBpiInitNotif.setStatus(
        "current"
    )

docsDevCmtsBPKMNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 8)
)
docsDevCmtsBPKMNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsBPKMNotif.setStatus(
        "current"
    )

docsDevCmtsDynamicSANotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 9)
)
docsDevCmtsDynamicSANotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDynamicSANotif.setStatus(
        "current"
    )

docsDevCmtsDCCReqFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 10)
)
docsDevCmtsDCCReqFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDCCReqFailNotif.setStatus(
        "current"
    )

docsDevCmtsDCCRspFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 11)
)
docsDevCmtsDCCRspFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDCCRspFailNotif.setStatus(
        "current"
    )

docsDevCmtsDCCAckFailNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 132, 3, 0, 12)
)
docsDevCmtsDCCAckFailNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    docsDevCmtsDCCAckFailNotif.setStatus(
        "current"
    )


# Notifications groups

docsDevCmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 132, 4, 1, 2)
)
docsDevCmNotificationGroup.setObjects(
      *(("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmInitTLVUnknownNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDynServReqFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDynServRspFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDynServAckFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmBpiInitNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmBPKMNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDynamicSANotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDHCPFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmSwUpgradeInitNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmSwUpgradeFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmSwUpgradeSuccessNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmSwUpgradeCVCFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmTODFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDCCReqFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDCCRspFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmDCCAckFailNotif"))
)
if mibBuilder.loadTexts:
    docsDevCmNotificationGroup.setStatus(
        "current"
    )

docsDevCmtsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 132, 4, 1, 4)
)
docsDevCmtsNotificationGroup.setObjects(
      *(("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsInitRegReqFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsInitRegRspFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsInitRegAckFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDynServReqFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDynServRspFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDynServAckFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsBpiInitNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsBPKMNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDynamicSANotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDCCReqFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDCCRspFailNotif"),
        ("DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB", "docsDevCmtsDCCAckFailNotif"))
)
if mibBuilder.loadTexts:
    docsDevCmtsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

docsDevCmNotifCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 132, 4, 2, 1)
)
if mibBuilder.loadTexts:
    docsDevCmNotifCompliance.setStatus(
        "current"
    )

docsDevCmtsNotifCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 132, 4, 2, 2)
)
if mibBuilder.loadTexts:
    docsDevCmtsNotifCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB",
    **{"docsDevNotifMIB": docsDevNotifMIB,
       "docsDevNotifControl": docsDevNotifControl,
       "docsDevCmNotifControl": docsDevCmNotifControl,
       "docsDevCmtsNotifControl": docsDevCmtsNotifControl,
       "docsDevCmNotifs": docsDevCmNotifs,
       "docsDevCmInitTLVUnknownNotif": docsDevCmInitTLVUnknownNotif,
       "docsDevCmDynServReqFailNotif": docsDevCmDynServReqFailNotif,
       "docsDevCmDynServRspFailNotif": docsDevCmDynServRspFailNotif,
       "docsDevCmDynServAckFailNotif": docsDevCmDynServAckFailNotif,
       "docsDevCmBpiInitNotif": docsDevCmBpiInitNotif,
       "docsDevCmBPKMNotif": docsDevCmBPKMNotif,
       "docsDevCmDynamicSANotif": docsDevCmDynamicSANotif,
       "docsDevCmDHCPFailNotif": docsDevCmDHCPFailNotif,
       "docsDevCmSwUpgradeInitNotif": docsDevCmSwUpgradeInitNotif,
       "docsDevCmSwUpgradeFailNotif": docsDevCmSwUpgradeFailNotif,
       "docsDevCmSwUpgradeSuccessNotif": docsDevCmSwUpgradeSuccessNotif,
       "docsDevCmSwUpgradeCVCFailNotif": docsDevCmSwUpgradeCVCFailNotif,
       "docsDevCmTODFailNotif": docsDevCmTODFailNotif,
       "docsDevCmDCCReqFailNotif": docsDevCmDCCReqFailNotif,
       "docsDevCmDCCRspFailNotif": docsDevCmDCCRspFailNotif,
       "docsDevCmDCCAckFailNotif": docsDevCmDCCAckFailNotif,
       "docsDevCmtsNotifs": docsDevCmtsNotifs,
       "docsDevCmtsInitRegReqFailNotif": docsDevCmtsInitRegReqFailNotif,
       "docsDevCmtsInitRegRspFailNotif": docsDevCmtsInitRegRspFailNotif,
       "docsDevCmtsInitRegAckFailNotif": docsDevCmtsInitRegAckFailNotif,
       "docsDevCmtsDynServReqFailNotif": docsDevCmtsDynServReqFailNotif,
       "docsDevCmtsDynServRspFailNotif": docsDevCmtsDynServRspFailNotif,
       "docsDevCmtsDynServAckFailNotif": docsDevCmtsDynServAckFailNotif,
       "docsDevCmtsBpiInitNotif": docsDevCmtsBpiInitNotif,
       "docsDevCmtsBPKMNotif": docsDevCmtsBPKMNotif,
       "docsDevCmtsDynamicSANotif": docsDevCmtsDynamicSANotif,
       "docsDevCmtsDCCReqFailNotif": docsDevCmtsDCCReqFailNotif,
       "docsDevCmtsDCCRspFailNotif": docsDevCmtsDCCRspFailNotif,
       "docsDevCmtsDCCAckFailNotif": docsDevCmtsDCCAckFailNotif,
       "docsDevNotifConformance": docsDevNotifConformance,
       "docsDevNotifGroups": docsDevNotifGroups,
       "docsDevCmNotifControlGroup": docsDevCmNotifControlGroup,
       "docsDevCmNotificationGroup": docsDevCmNotificationGroup,
       "docsDevCmtsNotifControlGroup": docsDevCmtsNotifControlGroup,
       "docsDevCmtsNotificationGroup": docsDevCmtsNotificationGroup,
       "docsDevNotifCompliances": docsDevNotifCompliances,
       "docsDevCmNotifCompliance": docsDevCmNotifCompliance,
       "docsDevCmtsNotifCompliance": docsDevCmtsNotifCompliance}
)
