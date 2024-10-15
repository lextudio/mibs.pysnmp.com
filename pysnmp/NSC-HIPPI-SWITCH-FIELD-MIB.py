# SNMP MIB module (NSC-HIPPI-SWITCH-FIELD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSC-HIPPI-SWITCH-FIELD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:26 2024
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

(nsc,
 nscHippiSwitch,
 nscMib,
 nscProducts) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nsc",
    "nscHippiSwitch",
    "nscMib",
    "nscProducts")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ps32FieldDir_ObjectIdentity = ObjectIdentity
ps32FieldDir = _Ps32FieldDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7)
)


class _Ps32BistAPort_Type(DisplayString):
    """Custom type ps32BistAPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32BistAPort_Type.__name__ = "DisplayString"
_Ps32BistAPort_Object = MibScalar
ps32BistAPort = _Ps32BistAPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 1),
    _Ps32BistAPort_Type()
)
ps32BistAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32BistAPort.setStatus("mandatory")
_Ps32Clear_ObjectIdentity = ObjectIdentity
ps32Clear = _Ps32Clear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2)
)


class _Ps32ClearAll_Type(DisplayString):
    """Custom type ps32ClearAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearAll_Type.__name__ = "DisplayString"
_Ps32ClearAll_Object = MibScalar
ps32ClearAll = _Ps32ClearAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 1),
    _Ps32ClearAll_Type()
)
ps32ClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearAll.setStatus("mandatory")


class _Ps32ClearErrorsAll_Type(DisplayString):
    """Custom type ps32ClearErrorsAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearErrorsAll_Type.__name__ = "DisplayString"
_Ps32ClearErrorsAll_Object = MibScalar
ps32ClearErrorsAll = _Ps32ClearErrorsAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 2),
    _Ps32ClearErrorsAll_Type()
)
ps32ClearErrorsAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearErrorsAll.setStatus("mandatory")


class _Ps32ClearErrorsInPort_Type(DisplayString):
    """Custom type ps32ClearErrorsInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearErrorsInPort_Type.__name__ = "DisplayString"
_Ps32ClearErrorsInPort_Object = MibScalar
ps32ClearErrorsInPort = _Ps32ClearErrorsInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 3),
    _Ps32ClearErrorsInPort_Type()
)
ps32ClearErrorsInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearErrorsInPort.setStatus("mandatory")


class _Ps32ClearPathAll_Type(DisplayString):
    """Custom type ps32ClearPathAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearPathAll_Type.__name__ = "DisplayString"
_Ps32ClearPathAll_Object = MibScalar
ps32ClearPathAll = _Ps32ClearPathAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 4),
    _Ps32ClearPathAll_Type()
)
ps32ClearPathAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearPathAll.setStatus("mandatory")


class _Ps32ClearPathInPort_Type(DisplayString):
    """Custom type ps32ClearPathInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearPathInPort_Type.__name__ = "DisplayString"
_Ps32ClearPathInPort_Object = MibScalar
ps32ClearPathInPort = _Ps32ClearPathInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 5),
    _Ps32ClearPathInPort_Type()
)
ps32ClearPathInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearPathInPort.setStatus("mandatory")


class _Ps32ClearPathDest_Type(DisplayString):
    """Custom type ps32ClearPathDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearPathDest_Type.__name__ = "DisplayString"
_Ps32ClearPathDest_Object = MibScalar
ps32ClearPathDest = _Ps32ClearPathDest_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 6),
    _Ps32ClearPathDest_Type()
)
ps32ClearPathDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearPathDest.setStatus("mandatory")


class _Ps32ClearPathForce_Type(DisplayString):
    """Custom type ps32ClearPathForce based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearPathForce_Type.__name__ = "DisplayString"
_Ps32ClearPathForce_Object = MibScalar
ps32ClearPathForce = _Ps32ClearPathForce_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 7),
    _Ps32ClearPathForce_Type()
)
ps32ClearPathForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearPathForce.setStatus("mandatory")


