# SNMP MIB module (NNCGNI00X9-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X9-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:30 2024
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

(nncExtSyncDataCct,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtSyncDataCct")

(PositionIndex,) = mibBuilder.importSymbols(
    "NNCGNI00X4-MIB",
    "PositionIndex")

(CircuitIndex,
 PortIndex) = mibBuilder.importSymbols(
    "NNCGNI00X7-MIB",
    "CircuitIndex",
    "PortIndex")

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



class LeadIndex(Integer32):
    """Custom type LeadIndex based on Integer32"""
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
        *(("alb", 2),
          ("cts", 6),
          ("dcd", 7),
          ("dsr", 8),
          ("dtr", 4),
          ("rdl", 1),
          ("ri", 5),
          ("rts", 3))
    )





class LeadAdminState(Integer32):
    """Custom type LeadAdminState based on Integer32"""
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
        *(("assumedOff", 4),
          ("assumedOn", 3),
          ("forcedOff", 2),
          ("forcedOn", 1),
          ("monitor", 5))
    )





class LeadOperState(Integer32):
    """Custom type LeadOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtSdcTable_Object = MibTable
nncExtSdcTable = _NncExtSdcTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1)
)
if mibBuilder.loadTexts:
    nncExtSdcTable.setStatus("mandatory")
_NncExtSdcEntry_Object = MibTableRow
nncExtSdcEntry = _NncExtSdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1)
)
nncExtSdcEntry.setIndexNames(
    (0, "NNCGNI00X9-MIB", "nncExtSdcPosnIdx"),
    (0, "NNCGNI00X9-MIB", "nncExtSdcPortIdx"),
    (0, "NNCGNI00X9-MIB", "nncExtSdcCctIdx"),
)
if mibBuilder.loadTexts:
    nncExtSdcEntry.setStatus("mandatory")
_NncExtSdcPosnIdx_Type = PositionIndex
_NncExtSdcPosnIdx_Object = MibTableColumn
nncExtSdcPosnIdx = _NncExtSdcPosnIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 1),
    _NncExtSdcPosnIdx_Type()
)
nncExtSdcPosnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcPosnIdx.setStatus("mandatory")
_NncExtSdcPortIdx_Type = PortIndex
_NncExtSdcPortIdx_Object = MibTableColumn
nncExtSdcPortIdx = _NncExtSdcPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 2),
    _NncExtSdcPortIdx_Type()
)
nncExtSdcPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcPortIdx.setStatus("mandatory")
_NncExtSdcCctIdx_Type = CircuitIndex
_NncExtSdcCctIdx_Object = MibTableColumn
nncExtSdcCctIdx = _NncExtSdcCctIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 3),
    _NncExtSdcCctIdx_Type()
)
nncExtSdcCctIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcCctIdx.setStatus("mandatory")


class _NncExtSdcGender_Type(Integer32):
    """Custom type nncExtSdcGender based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_NncExtSdcGender_Type.__name__ = "Integer32"
_NncExtSdcGender_Object = MibTableColumn
nncExtSdcGender = _NncExtSdcGender_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 4),
    _NncExtSdcGender_Type()
)
nncExtSdcGender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtSdcGender.setStatus("mandatory")


class _NncExtSdcSpeed_Type(Integer32):
    """Custom type nncExtSdcSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048000),
    )


_NncExtSdcSpeed_Type.__name__ = "Integer32"
_NncExtSdcSpeed_Object = MibTableColumn
nncExtSdcSpeed = _NncExtSdcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 5),
    _NncExtSdcSpeed_Type()
)
nncExtSdcSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtSdcSpeed.setStatus("mandatory")


class _NncExtSdcActualSpeed_Type(Integer32):
    """Custom type nncExtSdcActualSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_NncExtSdcActualSpeed_Type.__name__ = "Integer32"
_NncExtSdcActualSpeed_Object = MibTableColumn
nncExtSdcActualSpeed = _NncExtSdcActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 6),
    _NncExtSdcActualSpeed_Type()
)
nncExtSdcActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcActualSpeed.setStatus("mandatory")
_NncExtSdcLeadsTable_Object = MibTable
nncExtSdcLeadsTable = _NncExtSdcLeadsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 2)
)
if mibBuilder.loadTexts:
    nncExtSdcLeadsTable.setStatus("mandatory")
