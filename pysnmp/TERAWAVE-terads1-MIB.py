# SNMP MIB module (TERAWAVE-terads1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-terads1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:23 2024
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

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraDs1Group_ObjectIdentity = ObjectIdentity
teraDs1Group = _TeraDs1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 11)
)
_Teradsx1CurrentTable_Object = MibTable
teradsx1CurrentTable = _Teradsx1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1)
)
if mibBuilder.loadTexts:
    teradsx1CurrentTable.setStatus("mandatory")
_Teradsx1CurrentTableEntry_Object = MibTableRow
teradsx1CurrentTableEntry = _Teradsx1CurrentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1)
)
teradsx1CurrentTableEntry.setIndexNames(
    (0, "TERAWAVE-terads1-MIB", "teradsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    teradsx1CurrentTableEntry.setStatus("mandatory")
_Teradsx1CurrentIndex_Type = Integer32
_Teradsx1CurrentIndex_Object = MibTableColumn
teradsx1CurrentIndex = _Teradsx1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 1),
    _Teradsx1CurrentIndex_Type()
)
teradsx1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentIndex.setStatus("mandatory")
_Teradsx1CurrentESs_Type = Integer32
_Teradsx1CurrentESs_Object = MibTableColumn
teradsx1CurrentESs = _Teradsx1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 2),
    _Teradsx1CurrentESs_Type()
)
teradsx1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentESs.setStatus("mandatory")
_Teradsx1CurrentSESs_Type = Integer32
_Teradsx1CurrentSESs_Object = MibTableColumn
teradsx1CurrentSESs = _Teradsx1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 3),
    _Teradsx1CurrentSESs_Type()
)
teradsx1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentSESs.setStatus("mandatory")
_Teradsx1CurrentSEFSs_Type = Integer32
_Teradsx1CurrentSEFSs_Object = MibTableColumn
teradsx1CurrentSEFSs = _Teradsx1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 4),
    _Teradsx1CurrentSEFSs_Type()
)
teradsx1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentSEFSs.setStatus("mandatory")
_Teradsx1CurrentUASs_Type = Integer32
_Teradsx1CurrentUASs_Object = MibTableColumn
teradsx1CurrentUASs = _Teradsx1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 5),
    _Teradsx1CurrentUASs_Type()
)
teradsx1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentUASs.setStatus("mandatory")
_Teradsx1CurrentCSSs_Type = Gauge32
_Teradsx1CurrentCSSs_Object = MibTableColumn
teradsx1CurrentCSSs = _Teradsx1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 6),
    _Teradsx1CurrentCSSs_Type()
)
teradsx1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentCSSs.setStatus("mandatory")
_Teradsx1CurrentPCVs_Type = Gauge32
_Teradsx1CurrentPCVs_Object = MibTableColumn
teradsx1CurrentPCVs = _Teradsx1CurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 7),
    _Teradsx1CurrentPCVs_Type()
)
teradsx1CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentPCVs.setStatus("mandatory")
_Teradsx1CurrentLESs_Type = Gauge32
_Teradsx1CurrentLESs_Object = MibTableColumn
teradsx1CurrentLESs = _Teradsx1CurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 8),
    _Teradsx1CurrentLESs_Type()
)
teradsx1CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentLESs.setStatus("mandatory")
_Teradsx1CurrentBESs_Type = Gauge32
_Teradsx1CurrentBESs_Object = MibTableColumn
teradsx1CurrentBESs = _Teradsx1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 9),
    _Teradsx1CurrentBESs_Type()
)
teradsx1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentBESs.setStatus("mandatory")
_Teradsx1CurrentDMs_Type = Gauge32
_Teradsx1CurrentDMs_Object = MibTableColumn
teradsx1CurrentDMs = _Teradsx1CurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 10),
    _Teradsx1CurrentDMs_Type()
)
teradsx1CurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentDMs.setStatus("mandatory")
_Teradsx1CurrentLCVs_Type = Gauge32
_Teradsx1CurrentLCVs_Object = MibTableColumn
teradsx1CurrentLCVs = _Teradsx1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 11),
    _Teradsx1CurrentLCVs_Type()
)
teradsx1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentLCVs.setStatus("mandatory")
_Teradsx1CurrentLOF_Type = Gauge32
_Teradsx1CurrentLOF_Object = MibTableColumn
teradsx1CurrentLOF = _Teradsx1CurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 12),
    _Teradsx1CurrentLOF_Type()
)
teradsx1CurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentLOF.setStatus("mandatory")
_Teradsx1CurrentYELLOW_Type = Gauge32
_Teradsx1CurrentYELLOW_Object = MibTableColumn
teradsx1CurrentYELLOW = _Teradsx1CurrentYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 13),
    _Teradsx1CurrentYELLOW_Type()
)
teradsx1CurrentYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentYELLOW.setStatus("mandatory")
_Teradsx1CurrentAIS_Type = Gauge32
_Teradsx1CurrentAIS_Object = MibTableColumn
teradsx1CurrentAIS = _Teradsx1CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 14),
    _Teradsx1CurrentAIS_Type()
)
teradsx1CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1CurrentAIS.setStatus("mandatory")
_TeraStandarddsx1CurrentLOF_Type = Gauge32
_TeraStandarddsx1CurrentLOF_Object = MibTableColumn
teraStandarddsx1CurrentLOF = _TeraStandarddsx1CurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 15),
    _TeraStandarddsx1CurrentLOF_Type()
)
teraStandarddsx1CurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1CurrentLOF.setStatus("mandatory")
_TeraStandarddsx1CurrentYELLOW_Type = Gauge32
_TeraStandarddsx1CurrentYELLOW_Object = MibTableColumn
teraStandarddsx1CurrentYELLOW = _TeraStandarddsx1CurrentYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 16),
    _TeraStandarddsx1CurrentYELLOW_Type()
)
teraStandarddsx1CurrentYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1CurrentYELLOW.setStatus("mandatory")
_TeraStandarddsx1CurrentAIS_Type = Gauge32
_TeraStandarddsx1CurrentAIS_Object = MibTableColumn
teraStandarddsx1CurrentAIS = _TeraStandarddsx1CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 17),
    _TeraStandarddsx1CurrentAIS_Type()
)
teraStandarddsx1CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1CurrentAIS.setStatus("mandatory")
_TeraStandarddsx1CurrentLOSs_Type = Gauge32
_TeraStandarddsx1CurrentLOSs_Object = MibTableColumn
teraStandarddsx1CurrentLOSs = _TeraStandarddsx1CurrentLOSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 18),
    _TeraStandarddsx1CurrentLOSs_Type()
)
teraStandarddsx1CurrentLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1CurrentLOSs.setStatus("mandatory")
_Teradsx1IntervalTable_Object = MibTable
teradsx1IntervalTable = _Teradsx1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2)
)
if mibBuilder.loadTexts:
    teradsx1IntervalTable.setStatus("mandatory")
