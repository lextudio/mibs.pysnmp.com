# SNMP MIB module (ATT-CNM-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-DS3-MIB
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
_Att_cnm_ds3_ObjectIdentity = ObjectIdentity
att_cnm_ds3 = _Att_cnm_ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4)
)
_AttCNMds3ConfigTable_Object = MibTable
attCNMds3ConfigTable = _AttCNMds3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    attCNMds3ConfigTable.setStatus("mandatory")
_AttCNMds3ConfigEntry_Object = MibTableRow
attCNMds3ConfigEntry = _AttCNMds3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1)
)
attCNMds3ConfigEntry.setIndexNames(
    (0, "ATT-CNM-DS3-MIB", "attCNMds3ConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMds3ConfigEntry.setStatus("mandatory")
_AttCNMds3ConfigIndex_Type = Integer32
_AttCNMds3ConfigIndex_Object = MibTableColumn
attCNMds3ConfigIndex = _AttCNMds3ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 1),
    _AttCNMds3ConfigIndex_Type()
)
attCNMds3ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ConfigIndex.setStatus("mandatory")


class _AttCNMds3LineType_Type(Integer32):
    """Custom type attCNMds3LineType based on Integer32"""
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
        *(("ds3CbitParity", 4),
          ("ds3ClearChannel", 5),
          ("ds3M23", 2),
          ("ds3SYNTRAN", 3),
          ("other", 1))
    )


_AttCNMds3LineType_Type.__name__ = "Integer32"
_AttCNMds3LineType_Object = MibTableColumn
attCNMds3LineType = _AttCNMds3LineType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 2),
    _AttCNMds3LineType_Type()
)
attCNMds3LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3LineType.setStatus("mandatory")


class _AttCNMds3ZeroCoding_Type(Integer32):
    """Custom type attCNMds3ZeroCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3B3ZS", 2),
          ("ds3other", 1))
    )


_AttCNMds3ZeroCoding_Type.__name__ = "Integer32"
_AttCNMds3ZeroCoding_Object = MibTableColumn
attCNMds3ZeroCoding = _AttCNMds3ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 3),
    _AttCNMds3ZeroCoding_Type()
)
attCNMds3ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ZeroCoding.setStatus("mandatory")
_AttCNMds3ErrorsMaxIntervals_Type = Integer32
_AttCNMds3ErrorsMaxIntervals_Object = MibTableColumn
attCNMds3ErrorsMaxIntervals = _AttCNMds3ErrorsMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 4),
    _AttCNMds3ErrorsMaxIntervals_Type()
)
attCNMds3ErrorsMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ErrorsMaxIntervals.setStatus("mandatory")
_AttCNMds3ErrorsIntervalLen_Type = Integer32
_AttCNMds3ErrorsIntervalLen_Object = MibTableColumn
attCNMds3ErrorsIntervalLen = _AttCNMds3ErrorsIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 5),
    _AttCNMds3ErrorsIntervalLen_Type()
)
attCNMds3ErrorsIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ErrorsIntervalLen.setStatus("mandatory")
_AttCNMds3StatusTable_Object = MibTable
attCNMds3StatusTable = _AttCNMds3StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2)
)
if mibBuilder.loadTexts:
    attCNMds3StatusTable.setStatus("mandatory")
_AttCNMds3StatusEntry_Object = MibTableRow
attCNMds3StatusEntry = _AttCNMds3StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1)
)
attCNMds3StatusEntry.setIndexNames(
    (0, "ATT-CNM-DS3-MIB", "attCNMds3StatusIndex"),
)
if mibBuilder.loadTexts:
    attCNMds3StatusEntry.setStatus("mandatory")
_AttCNMds3StatusIndex_Type = Integer32
_AttCNMds3StatusIndex_Object = MibTableColumn
attCNMds3StatusIndex = _AttCNMds3StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1, 1),
    _AttCNMds3StatusIndex_Type()
)
attCNMds3StatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3StatusIndex.setStatus("mandatory")
_AttCNMds3LineStatus_Type = Integer32
_AttCNMds3LineStatus_Object = MibTableColumn
attCNMds3LineStatus = _AttCNMds3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1, 2),
    _AttCNMds3LineStatus_Type()
)
attCNMds3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3LineStatus.setStatus("mandatory")
_AttCNMds3ErrorsTable_Object = MibTable
attCNMds3ErrorsTable = _AttCNMds3ErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3)
)
if mibBuilder.loadTexts:
    attCNMds3ErrorsTable.setStatus("mandatory")
_AttCNMds3ErrorsEntry_Object = MibTableRow
attCNMds3ErrorsEntry = _AttCNMds3ErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1)
)
attCNMds3ErrorsEntry.setIndexNames(
    (0, "ATT-CNM-DS3-MIB", "attCNMds3ErrorsIndex"),
    (0, "ATT-CNM-DS3-MIB", "attCNMds3ErrorsInterval"),
)
if mibBuilder.loadTexts:
    attCNMds3ErrorsEntry.setStatus("mandatory")
_AttCNMds3ErrorsIndex_Type = Integer32
_AttCNMds3ErrorsIndex_Object = MibTableColumn
attCNMds3ErrorsIndex = _AttCNMds3ErrorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 1),
    _AttCNMds3ErrorsIndex_Type()
)
attCNMds3ErrorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ErrorsIndex.setStatus("mandatory")
_AttCNMds3ErrorsInterval_Type = Integer32
_AttCNMds3ErrorsInterval_Object = MibTableColumn
attCNMds3ErrorsInterval = _AttCNMds3ErrorsInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 2),
    _AttCNMds3ErrorsInterval_Type()
)
attCNMds3ErrorsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ErrorsInterval.setStatus("mandatory")
_AttCNMds3ErrorsTimeStamp_Type = Integer32
_AttCNMds3ErrorsTimeStamp_Object = MibTableColumn
attCNMds3ErrorsTimeStamp = _AttCNMds3ErrorsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 3),
    _AttCNMds3ErrorsTimeStamp_Type()
)
attCNMds3ErrorsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ErrorsTimeStamp.setStatus("mandatory")


class _AttCNMds3ErrorsLocalTime_Type(DisplayString):
    """Custom type attCNMds3ErrorsLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMds3ErrorsLocalTime_Type.__name__ = "DisplayString"
