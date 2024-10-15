# SNMP MIB module (ATT-CNM-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:16 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_cnmAgent_ObjectIdentity = ObjectIdentity
att_cnmAgent = _Att_cnmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 9)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_cnm_ObjectIdentity = ObjectIdentity
att_cnm = _Att_cnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15)
)
_Att_cnm_ds1_ObjectIdentity = ObjectIdentity
att_cnm_ds1 = _Att_cnm_ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3)
)
_AttCNMds1ConfigTable_Object = MibTable
attCNMds1ConfigTable = _AttCNMds1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    attCNMds1ConfigTable.setStatus("mandatory")
_AttCNMds1ConfigEntry_Object = MibTableRow
attCNMds1ConfigEntry = _AttCNMds1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1)
)
attCNMds1ConfigEntry.setIndexNames(
    (0, "ATT-CNM-DS1-MIB", "attCNMds1ConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMds1ConfigEntry.setStatus("mandatory")
_AttCNMds1ConfigIndex_Type = Integer32
_AttCNMds1ConfigIndex_Object = MibTableColumn
attCNMds1ConfigIndex = _AttCNMds1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 1),
    _AttCNMds1ConfigIndex_Type()
)
attCNMds1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ConfigIndex.setStatus("mandatory")


class _AttCNMds1LineType_Type(Integer32):
    """Custom type attCNMds1LineType based on Integer32"""
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
        *(("ds1ANSI-ESF", 4),
          ("ds1D4", 3),
          ("ds1ESF", 2),
          ("ds1G704", 5),
          ("ds1G704-CRC", 6),
          ("other", 1))
    )


_AttCNMds1LineType_Type.__name__ = "Integer32"
_AttCNMds1LineType_Object = MibTableColumn
attCNMds1LineType = _AttCNMds1LineType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 2),
    _AttCNMds1LineType_Type()
)
attCNMds1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1LineType.setStatus("mandatory")


class _AttCNMds1ZeroCoding_Type(Integer32):
    """Custom type attCNMds1ZeroCoding based on Integer32"""
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
        *(("ds1B8ZS", 2),
          ("ds1HDB3", 4),
          ("ds1InvertedHDLC", 3),
          ("ds1JammedBit", 1),
          ("ds1ZBTSI", 5))
    )


_AttCNMds1ZeroCoding_Type.__name__ = "Integer32"
_AttCNMds1ZeroCoding_Object = MibTableColumn
attCNMds1ZeroCoding = _AttCNMds1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 3),
    _AttCNMds1ZeroCoding_Type()
)
attCNMds1ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ZeroCoding.setStatus("mandatory")
_AttCNMds1ErrorsMaxIntervals_Type = Integer32
_AttCNMds1ErrorsMaxIntervals_Object = MibTableColumn
attCNMds1ErrorsMaxIntervals = _AttCNMds1ErrorsMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 4),
    _AttCNMds1ErrorsMaxIntervals_Type()
)
attCNMds1ErrorsMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ErrorsMaxIntervals.setStatus("mandatory")
_AttCNMds1ErrorsIntervalLen_Type = Integer32
_AttCNMds1ErrorsIntervalLen_Object = MibTableColumn
attCNMds1ErrorsIntervalLen = _AttCNMds1ErrorsIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 1, 1, 5),
    _AttCNMds1ErrorsIntervalLen_Type()
)
attCNMds1ErrorsIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ErrorsIntervalLen.setStatus("mandatory")
_AttCNMds1StatusTable_Object = MibTable
attCNMds1StatusTable = _AttCNMds1StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2)
)
if mibBuilder.loadTexts:
    attCNMds1StatusTable.setStatus("mandatory")
_AttCNMds1StatusEntry_Object = MibTableRow
attCNMds1StatusEntry = _AttCNMds1StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2, 1)
)
attCNMds1StatusEntry.setIndexNames(
    (0, "ATT-CNM-DS1-MIB", "attCNMds1StatusIndex"),
)
if mibBuilder.loadTexts:
    attCNMds1StatusEntry.setStatus("mandatory")
_AttCNMds1StatusIndex_Type = Integer32
_AttCNMds1StatusIndex_Object = MibTableColumn
attCNMds1StatusIndex = _AttCNMds1StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2, 1, 1),
    _AttCNMds1StatusIndex_Type()
)
attCNMds1StatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1StatusIndex.setStatus("mandatory")
_AttCNMds1LineStatus_Type = Integer32
_AttCNMds1LineStatus_Object = MibTableColumn
attCNMds1LineStatus = _AttCNMds1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 2, 1, 2),
    _AttCNMds1LineStatus_Type()
)
attCNMds1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1LineStatus.setStatus("mandatory")
_AttCNMds1ErrorsTable_Object = MibTable
attCNMds1ErrorsTable = _AttCNMds1ErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3)
)
if mibBuilder.loadTexts:
    attCNMds1ErrorsTable.setStatus("mandatory")
_AttCNMds1ErrorsEntry_Object = MibTableRow
attCNMds1ErrorsEntry = _AttCNMds1ErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1)
)
attCNMds1ErrorsEntry.setIndexNames(
    (0, "ATT-CNM-DS1-MIB", "attCNMds1ErrorsIndex"),
    (0, "ATT-CNM-DS1-MIB", "attCNMds1ErrorsInterval"),
)
if mibBuilder.loadTexts:
    attCNMds1ErrorsEntry.setStatus("mandatory")