_Teradsx1IntervalTableEntry_Object = MibTableRow
teradsx1IntervalTableEntry = _Teradsx1IntervalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1)
)
teradsx1IntervalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads1-MIB", "teradsx1IntervalIndex"),
    (0, "TERAWAVE-terads1-MIB", "teradsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    teradsx1IntervalTableEntry.setStatus("mandatory")
_Teradsx1IntervalIndex_Type = Integer32
_Teradsx1IntervalIndex_Object = MibTableColumn
teradsx1IntervalIndex = _Teradsx1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 1),
    _Teradsx1IntervalIndex_Type()
)
teradsx1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalIndex.setStatus("mandatory")
_Teradsx1IntervalNumber_Type = Integer32
_Teradsx1IntervalNumber_Object = MibTableColumn
teradsx1IntervalNumber = _Teradsx1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 2),
    _Teradsx1IntervalNumber_Type()
)
teradsx1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalNumber.setStatus("mandatory")
_Teradsx1IntervalESs_Type = Gauge32
_Teradsx1IntervalESs_Object = MibTableColumn
teradsx1IntervalESs = _Teradsx1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 3),
    _Teradsx1IntervalESs_Type()
)
teradsx1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalESs.setStatus("mandatory")
_Teradsx1IntervalSESs_Type = Gauge32
_Teradsx1IntervalSESs_Object = MibTableColumn
teradsx1IntervalSESs = _Teradsx1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 4),
    _Teradsx1IntervalSESs_Type()
)
teradsx1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalSESs.setStatus("mandatory")
_Teradsx1IntervalSEFSs_Type = Gauge32
_Teradsx1IntervalSEFSs_Object = MibTableColumn
teradsx1IntervalSEFSs = _Teradsx1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 5),
    _Teradsx1IntervalSEFSs_Type()
)
teradsx1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalSEFSs.setStatus("mandatory")
_Teradsx1IntervalUASs_Type = Gauge32
_Teradsx1IntervalUASs_Object = MibTableColumn
teradsx1IntervalUASs = _Teradsx1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 6),
    _Teradsx1IntervalUASs_Type()
)
teradsx1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalUASs.setStatus("mandatory")
_Teradsx1IntervalCSSs_Type = Gauge32
_Teradsx1IntervalCSSs_Object = MibTableColumn
teradsx1IntervalCSSs = _Teradsx1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 7),
    _Teradsx1IntervalCSSs_Type()
)
teradsx1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalCSSs.setStatus("mandatory")
_Teradsx1IntervalPCVs_Type = Gauge32
_Teradsx1IntervalPCVs_Object = MibTableColumn
teradsx1IntervalPCVs = _Teradsx1IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 8),
    _Teradsx1IntervalPCVs_Type()
)
teradsx1IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalPCVs.setStatus("mandatory")
_Teradsx1IntervalLESs_Type = Gauge32
_Teradsx1IntervalLESs_Object = MibTableColumn
teradsx1IntervalLESs = _Teradsx1IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 9),
    _Teradsx1IntervalLESs_Type()
)
teradsx1IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalLESs.setStatus("mandatory")
_Teradsx1IntervalBESs_Type = Gauge32
_Teradsx1IntervalBESs_Object = MibTableColumn
teradsx1IntervalBESs = _Teradsx1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 10),
    _Teradsx1IntervalBESs_Type()
)
teradsx1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalBESs.setStatus("mandatory")
_Teradsx1IntervalDMs_Type = Gauge32
_Teradsx1IntervalDMs_Object = MibTableColumn
teradsx1IntervalDMs = _Teradsx1IntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 11),
    _Teradsx1IntervalDMs_Type()
)
teradsx1IntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalDMs.setStatus("mandatory")
_Teradsx1IntervalLCVs_Type = Gauge32
_Teradsx1IntervalLCVs_Object = MibTableColumn
teradsx1IntervalLCVs = _Teradsx1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 12),
    _Teradsx1IntervalLCVs_Type()
)
teradsx1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalLCVs.setStatus("mandatory")
_Teradsx1IntervalLOF_Type = Gauge32
_Teradsx1IntervalLOF_Object = MibTableColumn
teradsx1IntervalLOF = _Teradsx1IntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 13),
    _Teradsx1IntervalLOF_Type()
)
teradsx1IntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalLOF.setStatus("mandatory")
_Teradsx1IntervalYELLOW_Type = Gauge32
_Teradsx1IntervalYELLOW_Object = MibTableColumn
teradsx1IntervalYELLOW = _Teradsx1IntervalYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 14),
    _Teradsx1IntervalYELLOW_Type()
)
teradsx1IntervalYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalYELLOW.setStatus("mandatory")
_Teradsx1IntervalAIS_Type = Gauge32
_Teradsx1IntervalAIS_Object = MibTableColumn
teradsx1IntervalAIS = _Teradsx1IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 15),
    _Teradsx1IntervalAIS_Type()
)
teradsx1IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1IntervalAIS.setStatus("mandatory")
_TeraStandarddsx1IntervalLOF_Type = Gauge32
_TeraStandarddsx1IntervalLOF_Object = MibTableColumn
teraStandarddsx1IntervalLOF = _TeraStandarddsx1IntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 16),
    _TeraStandarddsx1IntervalLOF_Type()
)
teraStandarddsx1IntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1IntervalLOF.setStatus("mandatory")
_TeraStandarddsx1IntervalYELLOW_Type = Gauge32
_TeraStandarddsx1IntervalYELLOW_Object = MibTableColumn
teraStandarddsx1IntervalYELLOW = _TeraStandarddsx1IntervalYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 17),
    _TeraStandarddsx1IntervalYELLOW_Type()
)
teraStandarddsx1IntervalYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1IntervalYELLOW.setStatus("mandatory")
_TeraStandarddsx1IntervalAIS_Type = Gauge32
_TeraStandarddsx1IntervalAIS_Object = MibTableColumn
teraStandarddsx1IntervalAIS = _TeraStandarddsx1IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 18),
    _TeraStandarddsx1IntervalAIS_Type()
)
teraStandarddsx1IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1IntervalAIS.setStatus("mandatory")
_TeraStandarddsx1IntervalLOSs_Type = Gauge32
_TeraStandarddsx1IntervalLOSs_Object = MibTableColumn
teraStandarddsx1IntervalLOSs = _TeraStandarddsx1IntervalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 19),
    _TeraStandarddsx1IntervalLOSs_Type()
)
teraStandarddsx1IntervalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1IntervalLOSs.setStatus("mandatory")
_Teradsx1TotalTable_Object = MibTable
teradsx1TotalTable = _Teradsx1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3)
)
if mibBuilder.loadTexts:
    teradsx1TotalTable.setStatus("mandatory")