class _Ps32ClearStatsAll_Type(DisplayString):
    """Custom type ps32ClearStatsAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearStatsAll_Type.__name__ = "DisplayString"
_Ps32ClearStatsAll_Object = MibScalar
ps32ClearStatsAll = _Ps32ClearStatsAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 8),
    _Ps32ClearStatsAll_Type()
)
ps32ClearStatsAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearStatsAll.setStatus("mandatory")


class _Ps32ClearStatsInPort_Type(DisplayString):
    """Custom type ps32ClearStatsInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ClearStatsInPort_Type.__name__ = "DisplayString"
_Ps32ClearStatsInPort_Object = MibScalar
ps32ClearStatsInPort = _Ps32ClearStatsInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 2, 9),
    _Ps32ClearStatsInPort_Type()
)
ps32ClearStatsInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ClearStatsInPort.setStatus("mandatory")
_Ps32Disable_ObjectIdentity = ObjectIdentity
ps32Disable = _Ps32Disable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 3)
)
_Ps32Disable2_ObjectIdentity = ObjectIdentity
ps32Disable2 = _Ps32Disable2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 3)
)


class _Ps32DisablePortAll_Type(DisplayString):
    """Custom type ps32DisablePortAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32DisablePortAll_Type.__name__ = "DisplayString"
_Ps32DisablePortAll_Object = MibScalar
ps32DisablePortAll = _Ps32DisablePortAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 3, 1),
    _Ps32DisablePortAll_Type()
)
ps32DisablePortAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32DisablePortAll.setStatus("mandatory")


class _Ps32DisablePortInPort_Type(DisplayString):
    """Custom type ps32DisablePortInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32DisablePortInPort_Type.__name__ = "DisplayString"
_Ps32DisablePortInPort_Object = MibScalar
ps32DisablePortInPort = _Ps32DisablePortInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 3, 2),
    _Ps32DisablePortInPort_Type()
)
ps32DisablePortInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32DisablePortInPort.setStatus("mandatory")
_Ps32Display_ObjectIdentity = ObjectIdentity
ps32Display = _Ps32Display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4)
)
_Ps32Display2_ObjectIdentity = ObjectIdentity
ps32Display2 = _Ps32Display2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4)
)
_Ps32Config_ObjectIdentity = ObjectIdentity
ps32Config = _Ps32Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 1)
)
_Ps32DCTitle_Type = DisplayString
_Ps32DCTitle_Object = MibScalar
ps32DCTitle = _Ps32DCTitle_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 1, 1),
    _Ps32DCTitle_Type()
)
ps32DCTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DCTitle.setStatus("mandatory")
_Ps32DCTable_Object = MibTable
ps32DCTable = _Ps32DCTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ps32DCTable.setStatus("mandatory")
_Ps32DCEntry_Object = MibTableRow
ps32DCEntry = _Ps32DCEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ps32DCEntry.setStatus("mandatory")
_Ps32DCLine_Type = DisplayString
_Ps32DCLine_Object = MibTableColumn
ps32DCLine = _Ps32DCLine_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 1, 2, 1, 1),
    _Ps32DCLine_Type()
)
ps32DCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DCLine.setStatus("mandatory")
_Ps32PathList_ObjectIdentity = ObjectIdentity
ps32PathList = _Ps32PathList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2)
)
_Ps32DSPTable_Type = DisplayString
_Ps32DSPTable_Object = MibScalar
ps32DSPTable = _Ps32DSPTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 1),
    _Ps32DSPTable_Type()
)
ps32DSPTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSPTable.setStatus("mandatory")
_Ps32DSPPathwayTable_Object = MibTable
ps32DSPPathwayTable = _Ps32DSPPathwayTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ps32DSPPathwayTable.setStatus("mandatory")
_Ps32DSPPathwayEntry_Object = MibTableRow
ps32DSPPathwayEntry = _Ps32DSPPathwayEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 1, 1, 1)
)
ps32DSPPathwayEntry.setIndexNames(
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PortNumber"),
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PathwayHDA"),
)
if mibBuilder.loadTexts:
    ps32DSPPathwayEntry.setStatus("mandatory")
