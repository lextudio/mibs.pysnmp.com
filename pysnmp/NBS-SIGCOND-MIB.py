# SNMP MIB module (NBS-SIGCOND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-SIGCOND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:00 2024
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

(nbs,) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nbsSigCondMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227)
)


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsSigCondVoaPortGrp_ObjectIdentity = ObjectIdentity
nbsSigCondVoaPortGrp = _NbsSigCondVoaPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 1)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaPortGrp.setStatus("current")
_NbsSigCondVoaPortTableSize_Type = Unsigned32
_NbsSigCondVoaPortTableSize_Object = MibScalar
nbsSigCondVoaPortTableSize = _NbsSigCondVoaPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 1),
    _NbsSigCondVoaPortTableSize_Type()
)
nbsSigCondVoaPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTableSize.setStatus("current")
_NbsSigCondVoaPortTable_Object = MibTable
nbsSigCondVoaPortTable = _NbsSigCondVoaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTable.setStatus("current")
_NbsSigCondVoaPortEntry_Object = MibTableRow
nbsSigCondVoaPortEntry = _NbsSigCondVoaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1)
)
nbsSigCondVoaPortEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVoaPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondVoaPortEntry.setStatus("current")
_NbsSigCondVoaPortIfIndex_Type = InterfaceIndex
_NbsSigCondVoaPortIfIndex_Object = MibTableColumn
nbsSigCondVoaPortIfIndex = _NbsSigCondVoaPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 1),
    _NbsSigCondVoaPortIfIndex_Type()
)
nbsSigCondVoaPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortIfIndex.setStatus("current")


class _NbsSigCondVoaPortRxAttenuAdmin_Type(Integer32):
    """Custom type nbsSigCondVoaPortRxAttenuAdmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVoaPortRxAttenuAdmin_Type.__name__ = "Integer32"
_NbsSigCondVoaPortRxAttenuAdmin_Object = MibTableColumn
nbsSigCondVoaPortRxAttenuAdmin = _NbsSigCondVoaPortRxAttenuAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 2),
    _NbsSigCondVoaPortRxAttenuAdmin_Type()
)
nbsSigCondVoaPortRxAttenuAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortRxAttenuAdmin.setStatus("current")


class _NbsSigCondVoaPortRxAttenuOper_Type(Integer32):
    """Custom type nbsSigCondVoaPortRxAttenuOper based on Integer32"""
    defaultValue = 0


_NbsSigCondVoaPortRxAttenuOper_Object = MibTableColumn
nbsSigCondVoaPortRxAttenuOper = _NbsSigCondVoaPortRxAttenuOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 3),
    _NbsSigCondVoaPortRxAttenuOper_Type()
)
nbsSigCondVoaPortRxAttenuOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortRxAttenuOper.setStatus("current")


class _NbsSigCondVoaPortTxAttenuAdmin_Type(Integer32):
    """Custom type nbsSigCondVoaPortTxAttenuAdmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVoaPortTxAttenuAdmin_Type.__name__ = "Integer32"
_NbsSigCondVoaPortTxAttenuAdmin_Object = MibTableColumn
nbsSigCondVoaPortTxAttenuAdmin = _NbsSigCondVoaPortTxAttenuAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 4),
    _NbsSigCondVoaPortTxAttenuAdmin_Type()
)
nbsSigCondVoaPortTxAttenuAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTxAttenuAdmin.setStatus("current")


class _NbsSigCondVoaPortTxAttenuOper_Type(Integer32):
    """Custom type nbsSigCondVoaPortTxAttenuOper based on Integer32"""
    defaultValue = 0


_NbsSigCondVoaPortTxAttenuOper_Object = MibTableColumn
nbsSigCondVoaPortTxAttenuOper = _NbsSigCondVoaPortTxAttenuOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 5),
    _NbsSigCondVoaPortTxAttenuOper_Type()
)
nbsSigCondVoaPortTxAttenuOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTxAttenuOper.setStatus("current")
_NbsSigCondVoaFlowGrp_ObjectIdentity = ObjectIdentity
nbsSigCondVoaFlowGrp = _NbsSigCondVoaFlowGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowGrp.setStatus("current")
_NbsSigCondVoaFlowTableSize_Type = Unsigned32
_NbsSigCondVoaFlowTableSize_Object = MibScalar
nbsSigCondVoaFlowTableSize = _NbsSigCondVoaFlowTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 1),
    _NbsSigCondVoaFlowTableSize_Type()
)
nbsSigCondVoaFlowTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowTableSize.setStatus("current")
_NbsSigCondVoaFlowTable_Object = MibTable
nbsSigCondVoaFlowTable = _NbsSigCondVoaFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowTable.setStatus("current")
_NbsSigCondVoaFlowEntry_Object = MibTableRow
nbsSigCondVoaFlowEntry = _NbsSigCondVoaFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1)
)
nbsSigCondVoaFlowEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVoaFlowIfIndex"),
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVoaFlowWavelength"),
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVoaFlowDirection"),
)
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowEntry.setStatus("current")
_NbsSigCondVoaFlowIfIndex_Type = InterfaceIndex
_NbsSigCondVoaFlowIfIndex_Object = MibTableColumn
nbsSigCondVoaFlowIfIndex = _NbsSigCondVoaFlowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 1),
    _NbsSigCondVoaFlowIfIndex_Type()
)
nbsSigCondVoaFlowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowIfIndex.setStatus("current")
_NbsSigCondVoaFlowWavelength_Type = Integer32
_NbsSigCondVoaFlowWavelength_Object = MibTableColumn
nbsSigCondVoaFlowWavelength = _NbsSigCondVoaFlowWavelength_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 2),
    _NbsSigCondVoaFlowWavelength_Type()
)
nbsSigCondVoaFlowWavelength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowWavelength.setStatus("current")