_Teradsx1TotalTableEntry_Object = MibTableRow
teradsx1TotalTableEntry = _Teradsx1TotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1)
)
teradsx1TotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads1-MIB", "teradsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    teradsx1TotalTableEntry.setStatus("mandatory")
_Teradsx1TotalIndex_Type = Integer32
_Teradsx1TotalIndex_Object = MibTableColumn
teradsx1TotalIndex = _Teradsx1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 1),
    _Teradsx1TotalIndex_Type()
)
teradsx1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalIndex.setStatus("mandatory")
_Teradsx1TotalESs_Type = Gauge32
_Teradsx1TotalESs_Object = MibTableColumn
teradsx1TotalESs = _Teradsx1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 2),
    _Teradsx1TotalESs_Type()
)
teradsx1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalESs.setStatus("mandatory")
_Teradsx1TotalSESs_Type = Gauge32
_Teradsx1TotalSESs_Object = MibTableColumn
teradsx1TotalSESs = _Teradsx1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 3),
    _Teradsx1TotalSESs_Type()
)
teradsx1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalSESs.setStatus("mandatory")
_Teradsx1TotalSEFSs_Type = Gauge32
_Teradsx1TotalSEFSs_Object = MibTableColumn
teradsx1TotalSEFSs = _Teradsx1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 4),
    _Teradsx1TotalSEFSs_Type()
)
teradsx1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalSEFSs.setStatus("mandatory")
_Teradsx1TotalUAS_Type = Gauge32
_Teradsx1TotalUAS_Object = MibTableColumn
teradsx1TotalUAS = _Teradsx1TotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 5),
    _Teradsx1TotalUAS_Type()
)
teradsx1TotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalUAS.setStatus("mandatory")
_Teradsx1TotalCSSs_Type = Gauge32
_Teradsx1TotalCSSs_Object = MibTableColumn
teradsx1TotalCSSs = _Teradsx1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 6),
    _Teradsx1TotalCSSs_Type()
)
teradsx1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalCSSs.setStatus("mandatory")
_Teradsx1TotalPCVs_Type = Gauge32
_Teradsx1TotalPCVs_Object = MibTableColumn
teradsx1TotalPCVs = _Teradsx1TotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 7),
    _Teradsx1TotalPCVs_Type()
)
teradsx1TotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalPCVs.setStatus("mandatory")
_Teradsx1TotalLESs_Type = Gauge32
_Teradsx1TotalLESs_Object = MibTableColumn
teradsx1TotalLESs = _Teradsx1TotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 8),
    _Teradsx1TotalLESs_Type()
)
teradsx1TotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalLESs.setStatus("mandatory")
_Teradsx1TotalBESs_Type = Gauge32
_Teradsx1TotalBESs_Object = MibTableColumn
teradsx1TotalBESs = _Teradsx1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 9),
    _Teradsx1TotalBESs_Type()
)
teradsx1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalBESs.setStatus("mandatory")
_Teradsx1TotalDMs_Type = Gauge32
_Teradsx1TotalDMs_Object = MibTableColumn
teradsx1TotalDMs = _Teradsx1TotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 10),
    _Teradsx1TotalDMs_Type()
)
teradsx1TotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalDMs.setStatus("mandatory")
_Teradsx1TotalLCVs_Type = Gauge32
_Teradsx1TotalLCVs_Object = MibTableColumn
teradsx1TotalLCVs = _Teradsx1TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 11),
    _Teradsx1TotalLCVs_Type()
)
teradsx1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalLCVs.setStatus("mandatory")
_Teradsx1TotalLOF_Type = Gauge32
_Teradsx1TotalLOF_Object = MibTableColumn
teradsx1TotalLOF = _Teradsx1TotalLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 12),
    _Teradsx1TotalLOF_Type()
)
teradsx1TotalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalLOF.setStatus("mandatory")
_Teradsx1TotalYELLOW_Type = Gauge32
_Teradsx1TotalYELLOW_Object = MibTableColumn
teradsx1TotalYELLOW = _Teradsx1TotalYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 13),
    _Teradsx1TotalYELLOW_Type()
)
teradsx1TotalYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalYELLOW.setStatus("mandatory")
_Teradsx1TotalAIS_Type = Gauge32
_Teradsx1TotalAIS_Object = MibTableColumn
teradsx1TotalAIS = _Teradsx1TotalAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 14),
    _Teradsx1TotalAIS_Type()
)
teradsx1TotalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TotalAIS.setStatus("mandatory")