_Ps32DSPLine_Type = DisplayString
_Ps32DSPLine_Object = MibTableColumn
ps32DSPLine = _Ps32DSPLine_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 1, 1, 1, 1),
    _Ps32DSPLine_Type()
)
ps32DSPLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSPLine.setStatus("mandatory")
_Ps32DSPDPathwayTable_Object = MibTable
ps32DSPDPathwayTable = _Ps32DSPDPathwayTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ps32DSPDPathwayTable.setStatus("mandatory")
_Ps32DSPDPathwayEntry_Object = MibTableRow
ps32DSPDPathwayEntry = _Ps32DSPDPathwayEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 2, 1)
)
ps32DSPDPathwayEntry.setIndexNames(
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PortNumber"),
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PathwayHDA"),
)
if mibBuilder.loadTexts:
    ps32DSPDPathwayEntry.setStatus("mandatory")
_Ps32DSPDLine_Type = DisplayString
_Ps32DSPDLine_Object = MibTableColumn
ps32DSPDLine = _Ps32DSPDLine_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 2, 1, 1),
    _Ps32DSPDLine_Type()
)
ps32DSPDLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSPDLine.setStatus("mandatory")
_Ps32DSPIPathwayTable_Object = MibTable
ps32DSPIPathwayTable = _Ps32DSPIPathwayTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 3)
)
if mibBuilder.loadTexts:
    ps32DSPIPathwayTable.setStatus("mandatory")
_Ps32DSPIPathwayEntry_Object = MibTableRow
ps32DSPIPathwayEntry = _Ps32DSPIPathwayEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 3, 1)
)
ps32DSPIPathwayEntry.setIndexNames(
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PortNumber"),
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PathwayHDA"),
)
if mibBuilder.loadTexts:
    ps32DSPIPathwayEntry.setStatus("mandatory")
_Ps32DSPILine_Type = DisplayString
_Ps32DSPILine_Object = MibTableColumn
ps32DSPILine = _Ps32DSPILine_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 2, 3, 1, 1),
    _Ps32DSPILine_Type()
)
ps32DSPILine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSPILine.setStatus("mandatory")
_Ps32Status_ObjectIdentity = ObjectIdentity
ps32Status = _Ps32Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3)
)
_Ps32AllStatus_ObjectIdentity = ObjectIdentity
ps32AllStatus = _Ps32AllStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 1)
)
_Ps32DSATitle_Type = DisplayString
_Ps32DSATitle_Object = MibScalar
ps32DSATitle = _Ps32DSATitle_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 1, 1),
    _Ps32DSATitle_Type()
)
ps32DSATitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSATitle.setStatus("mandatory")
_Ps32DSATable_Object = MibTable
ps32DSATable = _Ps32DSATable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ps32DSATable.setStatus("mandatory")
_Ps32DSAEntry_Object = MibTableRow
ps32DSAEntry = _Ps32DSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ps32DSAEntry.setStatus("mandatory")
_Ps32DSALine_Type = DisplayString
_Ps32DSALine_Object = MibTableColumn
ps32DSALine = _Ps32DSALine_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 1, 2, 1, 1),
    _Ps32DSALine_Type()
)
ps32DSALine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSALine.setStatus("mandatory")
_Ps32IPStatus_ObjectIdentity = ObjectIdentity
ps32IPStatus = _Ps32IPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2)
)
_Ps32DSITable_Object = MibTable
ps32DSITable = _Ps32DSITable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ps32DSITable.setStatus("mandatory")
_Ps32DSIEntry_Object = MibTableRow
ps32DSIEntry = _Ps32DSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1)
)
ps32DSIEntry.setIndexNames(
    (0, "NSC-HIPPI-SWITCH-FIELD-MIB", "ps32PortNumber"),
)
if mibBuilder.loadTexts:
    ps32DSIEntry.setStatus("mandatory")
