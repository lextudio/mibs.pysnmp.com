# SNMP MIB module (CXLLCInterfaceModule-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXLLCInterfaceModule-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:34 2024
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

(Alias,
 cxLlcim) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxLlcim")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LlcimConnectInterval_Type(Integer32):
    """Custom type llcimConnectInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 900),
    )


_LlcimConnectInterval_Type.__name__ = "Integer32"
_LlcimConnectInterval_Object = MibScalar
llcimConnectInterval = _LlcimConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 1),
    _LlcimConnectInterval_Type()
)
llcimConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcimConnectInterval.setStatus("mandatory")
_LlcimSapTable_Object = MibTable
llcimSapTable = _LlcimSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10)
)
if mibBuilder.loadTexts:
    llcimSapTable.setStatus("mandatory")
_LlcimSapEntry_Object = MibTableRow
llcimSapEntry = _LlcimSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1)
)
llcimSapEntry.setIndexNames(
    (0, "CXLLCInterfaceModule-MIB", "llcimSapNumber"),
)
if mibBuilder.loadTexts:
    llcimSapEntry.setStatus("mandatory")


class _LlcimSapNumber_Type(Integer32):
    """Custom type llcimSapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LlcimSapNumber_Type.__name__ = "Integer32"
_LlcimSapNumber_Object = MibTableColumn
llcimSapNumber = _LlcimSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 1),
    _LlcimSapNumber_Type()
)
llcimSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcimSapNumber.setStatus("mandatory")


class _LlcimSapRowStatus_Type(Integer32):
    """Custom type llcimSapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LlcimSapRowStatus_Type.__name__ = "Integer32"
_LlcimSapRowStatus_Object = MibTableColumn
llcimSapRowStatus = _LlcimSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 2),
    _LlcimSapRowStatus_Type()
)
llcimSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcimSapRowStatus.setStatus("mandatory")
_LlcimSapAlias_Type = Alias
_LlcimSapAlias_Object = MibTableColumn
llcimSapAlias = _LlcimSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 3),
    _LlcimSapAlias_Type()
)
llcimSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcimSapAlias.setStatus("mandatory")
_LlcimSapCompanionAlias_Type = Alias
_LlcimSapCompanionAlias_Object = MibTableColumn
llcimSapCompanionAlias = _LlcimSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 4),
    _LlcimSapCompanionAlias_Type()
)
llcimSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcimSapCompanionAlias.setStatus("mandatory")


class _LlcimSapType_Type(Integer32):
    """Custom type llcimSapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_LlcimSapType_Type.__name__ = "Integer32"
_LlcimSapType_Object = MibTableColumn
llcimSapType = _LlcimSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 5),
    _LlcimSapType_Type()
)
llcimSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcimSapType.setStatus("mandatory")


class _LlcimSapConnectMethod_Type(Integer32):
    """Custom type llcimSapConnectMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generateXid", 1),
          ("immediate", 3),
          ("waitForXid", 2))
    )


_LlcimSapConnectMethod_Type.__name__ = "Integer32"
_LlcimSapConnectMethod_Object = MibTableColumn
llcimSapConnectMethod = _LlcimSapConnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 6),
    _LlcimSapConnectMethod_Type()
)
llcimSapConnectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcimSapConnectMethod.setStatus("mandatory")


class _LlcimSapState_Type(Integer32):
    """Custom type llcimSapState based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("connected", 7),
          ("data", 11),
          ("inLinkDisconnect", 12),
          ("notConnected", 3),
          ("offLine", 1),
          ("outLineDisconnect", 14),
          ("outLinkDisconnect", 13),
          ("setMode", 8),
          ("setModeReceived", 10),
          ("testExchange", 4),
          ("unbound", 2),
          ("waitSetMode", 9),
          ("waitXid", 6),
          ("xidIssued", 5))
    )


_LlcimSapState_Type.__name__ = "Integer32"
_LlcimSapState_Object = MibTableColumn
llcimSapState = _LlcimSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34, 10, 1, 7),
    _LlcimSapState_Type()
)
llcimSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcimSapState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXLLCInterfaceModule-MIB",
    **{"llcimConnectInterval": llcimConnectInterval,
       "llcimSapTable": llcimSapTable,
       "llcimSapEntry": llcimSapEntry,
       "llcimSapNumber": llcimSapNumber,
       "llcimSapRowStatus": llcimSapRowStatus,
       "llcimSapAlias": llcimSapAlias,
       "llcimSapCompanionAlias": llcimSapCompanionAlias,
       "llcimSapType": llcimSapType,
       "llcimSapConnectMethod": llcimSapConnectMethod,
       "llcimSapState": llcimSapState}
)
