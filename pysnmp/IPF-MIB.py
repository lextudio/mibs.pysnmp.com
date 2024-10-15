# SNMP MIB module (IPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:46 2024
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

_Sbe_ObjectIdentity = ObjectIdentity
sbe = _Sbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055)
)
_Ipf_ObjectIdentity = ObjectIdentity
ipf = _Ipf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 5)
)
_IpfMIBVersion_Type = Integer32
_IpfMIBVersion_Object = MibScalar
ipfMIBVersion = _IpfMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 1),
    _IpfMIBVersion_Type()
)
ipfMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfMIBVersion.setStatus("mandatory")
_IpfVersion_Type = Integer32
_IpfVersion_Object = MibScalar
ipfVersion = _IpfVersion_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 2),
    _IpfVersion_Type()
)
ipfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfVersion.setStatus("mandatory")


class _IpfState_Type(Integer32):
    """Custom type ipfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_IpfState_Type.__name__ = "Integer32"
_IpfState_Object = MibScalar
ipfState = _IpfState_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 3),
    _IpfState_Type()
)
ipfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfState.setStatus("mandatory")


class _IpfCommand_Type(Integer32):
    """Custom type ipfCommand based on Integer32"""
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
        *(("clear", 5),
          ("delete", 4),
          ("disable", 2),
          ("enable", 3),
          ("update", 1))
    )


_IpfCommand_Type.__name__ = "Integer32"
_IpfCommand_Object = MibScalar
ipfCommand = _IpfCommand_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 4),
    _IpfCommand_Type()
)
ipfCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfCommand.setStatus("mandatory")


class _IpfDefAction_Type(Integer32):
    """Custom type ipfDefAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_IpfDefAction_Type.__name__ = "Integer32"
_IpfDefAction_Object = MibScalar
ipfDefAction = _IpfDefAction_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 5),
    _IpfDefAction_Type()
)
ipfDefAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfDefAction.setStatus("mandatory")
_IpfParseTable_Object = MibTable
ipfParseTable = _IpfParseTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 6)
)
if mibBuilder.loadTexts:
    ipfParseTable.setStatus("mandatory")
_IpfParseEntry_Object = MibTableRow
ipfParseEntry = _IpfParseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 6, 2)
)
ipfParseEntry.setIndexNames(
    (0, "IPF-MIB", "ipfParseEntryNumber"),
)
if mibBuilder.loadTexts:
    ipfParseEntry.setStatus("mandatory")


class _IpfParseEntryStatus_Type(Integer32):
    """Custom type ipfParseEntryStatus based on Integer32"""
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
        *(("create-request", 2),
          ("invalid", 4),
          ("under-creation", 3),
          ("valid", 1))
    )


_IpfParseEntryStatus_Type.__name__ = "Integer32"
_IpfParseEntryStatus_Object = MibTableColumn
ipfParseEntryStatus = _IpfParseEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 1),
    _IpfParseEntryStatus_Type()
)
ipfParseEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfParseEntryStatus.setStatus("mandatory")
_IpfParseEntryNumber_Type = Integer32
_IpfParseEntryNumber_Object = MibTableColumn
ipfParseEntryNumber = _IpfParseEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 2),
    _IpfParseEntryNumber_Type()
)
ipfParseEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfParseEntryNumber.setStatus("mandatory")


class _IpfParseEntryText_Type(DisplayString):
    """Custom type ipfParseEntryText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpfParseEntryText_Type.__name__ = "DisplayString"
_IpfParseEntryText_Object = MibTableColumn
ipfParseEntryText = _IpfParseEntryText_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 3),
    _IpfParseEntryText_Type()
)
ipfParseEntryText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfParseEntryText.setStatus("mandatory")


class _IpfParseEntryError_Type(DisplayString):
    """Custom type ipfParseEntryError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpfParseEntryError_Type.__name__ = "DisplayString"
_IpfParseEntryError_Object = MibTableColumn
ipfParseEntryError = _IpfParseEntryError_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 4),
    _IpfParseEntryError_Type()
)
ipfParseEntryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfParseEntryError.setStatus("mandatory")
_IpfCurrRules_Object = MibTable
ipfCurrRules = _IpfCurrRules_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7)
)
if mibBuilder.loadTexts:
    ipfCurrRules.setStatus("mandatory")
_IpfCurrRule_Object = MibTableRow
ipfCurrRule = _IpfCurrRule_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2)
)
ipfCurrRule.setIndexNames(
    (0, "IPF-MIB", "ipfCurrRuleNumber"),
)
if mibBuilder.loadTexts:
    ipfCurrRule.setStatus("mandatory")


class _IpfCurrRuleStatus_Type(Integer32):
    """Custom type ipfCurrRuleStatus based on Integer32"""
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
        *(("create-request", 2),
          ("invalid", 4),
          ("under-creation", 3),
          ("valid", 1))
    )


_IpfCurrRuleStatus_Type.__name__ = "Integer32"
_IpfCurrRuleStatus_Object = MibTableColumn
ipfCurrRuleStatus = _IpfCurrRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 1),
    _IpfCurrRuleStatus_Type()
)
ipfCurrRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfCurrRuleStatus.setStatus("mandatory")
_IpfCurrRuleNumber_Type = Integer32
_IpfCurrRuleNumber_Object = MibTableColumn
ipfCurrRuleNumber = _IpfCurrRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 2),
    _IpfCurrRuleNumber_Type()
)
ipfCurrRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfCurrRuleNumber.setStatus("mandatory")