_Ps32DSILine1_Type = DisplayString
_Ps32DSILine1_Object = MibTableColumn
ps32DSILine1 = _Ps32DSILine1_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 1),
    _Ps32DSILine1_Type()
)
ps32DSILine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine1.setStatus("mandatory")
_Ps32DSILine2_Type = DisplayString
_Ps32DSILine2_Object = MibTableColumn
ps32DSILine2 = _Ps32DSILine2_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 2),
    _Ps32DSILine2_Type()
)
ps32DSILine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine2.setStatus("mandatory")
_Ps32DSILine3_Type = DisplayString
_Ps32DSILine3_Object = MibTableColumn
ps32DSILine3 = _Ps32DSILine3_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 3),
    _Ps32DSILine3_Type()
)
ps32DSILine3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine3.setStatus("mandatory")
_Ps32DSILine4_Type = DisplayString
_Ps32DSILine4_Object = MibTableColumn
ps32DSILine4 = _Ps32DSILine4_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 4),
    _Ps32DSILine4_Type()
)
ps32DSILine4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine4.setStatus("mandatory")
_Ps32DSILine5_Type = DisplayString
_Ps32DSILine5_Object = MibTableColumn
ps32DSILine5 = _Ps32DSILine5_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 5),
    _Ps32DSILine5_Type()
)
ps32DSILine5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine5.setStatus("mandatory")
_Ps32DSILine6_Type = DisplayString
_Ps32DSILine6_Object = MibTableColumn
ps32DSILine6 = _Ps32DSILine6_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 6),
    _Ps32DSILine6_Type()
)
ps32DSILine6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine6.setStatus("mandatory")
_Ps32DSILine7_Type = DisplayString
_Ps32DSILine7_Object = MibTableColumn
ps32DSILine7 = _Ps32DSILine7_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 7),
    _Ps32DSILine7_Type()
)
ps32DSILine7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine7.setStatus("mandatory")
_Ps32DSILine8_Type = DisplayString
_Ps32DSILine8_Object = MibTableColumn
ps32DSILine8 = _Ps32DSILine8_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 8),
    _Ps32DSILine8_Type()
)
ps32DSILine8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine8.setStatus("mandatory")
_Ps32DSILine9_Type = DisplayString
_Ps32DSILine9_Object = MibTableColumn
ps32DSILine9 = _Ps32DSILine9_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 2, 1, 1, 9),
    _Ps32DSILine9_Type()
)
ps32DSILine9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSILine9.setStatus("mandatory")
_Ps32MiscStatus_ObjectIdentity = ObjectIdentity
ps32MiscStatus = _Ps32MiscStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 3)
)
_Ps32DSMTable_Object = MibTable
ps32DSMTable = _Ps32DSMTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ps32DSMTable.setStatus("mandatory")
_Ps32DSMEntry_Object = MibTableRow
ps32DSMEntry = _Ps32DSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ps32DSMEntry.setStatus("mandatory")
_Ps32DSMLine_Type = DisplayString
_Ps32DSMLine_Object = MibTableColumn
ps32DSMLine = _Ps32DSMLine_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 3, 3, 1, 1, 1),
    _Ps32DSMLine_Type()
)
ps32DSMLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32DSMLine.setStatus("mandatory")
_Ps32Version_Type = DisplayString
_Ps32Version_Object = MibScalar
ps32Version = _Ps32Version_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 4, 4),
    _Ps32Version_Type()
)
ps32Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32Version.setStatus("mandatory")
_Ps32Enable_ObjectIdentity = ObjectIdentity
ps32Enable = _Ps32Enable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 5)
)
_Ps32Enable2_ObjectIdentity = ObjectIdentity
ps32Enable2 = _Ps32Enable2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 5)
)


class _Ps32EnablePortAll_Type(DisplayString):
    """Custom type ps32EnablePortAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32EnablePortAll_Type.__name__ = "DisplayString"
_Ps32EnablePortAll_Object = MibScalar
ps32EnablePortAll = _Ps32EnablePortAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 5, 1),
    _Ps32EnablePortAll_Type()
)
ps32EnablePortAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32EnablePortAll.setStatus("mandatory")


class _Ps32EnablePortInPort_Type(DisplayString):
    """Custom type ps32EnablePortInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32EnablePortInPort_Type.__name__ = "DisplayString"
_Ps32EnablePortInPort_Object = MibScalar
ps32EnablePortInPort = _Ps32EnablePortInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 5, 2),
    _Ps32EnablePortInPort_Type()
)
ps32EnablePortInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32EnablePortInPort.setStatus("mandatory")


class _Ps32ResetSwitch_Type(DisplayString):
    """Custom type ps32ResetSwitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32ResetSwitch_Type.__name__ = "DisplayString"
_Ps32ResetSwitch_Object = MibScalar
ps32ResetSwitch = _Ps32ResetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 6),
    _Ps32ResetSwitch_Type()
)
ps32ResetSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32ResetSwitch.setStatus("mandatory")
_Ps32Restore_ObjectIdentity = ObjectIdentity
ps32Restore = _Ps32Restore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 7)
)
_Ps32Restore2_ObjectIdentity = ObjectIdentity
ps32Restore2 = _Ps32Restore2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 7)
)


class _Ps32RestorePathAll_Type(DisplayString):
    """Custom type ps32RestorePathAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32RestorePathAll_Type.__name__ = "DisplayString"
