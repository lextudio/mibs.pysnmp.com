# SNMP MIB module (IBMHPRROUTETEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMHPRROUTETEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:54 2024
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmArchitecture_ObjectIdentity = ObjectIdentity
ibmArchitecture = _IbmArchitecture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5)
)
_Hpr_ObjectIdentity = ObjectIdentity
hpr = _Hpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10)
)
_IbmHprRouteTest_ObjectIdentity = ObjectIdentity
ibmHprRouteTest = _IbmHprRouteTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4)
)
_IbmHprRtGlobe_ObjectIdentity = ObjectIdentity
ibmHprRtGlobe = _IbmHprRtGlobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 1)
)


class _IbmHprRtGlobeConnTrigger_Type(OctetString):
    """Custom type ibmHprRtGlobeConnTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 17),
    )


_IbmHprRtGlobeConnTrigger_Type.__name__ = "OctetString"
_IbmHprRtGlobeConnTrigger_Object = MibScalar
ibmHprRtGlobeConnTrigger = _IbmHprRtGlobeConnTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 1, 1),
    _IbmHprRtGlobeConnTrigger_Type()
)
ibmHprRtGlobeConnTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmHprRtGlobeConnTrigger.setStatus("mandatory")


class _IbmHprRtGlobeNameTrigger_Type(DisplayString):
    """Custom type ibmHprRtGlobeNameTrigger based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 26),
    )


_IbmHprRtGlobeNameTrigger_Type.__name__ = "DisplayString"
_IbmHprRtGlobeNameTrigger_Object = MibScalar
ibmHprRtGlobeNameTrigger = _IbmHprRtGlobeNameTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 1, 2),
    _IbmHprRtGlobeNameTrigger_Type()
)
ibmHprRtGlobeNameTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmHprRtGlobeNameTrigger.setStatus("mandatory")
_IbmHprRtGenResults_ObjectIdentity = ObjectIdentity
ibmHprRtGenResults = _IbmHprRtGenResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2)
)
_IbmHprRtGenTable_Object = MibTable
ibmHprRtGenTable = _IbmHprRtGenTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ibmHprRtGenTable.setStatus("mandatory")
_IbmHprRtGenEntry_Object = MibTableRow
ibmHprRtGenEntry = _IbmHprRtGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1)
)
ibmHprRtGenEntry.setIndexNames(
    (0, "IBMHPRROUTETEST-MIB", "ibmHprRtGenTestId"),
)
if mibBuilder.loadTexts:
    ibmHprRtGenEntry.setStatus("mandatory")
_IbmHprRtGenTestId_Type = Gauge32
_IbmHprRtGenTestId_Object = MibTableColumn
ibmHprRtGenTestId = _IbmHprRtGenTestId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 1),
    _IbmHprRtGenTestId_Type()
)
ibmHprRtGenTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenTestId.setStatus("mandatory")


class _IbmHprRtGenTestType_Type(Integer32):
    """Custom type ibmHprRtGenTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connTrigger", 1),
          ("nameTrigger", 2))
    )


_IbmHprRtGenTestType_Type.__name__ = "Integer32"
_IbmHprRtGenTestType_Object = MibTableColumn
ibmHprRtGenTestType = _IbmHprRtGenTestType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 2),
    _IbmHprRtGenTestType_Type()
)
ibmHprRtGenTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenTestType.setStatus("mandatory")


class _IbmHprRtGenConnTrigger_Type(OctetString):
    """Custom type ibmHprRtGenConnTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 17),
    )


_IbmHprRtGenConnTrigger_Type.__name__ = "OctetString"
_IbmHprRtGenConnTrigger_Object = MibTableColumn
ibmHprRtGenConnTrigger = _IbmHprRtGenConnTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 3),
    _IbmHprRtGenConnTrigger_Type()
)
ibmHprRtGenConnTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenConnTrigger.setStatus("mandatory")