_AttCNMds3ErrorsLocalTime_Object = MibTableColumn
attCNMds3ErrorsLocalTime = _AttCNMds3ErrorsLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 4),
    _AttCNMds3ErrorsLocalTime_Type()
)
attCNMds3ErrorsLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ErrorsLocalTime.setStatus("mandatory")
_AttCNMds3LCVs_Type = Gauge32
_AttCNMds3LCVs_Object = MibTableColumn
attCNMds3LCVs = _AttCNMds3LCVs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 5),
    _AttCNMds3LCVs_Type()
)
attCNMds3LCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3LCVs.setStatus("mandatory")
_AttCNMds3LESs_Type = Gauge32
_AttCNMds3LESs_Object = MibTableColumn
attCNMds3LESs = _AttCNMds3LESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 6),
    _AttCNMds3LESs_Type()
)
attCNMds3LESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3LESs.setStatus("mandatory")
_AttCNMds3LSESs_Type = Gauge32
_AttCNMds3LSESs_Object = MibTableColumn
attCNMds3LSESs = _AttCNMds3LSESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 7),
    _AttCNMds3LSESs_Type()
)
attCNMds3LSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3LSESs.setStatus("mandatory")
_AttCNMds3CVs_Type = Gauge32
_AttCNMds3CVs_Object = MibTableColumn
attCNMds3CVs = _AttCNMds3CVs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 8),
    _AttCNMds3CVs_Type()
)
attCNMds3CVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3CVs.setStatus("mandatory")
_AttCNMds3ESs_Type = Gauge32
_AttCNMds3ESs_Object = MibTableColumn
attCNMds3ESs = _AttCNMds3ESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 9),
    _AttCNMds3ESs_Type()
)
attCNMds3ESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3ESs.setStatus("mandatory")
_AttCNMds3SESs_Type = Gauge32
_AttCNMds3SESs_Object = MibTableColumn
attCNMds3SESs = _AttCNMds3SESs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 10),
    _AttCNMds3SESs_Type()
)
attCNMds3SESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3SESs.setStatus("mandatory")
_AttCNMds3SEFSs_Type = Gauge32
_AttCNMds3SEFSs_Object = MibTableColumn
attCNMds3SEFSs = _AttCNMds3SEFSs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 11),
    _AttCNMds3SEFSs_Type()
)
attCNMds3SEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3SEFSs.setStatus("mandatory")
_AttCNMds3UASs_Type = Gauge32
_AttCNMds3UASs_Object = MibTableColumn
attCNMds3UASs = _AttCNMds3UASs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 12),
    _AttCNMds3UASs_Type()
)
attCNMds3UASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMds3UASs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-DS3-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-ds3": att_cnm_ds3,
       "attCNMds3ConfigTable": attCNMds3ConfigTable,
       "attCNMds3ConfigEntry": attCNMds3ConfigEntry,
       "attCNMds3ConfigIndex": attCNMds3ConfigIndex,
       "attCNMds3LineType": attCNMds3LineType,
       "attCNMds3ZeroCoding": attCNMds3ZeroCoding,
       "attCNMds3ErrorsMaxIntervals": attCNMds3ErrorsMaxIntervals,
       "attCNMds3ErrorsIntervalLen": attCNMds3ErrorsIntervalLen,
       "attCNMds3StatusTable": attCNMds3StatusTable,
       "attCNMds3StatusEntry": attCNMds3StatusEntry,
       "attCNMds3StatusIndex": attCNMds3StatusIndex,
       "attCNMds3LineStatus": attCNMds3LineStatus,
       "attCNMds3ErrorsTable": attCNMds3ErrorsTable,
       "attCNMds3ErrorsEntry": attCNMds3ErrorsEntry,
       "attCNMds3ErrorsIndex": attCNMds3ErrorsIndex,
       "attCNMds3ErrorsInterval": attCNMds3ErrorsInterval,
       "attCNMds3ErrorsTimeStamp": attCNMds3ErrorsTimeStamp,
       "attCNMds3ErrorsLocalTime": attCNMds3ErrorsLocalTime,
       "attCNMds3LCVs": attCNMds3LCVs,
       "attCNMds3LESs": attCNMds3LESs,
       "attCNMds3LSESs": attCNMds3LSESs,
       "attCNMds3CVs": attCNMds3CVs,
       "attCNMds3ESs": attCNMds3ESs,
       "attCNMds3SESs": attCNMds3SESs,
       "attCNMds3SEFSs": attCNMds3SEFSs,
       "attCNMds3UASs": attCNMds3UASs}
)