class _Teradsx1TotalPerfStat_Type(Integer32):
    """Custom type teradsx1TotalPerfStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_Teradsx1TotalPerfStat_Type.__name__ = "Integer32"
_Teradsx1TotalPerfStat_Object = MibTableColumn
teradsx1TotalPerfStat = _Teradsx1TotalPerfStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 15),
    _Teradsx1TotalPerfStat_Type()
)
teradsx1TotalPerfStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teradsx1TotalPerfStat.setStatus("mandatory")
_TeraStandarddsx1TotalLOF_Type = Gauge32
_TeraStandarddsx1TotalLOF_Object = MibTableColumn
teraStandarddsx1TotalLOF = _TeraStandarddsx1TotalLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 16),
    _TeraStandarddsx1TotalLOF_Type()
)
teraStandarddsx1TotalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1TotalLOF.setStatus("mandatory")
_TeraStandarddsx1TotalYELLOW_Type = Gauge32
_TeraStandarddsx1TotalYELLOW_Object = MibTableColumn
teraStandarddsx1TotalYELLOW = _TeraStandarddsx1TotalYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 17),
    _TeraStandarddsx1TotalYELLOW_Type()
)
teraStandarddsx1TotalYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1TotalYELLOW.setStatus("mandatory")
_TeraStandarddsx1TotalAIS_Type = Gauge32
_TeraStandarddsx1TotalAIS_Object = MibTableColumn
teraStandarddsx1TotalAIS = _TeraStandarddsx1TotalAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 18),
    _TeraStandarddsx1TotalAIS_Type()
)
teraStandarddsx1TotalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1TotalAIS.setStatus("mandatory")
_TeraStandarddsx1TotalLOSs_Type = Gauge32
_TeraStandarddsx1TotalLOSs_Object = MibTableColumn
teraStandarddsx1TotalLOSs = _TeraStandarddsx1TotalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 19),
    _TeraStandarddsx1TotalLOSs_Type()
)
teraStandarddsx1TotalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1TotalLOSs.setStatus("mandatory")
_Teradsx1Standard7DayTotalTable_Object = MibTable
teradsx1Standard7DayTotalTable = _Teradsx1Standard7DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4)
)
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalTable.setStatus("mandatory")
_Teradsx1Standard7DayTotalTableEntry_Object = MibTableRow
teradsx1Standard7DayTotalTableEntry = _Teradsx1Standard7DayTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1)
)
teradsx1Standard7DayTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads1-MIB", "teradsx1Standard7DayTotalIndex"),
    (0, "TERAWAVE-terads1-MIB", "teradsx1Standard7DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalTableEntry.setStatus("mandatory")
_Teradsx1Standard7DayTotalIndex_Type = Integer32
_Teradsx1Standard7DayTotalIndex_Object = MibTableColumn
teradsx1Standard7DayTotalIndex = _Teradsx1Standard7DayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 1),
    _Teradsx1Standard7DayTotalIndex_Type()
)
teradsx1Standard7DayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalIndex.setStatus("mandatory")


class _Teradsx1Standard7DayTotalNumber_Type(Integer32):
    """Custom type teradsx1Standard7DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Teradsx1Standard7DayTotalNumber_Type.__name__ = "Integer32"