class _IbmHprRtGenNameTrigger_Type(DisplayString):
    """Custom type ibmHprRtGenNameTrigger based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 26),
    )


_IbmHprRtGenNameTrigger_Type.__name__ = "DisplayString"
_IbmHprRtGenNameTrigger_Object = MibTableColumn
ibmHprRtGenNameTrigger = _IbmHprRtGenNameTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 4),
    _IbmHprRtGenNameTrigger_Type()
)
ibmHprRtGenNameTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenNameTrigger.setStatus("mandatory")


class _IbmHprRtGenResult_Type(Integer32):
    """Custom type ibmHprRtGenResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("inProgess", 2),
          ("luInvalid", 6),
          ("modeInvalid", 7),
          ("nceidInvalid", 4),
          ("noHprRoute", 8),
          ("noResponse", 3),
          ("successful", 1),
          ("tcidInvalid", 5))
    )


_IbmHprRtGenResult_Type.__name__ = "Integer32"
_IbmHprRtGenResult_Object = MibTableColumn
ibmHprRtGenResult = _IbmHprRtGenResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 5),
    _IbmHprRtGenResult_Type()
)
ibmHprRtGenResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenResult.setStatus("mandatory")


class _IbmHprRtGenSenseCode_Type(OctetString):
    """Custom type ibmHprRtGenSenseCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmHprRtGenSenseCode_Type.__name__ = "OctetString"
_IbmHprRtGenSenseCode_Object = MibTableColumn
ibmHprRtGenSenseCode = _IbmHprRtGenSenseCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 6),
    _IbmHprRtGenSenseCode_Type()
)
ibmHprRtGenSenseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenSenseCode.setStatus("mandatory")


class _IbmHprRtGenCosName_Type(DisplayString):
    """Custom type ibmHprRtGenCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmHprRtGenCosName_Type.__name__ = "DisplayString"
_IbmHprRtGenCosName_Object = MibTableColumn
ibmHprRtGenCosName = _IbmHprRtGenCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 7),
    _IbmHprRtGenCosName_Type()
)
ibmHprRtGenCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenCosName.setStatus("mandatory")


class _IbmHprRtGenRscv_Type(OctetString):
    """Custom type ibmHprRtGenRscv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IbmHprRtGenRscv_Type.__name__ = "OctetString"
_IbmHprRtGenRscv_Object = MibTableColumn
ibmHprRtGenRscv = _IbmHprRtGenRscv_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 2, 1, 1, 8),
    _IbmHprRtGenRscv_Type()
)
ibmHprRtGenRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtGenRscv.setStatus("mandatory")
_IbmHprRtDetResults_ObjectIdentity = ObjectIdentity
ibmHprRtDetResults = _IbmHprRtDetResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3)
)
_IbmHprRtDetTable_Object = MibTable
ibmHprRtDetTable = _IbmHprRtDetTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ibmHprRtDetTable.setStatus("mandatory")
_IbmHprRtDetEntry_Object = MibTableRow
ibmHprRtDetEntry = _IbmHprRtDetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1)
)
ibmHprRtDetEntry.setIndexNames(
    (0, "IBMHPRROUTETEST-MIB", "ibmHprRtDetTestId"),
    (0, "IBMHPRROUTETEST-MIB", "ibmHprRtDetSubTestId"),
)
if mibBuilder.loadTexts:
    ibmHprRtDetEntry.setStatus("mandatory")
_IbmHprRtDetTestId_Type = Gauge32
_IbmHprRtDetTestId_Object = MibTableColumn
ibmHprRtDetTestId = _IbmHprRtDetTestId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 1),
    _IbmHprRtDetTestId_Type()
)
ibmHprRtDetTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetTestId.setStatus("mandatory")


class _IbmHprRtDetSubTestId_Type(Integer32):
    """Custom type ibmHprRtDetSubTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmHprRtDetSubTestId_Type.__name__ = "Integer32"
_IbmHprRtDetSubTestId_Object = MibTableColumn
ibmHprRtDetSubTestId = _IbmHprRtDetSubTestId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 2),
    _IbmHprRtDetSubTestId_Type()
)
ibmHprRtDetSubTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetSubTestId.setStatus("mandatory")


