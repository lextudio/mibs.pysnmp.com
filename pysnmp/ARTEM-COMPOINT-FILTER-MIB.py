# SNMP MIB module (ARTEM-COMPOINT-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARTEM-COMPOINT-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:43 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

artem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4280)
)
artem.setRevisions(
        ("2005-06-10 12:16",
         "2005-05-25 13:00",
         "2005-05-24 13:24",
         "2005-05-10 07:20",
         "2005-04-21 14:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ArtemFilterProcessing(Integer32, TextualConvention):
    status = "current"
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
        *(("arpProcess", 4),
          ("discard", 2),
          ("filterMAC", 3),
          ("forward", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ArtemFilter_ObjectIdentity = ObjectIdentity
artemFilter = _ArtemFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 7)
)
if mibBuilder.loadTexts:
    artemFilter.setStatus("current")


class _ArtemFilterArpTranslation_Type(TruthValue):
    """Custom type artemFilterArpTranslation based on TruthValue"""


_ArtemFilterArpTranslation_Object = MibScalar
artemFilterArpTranslation = _ArtemFilterArpTranslation_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 1),
    _ArtemFilterArpTranslation_Type()
)
artemFilterArpTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemFilterArpTranslation.setStatus("current")


class _ArtemFilterDefaultProcessing_Type(ArtemFilterProcessing):
    """Custom type artemFilterDefaultProcessing based on ArtemFilterProcessing"""


_ArtemFilterDefaultProcessing_Object = MibScalar
artemFilterDefaultProcessing = _ArtemFilterDefaultProcessing_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 2),
    _ArtemFilterDefaultProcessing_Type()
)
artemFilterDefaultProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemFilterDefaultProcessing.setStatus("current")
_ArtemFilterProtocolTable_Object = MibTable
artemFilterProtocolTable = _ArtemFilterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 3)
)
if mibBuilder.loadTexts:
    artemFilterProtocolTable.setStatus("current")
_ArtemFilterProtocolEntry_Object = MibTableRow
artemFilterProtocolEntry = _ArtemFilterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 3, 1)
)
artemFilterProtocolEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-FILTER-MIB", "artemFilterProtocolType"),
)
if mibBuilder.loadTexts:
    artemFilterProtocolEntry.setStatus("current")
_ArtemFilterProtocolRowStatus_Type = RowStatus
_ArtemFilterProtocolRowStatus_Object = MibTableColumn
artemFilterProtocolRowStatus = _ArtemFilterProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 3, 1, 1),
    _ArtemFilterProtocolRowStatus_Type()
)
artemFilterProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterProtocolRowStatus.setStatus("current")


class _ArtemFilterProtocolType_Type(Integer32):
    """Custom type artemFilterProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArtemFilterProtocolType_Type.__name__ = "Integer32"
_ArtemFilterProtocolType_Object = MibTableColumn
artemFilterProtocolType = _ArtemFilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 3, 1, 2),
    _ArtemFilterProtocolType_Type()
)
artemFilterProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artemFilterProtocolType.setStatus("current")


class _ArtemFilterProtocolProcessing_Type(ArtemFilterProcessing):
    """Custom type artemFilterProtocolProcessing based on ArtemFilterProcessing"""


_ArtemFilterProtocolProcessing_Object = MibTableColumn
artemFilterProtocolProcessing = _ArtemFilterProtocolProcessing_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 3, 1, 3),
    _ArtemFilterProtocolProcessing_Type()
)
artemFilterProtocolProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterProtocolProcessing.setStatus("current")
_ArtemFilterMACTable_Object = MibTable
artemFilterMACTable = _ArtemFilterMACTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4)
)
if mibBuilder.loadTexts:
    artemFilterMACTable.setStatus("current")
_ArtemFilterMACEntry_Object = MibTableRow
artemFilterMACEntry = _ArtemFilterMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4, 1)
)
artemFilterMACEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACIndex"),
)
if mibBuilder.loadTexts:
    artemFilterMACEntry.setStatus("current")


class _ArtemFilterMACIndex_Type(Integer32):
    """Custom type artemFilterMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemFilterMACIndex_Type.__name__ = "Integer32"
_ArtemFilterMACIndex_Object = MibTableColumn
artemFilterMACIndex = _ArtemFilterMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4, 1, 1),
    _ArtemFilterMACIndex_Type()
)
artemFilterMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artemFilterMACIndex.setStatus("current")
_ArtemFilterMACRowStatus_Type = RowStatus
_ArtemFilterMACRowStatus_Object = MibTableColumn
artemFilterMACRowStatus = _ArtemFilterMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4, 1, 2),
    _ArtemFilterMACRowStatus_Type()
)
artemFilterMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterMACRowStatus.setStatus("current")


