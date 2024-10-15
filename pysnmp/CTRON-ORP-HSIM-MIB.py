# SNMP MIB module (CTRON-ORP-HSIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ORP-HSIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:04 2024
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

(ctOrpHSIM,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctOrpHSIM")

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


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtOrpHSIMTable_Object = MibTable
ctOrpHSIMTable = _CtOrpHSIMTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    ctOrpHSIMTable.setStatus("mandatory")
_CtOrpHSIMEntry_Object = MibTableRow
ctOrpHSIMEntry = _CtOrpHSIMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1)
)
ctOrpHSIMEntry.setIndexNames(
    (0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMSlot"),
    (0, "CTRON-ORP-HSIM-MIB", "ctOrpHSIMIndex"),
)
if mibBuilder.loadTexts:
    ctOrpHSIMEntry.setStatus("mandatory")
_CtOrpHSIMSlot_Type = Integer32
_CtOrpHSIMSlot_Object = MibTableColumn
ctOrpHSIMSlot = _CtOrpHSIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 1),
    _CtOrpHSIMSlot_Type()
)
ctOrpHSIMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctOrpHSIMSlot.setStatus("mandatory")
_CtOrpHSIMIndex_Type = Integer32
_CtOrpHSIMIndex_Object = MibTableColumn
ctOrpHSIMIndex = _CtOrpHSIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 2),
    _CtOrpHSIMIndex_Type()
)
ctOrpHSIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctOrpHSIMIndex.setStatus("mandatory")
_CtOrpHSIMIfRef_Type = ObjectIdentifier
_CtOrpHSIMIfRef_Object = MibTableColumn
ctOrpHSIMIfRef = _CtOrpHSIMIfRef_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 3),
    _CtOrpHSIMIfRef_Type()
)
ctOrpHSIMIfRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctOrpHSIMIfRef.setStatus("mandatory")
_CtOrpHSIMMACAddress_Type = MacAddress
_CtOrpHSIMMACAddress_Object = MibTableColumn
ctOrpHSIMMACAddress = _CtOrpHSIMMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 4),
    _CtOrpHSIMMACAddress_Type()
)
ctOrpHSIMMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctOrpHSIMMACAddress.setStatus("mandatory")
_CtOrpHSIMIPAddress_Type = IpAddress
_CtOrpHSIMIPAddress_Object = MibTableColumn
ctOrpHSIMIPAddress = _CtOrpHSIMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 5),
    _CtOrpHSIMIPAddress_Type()
)
ctOrpHSIMIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctOrpHSIMIPAddress.setStatus("mandatory")
_CtOrpHSIMSubnetMask_Type = IpAddress
_CtOrpHSIMSubnetMask_Object = MibTableColumn
ctOrpHSIMSubnetMask = _CtOrpHSIMSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 6),
    _CtOrpHSIMSubnetMask_Type()
)
ctOrpHSIMSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctOrpHSIMSubnetMask.setStatus("mandatory")
_CtOrpHSIMROCommName_Type = OctetString
_CtOrpHSIMROCommName_Object = MibTableColumn
ctOrpHSIMROCommName = _CtOrpHSIMROCommName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 7),
    _CtOrpHSIMROCommName_Type()
)
ctOrpHSIMROCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctOrpHSIMROCommName.setStatus("mandatory")
_CtOrpHSIMRWCommName_Type = OctetString
_CtOrpHSIMRWCommName_Object = MibTableColumn
ctOrpHSIMRWCommName = _CtOrpHSIMRWCommName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 8),
    _CtOrpHSIMRWCommName_Type()
)
ctOrpHSIMRWCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctOrpHSIMRWCommName.setStatus("mandatory")
_CtOrpHSIMSUCommName_Type = OctetString
_CtOrpHSIMSUCommName_Object = MibTableColumn
ctOrpHSIMSUCommName = _CtOrpHSIMSUCommName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15, 1, 1, 9),
    _CtOrpHSIMSUCommName_Type()
)
ctOrpHSIMSUCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctOrpHSIMSUCommName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ORP-HSIM-MIB",
    **{"MacAddress": MacAddress,
       "ctOrpHSIMTable": ctOrpHSIMTable,
       "ctOrpHSIMEntry": ctOrpHSIMEntry,
       "ctOrpHSIMSlot": ctOrpHSIMSlot,
       "ctOrpHSIMIndex": ctOrpHSIMIndex,
       "ctOrpHSIMIfRef": ctOrpHSIMIfRef,
       "ctOrpHSIMMACAddress": ctOrpHSIMMACAddress,
       "ctOrpHSIMIPAddress": ctOrpHSIMIPAddress,
       "ctOrpHSIMSubnetMask": ctOrpHSIMSubnetMask,
       "ctOrpHSIMROCommName": ctOrpHSIMROCommName,
       "ctOrpHSIMRWCommName": ctOrpHSIMRWCommName,
       "ctOrpHSIMSUCommName": ctOrpHSIMSUCommName}
)