_AttCNMds1ErrorsIndex_Type = Integer32
_AttCNMds1ErrorsIndex_Object = MibTableColumn
attCNMds1ErrorsIndex = _AttCNMds1ErrorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 1),
    _AttCNMds1ErrorsIndex_Type()
)
attCNMds1ErrorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ErrorsIndex.setStatus("mandatory")
_AttCNMds1ErrorsInterval_Type = Integer32
_AttCNMds1ErrorsInterval_Object = MibTableColumn
attCNMds1ErrorsInterval = _AttCNMds1ErrorsInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 2),
    _AttCNMds1ErrorsInterval_Type()
)
attCNMds1ErrorsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ErrorsInterval.setStatus("mandatory")
_AttCNMds1ErrorsTimeStamp_Type = Integer32
_AttCNMds1ErrorsTimeStamp_Object = MibTableColumn
attCNMds1ErrorsTimeStamp = _AttCNMds1ErrorsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 3),
    _AttCNMds1ErrorsTimeStamp_Type()
)
attCNMds1ErrorsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ErrorsTimeStamp.setStatus("mandatory")


class _AttCNMds1ErrorsLocalTime_Type(DisplayString):
    """Custom type attCNMds1ErrorsLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMds1ErrorsLocalTime_Type.__name__ = "DisplayString"
_AttCNMds1ErrorsLocalTime_Object = MibTableColumn
attCNMds1ErrorsLocalTime = _AttCNMds1ErrorsLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 4),
    _AttCNMds1ErrorsLocalTime_Type()
)
attCNMds1ErrorsLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ErrorsLocalTime.setStatus("mandatory")
_AttCNMds1LCVs_Type = Gauge32
_AttCNMds1LCVs_Object = MibTableColumn
attCNMds1LCVs = _AttCNMds1LCVs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 5),
    _AttCNMds1LCVs_Type()
)
attCNMds1LCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1LCVs.setStatus("mandatory")
_AttCNMds1LESs_Type = Gauge32
_AttCNMds1LESs_Object = MibTableColumn
attCNMds1LESs = _AttCNMds1LESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 6),
    _AttCNMds1LESs_Type()
)
attCNMds1LESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1LESs.setStatus("mandatory")
_AttCNMds1LSESs_Type = Gauge32
_AttCNMds1LSESs_Object = MibTableColumn
attCNMds1LSESs = _AttCNMds1LSESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 7),
    _AttCNMds1LSESs_Type()
)
attCNMds1LSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1LSESs.setStatus("mandatory")
_AttCNMds1CVs_Type = Gauge32
_AttCNMds1CVs_Object = MibTableColumn
attCNMds1CVs = _AttCNMds1CVs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 8),
    _AttCNMds1CVs_Type()
)
attCNMds1CVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1CVs.setStatus("mandatory")
_AttCNMds1ESs_Type = Gauge32
_AttCNMds1ESs_Object = MibTableColumn
attCNMds1ESs = _AttCNMds1ESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 9),
    _AttCNMds1ESs_Type()
)
attCNMds1ESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1ESs.setStatus("mandatory")
_AttCNMds1SESs_Type = Gauge32
_AttCNMds1SESs_Object = MibTableColumn
attCNMds1SESs = _AttCNMds1SESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 10),
    _AttCNMds1SESs_Type()
)
attCNMds1SESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1SESs.setStatus("mandatory")
_AttCNMds1SEFSs_Type = Gauge32
_AttCNMds1SEFSs_Object = MibTableColumn
attCNMds1SEFSs = _AttCNMds1SEFSs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 11),
    _AttCNMds1SEFSs_Type()
)
attCNMds1SEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1SEFSs.setStatus("mandatory")
_AttCNMds1UASs_Type = Gauge32
_AttCNMds1UASs_Object = MibTableColumn
attCNMds1UASs = _AttCNMds1UASs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 3, 3, 1, 12),
    _AttCNMds1UASs_Type()
)
attCNMds1UASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds1UASs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-DS1-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-ds1": att_cnm_ds1,
       "attCNMds1ConfigTable": attCNMds1ConfigTable,
       "attCNMds1ConfigEntry": attCNMds1ConfigEntry,
       "attCNMds1ConfigIndex": attCNMds1ConfigIndex,
       "attCNMds1LineType": attCNMds1LineType,
       "attCNMds1ZeroCoding": attCNMds1ZeroCoding,
       "attCNMds1ErrorsMaxIntervals": attCNMds1ErrorsMaxIntervals,
       "attCNMds1ErrorsIntervalLen": attCNMds1ErrorsIntervalLen,
       "attCNMds1StatusTable": attCNMds1StatusTable,
       "attCNMds1StatusEntry": attCNMds1StatusEntry,
       "attCNMds1StatusIndex": attCNMds1StatusIndex,
       "attCNMds1LineStatus": attCNMds1LineStatus,
       "attCNMds1ErrorsTable": attCNMds1ErrorsTable,
       "attCNMds1ErrorsEntry": attCNMds1ErrorsEntry,
       "attCNMds1ErrorsIndex": attCNMds1ErrorsIndex,
       "attCNMds1ErrorsInterval": attCNMds1ErrorsInterval,
       "attCNMds1ErrorsTimeStamp": attCNMds1ErrorsTimeStamp,
       "attCNMds1ErrorsLocalTime": attCNMds1ErrorsLocalTime,
       "attCNMds1LCVs": attCNMds1LCVs,
       "attCNMds1LESs": attCNMds1LESs,
       "attCNMds1LSESs": attCNMds1LSESs,
       "attCNMds1CVs": attCNMds1CVs,
       "attCNMds1ESs": attCNMds1ESs,
       "attCNMds1SESs": attCNMds1SESs,
       "attCNMds1SEFSs": attCNMds1SEFSs,
       "attCNMds1UASs": attCNMds1UASs}
)