class _ArtemFilterMACState_Type(Integer32):
    """Custom type artemFilterMACState based on Integer32"""
    defaultValue = 0

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
        *(("conflict", 2),
          ("disabled", 0),
          ("enabled", 1),
          ("invalid", 3))
    )


_ArtemFilterMACState_Type.__name__ = "Integer32"
_ArtemFilterMACState_Object = MibTableColumn
artemFilterMACState = _ArtemFilterMACState_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4, 1, 3),
    _ArtemFilterMACState_Type()
)
artemFilterMACState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterMACState.setStatus("current")
_ArtemFilterMACSourceAddress_Type = MacAddress
_ArtemFilterMACSourceAddress_Object = MibTableColumn
artemFilterMACSourceAddress = _ArtemFilterMACSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4, 1, 4),
    _ArtemFilterMACSourceAddress_Type()
)
artemFilterMACSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterMACSourceAddress.setStatus("current")
_ArtemFilterMACDestAddress_Type = MacAddress
_ArtemFilterMACDestAddress_Object = MibTableColumn
artemFilterMACDestAddress = _ArtemFilterMACDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 4, 1, 5),
    _ArtemFilterMACDestAddress_Type()
)
artemFilterMACDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterMACDestAddress.setStatus("current")
_ArtemFilterMACDestIfTable_Object = MibTable
artemFilterMACDestIfTable = _ArtemFilterMACDestIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 5)
)
if mibBuilder.loadTexts:
    artemFilterMACDestIfTable.setStatus("current")
_ArtemFilterMACDestIfEntry_Object = MibTableRow
artemFilterMACDestIfEntry = _ArtemFilterMACDestIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 5, 1)
)
artemFilterMACDestIfEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    artemFilterMACDestIfEntry.setStatus("current")
_ArtemFilterMACDestIfRowStatus_Type = RowStatus
_ArtemFilterMACDestIfRowStatus_Object = MibTableColumn
artemFilterMACDestIfRowStatus = _ArtemFilterMACDestIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 7, 5, 1, 1),
    _ArtemFilterMACDestIfRowStatus_Type()
)
artemFilterMACDestIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemFilterMACDestIfRowStatus.setStatus("current")

# Managed Objects groups

artemFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 7, 7)
)
artemFilterGroup.setObjects(
      *(("ARTEM-COMPOINT-FILTER-MIB", "artemFilterArpTranslation"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterDefaultProcessing"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterProtocolProcessing"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACState"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACSourceAddress"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACDestAddress"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterProtocolRowStatus"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACRowStatus"),
        ("ARTEM-COMPOINT-FILTER-MIB", "artemFilterMACDestIfRowStatus"))
)
if mibBuilder.loadTexts:
    artemFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARTEM-COMPOINT-FILTER-MIB",
    **{"ArtemFilterProcessing": ArtemFilterProcessing,
       "artem": artem,
       "artemFilter": artemFilter,
       "artemFilterArpTranslation": artemFilterArpTranslation,
       "artemFilterDefaultProcessing": artemFilterDefaultProcessing,
       "artemFilterProtocolTable": artemFilterProtocolTable,
       "artemFilterProtocolEntry": artemFilterProtocolEntry,
       "artemFilterProtocolRowStatus": artemFilterProtocolRowStatus,
       "artemFilterProtocolType": artemFilterProtocolType,
       "artemFilterProtocolProcessing": artemFilterProtocolProcessing,
       "artemFilterMACTable": artemFilterMACTable,
       "artemFilterMACEntry": artemFilterMACEntry,
       "artemFilterMACIndex": artemFilterMACIndex,
       "artemFilterMACRowStatus": artemFilterMACRowStatus,
       "artemFilterMACState": artemFilterMACState,
       "artemFilterMACSourceAddress": artemFilterMACSourceAddress,
       "artemFilterMACDestAddress": artemFilterMACDestAddress,
       "artemFilterMACDestIfTable": artemFilterMACDestIfTable,
       "artemFilterMACDestIfEntry": artemFilterMACDestIfEntry,
       "artemFilterMACDestIfRowStatus": artemFilterMACDestIfRowStatus,
       "artemFilterGroup": artemFilterGroup}
)