_Ps32RestorePathAll_Object = MibScalar
ps32RestorePathAll = _Ps32RestorePathAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 7, 1),
    _Ps32RestorePathAll_Type()
)
ps32RestorePathAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32RestorePathAll.setStatus("mandatory")


class _Ps32RestorePathInPort_Type(DisplayString):
    """Custom type ps32RestorePathInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32RestorePathInPort_Type.__name__ = "DisplayString"
_Ps32RestorePathInPort_Object = MibScalar
ps32RestorePathInPort = _Ps32RestorePathInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 7, 2),
    _Ps32RestorePathInPort_Type()
)
ps32RestorePathInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32RestorePathInPort.setStatus("mandatory")
_Ps32Save_ObjectIdentity = ObjectIdentity
ps32Save = _Ps32Save_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 8)
)
_Ps32Save2_ObjectIdentity = ObjectIdentity
ps32Save2 = _Ps32Save2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 8)
)


class _Ps32SaveAll_Type(DisplayString):
    """Custom type ps32SaveAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SaveAll_Type.__name__ = "DisplayString"
_Ps32SaveAll_Object = MibScalar
ps32SaveAll = _Ps32SaveAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 8, 1),
    _Ps32SaveAll_Type()
)
ps32SaveAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SaveAll.setStatus("mandatory")


class _Ps32SaveConfig_Type(DisplayString):
    """Custom type ps32SaveConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SaveConfig_Type.__name__ = "DisplayString"
_Ps32SaveConfig_Object = MibScalar
ps32SaveConfig = _Ps32SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 8, 2),
    _Ps32SaveConfig_Type()
)
ps32SaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SaveConfig.setStatus("mandatory")


class _Ps32SavePathAll_Type(DisplayString):
    """Custom type ps32SavePathAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SavePathAll_Type.__name__ = "DisplayString"
_Ps32SavePathAll_Object = MibScalar
ps32SavePathAll = _Ps32SavePathAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 8, 3),
    _Ps32SavePathAll_Type()
)
ps32SavePathAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SavePathAll.setStatus("mandatory")


class _Ps32SavePathInPort_Type(DisplayString):
    """Custom type ps32SavePathInPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SavePathInPort_Type.__name__ = "DisplayString"
_Ps32SavePathInPort_Object = MibScalar
ps32SavePathInPort = _Ps32SavePathInPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 8, 4),
    _Ps32SavePathInPort_Type()
)
ps32SavePathInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SavePathInPort.setStatus("mandatory")
_Ps32Set_ObjectIdentity = ObjectIdentity
ps32Set = _Ps32Set_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 9)
)
_Ps32Set2_ObjectIdentity = ObjectIdentity
ps32Set2 = _Ps32Set2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 9)
)


class _Ps32SetPathAll_Type(DisplayString):
    """Custom type ps32SetPathAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SetPathAll_Type.__name__ = "DisplayString"
_Ps32SetPathAll_Object = MibScalar
ps32SetPathAll = _Ps32SetPathAll_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 9, 1),
    _Ps32SetPathAll_Type()
)
ps32SetPathAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SetPathAll.setStatus("mandatory")


class _Ps32SetPathDest_Type(DisplayString):
    """Custom type ps32SetPathDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SetPathDest_Type.__name__ = "DisplayString"
_Ps32SetPathDest_Object = MibScalar
ps32SetPathDest = _Ps32SetPathDest_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 9, 2),
    _Ps32SetPathDest_Type()
)
ps32SetPathDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SetPathDest.setStatus("mandatory")


class _Ps32SetPathForce_Type(DisplayString):
    """Custom type ps32SetPathForce based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SetPathForce_Type.__name__ = "DisplayString"
