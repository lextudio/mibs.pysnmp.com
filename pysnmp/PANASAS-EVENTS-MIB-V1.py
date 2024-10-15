# SNMP MIB module (PANASAS-EVENTS-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANASAS-EVENTS-MIB-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:36 2024
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

(panFs,) = mibBuilder.importSymbols(
    "PANASAS-PANFS-MIB-V1",
    "panFs")

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

panEvents = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1)
)
panEvents.setRevisions(
        ("2011-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PanEventTableSize_Type(Integer32):
    """Custom type panEventTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PanEventTableSize_Type.__name__ = "Integer32"
_PanEventTableSize_Object = MibScalar
panEventTableSize = _PanEventTableSize_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 1),
    _PanEventTableSize_Type()
)
panEventTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventTableSize.setStatus("current")
_PanEventTable_Object = MibTable
panEventTable = _PanEventTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    panEventTable.setStatus("current")
_PanEventEntry_Object = MibTableRow
panEventEntry = _PanEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1)
)
panEventEntry.setIndexNames(
    (0, "PANASAS-EVENTS-MIB-V1", "panEventIndex"),
)
if mibBuilder.loadTexts:
    panEventEntry.setStatus("current")


class _PanEventIndex_Type(Integer32):
    """Custom type panEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PanEventIndex_Type.__name__ = "Integer32"
_PanEventIndex_Object = MibTableColumn
panEventIndex = _PanEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 1),
    _PanEventIndex_Type()
)
panEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventIndex.setStatus("current")
_PanEventCategory_Type = DisplayString
_PanEventCategory_Object = MibTableColumn
panEventCategory = _PanEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 2),
    _PanEventCategory_Type()
)
panEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventCategory.setStatus("current")
_PanEventDate_Type = DisplayString
_PanEventDate_Object = MibTableColumn
panEventDate = _PanEventDate_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 3),
    _PanEventDate_Type()
)
panEventDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventDate.setStatus("current")
_PanEventTime_Type = DisplayString
_PanEventTime_Object = MibTableColumn
panEventTime = _PanEventTime_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 4),
    _PanEventTime_Type()
)
panEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventTime.setStatus("current")
_PanEventShelfName_Type = DisplayString
_PanEventShelfName_Object = MibTableColumn
panEventShelfName = _PanEventShelfName_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 5),
    _PanEventShelfName_Type()
)
panEventShelfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventShelfName.setStatus("current")
_PanEventShelfSlot_Type = Unsigned32
_PanEventShelfSlot_Object = MibTableColumn
panEventShelfSlot = _PanEventShelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 6),
    _PanEventShelfSlot_Type()
)
panEventShelfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventShelfSlot.setStatus("current")
_PanEventHwDesc_Type = DisplayString
_PanEventHwDesc_Object = MibTableColumn
panEventHwDesc = _PanEventHwDesc_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 7),
    _PanEventHwDesc_Type()
)
panEventHwDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventHwDesc.setStatus("current")
_PanEventBladeIPAddr_Type = IpAddress
_PanEventBladeIPAddr_Object = MibTableColumn
panEventBladeIPAddr = _PanEventBladeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 8),
    _PanEventBladeIPAddr_Type()
)
panEventBladeIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventBladeIPAddr.setStatus("current")
_PanEventText_Type = DisplayString
_PanEventText_Object = MibTableColumn
panEventText = _PanEventText_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 9),
    _PanEventText_Type()
)
panEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventText.setStatus("current")


class _PanEventCode_Type(Integer32):
    """Custom type panEventCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PanEventCode_Type.__name__ = "Integer32"
_PanEventCode_Object = MibTableColumn
panEventCode = _PanEventCode_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 10),
    _PanEventCode_Type()
)
panEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panEventCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANASAS-EVENTS-MIB-V1",
    **{"panEvents": panEvents,
       "panEventTableSize": panEventTableSize,
       "panEventTable": panEventTable,
       "panEventEntry": panEventEntry,
       "panEventIndex": panEventIndex,
       "panEventCategory": panEventCategory,
       "panEventDate": panEventDate,
       "panEventTime": panEventTime,
       "panEventShelfName": panEventShelfName,
       "panEventShelfSlot": panEventShelfSlot,
       "panEventHwDesc": panEventHwDesc,
       "panEventBladeIPAddr": panEventBladeIPAddr,
       "panEventText": panEventText,
       "panEventCode": panEventCode}
)
