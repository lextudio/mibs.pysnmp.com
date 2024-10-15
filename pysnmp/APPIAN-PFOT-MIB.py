# SNMP MIB module (APPIAN-PFOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PFOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:37 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcNodeId,
 AcPortNumber,
 AcSlotNumber,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcNodeId",
    "AcPortNumber",
    "AcSlotNumber",
    "acPport")

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

acPfot = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7)
)
acPfot.setRevisions(
        ("1900-02-23 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcPfotType(Integer32, TextualConvention):
    status = "current"
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
        *(("not-present", 0),
          ("sfp-gbe-lx-ir", 3),
          ("sfp-gbe-lx-lr", 4),
          ("sfp-gbe-lx-sr", 2),
          ("sfp-gbe-sx", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AcPfotTraps_ObjectIdentity = ObjectIdentity
acPfotTraps = _AcPfotTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 0)
)
_AcPfotTable_Object = MibTable
acPfotTable = _AcPfotTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    acPfotTable.setStatus("current")
_AcPfotEntry_Object = MibTableRow
acPfotEntry = _AcPfotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1)
)
acPfotEntry.setIndexNames(
    (0, "APPIAN-PFOT-MIB", "acPfotNodeId"),
    (0, "APPIAN-PFOT-MIB", "acPfotSlot"),
    (0, "APPIAN-PFOT-MIB", "acPfotPort"),
)
if mibBuilder.loadTexts:
    acPfotEntry.setStatus("current")
_AcPfotNodeId_Type = AcNodeId
_AcPfotNodeId_Object = MibTableColumn
acPfotNodeId = _AcPfotNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 1),
    _AcPfotNodeId_Type()
)
acPfotNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acPfotNodeId.setStatus("current")
_AcPfotSlot_Type = AcSlotNumber
_AcPfotSlot_Object = MibTableColumn
acPfotSlot = _AcPfotSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 2),
    _AcPfotSlot_Type()
)
acPfotSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acPfotSlot.setStatus("current")
_AcPfotPort_Type = AcPortNumber
_AcPfotPort_Object = MibTableColumn
acPfotPort = _AcPfotPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 3),
    _AcPfotPort_Type()
)
acPfotPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acPfotPort.setStatus("current")


class _AcPfotCfgType_Type(AcPfotType):
    """Custom type acPfotCfgType based on AcPfotType"""


_AcPfotCfgType_Object = MibTableColumn
acPfotCfgType = _AcPfotCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 4),
    _AcPfotCfgType_Type()
)
acPfotCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acPfotCfgType.setStatus("current")
_AcPfotType_Type = AcPfotType
_AcPfotType_Object = MibTableColumn
acPfotType = _AcPfotType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 5),
    _AcPfotType_Type()
)
acPfotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPfotType.setStatus("current")


class _AcPfotConnectorType_Type(Integer32):
    """Custom type acPfotConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lc", 2),
          ("mtrj", 3),
          ("none", 0),
          ("sc", 1))
    )


_AcPfotConnectorType_Type.__name__ = "Integer32"
_AcPfotConnectorType_Object = MibTableColumn
acPfotConnectorType = _AcPfotConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 6),
    _AcPfotConnectorType_Type()
)
acPfotConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPfotConnectorType.setStatus("current")


class _AcPfotVendorName_Type(DisplayString):
    """Custom type acPfotVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcPfotVendorName_Type.__name__ = "DisplayString"
_AcPfotVendorName_Object = MibTableColumn
acPfotVendorName = _AcPfotVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 7),
    _AcPfotVendorName_Type()
)
acPfotVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPfotVendorName.setStatus("current")


class _AcPfotVendorPartNumber_Type(DisplayString):
    """Custom type acPfotVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcPfotVendorPartNumber_Type.__name__ = "DisplayString"
_AcPfotVendorPartNumber_Object = MibTableColumn
acPfotVendorPartNumber = _AcPfotVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 1, 1, 8),
    _AcPfotVendorPartNumber_Type()
)
acPfotVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPfotVendorPartNumber.setStatus("current")

# Managed Objects groups


# Notification objects

acPfotCfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 7, 0, 1)
)
acPfotCfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PFOT-MIB", "acPfotNodeId"),
        ("APPIAN-PFOT-MIB", "acPfotSlot"),
        ("APPIAN-PFOT-MIB", "acPfotPort"),
        ("APPIAN-PFOT-MIB", "acPfotCfgType"),
        ("APPIAN-PFOT-MIB", "acPfotType"))
)
if mibBuilder.loadTexts:
    acPfotCfgErrorTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PFOT-MIB",
    **{"AcPfotType": AcPfotType,
       "acPfot": acPfot,
       "acPfotTraps": acPfotTraps,
       "acPfotCfgErrorTrap": acPfotCfgErrorTrap,
       "acPfotTable": acPfotTable,
       "acPfotEntry": acPfotEntry,
       "acPfotNodeId": acPfotNodeId,
       "acPfotSlot": acPfotSlot,
       "acPfotPort": acPfotPort,
       "acPfotCfgType": acPfotCfgType,
       "acPfotType": acPfotType,
       "acPfotConnectorType": acPfotConnectorType,
       "acPfotVendorName": acPfotVendorName,
       "acPfotVendorPartNumber": acPfotVendorPartNumber}
)
