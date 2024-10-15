# SNMP MIB module (CISCO-VISM-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:54 2024
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

(vismPort,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "vismPort")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoVismPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 92)
)
ciscoVismPortMIB.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismPortCnfGrp_ObjectIdentity = ObjectIdentity
vismPortCnfGrp = _VismPortCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1)
)
_VismPortCnfGrpTable_Object = MibTable
vismPortCnfGrpTable = _VismPortCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vismPortCnfGrpTable.setStatus("current")
_VismPortCnfGrpEntry_Object = MibTableRow
vismPortCnfGrpEntry = _VismPortCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1)
)
vismPortCnfGrpEntry.setIndexNames(
    (0, "CISCO-VISM-PORT-MIB", "vismPortNum"),
)
if mibBuilder.loadTexts:
    vismPortCnfGrpEntry.setStatus("current")


class _VismPortNum_Type(Integer32):
    """Custom type vismPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismPortNum_Type.__name__ = "Integer32"
_VismPortNum_Object = MibTableColumn
vismPortNum = _VismPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 1),
    _VismPortNum_Type()
)
vismPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPortNum.setStatus("current")


class _VismPortRowStatus_Type(Integer32):
    """Custom type vismPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_VismPortRowStatus_Type.__name__ = "Integer32"
_VismPortRowStatus_Object = MibTableColumn
vismPortRowStatus = _VismPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 2),
    _VismPortRowStatus_Type()
)
vismPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismPortRowStatus.setStatus("current")


class _VismPortLineNum_Type(Integer32):
    """Custom type vismPortLineNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VismPortLineNum_Type.__name__ = "Integer32"
_VismPortLineNum_Object = MibTableColumn
vismPortLineNum = _VismPortLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 3),
    _VismPortLineNum_Type()
)
vismPortLineNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismPortLineNum.setStatus("current")


class _VismPortType_Type(Integer32):
    """Custom type vismPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userPort", 2),
          ("voIP", 1))
    )


_VismPortType_Type.__name__ = "Integer32"
_VismPortType_Object = MibTableColumn
vismPortType = _VismPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 4),
    _VismPortType_Type()
)
vismPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismPortType.setStatus("current")


class _VismPortDs0ConfigBitMap_Type(Integer32):
    """Custom type vismPortDs0ConfigBitMap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VismPortDs0ConfigBitMap_Type.__name__ = "Integer32"
_VismPortDs0ConfigBitMap_Object = MibTableColumn
vismPortDs0ConfigBitMap = _VismPortDs0ConfigBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 5),
    _VismPortDs0ConfigBitMap_Type()
)
vismPortDs0ConfigBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismPortDs0ConfigBitMap.setStatus("current")


class _VismPortSpeed_Type(Integer32):
    """Custom type vismPortSpeed based on Integer32"""
    defaultValue = 5651320

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5651320),
    )


_VismPortSpeed_Type.__name__ = "Integer32"
_VismPortSpeed_Object = MibTableColumn
vismPortSpeed = _VismPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 6),
    _VismPortSpeed_Type()
)
vismPortSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismPortSpeed.setStatus("current")


class _VismPortState_Type(Integer32):
    """Custom type vismPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notConfigured", 1))
    )


_VismPortState_Type.__name__ = "Integer32"
_VismPortState_Object = MibTableColumn
vismPortState = _VismPortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 7),
    _VismPortState_Type()
)
vismPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPortState.setStatus("current")
_CiscoVismPortMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismPortMIBConformance = _CiscoVismPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 92, 2)
)
_CiscoVismPortMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismPortMIBGroups = _CiscoVismPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 1)
)
_CiscoVismPortMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismPortMIBCompliances = _CiscoVismPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 2)
)

# Managed Objects groups

ciscoVismPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 1, 1)
)
ciscoVismPortGroup.setObjects(
      *(("CISCO-VISM-PORT-MIB", "vismPortNum"),
        ("CISCO-VISM-PORT-MIB", "vismPortRowStatus"),
        ("CISCO-VISM-PORT-MIB", "vismPortLineNum"),
        ("CISCO-VISM-PORT-MIB", "vismPortType"),
        ("CISCO-VISM-PORT-MIB", "vismPortDs0ConfigBitMap"),
        ("CISCO-VISM-PORT-MIB", "vismPortSpeed"),
        ("CISCO-VISM-PORT-MIB", "vismPortState"))
)
if mibBuilder.loadTexts:
    ciscoVismPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-PORT-MIB",
    **{"vismPortCnfGrp": vismPortCnfGrp,
       "vismPortCnfGrpTable": vismPortCnfGrpTable,
       "vismPortCnfGrpEntry": vismPortCnfGrpEntry,
       "vismPortNum": vismPortNum,
       "vismPortRowStatus": vismPortRowStatus,
       "vismPortLineNum": vismPortLineNum,
       "vismPortType": vismPortType,
       "vismPortDs0ConfigBitMap": vismPortDs0ConfigBitMap,
       "vismPortSpeed": vismPortSpeed,
       "vismPortState": vismPortState,
       "ciscoVismPortMIB": ciscoVismPortMIB,
       "ciscoVismPortMIBConformance": ciscoVismPortMIBConformance,
       "ciscoVismPortMIBGroups": ciscoVismPortMIBGroups,
       "ciscoVismPortGroup": ciscoVismPortGroup,
       "ciscoVismPortMIBCompliances": ciscoVismPortMIBCompliances,
       "ciscoVismPortCompliance": ciscoVismPortCompliance}
)