class _IpfCurrRuleText_Type(DisplayString):
    """Custom type ipfCurrRuleText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpfCurrRuleText_Type.__name__ = "DisplayString"
_IpfCurrRuleText_Object = MibTableColumn
ipfCurrRuleText = _IpfCurrRuleText_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 3),
    _IpfCurrRuleText_Type()
)
ipfCurrRuleText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfCurrRuleText.setStatus("mandatory")
_IpfCurrRuleFlags_Type = Integer32
_IpfCurrRuleFlags_Object = MibTableColumn
ipfCurrRuleFlags = _IpfCurrRuleFlags_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 4),
    _IpfCurrRuleFlags_Type()
)
ipfCurrRuleFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfCurrRuleFlags.setStatus("mandatory")
_IpfCurrRuleHits_Type = Integer32
_IpfCurrRuleHits_Object = MibTableColumn
ipfCurrRuleHits = _IpfCurrRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 5),
    _IpfCurrRuleHits_Type()
)
ipfCurrRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfCurrRuleHits.setStatus("mandatory")
_IpfCurrRuleBytes_Type = Integer32
_IpfCurrRuleBytes_Object = MibTableColumn
ipfCurrRuleBytes = _IpfCurrRuleBytes_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 6),
    _IpfCurrRuleBytes_Type()
)
ipfCurrRuleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfCurrRuleBytes.setStatus("mandatory")
_NatCurrRules_Object = MibTable
natCurrRules = _NatCurrRules_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8)
)
if mibBuilder.loadTexts:
    natCurrRules.setStatus("mandatory")
_NatCurrRule_Object = MibTableRow
natCurrRule = _NatCurrRule_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8, 2)
)
natCurrRule.setIndexNames(
    (0, "IPF-MIB", "natCurrRuleNumber"),
)
if mibBuilder.loadTexts:
    natCurrRule.setStatus("mandatory")


class _NatCurrRuleStatus_Type(Integer32):
    """Custom type natCurrRuleStatus based on Integer32"""
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
        *(("create-request", 2),
          ("invalid", 4),
          ("under-creation", 3),
          ("valid", 1))
    )


_NatCurrRuleStatus_Type.__name__ = "Integer32"
_NatCurrRuleStatus_Object = MibTableColumn
natCurrRuleStatus = _NatCurrRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 1),
    _NatCurrRuleStatus_Type()
)
natCurrRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natCurrRuleStatus.setStatus("mandatory")
_NatCurrRuleNumber_Type = Integer32
_NatCurrRuleNumber_Object = MibTableColumn
natCurrRuleNumber = _NatCurrRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 2),
    _NatCurrRuleNumber_Type()
)
natCurrRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natCurrRuleNumber.setStatus("mandatory")


class _NatCurrRuleText_Type(DisplayString):
    """Custom type natCurrRuleText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NatCurrRuleText_Type.__name__ = "DisplayString"
_NatCurrRuleText_Object = MibTableColumn
natCurrRuleText = _NatCurrRuleText_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 3),
    _NatCurrRuleText_Type()
)
natCurrRuleText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natCurrRuleText.setStatus("mandatory")
_NatCurrRuleHits_Type = Integer32
_NatCurrRuleHits_Object = MibTableColumn
natCurrRuleHits = _NatCurrRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 4),
    _NatCurrRuleHits_Type()
)
natCurrRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natCurrRuleHits.setStatus("mandatory")
_NatCurrRulePend_Type = Integer32
_NatCurrRulePend_Object = MibTableColumn
natCurrRulePend = _NatCurrRulePend_Object(
    (1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 5),
    _NatCurrRulePend_Type()
)
natCurrRulePend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natCurrRulePend.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPF-MIB",
    **{"sbe": sbe,
       "ipf": ipf,
       "ipfMIBVersion": ipfMIBVersion,
       "ipfVersion": ipfVersion,
       "ipfState": ipfState,
       "ipfCommand": ipfCommand,
       "ipfDefAction": ipfDefAction,
       "ipfParseTable": ipfParseTable,
       "ipfParseEntry": ipfParseEntry,
       "ipfParseEntryStatus": ipfParseEntryStatus,
       "ipfParseEntryNumber": ipfParseEntryNumber,
       "ipfParseEntryText": ipfParseEntryText,
       "ipfParseEntryError": ipfParseEntryError,
       "ipfCurrRules": ipfCurrRules,
       "ipfCurrRule": ipfCurrRule,
       "ipfCurrRuleStatus": ipfCurrRuleStatus,
       "ipfCurrRuleNumber": ipfCurrRuleNumber,
       "ipfCurrRuleText": ipfCurrRuleText,
       "ipfCurrRuleFlags": ipfCurrRuleFlags,
       "ipfCurrRuleHits": ipfCurrRuleHits,
       "ipfCurrRuleBytes": ipfCurrRuleBytes,
       "natCurrRules": natCurrRules,
       "natCurrRule": natCurrRule,
       "natCurrRuleStatus": natCurrRuleStatus,
       "natCurrRuleNumber": natCurrRuleNumber,
       "natCurrRuleText": natCurrRuleText,
       "natCurrRuleHits": natCurrRuleHits,
       "natCurrRulePend": natCurrRulePend}
)