_Teradsx1Standard7DayTotalNumber_Object = MibTableColumn
teradsx1Standard7DayTotalNumber = _Teradsx1Standard7DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 2),
    _Teradsx1Standard7DayTotalNumber_Type()
)
teradsx1Standard7DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalNumber.setStatus("mandatory")
_Teradsx1Standard7DayTotalESs_Type = Gauge32
_Teradsx1Standard7DayTotalESs_Object = MibTableColumn
teradsx1Standard7DayTotalESs = _Teradsx1Standard7DayTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 3),
    _Teradsx1Standard7DayTotalESs_Type()
)
teradsx1Standard7DayTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalESs.setStatus("mandatory")
_Teradsx1Standard7DayTotalSESs_Type = Gauge32
_Teradsx1Standard7DayTotalSESs_Object = MibTableColumn
teradsx1Standard7DayTotalSESs = _Teradsx1Standard7DayTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 4),
    _Teradsx1Standard7DayTotalSESs_Type()
)
teradsx1Standard7DayTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalSESs.setStatus("mandatory")
_Teradsx1Standard7DayTotalSEFSs_Type = Gauge32
_Teradsx1Standard7DayTotalSEFSs_Object = MibTableColumn
teradsx1Standard7DayTotalSEFSs = _Teradsx1Standard7DayTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 5),
    _Teradsx1Standard7DayTotalSEFSs_Type()
)
teradsx1Standard7DayTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalSEFSs.setStatus("mandatory")
_Teradsx1Standard7DayTotalUAS_Type = Gauge32
_Teradsx1Standard7DayTotalUAS_Object = MibTableColumn
teradsx1Standard7DayTotalUAS = _Teradsx1Standard7DayTotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 6),
    _Teradsx1Standard7DayTotalUAS_Type()
)
teradsx1Standard7DayTotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalUAS.setStatus("mandatory")
_Teradsx1Standard7DayTotalCSSs_Type = Gauge32
_Teradsx1Standard7DayTotalCSSs_Object = MibTableColumn
teradsx1Standard7DayTotalCSSs = _Teradsx1Standard7DayTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 7),
    _Teradsx1Standard7DayTotalCSSs_Type()
)
teradsx1Standard7DayTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalCSSs.setStatus("mandatory")
_Teradsx1Standard7DayTotalPCVs_Type = Gauge32
_Teradsx1Standard7DayTotalPCVs_Object = MibTableColumn
teradsx1Standard7DayTotalPCVs = _Teradsx1Standard7DayTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 8),
    _Teradsx1Standard7DayTotalPCVs_Type()
)
teradsx1Standard7DayTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalPCVs.setStatus("mandatory")
_Teradsx1Standard7DayTotalLESs_Type = Gauge32
_Teradsx1Standard7DayTotalLESs_Object = MibTableColumn
teradsx1Standard7DayTotalLESs = _Teradsx1Standard7DayTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 9),
    _Teradsx1Standard7DayTotalLESs_Type()
)
teradsx1Standard7DayTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalLESs.setStatus("mandatory")
_Teradsx1Standard7DayTotalBESs_Type = Gauge32
_Teradsx1Standard7DayTotalBESs_Object = MibTableColumn
teradsx1Standard7DayTotalBESs = _Teradsx1Standard7DayTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 10),
    _Teradsx1Standard7DayTotalBESs_Type()
)
teradsx1Standard7DayTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalBESs.setStatus("mandatory")
_Teradsx1Standard7DayTotalDMs_Type = Gauge32
_Teradsx1Standard7DayTotalDMs_Object = MibTableColumn
teradsx1Standard7DayTotalDMs = _Teradsx1Standard7DayTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 11),
    _Teradsx1Standard7DayTotalDMs_Type()
)
teradsx1Standard7DayTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalDMs.setStatus("mandatory")
_Teradsx1Standard7DayTotalLCVs_Type = Gauge32
_Teradsx1Standard7DayTotalLCVs_Object = MibTableColumn
teradsx1Standard7DayTotalLCVs = _Teradsx1Standard7DayTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 12),
    _Teradsx1Standard7DayTotalLCVs_Type()
)
teradsx1Standard7DayTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalLCVs.setStatus("mandatory")


class _Teradsx1Standard7DayTotalValidData_Type(Integer32):
    """Custom type teradsx1Standard7DayTotalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Teradsx1Standard7DayTotalValidData_Type.__name__ = "Integer32"
_Teradsx1Standard7DayTotalValidData_Object = MibTableColumn
teradsx1Standard7DayTotalValidData = _Teradsx1Standard7DayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 13),
    _Teradsx1Standard7DayTotalValidData_Type()
)
teradsx1Standard7DayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Standard7DayTotalValidData.setStatus("mandatory")
_Teradsx1Tera7DayTotalTable_Object = MibTable
teradsx1Tera7DayTotalTable = _Teradsx1Tera7DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5)
)
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalTable.setStatus("mandatory")
_Teradsx1Tera7DayTotalTableEntry_Object = MibTableRow
teradsx1Tera7DayTotalTableEntry = _Teradsx1Tera7DayTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1)
)
teradsx1Tera7DayTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads1-MIB", "teradsx1Tera7DayTotalIndex"),
    (0, "TERAWAVE-terads1-MIB", "teradsx1Tera7DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalTableEntry.setStatus("mandatory")
_Teradsx1Tera7DayTotalIndex_Type = Integer32
_Teradsx1Tera7DayTotalIndex_Object = MibTableColumn
teradsx1Tera7DayTotalIndex = _Teradsx1Tera7DayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 1),
    _Teradsx1Tera7DayTotalIndex_Type()
)
teradsx1Tera7DayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalIndex.setStatus("mandatory")


class _Teradsx1Tera7DayTotalNumber_Type(Integer32):
    """Custom type teradsx1Tera7DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Teradsx1Tera7DayTotalNumber_Type.__name__ = "Integer32"
