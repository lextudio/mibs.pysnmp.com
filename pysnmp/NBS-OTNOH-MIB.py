# SNMP MIB module (NBS-OTNOH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-OTNOH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:55 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nbsOtnohMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 224)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsOtnohTtiGrp_ObjectIdentity = ObjectIdentity
nbsOtnohTtiGrp = _NbsOtnohTtiGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 224, 1)
)
if mibBuilder.loadTexts:
    nbsOtnohTtiGrp.setStatus("current")
_NbsOtnohTtiTable_Object = MibTable
nbsOtnohTtiTable = _NbsOtnohTtiTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1)
)
if mibBuilder.loadTexts:
    nbsOtnohTtiTable.setStatus("current")
_NbsOtnohTtiEntry_Object = MibTableRow
nbsOtnohTtiEntry = _NbsOtnohTtiEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1)
)
nbsOtnohTtiEntry.setIndexNames(
    (0, "NBS-OTNOH-MIB", "nbsOtnohTtiIfIndex"),
    (0, "NBS-OTNOH-MIB", "nbsOtnohTtiScope"),
)
if mibBuilder.loadTexts:
    nbsOtnohTtiEntry.setStatus("current")
_NbsOtnohTtiIfIndex_Type = InterfaceIndex
_NbsOtnohTtiIfIndex_Object = MibTableColumn
nbsOtnohTtiIfIndex = _NbsOtnohTtiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 1),
    _NbsOtnohTtiIfIndex_Type()
)
nbsOtnohTtiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOtnohTtiIfIndex.setStatus("current")


class _NbsOtnohTtiScope_Type(Integer32):
    """Custom type nbsOtnohTtiScope based on Integer32"""
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
        *(("path", 8),
          ("section", 7),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6))
    )


_NbsOtnohTtiScope_Type.__name__ = "Integer32"
_NbsOtnohTtiScope_Object = MibTableColumn
nbsOtnohTtiScope = _NbsOtnohTtiScope_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 2),
    _NbsOtnohTtiScope_Type()
)
nbsOtnohTtiScope.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOtnohTtiScope.setStatus("current")


class _NbsOtnohTtiSendSapi_Type(OctetString):
    """Custom type nbsOtnohTtiSendSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsOtnohTtiSendSapi_Type.__name__ = "OctetString"
_NbsOtnohTtiSendSapi_Object = MibTableColumn
nbsOtnohTtiSendSapi = _NbsOtnohTtiSendSapi_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 3),
    _NbsOtnohTtiSendSapi_Type()
)
nbsOtnohTtiSendSapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiSendSapi.setStatus("current")


class _NbsOtnohTtiSendDapi_Type(OctetString):
    """Custom type nbsOtnohTtiSendDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsOtnohTtiSendDapi_Type.__name__ = "OctetString"
_NbsOtnohTtiSendDapi_Object = MibTableColumn
nbsOtnohTtiSendDapi = _NbsOtnohTtiSendDapi_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 4),
    _NbsOtnohTtiSendDapi_Type()
)
nbsOtnohTtiSendDapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiSendDapi.setStatus("current")


class _NbsOtnohTtiSendOpSpec_Type(OctetString):
    """Custom type nbsOtnohTtiSendOpSpec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsOtnohTtiSendOpSpec_Type.__name__ = "OctetString"
_NbsOtnohTtiSendOpSpec_Object = MibTableColumn
nbsOtnohTtiSendOpSpec = _NbsOtnohTtiSendOpSpec_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 5),
    _NbsOtnohTtiSendOpSpec_Type()
)
nbsOtnohTtiSendOpSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiSendOpSpec.setStatus("current")


class _NbsOtnohTtiExpectSapi_Type(OctetString):
    """Custom type nbsOtnohTtiExpectSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsOtnohTtiExpectSapi_Type.__name__ = "OctetString"
_NbsOtnohTtiExpectSapi_Object = MibTableColumn
nbsOtnohTtiExpectSapi = _NbsOtnohTtiExpectSapi_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 6),
    _NbsOtnohTtiExpectSapi_Type()
)
nbsOtnohTtiExpectSapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiExpectSapi.setStatus("current")


class _NbsOtnohTtiExpectDapi_Type(OctetString):
    """Custom type nbsOtnohTtiExpectDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsOtnohTtiExpectDapi_Type.__name__ = "OctetString"
_NbsOtnohTtiExpectDapi_Object = MibTableColumn
nbsOtnohTtiExpectDapi = _NbsOtnohTtiExpectDapi_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 7),
    _NbsOtnohTtiExpectDapi_Type()
)
nbsOtnohTtiExpectDapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiExpectDapi.setStatus("current")


class _NbsOtnohTtiExpectOpSpec_Type(OctetString):
    """Custom type nbsOtnohTtiExpectOpSpec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsOtnohTtiExpectOpSpec_Type.__name__ = "OctetString"
_NbsOtnohTtiExpectOpSpec_Object = MibTableColumn
nbsOtnohTtiExpectOpSpec = _NbsOtnohTtiExpectOpSpec_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 8),
    _NbsOtnohTtiExpectOpSpec_Type()
)
nbsOtnohTtiExpectOpSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiExpectOpSpec.setStatus("current")
_NbsOtnohTtiRowStatus_Type = RowStatus
_NbsOtnohTtiRowStatus_Object = MibTableColumn
nbsOtnohTtiRowStatus = _NbsOtnohTtiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 10),
    _NbsOtnohTtiRowStatus_Type()
)
nbsOtnohTtiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsOtnohTtiRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-OTNOH-MIB",
    **{"nbsOtnohMib": nbsOtnohMib,
       "nbsOtnohTtiGrp": nbsOtnohTtiGrp,
       "nbsOtnohTtiTable": nbsOtnohTtiTable,
       "nbsOtnohTtiEntry": nbsOtnohTtiEntry,
       "nbsOtnohTtiIfIndex": nbsOtnohTtiIfIndex,
       "nbsOtnohTtiScope": nbsOtnohTtiScope,
       "nbsOtnohTtiSendSapi": nbsOtnohTtiSendSapi,
       "nbsOtnohTtiSendDapi": nbsOtnohTtiSendDapi,
       "nbsOtnohTtiSendOpSpec": nbsOtnohTtiSendOpSpec,
       "nbsOtnohTtiExpectSapi": nbsOtnohTtiExpectSapi,
       "nbsOtnohTtiExpectDapi": nbsOtnohTtiExpectDapi,
       "nbsOtnohTtiExpectOpSpec": nbsOtnohTtiExpectOpSpec,
       "nbsOtnohTtiRowStatus": nbsOtnohTtiRowStatus}
)