class _NbsSigCondVoaFlowDirection_Type(Integer32):
    """Custom type nbsSigCondVoaFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_NbsSigCondVoaFlowDirection_Type.__name__ = "Integer32"
_NbsSigCondVoaFlowDirection_Object = MibTableColumn
nbsSigCondVoaFlowDirection = _NbsSigCondVoaFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 3),
    _NbsSigCondVoaFlowDirection_Type()
)
nbsSigCondVoaFlowDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowDirection.setStatus("current")
_NbsSigCondVoaFlowAttenuAdmin_Type = Integer32
_NbsSigCondVoaFlowAttenuAdmin_Object = MibTableColumn
nbsSigCondVoaFlowAttenuAdmin = _NbsSigCondVoaFlowAttenuAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 4),
    _NbsSigCondVoaFlowAttenuAdmin_Type()
)
nbsSigCondVoaFlowAttenuAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowAttenuAdmin.setStatus("current")
_NbsSigCondVoaFlowAttenuOper_Type = Integer32
_NbsSigCondVoaFlowAttenuOper_Object = MibTableColumn
nbsSigCondVoaFlowAttenuOper = _NbsSigCondVoaFlowAttenuOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 5),
    _NbsSigCondVoaFlowAttenuOper_Type()
)
nbsSigCondVoaFlowAttenuOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaFlowAttenuOper.setStatus("current")
_NbsSigCondRamanGrp_ObjectIdentity = ObjectIdentity
nbsSigCondRamanGrp = _NbsSigCondRamanGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 3)
)
if mibBuilder.loadTexts:
    nbsSigCondRamanGrp.setStatus("current")
_NbsSigCondRamanTableSize_Type = Unsigned32
_NbsSigCondRamanTableSize_Object = MibScalar
nbsSigCondRamanTableSize = _NbsSigCondRamanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 1),
    _NbsSigCondRamanTableSize_Type()
)
nbsSigCondRamanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRamanTableSize.setStatus("current")
_NbsSigCondRamanTable_Object = MibTable
nbsSigCondRamanTable = _NbsSigCondRamanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondRamanTable.setStatus("current")
_NbsSigCondRamanEntry_Object = MibTableRow
nbsSigCondRamanEntry = _NbsSigCondRamanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1)
)
nbsSigCondRamanEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondRamanIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondRamanEntry.setStatus("current")
_NbsSigCondRamanIfIndex_Type = InterfaceIndex
_NbsSigCondRamanIfIndex_Object = MibTableColumn
nbsSigCondRamanIfIndex = _NbsSigCondRamanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 1),
    _NbsSigCondRamanIfIndex_Type()
)
nbsSigCondRamanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondRamanIfIndex.setStatus("current")
_NbsSigCondRamanPumpPwrAdmin_Type = Integer32
_NbsSigCondRamanPumpPwrAdmin_Object = MibTableColumn
nbsSigCondRamanPumpPwrAdmin = _NbsSigCondRamanPumpPwrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 2),
    _NbsSigCondRamanPumpPwrAdmin_Type()
)
nbsSigCondRamanPumpPwrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondRamanPumpPwrAdmin.setStatus("current")
_NbsSigCondRamanPumpPwrOper_Type = Integer32
_NbsSigCondRamanPumpPwrOper_Object = MibTableColumn
nbsSigCondRamanPumpPwrOper = _NbsSigCondRamanPumpPwrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 3),
    _NbsSigCondRamanPumpPwrOper_Type()
)
nbsSigCondRamanPumpPwrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRamanPumpPwrOper.setStatus("current")
_NbsSigCondPortGrp_ObjectIdentity = ObjectIdentity
nbsSigCondPortGrp = _NbsSigCondPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 100)
)
if mibBuilder.loadTexts:
    nbsSigCondPortGrp.setStatus("current")
_NbsSigCondPortTableSize_Type = Unsigned32
_NbsSigCondPortTableSize_Object = MibScalar
nbsSigCondPortTableSize = _NbsSigCondPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 1),
    _NbsSigCondPortTableSize_Type()
)
nbsSigCondPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortTableSize.setStatus("current")
_NbsSigCondPortTable_Object = MibTable
nbsSigCondPortTable = _NbsSigCondPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondPortTable.setStatus("current")
_NbsSigCondPortEntry_Object = MibTableRow
nbsSigCondPortEntry = _NbsSigCondPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 2, 1)
)
nbsSigCondPortEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondPortEntry.setStatus("current")
_NbsSigCondPortIfIndex_Type = InterfaceIndex
_NbsSigCondPortIfIndex_Object = MibTableColumn
nbsSigCondPortIfIndex = _NbsSigCondPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 2, 1, 1),
    _NbsSigCondPortIfIndex_Type()
)
nbsSigCondPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondPortIfIndex.setStatus("current")
_NbsSigCondPortRxPower_Type = Integer32
_NbsSigCondPortRxPower_Object = MibTableColumn
nbsSigCondPortRxPower = _NbsSigCondPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 2, 1, 2),
    _NbsSigCondPortRxPower_Type()
)
nbsSigCondPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortRxPower.setStatus("current")
_NbsSigCondPortTxPower_Type = Integer32
_NbsSigCondPortTxPower_Object = MibTableColumn
nbsSigCondPortTxPower = _NbsSigCondPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 2, 1, 3),
    _NbsSigCondPortTxPower_Type()
)
nbsSigCondPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortTxPower.setStatus("current")
_NbsSigCondPortReflection_Type = Integer32
_NbsSigCondPortReflection_Object = MibTableColumn
nbsSigCondPortReflection = _NbsSigCondPortReflection_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 100, 2, 1, 4),
    _NbsSigCondPortReflection_Type()
)
nbsSigCondPortReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortReflection.setStatus("current")
_NbsSigCondTraps_ObjectIdentity = ObjectIdentity
nbsSigCondTraps = _NbsSigCondTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 200)
)
if mibBuilder.loadTexts:
    nbsSigCondTraps.setStatus("current")
_NbsSigCondTrap0_ObjectIdentity = ObjectIdentity
nbsSigCondTrap0 = _NbsSigCondTrap0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 200, 0)
)
if mibBuilder.loadTexts:
    nbsSigCondTrap0.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SIGCOND-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "nbsSigCondMib": nbsSigCondMib,
       "nbsSigCondVoaPortGrp": nbsSigCondVoaPortGrp,
       "nbsSigCondVoaPortTableSize": nbsSigCondVoaPortTableSize,
       "nbsSigCondVoaPortTable": nbsSigCondVoaPortTable,
       "nbsSigCondVoaPortEntry": nbsSigCondVoaPortEntry,
       "nbsSigCondVoaPortIfIndex": nbsSigCondVoaPortIfIndex,
       "nbsSigCondVoaPortRxAttenuAdmin": nbsSigCondVoaPortRxAttenuAdmin,
       "nbsSigCondVoaPortRxAttenuOper": nbsSigCondVoaPortRxAttenuOper,
       "nbsSigCondVoaPortTxAttenuAdmin": nbsSigCondVoaPortTxAttenuAdmin,
       "nbsSigCondVoaPortTxAttenuOper": nbsSigCondVoaPortTxAttenuOper,
       "nbsSigCondVoaFlowGrp": nbsSigCondVoaFlowGrp,
       "nbsSigCondVoaFlowTableSize": nbsSigCondVoaFlowTableSize,
       "nbsSigCondVoaFlowTable": nbsSigCondVoaFlowTable,
       "nbsSigCondVoaFlowEntry": nbsSigCondVoaFlowEntry,
       "nbsSigCondVoaFlowIfIndex": nbsSigCondVoaFlowIfIndex,
       "nbsSigCondVoaFlowWavelength": nbsSigCondVoaFlowWavelength,
       "nbsSigCondVoaFlowDirection": nbsSigCondVoaFlowDirection,
       "nbsSigCondVoaFlowAttenuAdmin": nbsSigCondVoaFlowAttenuAdmin,
       "nbsSigCondVoaFlowAttenuOper": nbsSigCondVoaFlowAttenuOper,
       "nbsSigCondRamanGrp": nbsSigCondRamanGrp,
       "nbsSigCondRamanTableSize": nbsSigCondRamanTableSize,
       "nbsSigCondRamanTable": nbsSigCondRamanTable,
       "nbsSigCondRamanEntry": nbsSigCondRamanEntry,
       "nbsSigCondRamanIfIndex": nbsSigCondRamanIfIndex,
       "nbsSigCondRamanPumpPwrAdmin": nbsSigCondRamanPumpPwrAdmin,
       "nbsSigCondRamanPumpPwrOper": nbsSigCondRamanPumpPwrOper,
       "nbsSigCondPortGrp": nbsSigCondPortGrp,
       "nbsSigCondPortTableSize": nbsSigCondPortTableSize,
       "nbsSigCondPortTable": nbsSigCondPortTable,
       "nbsSigCondPortEntry": nbsSigCondPortEntry,
       "nbsSigCondPortIfIndex": nbsSigCondPortIfIndex,
       "nbsSigCondPortRxPower": nbsSigCondPortRxPower,
       "nbsSigCondPortTxPower": nbsSigCondPortTxPower,
       "nbsSigCondPortReflection": nbsSigCondPortReflection,
       "nbsSigCondTraps": nbsSigCondTraps,
       "nbsSigCondTrap0": nbsSigCondTrap0}
)