class _IbmHprRtDetDestNode_Type(DisplayString):
    """Custom type ibmHprRtDetDestNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IbmHprRtDetDestNode_Type.__name__ = "DisplayString"
_IbmHprRtDetDestNode_Object = MibTableColumn
ibmHprRtDetDestNode = _IbmHprRtDetDestNode_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 3),
    _IbmHprRtDetDestNode_Type()
)
ibmHprRtDetDestNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetDestNode.setStatus("mandatory")


class _IbmHprRtDetPriorNode_Type(DisplayString):
    """Custom type ibmHprRtDetPriorNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IbmHprRtDetPriorNode_Type.__name__ = "DisplayString"
_IbmHprRtDetPriorNode_Object = MibTableColumn
ibmHprRtDetPriorNode = _IbmHprRtDetPriorNode_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 4),
    _IbmHprRtDetPriorNode_Type()
)
ibmHprRtDetPriorNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetPriorNode.setStatus("mandatory")


class _IbmHprRtDetLastTgNumber_Type(Integer32):
    """Custom type ibmHprRtDetLastTgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmHprRtDetLastTgNumber_Type.__name__ = "Integer32"
_IbmHprRtDetLastTgNumber_Object = MibTableColumn
ibmHprRtDetLastTgNumber = _IbmHprRtDetLastTgNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 5),
    _IbmHprRtDetLastTgNumber_Type()
)
ibmHprRtDetLastTgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetLastTgNumber.setStatus("mandatory")
_IbmHprRtDetRtripTime_Type = Gauge32
_IbmHprRtDetRtripTime_Object = MibTableColumn
ibmHprRtDetRtripTime = _IbmHprRtDetRtripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 6),
    _IbmHprRtDetRtripTime_Type()
)
ibmHprRtDetRtripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetRtripTime.setStatus("mandatory")


class _IbmHprRtDetResult_Type(Integer32):
    """Custom type ibmHprRtDetResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResponse", 2),
          ("successful", 1))
    )


_IbmHprRtDetResult_Type.__name__ = "Integer32"
_IbmHprRtDetResult_Object = MibTableColumn
ibmHprRtDetResult = _IbmHprRtDetResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 4, 3, 1, 1, 7),
    _IbmHprRtDetResult_Type()
)
ibmHprRtDetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprRtDetResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMHPRROUTETEST-MIB",
    **{"ibm": ibm,
       "ibmArchitecture": ibmArchitecture,
       "hpr": hpr,
       "ibmHprRouteTest": ibmHprRouteTest,
       "ibmHprRtGlobe": ibmHprRtGlobe,
       "ibmHprRtGlobeConnTrigger": ibmHprRtGlobeConnTrigger,
       "ibmHprRtGlobeNameTrigger": ibmHprRtGlobeNameTrigger,
       "ibmHprRtGenResults": ibmHprRtGenResults,
       "ibmHprRtGenTable": ibmHprRtGenTable,
       "ibmHprRtGenEntry": ibmHprRtGenEntry,
       "ibmHprRtGenTestId": ibmHprRtGenTestId,
       "ibmHprRtGenTestType": ibmHprRtGenTestType,
       "ibmHprRtGenConnTrigger": ibmHprRtGenConnTrigger,
       "ibmHprRtGenNameTrigger": ibmHprRtGenNameTrigger,
       "ibmHprRtGenResult": ibmHprRtGenResult,
       "ibmHprRtGenSenseCode": ibmHprRtGenSenseCode,
       "ibmHprRtGenCosName": ibmHprRtGenCosName,
       "ibmHprRtGenRscv": ibmHprRtGenRscv,
       "ibmHprRtDetResults": ibmHprRtDetResults,
       "ibmHprRtDetTable": ibmHprRtDetTable,
       "ibmHprRtDetEntry": ibmHprRtDetEntry,
       "ibmHprRtDetTestId": ibmHprRtDetTestId,
       "ibmHprRtDetSubTestId": ibmHprRtDetSubTestId,
       "ibmHprRtDetDestNode": ibmHprRtDetDestNode,
       "ibmHprRtDetPriorNode": ibmHprRtDetPriorNode,
       "ibmHprRtDetLastTgNumber": ibmHprRtDetLastTgNumber,
       "ibmHprRtDetRtripTime": ibmHprRtDetRtripTime,
       "ibmHprRtDetResult": ibmHprRtDetResult}
)