_Teradsx1Tera7DayTotalNumber_Object = MibTableColumn
teradsx1Tera7DayTotalNumber = _Teradsx1Tera7DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 2),
    _Teradsx1Tera7DayTotalNumber_Type()
)
teradsx1Tera7DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalNumber.setStatus("mandatory")
_Teradsx1Tera7DayTotalESs_Type = Gauge32
_Teradsx1Tera7DayTotalESs_Object = MibTableColumn
teradsx1Tera7DayTotalESs = _Teradsx1Tera7DayTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 3),
    _Teradsx1Tera7DayTotalESs_Type()
)
teradsx1Tera7DayTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalESs.setStatus("mandatory")
_Teradsx1Tera7DayTotalSESs_Type = Gauge32
_Teradsx1Tera7DayTotalSESs_Object = MibTableColumn
teradsx1Tera7DayTotalSESs = _Teradsx1Tera7DayTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 4),
    _Teradsx1Tera7DayTotalSESs_Type()
)
teradsx1Tera7DayTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalSESs.setStatus("mandatory")
_Teradsx1Tera7DayTotalSEFSs_Type = Gauge32
_Teradsx1Tera7DayTotalSEFSs_Object = MibTableColumn
teradsx1Tera7DayTotalSEFSs = _Teradsx1Tera7DayTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 5),
    _Teradsx1Tera7DayTotalSEFSs_Type()
)
teradsx1Tera7DayTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalSEFSs.setStatus("mandatory")
_Teradsx1Tera7DayTotalUAS_Type = Gauge32
_Teradsx1Tera7DayTotalUAS_Object = MibTableColumn
teradsx1Tera7DayTotalUAS = _Teradsx1Tera7DayTotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 6),
    _Teradsx1Tera7DayTotalUAS_Type()
)
teradsx1Tera7DayTotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalUAS.setStatus("mandatory")
_Teradsx1Tera7DayTotalCSSs_Type = Gauge32
_Teradsx1Tera7DayTotalCSSs_Object = MibTableColumn
teradsx1Tera7DayTotalCSSs = _Teradsx1Tera7DayTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 7),
    _Teradsx1Tera7DayTotalCSSs_Type()
)
teradsx1Tera7DayTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalCSSs.setStatus("mandatory")
_Teradsx1Tera7DayTotalPCVs_Type = Gauge32
_Teradsx1Tera7DayTotalPCVs_Object = MibTableColumn
teradsx1Tera7DayTotalPCVs = _Teradsx1Tera7DayTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 8),
    _Teradsx1Tera7DayTotalPCVs_Type()
)
teradsx1Tera7DayTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalPCVs.setStatus("mandatory")
_Teradsx1Tera7DayTotalLESs_Type = Gauge32
_Teradsx1Tera7DayTotalLESs_Object = MibTableColumn
teradsx1Tera7DayTotalLESs = _Teradsx1Tera7DayTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 9),
    _Teradsx1Tera7DayTotalLESs_Type()
)
teradsx1Tera7DayTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalLESs.setStatus("mandatory")
_Teradsx1Tera7DayTotalBESs_Type = Gauge32
_Teradsx1Tera7DayTotalBESs_Object = MibTableColumn
teradsx1Tera7DayTotalBESs = _Teradsx1Tera7DayTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 10),
    _Teradsx1Tera7DayTotalBESs_Type()
)
teradsx1Tera7DayTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalBESs.setStatus("mandatory")
_Teradsx1Tera7DayTotalDMs_Type = Gauge32
_Teradsx1Tera7DayTotalDMs_Object = MibTableColumn
teradsx1Tera7DayTotalDMs = _Teradsx1Tera7DayTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 11),
    _Teradsx1Tera7DayTotalDMs_Type()
)
teradsx1Tera7DayTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalDMs.setStatus("mandatory")
_Teradsx1Tera7DayTotalLCVs_Type = Gauge32
_Teradsx1Tera7DayTotalLCVs_Object = MibTableColumn
teradsx1Tera7DayTotalLCVs = _Teradsx1Tera7DayTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 12),
    _Teradsx1Tera7DayTotalLCVs_Type()
)
teradsx1Tera7DayTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalLCVs.setStatus("mandatory")
_Teradsx1Tera7DayTotalLOF_Type = Gauge32
_Teradsx1Tera7DayTotalLOF_Object = MibTableColumn
teradsx1Tera7DayTotalLOF = _Teradsx1Tera7DayTotalLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 13),
    _Teradsx1Tera7DayTotalLOF_Type()
)
teradsx1Tera7DayTotalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalLOF.setStatus("mandatory")
_Teradsx1Tera7DayTotalYELLOW_Type = Gauge32
_Teradsx1Tera7DayTotalYELLOW_Object = MibTableColumn
teradsx1Tera7DayTotalYELLOW = _Teradsx1Tera7DayTotalYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 14),
    _Teradsx1Tera7DayTotalYELLOW_Type()
)
teradsx1Tera7DayTotalYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalYELLOW.setStatus("mandatory")
_Teradsx1Tera7DayTotalAIS_Type = Gauge32
_Teradsx1Tera7DayTotalAIS_Object = MibTableColumn
teradsx1Tera7DayTotalAIS = _Teradsx1Tera7DayTotalAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 15),
    _Teradsx1Tera7DayTotalAIS_Type()
)
teradsx1Tera7DayTotalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalAIS.setStatus("mandatory")
_Teradsx1TeraStandard7DayTotalLOF_Type = Gauge32
_Teradsx1TeraStandard7DayTotalLOF_Object = MibTableColumn
teradsx1TeraStandard7DayTotalLOF = _Teradsx1TeraStandard7DayTotalLOF_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 16),
    _Teradsx1TeraStandard7DayTotalLOF_Type()
)
teradsx1TeraStandard7DayTotalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TeraStandard7DayTotalLOF.setStatus("mandatory")
_Teradsx1TeraStandard7DayTotalYELLOW_Type = Gauge32
_Teradsx1TeraStandard7DayTotalYELLOW_Object = MibTableColumn
teradsx1TeraStandard7DayTotalYELLOW = _Teradsx1TeraStandard7DayTotalYELLOW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 17),
    _Teradsx1TeraStandard7DayTotalYELLOW_Type()
)
teradsx1TeraStandard7DayTotalYELLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TeraStandard7DayTotalYELLOW.setStatus("mandatory")
_Teradsx1TeraStandard7DayTotalAIS_Type = Gauge32
_Teradsx1TeraStandard7DayTotalAIS_Object = MibTableColumn
teradsx1TeraStandard7DayTotalAIS = _Teradsx1TeraStandard7DayTotalAIS_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 18),
    _Teradsx1TeraStandard7DayTotalAIS_Type()
)
teradsx1TeraStandard7DayTotalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1TeraStandard7DayTotalAIS.setStatus("mandatory")