_NncExtSdcLeadsEntry_Object = MibTableRow
nncExtSdcLeadsEntry = _NncExtSdcLeadsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1)
)
nncExtSdcLeadsEntry.setIndexNames(
    (0, "NNCGNI00X9-MIB", "nncExtSdcPosnIdx"),
    (0, "NNCGNI00X9-MIB", "nncExtSdcPortIdx"),
    (0, "NNCGNI00X9-MIB", "nncExtSdcCctIdx"),
    (0, "NNCGNI00X9-MIB", "nncExtSdcLeadIdx"),
)
if mibBuilder.loadTexts:
    nncExtSdcLeadsEntry.setStatus("mandatory")


class _NncExtSdcLeadIdx_Type(Integer32):
    """Custom type nncExtSdcLeadIdx based on Integer32"""
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
        *(("alb", 2),
          ("cts", 6),
          ("dcd", 7),
          ("dsr", 8),
          ("dtr", 4),
          ("rdl", 1),
          ("ri", 5),
          ("rts", 3))
    )


_NncExtSdcLeadIdx_Type.__name__ = "Integer32"
_NncExtSdcLeadIdx_Object = MibTableColumn
nncExtSdcLeadIdx = _NncExtSdcLeadIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 1),
    _NncExtSdcLeadIdx_Type()
)
nncExtSdcLeadIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcLeadIdx.setStatus("mandatory")


class _NncExtSdcLeadAdminState_Type(Integer32):
    """Custom type nncExtSdcLeadAdminState based on Integer32"""
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
        *(("assumedOff", 4),
          ("assumedOn", 3),
          ("forcedOff", 2),
          ("forcedOn", 1),
          ("monitor", 5))
    )


_NncExtSdcLeadAdminState_Type.__name__ = "Integer32"
_NncExtSdcLeadAdminState_Object = MibTableColumn
nncExtSdcLeadAdminState = _NncExtSdcLeadAdminState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 2),
    _NncExtSdcLeadAdminState_Type()
)
nncExtSdcLeadAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtSdcLeadAdminState.setStatus("mandatory")


class _NncExtSdcLeadOperState_Type(Integer32):
    """Custom type nncExtSdcLeadOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_NncExtSdcLeadOperState_Type.__name__ = "Integer32"
_NncExtSdcLeadOperState_Object = MibTableColumn
nncExtSdcLeadOperState = _NncExtSdcLeadOperState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 3),
    _NncExtSdcLeadOperState_Type()
)
nncExtSdcLeadOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcLeadOperState.setStatus("mandatory")


class _NncExtSdcLeadUIName_Type(DisplayString):
    """Custom type nncExtSdcLeadUIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_NncExtSdcLeadUIName_Type.__name__ = "DisplayString"
_NncExtSdcLeadUIName_Object = MibTableColumn
nncExtSdcLeadUIName = _NncExtSdcLeadUIName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 4),
    _NncExtSdcLeadUIName_Type()
)
nncExtSdcLeadUIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSdcLeadUIName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X9-MIB",
    **{"LeadIndex": LeadIndex,
       "LeadAdminState": LeadAdminState,
       "LeadOperState": LeadOperState,
       "nncExtSdcTable": nncExtSdcTable,
       "nncExtSdcEntry": nncExtSdcEntry,
       "nncExtSdcPosnIdx": nncExtSdcPosnIdx,
       "nncExtSdcPortIdx": nncExtSdcPortIdx,
       "nncExtSdcCctIdx": nncExtSdcCctIdx,
       "nncExtSdcGender": nncExtSdcGender,
       "nncExtSdcSpeed": nncExtSdcSpeed,
       "nncExtSdcActualSpeed": nncExtSdcActualSpeed,
       "nncExtSdcLeadsTable": nncExtSdcLeadsTable,
       "nncExtSdcLeadsEntry": nncExtSdcLeadsEntry,
       "nncExtSdcLeadIdx": nncExtSdcLeadIdx,
       "nncExtSdcLeadAdminState": nncExtSdcLeadAdminState,
       "nncExtSdcLeadOperState": nncExtSdcLeadOperState,
       "nncExtSdcLeadUIName": nncExtSdcLeadUIName}
)