_Ps32SetPathForce_Object = MibScalar
ps32SetPathForce = _Ps32SetPathForce_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 7, 9, 3),
    _Ps32SetPathForce_Type()
)
ps32SetPathForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SetPathForce.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSC-HIPPI-SWITCH-FIELD-MIB",
    **{"ps32FieldDir": ps32FieldDir,
       "ps32BistAPort": ps32BistAPort,
       "ps32Clear": ps32Clear,
       "ps32ClearAll": ps32ClearAll,
       "ps32ClearErrorsAll": ps32ClearErrorsAll,
       "ps32ClearErrorsInPort": ps32ClearErrorsInPort,
       "ps32ClearPathAll": ps32ClearPathAll,
       "ps32ClearPathInPort": ps32ClearPathInPort,
       "ps32ClearPathDest": ps32ClearPathDest,
       "ps32ClearPathForce": ps32ClearPathForce,
       "ps32ClearStatsAll": ps32ClearStatsAll,
       "ps32ClearStatsInPort": ps32ClearStatsInPort,
       "ps32Disable": ps32Disable,
       "ps32Disable2": ps32Disable2,
       "ps32DisablePortAll": ps32DisablePortAll,
       "ps32DisablePortInPort": ps32DisablePortInPort,
       "ps32Display": ps32Display,
       "ps32Display2": ps32Display2,
       "ps32Config": ps32Config,
       "ps32DCTitle": ps32DCTitle,
       "ps32DCTable": ps32DCTable,
       "ps32DCEntry": ps32DCEntry,
       "ps32DCLine": ps32DCLine,
       "ps32PathList": ps32PathList,
       "ps32DSPTable": ps32DSPTable,
       "ps32DSPPathwayTable": ps32DSPPathwayTable,
       "ps32DSPPathwayEntry": ps32DSPPathwayEntry,
       "ps32DSPLine": ps32DSPLine,
       "ps32DSPDPathwayTable": ps32DSPDPathwayTable,
       "ps32DSPDPathwayEntry": ps32DSPDPathwayEntry,
       "ps32DSPDLine": ps32DSPDLine,
       "ps32DSPIPathwayTable": ps32DSPIPathwayTable,
       "ps32DSPIPathwayEntry": ps32DSPIPathwayEntry,
       "ps32DSPILine": ps32DSPILine,
       "ps32Status": ps32Status,
       "ps32AllStatus": ps32AllStatus,
       "ps32DSATitle": ps32DSATitle,
       "ps32DSATable": ps32DSATable,
       "ps32DSAEntry": ps32DSAEntry,
       "ps32DSALine": ps32DSALine,
       "ps32IPStatus": ps32IPStatus,
       "ps32DSITable": ps32DSITable,
       "ps32DSIEntry": ps32DSIEntry,
       "ps32DSILine1": ps32DSILine1,
       "ps32DSILine2": ps32DSILine2,
       "ps32DSILine3": ps32DSILine3,
       "ps32DSILine4": ps32DSILine4,
       "ps32DSILine5": ps32DSILine5,
       "ps32DSILine6": ps32DSILine6,
       "ps32DSILine7": ps32DSILine7,
       "ps32DSILine8": ps32DSILine8,
       "ps32DSILine9": ps32DSILine9,
       "ps32MiscStatus": ps32MiscStatus,
       "ps32DSMTable": ps32DSMTable,
       "ps32DSMEntry": ps32DSMEntry,
       "ps32DSMLine": ps32DSMLine,
       "ps32Version": ps32Version,
       "ps32Enable": ps32Enable,
       "ps32Enable2": ps32Enable2,
       "ps32EnablePortAll": ps32EnablePortAll,
       "ps32EnablePortInPort": ps32EnablePortInPort,
       "ps32ResetSwitch": ps32ResetSwitch,
       "ps32Restore": ps32Restore,
       "ps32Restore2": ps32Restore2,
       "ps32RestorePathAll": ps32RestorePathAll,
       "ps32RestorePathInPort": ps32RestorePathInPort,
       "ps32Save": ps32Save,
       "ps32Save2": ps32Save2,
       "ps32SaveAll": ps32SaveAll,
       "ps32SaveConfig": ps32SaveConfig,
       "ps32SavePathAll": ps32SavePathAll,
       "ps32SavePathInPort": ps32SavePathInPort,
       "ps32Set": ps32Set,
       "ps32Set2": ps32Set2,
       "ps32SetPathAll": ps32SetPathAll,
       "ps32SetPathDest": ps32SetPathDest,
       "ps32SetPathForce": ps32SetPathForce}
)