class _Teradsx1Tera7DayTotalValidData_Type(Integer32):
    """Custom type teradsx1Tera7DayTotalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Teradsx1Tera7DayTotalValidData_Type.__name__ = "Integer32"
_Teradsx1Tera7DayTotalValidData_Object = MibTableColumn
teradsx1Tera7DayTotalValidData = _Teradsx1Tera7DayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 19),
    _Teradsx1Tera7DayTotalValidData_Type()
)
teradsx1Tera7DayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx1Tera7DayTotalValidData.setStatus("mandatory")
_TeraStandarddsx1Tera7DayTotalLOSs_Type = Gauge32
_TeraStandarddsx1Tera7DayTotalLOSs_Object = MibTableColumn
teraStandarddsx1Tera7DayTotalLOSs = _TeraStandarddsx1Tera7DayTotalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 20),
    _TeraStandarddsx1Tera7DayTotalLOSs_Type()
)
teraStandarddsx1Tera7DayTotalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStandarddsx1Tera7DayTotalLOSs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-terads1-MIB",
    **{"terawave": terawave,
       "teraDs1Group": teraDs1Group,
       "teradsx1CurrentTable": teradsx1CurrentTable,
       "teradsx1CurrentTableEntry": teradsx1CurrentTableEntry,
       "teradsx1CurrentIndex": teradsx1CurrentIndex,
       "teradsx1CurrentESs": teradsx1CurrentESs,
       "teradsx1CurrentSESs": teradsx1CurrentSESs,
       "teradsx1CurrentSEFSs": teradsx1CurrentSEFSs,
       "teradsx1CurrentUASs": teradsx1CurrentUASs,
       "teradsx1CurrentCSSs": teradsx1CurrentCSSs,
       "teradsx1CurrentPCVs": teradsx1CurrentPCVs,
       "teradsx1CurrentLESs": teradsx1CurrentLESs,
       "teradsx1CurrentBESs": teradsx1CurrentBESs,
       "teradsx1CurrentDMs": teradsx1CurrentDMs,
       "teradsx1CurrentLCVs": teradsx1CurrentLCVs,
       "teradsx1CurrentLOF": teradsx1CurrentLOF,
       "teradsx1CurrentYELLOW": teradsx1CurrentYELLOW,
       "teradsx1CurrentAIS": teradsx1CurrentAIS,
       "teraStandarddsx1CurrentLOF": teraStandarddsx1CurrentLOF,
       "teraStandarddsx1CurrentYELLOW": teraStandarddsx1CurrentYELLOW,
       "teraStandarddsx1CurrentAIS": teraStandarddsx1CurrentAIS,
       "teraStandarddsx1CurrentLOSs": teraStandarddsx1CurrentLOSs,
       "teradsx1IntervalTable": teradsx1IntervalTable,
       "teradsx1IntervalTableEntry": teradsx1IntervalTableEntry,
       "teradsx1IntervalIndex": teradsx1IntervalIndex,
       "teradsx1IntervalNumber": teradsx1IntervalNumber,
       "teradsx1IntervalESs": teradsx1IntervalESs,
       "teradsx1IntervalSESs": teradsx1IntervalSESs,
       "teradsx1IntervalSEFSs": teradsx1IntervalSEFSs,
       "teradsx1IntervalUASs": teradsx1IntervalUASs,
       "teradsx1IntervalCSSs": teradsx1IntervalCSSs,
       "teradsx1IntervalPCVs": teradsx1IntervalPCVs,
       "teradsx1IntervalLESs": teradsx1IntervalLESs,
       "teradsx1IntervalBESs": teradsx1IntervalBESs,
       "teradsx1IntervalDMs": teradsx1IntervalDMs,
       "teradsx1IntervalLCVs": teradsx1IntervalLCVs,
       "teradsx1IntervalLOF": teradsx1IntervalLOF,
       "teradsx1IntervalYELLOW": teradsx1IntervalYELLOW,
       "teradsx1IntervalAIS": teradsx1IntervalAIS,
       "teraStandarddsx1IntervalLOF": teraStandarddsx1IntervalLOF,
       "teraStandarddsx1IntervalYELLOW": teraStandarddsx1IntervalYELLOW,
       "teraStandarddsx1IntervalAIS": teraStandarddsx1IntervalAIS,
       "teraStandarddsx1IntervalLOSs": teraStandarddsx1IntervalLOSs,
       "teradsx1TotalTable": teradsx1TotalTable,
       "teradsx1TotalTableEntry": teradsx1TotalTableEntry,
       "teradsx1TotalIndex": teradsx1TotalIndex,
       "teradsx1TotalESs": teradsx1TotalESs,
       "teradsx1TotalSESs": teradsx1TotalSESs,
       "teradsx1TotalSEFSs": teradsx1TotalSEFSs,
       "teradsx1TotalUAS": teradsx1TotalUAS,
       "teradsx1TotalCSSs": teradsx1TotalCSSs,
       "teradsx1TotalPCVs": teradsx1TotalPCVs,
       "teradsx1TotalLESs": teradsx1TotalLESs,
       "teradsx1TotalBESs": teradsx1TotalBESs,
       "teradsx1TotalDMs": teradsx1TotalDMs,
       "teradsx1TotalLCVs": teradsx1TotalLCVs,
       "teradsx1TotalLOF": teradsx1TotalLOF,
       "teradsx1TotalYELLOW": teradsx1TotalYELLOW,
       "teradsx1TotalAIS": teradsx1TotalAIS,
       "teradsx1TotalPerfStat": teradsx1TotalPerfStat,
       "teraStandarddsx1TotalLOF": teraStandarddsx1TotalLOF,
       "teraStandarddsx1TotalYELLOW": teraStandarddsx1TotalYELLOW,
       "teraStandarddsx1TotalAIS": teraStandarddsx1TotalAIS,
       "teraStandarddsx1TotalLOSs": teraStandarddsx1TotalLOSs,
       "teradsx1Standard7DayTotalTable": teradsx1Standard7DayTotalTable,
       "teradsx1Standard7DayTotalTableEntry": teradsx1Standard7DayTotalTableEntry,
       "teradsx1Standard7DayTotalIndex": teradsx1Standard7DayTotalIndex,
       "teradsx1Standard7DayTotalNumber": teradsx1Standard7DayTotalNumber,
       "teradsx1Standard7DayTotalESs": teradsx1Standard7DayTotalESs,
       "teradsx1Standard7DayTotalSESs": teradsx1Standard7DayTotalSESs,
       "teradsx1Standard7DayTotalSEFSs": teradsx1Standard7DayTotalSEFSs,
       "teradsx1Standard7DayTotalUAS": teradsx1Standard7DayTotalUAS,
       "teradsx1Standard7DayTotalCSSs": teradsx1Standard7DayTotalCSSs,
       "teradsx1Standard7DayTotalPCVs": teradsx1Standard7DayTotalPCVs,
       "teradsx1Standard7DayTotalLESs": teradsx1Standard7DayTotalLESs,
       "teradsx1Standard7DayTotalBESs": teradsx1Standard7DayTotalBESs,
       "teradsx1Standard7DayTotalDMs": teradsx1Standard7DayTotalDMs,
       "teradsx1Standard7DayTotalLCVs": teradsx1Standard7DayTotalLCVs,
       "teradsx1Standard7DayTotalValidData": teradsx1Standard7DayTotalValidData,
       "teradsx1Tera7DayTotalTable": teradsx1Tera7DayTotalTable,
       "teradsx1Tera7DayTotalTableEntry": teradsx1Tera7DayTotalTableEntry,
       "teradsx1Tera7DayTotalIndex": teradsx1Tera7DayTotalIndex,
       "teradsx1Tera7DayTotalNumber": teradsx1Tera7DayTotalNumber,
       "teradsx1Tera7DayTotalESs": teradsx1Tera7DayTotalESs,
       "teradsx1Tera7DayTotalSESs": teradsx1Tera7DayTotalSESs,
       "teradsx1Tera7DayTotalSEFSs": teradsx1Tera7DayTotalSEFSs,
       "teradsx1Tera7DayTotalUAS": teradsx1Tera7DayTotalUAS,
       "teradsx1Tera7DayTotalCSSs": teradsx1Tera7DayTotalCSSs,
       "teradsx1Tera7DayTotalPCVs": teradsx1Tera7DayTotalPCVs,
       "teradsx1Tera7DayTotalLESs": teradsx1Tera7DayTotalLESs,
       "teradsx1Tera7DayTotalBESs": teradsx1Tera7DayTotalBESs,
       "teradsx1Tera7DayTotalDMs": teradsx1Tera7DayTotalDMs,
       "teradsx1Tera7DayTotalLCVs": teradsx1Tera7DayTotalLCVs,
       "teradsx1Tera7DayTotalLOF": teradsx1Tera7DayTotalLOF,
       "teradsx1Tera7DayTotalYELLOW": teradsx1Tera7DayTotalYELLOW,
       "teradsx1Tera7DayTotalAIS": teradsx1Tera7DayTotalAIS,
       "teradsx1TeraStandard7DayTotalLOF": teradsx1TeraStandard7DayTotalLOF,
       "teradsx1TeraStandard7DayTotalYELLOW": teradsx1TeraStandard7DayTotalYELLOW,
       "teradsx1TeraStandard7DayTotalAIS": teradsx1TeraStandard7DayTotalAIS,
       "teradsx1Tera7DayTotalValidData": teradsx1Tera7DayTotalValidData,
       "teraStandarddsx1Tera7DayTotalLOSs": teraStandarddsx1Tera7DayTotalLOSs}
)
