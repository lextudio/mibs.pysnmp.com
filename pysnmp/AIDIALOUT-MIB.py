# SNMP MIB module (AIDIALOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIDIALOUT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:08 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiDialOut = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 36)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiDialOutTable_Object = MibTable
aiDialOutTable = _AiDialOutTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1)
)
if mibBuilder.loadTexts:
    aiDialOutTable.setStatus("current")
_AiDialOutEntry_Object = MibTableRow
aiDialOutEntry = _AiDialOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1)
)
aiDialOutEntry.setIndexNames(
    (0, "AIDIALOUT-MIB", "aiDialOutLinkNumber"),
)
if mibBuilder.loadTexts:
    aiDialOutEntry.setStatus("current")
_AiDialOutLinkNumber_Type = PositiveInteger
_AiDialOutLinkNumber_Object = MibTableColumn
aiDialOutLinkNumber = _AiDialOutLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 1),
    _AiDialOutLinkNumber_Type()
)
aiDialOutLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDialOutLinkNumber.setStatus("current")
_AiDialOutStatus_Type = TruthValue
_AiDialOutStatus_Object = MibTableColumn
aiDialOutStatus = _AiDialOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 2),
    _AiDialOutStatus_Type()
)
aiDialOutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDialOutStatus.setStatus("current")
_AiDialOutPrimaryDialString_Type = DisplayString
_AiDialOutPrimaryDialString_Object = MibTableColumn
aiDialOutPrimaryDialString = _AiDialOutPrimaryDialString_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 3),
    _AiDialOutPrimaryDialString_Type()
)
aiDialOutPrimaryDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDialOutPrimaryDialString.setStatus("current")
_AiDialOutSecondaryDialString_Type = DisplayString
_AiDialOutSecondaryDialString_Object = MibTableColumn
aiDialOutSecondaryDialString = _AiDialOutSecondaryDialString_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 4),
    _AiDialOutSecondaryDialString_Type()
)
aiDialOutSecondaryDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDialOutSecondaryDialString.setStatus("current")


class _AiDialOutTimeOut_Type(Integer32):
    """Custom type aiDialOutTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_AiDialOutTimeOut_Type.__name__ = "Integer32"
_AiDialOutTimeOut_Object = MibTableColumn
aiDialOutTimeOut = _AiDialOutTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 5),
    _AiDialOutTimeOut_Type()
)
aiDialOutTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDialOutTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    aiDialOutTimeOut.setUnits("seconds")


class _AiDialOutAttempts_Type(Integer32):
    """Custom type aiDialOutAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AiDialOutAttempts_Type.__name__ = "Integer32"
_AiDialOutAttempts_Object = MibTableColumn
aiDialOutAttempts = _AiDialOutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 6),
    _AiDialOutAttempts_Type()
)
aiDialOutAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDialOutAttempts.setStatus("current")
if mibBuilder.loadTexts:
    aiDialOutAttempts.setUnits("seconds")


class _AiDialOutInterval_Type(Integer32):
    """Custom type aiDialOutInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AiDialOutInterval_Type.__name__ = "Integer32"
_AiDialOutInterval_Object = MibTableColumn
aiDialOutInterval = _AiDialOutInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 7),
    _AiDialOutInterval_Type()
)
aiDialOutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDialOutInterval.setStatus("current")
if mibBuilder.loadTexts:
    aiDialOutInterval.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIDIALOUT-MIB",
    **{"PositiveInteger": PositiveInteger,
       "aii": aii,
       "aiDialOut": aiDialOut,
       "aiDialOutTable": aiDialOutTable,
       "aiDialOutEntry": aiDialOutEntry,
       "aiDialOutLinkNumber": aiDialOutLinkNumber,
       "aiDialOutStatus": aiDialOutStatus,
       "aiDialOutPrimaryDialString": aiDialOutPrimaryDialString,
       "aiDialOutSecondaryDialString": aiDialOutSecondaryDialString,
       "aiDialOutTimeOut": aiDialOutTimeOut,
       "aiDialOutAttempts": aiDialOutAttempts,
       "aiDialOutInterval": aiDialOutInterval}
)
