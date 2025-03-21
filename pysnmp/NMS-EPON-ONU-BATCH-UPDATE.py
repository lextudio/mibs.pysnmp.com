# SNMP MIB module (NMS-EPON-ONU-BATCH-UPDATE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-ONU-BATCH-UPDATE
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:48 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOnuBatchUpdate_ObjectIdentity = ObjectIdentity
nmsEponOnuBatchUpdate = _NmsEponOnuBatchUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 23)
)
_OnuUpdateLLIDs_Type = PortList
_OnuUpdateLLIDs_Object = MibScalar
onuUpdateLLIDs = _OnuUpdateLLIDs_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 1),
    _OnuUpdateLLIDs_Type()
)
onuUpdateLLIDs.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuUpdateLLIDs.setStatus("mandatory")
_OnuUpdateFileName_Type = OctetString
_OnuUpdateFileName_Object = MibScalar
onuUpdateFileName = _OnuUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 2),
    _OnuUpdateFileName_Type()
)
onuUpdateFileName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuUpdateFileName.setStatus("mandatory")


class _OnuUpdateAction_Type(Integer32):
    """Custom type onuUpdateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("no_action", 0),
          ("update", 1))
    )


_OnuUpdateAction_Type.__name__ = "Integer32"
_OnuUpdateAction_Object = MibScalar
onuUpdateAction = _OnuUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 3),
    _OnuUpdateAction_Type()
)
onuUpdateAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuUpdateAction.setStatus("mandatory")


class _OnuUpdateResult_Type(Integer32):
    """Custom type onuUpdateResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("processing", 1),
          ("success", 0))
    )


_OnuUpdateResult_Type.__name__ = "Integer32"
_OnuUpdateResult_Object = MibScalar
onuUpdateResult = _OnuUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 23, 4),
    _OnuUpdateResult_Type()
)
onuUpdateResult.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuUpdateResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-ONU-BATCH-UPDATE",
    **{"nmsEponOnuBatchUpdate": nmsEponOnuBatchUpdate,
       "onuUpdateLLIDs": onuUpdateLLIDs,
       "onuUpdateFileName": onuUpdateFileName,
       "onuUpdateAction": onuUpdateAction,
       "onuUpdateResult": onuUpdateResult}
)
