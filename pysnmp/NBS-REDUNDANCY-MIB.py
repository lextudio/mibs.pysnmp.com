# SNMP MIB module (NBS-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:58 2024
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

(nbsCmmcChassisIndex,
 nbsCmmcPortIndex,
 nbsCmmcSlotIndex) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "nbsCmmcChassisIndex",
    "nbsCmmcPortIndex",
    "nbsCmmcSlotIndex")

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

nbsRedundancyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 221)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsRedundCfgGrp_ObjectIdentity = ObjectIdentity
nbsRedundCfgGrp = _NbsRedundCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 221, 1)
)
if mibBuilder.loadTexts:
    nbsRedundCfgGrp.setStatus("current")
_NbsRedundCfgTableSize_Type = Integer32
_NbsRedundCfgTableSize_Object = MibScalar
nbsRedundCfgTableSize = _NbsRedundCfgTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 1),
    _NbsRedundCfgTableSize_Type()
)
nbsRedundCfgTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundCfgTableSize.setStatus("current")
_NbsRedundCfgTable_Object = MibTable
nbsRedundCfgTable = _NbsRedundCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2)
)
if mibBuilder.loadTexts:
    nbsRedundCfgTable.setStatus("current")
_NbsRedundCfgEntry_Object = MibTableRow
nbsRedundCfgEntry = _NbsRedundCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1)
)
nbsRedundCfgEntry.setIndexNames(
    (0, "NBS-REDUNDANCY-MIB", "nbsRedundCfgNdx"),
)
if mibBuilder.loadTexts:
    nbsRedundCfgEntry.setStatus("current")
_NbsRedundCfgNdx_Type = InterfaceIndex
_NbsRedundCfgNdx_Object = MibTableColumn
nbsRedundCfgNdx = _NbsRedundCfgNdx_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 1),
    _NbsRedundCfgNdx_Type()
)
nbsRedundCfgNdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsRedundCfgNdx.setStatus("current")
_NbsRedundCfgPartnerNdxAdmin_Type = InterfaceIndex
_NbsRedundCfgPartnerNdxAdmin_Object = MibTableColumn
nbsRedundCfgPartnerNdxAdmin = _NbsRedundCfgPartnerNdxAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 2),
    _NbsRedundCfgPartnerNdxAdmin_Type()
)
nbsRedundCfgPartnerNdxAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgPartnerNdxAdmin.setStatus("current")
_NbsRedundCfgPartnerNdxOper_Type = InterfaceIndex
_NbsRedundCfgPartnerNdxOper_Object = MibTableColumn
nbsRedundCfgPartnerNdxOper = _NbsRedundCfgPartnerNdxOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 3),
    _NbsRedundCfgPartnerNdxOper_Type()
)
nbsRedundCfgPartnerNdxOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundCfgPartnerNdxOper.setStatus("current")


class _NbsRedundCfgStatusAdmin_Type(Integer32):
    """Custom type nbsRedundCfgStatusAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notSupported", 1),
          ("standby", 2))
    )


_NbsRedundCfgStatusAdmin_Type.__name__ = "Integer32"
_NbsRedundCfgStatusAdmin_Object = MibTableColumn
nbsRedundCfgStatusAdmin = _NbsRedundCfgStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 10),
    _NbsRedundCfgStatusAdmin_Type()
)
nbsRedundCfgStatusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgStatusAdmin.setStatus("current")


class _NbsRedundCfgStatusOper_Type(Integer32):
    """Custom type nbsRedundCfgStatusOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notSupported", 1),
          ("standby", 2))
    )


_NbsRedundCfgStatusOper_Type.__name__ = "Integer32"
_NbsRedundCfgStatusOper_Object = MibTableColumn
nbsRedundCfgStatusOper = _NbsRedundCfgStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 11),
    _NbsRedundCfgStatusOper_Type()
)
nbsRedundCfgStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundCfgStatusOper.setStatus("current")


class _NbsRedundCfgPreferredAdmin_Type(Integer32):
    """Custom type nbsRedundCfgPreferredAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("preferActive", 3),
          ("preferNot", 2))
    )


_NbsRedundCfgPreferredAdmin_Type.__name__ = "Integer32"
_NbsRedundCfgPreferredAdmin_Object = MibTableColumn
nbsRedundCfgPreferredAdmin = _NbsRedundCfgPreferredAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 20),
    _NbsRedundCfgPreferredAdmin_Type()
)
nbsRedundCfgPreferredAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgPreferredAdmin.setStatus("current")


class _NbsRedundCfgStandbyTxAdmin_Type(Integer32):
    """Custom type nbsRedundCfgStandbyTxAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("standbyCold", 2),
          ("standbyHot", 3))
    )


_NbsRedundCfgStandbyTxAdmin_Type.__name__ = "Integer32"
_NbsRedundCfgStandbyTxAdmin_Object = MibTableColumn
nbsRedundCfgStandbyTxAdmin = _NbsRedundCfgStandbyTxAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 30),
    _NbsRedundCfgStandbyTxAdmin_Type()
)
nbsRedundCfgStandbyTxAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgStandbyTxAdmin.setStatus("current")


class _NbsRedundCfgStandbyTxToggle_Type(Integer32):
    """Custom type nbsRedundCfgStandbyTxToggle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("txOff", 2),
          ("txToggle", 3))
    )


_NbsRedundCfgStandbyTxToggle_Type.__name__ = "Integer32"
_NbsRedundCfgStandbyTxToggle_Object = MibTableColumn
nbsRedundCfgStandbyTxToggle = _NbsRedundCfgStandbyTxToggle_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 40),
    _NbsRedundCfgStandbyTxToggle_Type()
)
nbsRedundCfgStandbyTxToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgStandbyTxToggle.setStatus("current")


class _NbsRedundCfgIfTypeAdmin_Type(Integer32):
    """Custom type nbsRedundCfgIfTypeAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("notSupported", 1),
          ("trunk", 3))
    )


_NbsRedundCfgIfTypeAdmin_Type.__name__ = "Integer32"
_NbsRedundCfgIfTypeAdmin_Object = MibTableColumn
nbsRedundCfgIfTypeAdmin = _NbsRedundCfgIfTypeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 50),
    _NbsRedundCfgIfTypeAdmin_Type()
)
nbsRedundCfgIfTypeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgIfTypeAdmin.setStatus("current")


class _NbsRedundCfgIfTypeOper_Type(Integer32):
    """Custom type nbsRedundCfgIfTypeOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("notSupported", 1),
          ("trunk", 3))
    )


_NbsRedundCfgIfTypeOper_Type.__name__ = "Integer32"
_NbsRedundCfgIfTypeOper_Object = MibTableColumn
nbsRedundCfgIfTypeOper = _NbsRedundCfgIfTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 51),
    _NbsRedundCfgIfTypeOper_Type()
)
nbsRedundCfgIfTypeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundCfgIfTypeOper.setStatus("current")
_NbsRedundCfgGroupNumberAdmin_Type = Integer32
_NbsRedundCfgGroupNumberAdmin_Object = MibTableColumn
nbsRedundCfgGroupNumberAdmin = _NbsRedundCfgGroupNumberAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 60),
    _NbsRedundCfgGroupNumberAdmin_Type()
)
nbsRedundCfgGroupNumberAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRedundCfgGroupNumberAdmin.setStatus("current")
_NbsRedundCfgGroupNumberOper_Type = Integer32
_NbsRedundCfgGroupNumberOper_Object = MibTableColumn
nbsRedundCfgGroupNumberOper = _NbsRedundCfgGroupNumberOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 61),
    _NbsRedundCfgGroupNumberOper_Type()
)
nbsRedundCfgGroupNumberOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundCfgGroupNumberOper.setStatus("current")
_NbsRedundGroupCfgTableSize_Type = Integer32
_NbsRedundGroupCfgTableSize_Object = MibScalar
nbsRedundGroupCfgTableSize = _NbsRedundGroupCfgTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 3),
    _NbsRedundGroupCfgTableSize_Type()
)
nbsRedundGroupCfgTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgTableSize.setStatus("current")
_NbsRedundGroupCfgTable_Object = MibTable
nbsRedundGroupCfgTable = _NbsRedundGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4)
)
if mibBuilder.loadTexts:
    nbsRedundGroupCfgTable.setStatus("current")
_NbsRedundGroupCfgEntry_Object = MibTableRow
nbsRedundGroupCfgEntry = _NbsRedundGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1)
)
nbsRedundGroupCfgEntry.setIndexNames(
    (0, "NBS-REDUNDANCY-MIB", "nbsRedundGroupCfgNdx"),
    (0, "NBS-REDUNDANCY-MIB", "nbsRedundGroupCfgNumber"),
)
if mibBuilder.loadTexts:
    nbsRedundGroupCfgEntry.setStatus("current")
_NbsRedundGroupCfgNdx_Type = InterfaceIndex
_NbsRedundGroupCfgNdx_Object = MibTableColumn
nbsRedundGroupCfgNdx = _NbsRedundGroupCfgNdx_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 1),
    _NbsRedundGroupCfgNdx_Type()
)
nbsRedundGroupCfgNdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgNdx.setStatus("current")
_NbsRedundGroupCfgNumber_Type = Integer32
_NbsRedundGroupCfgNumber_Object = MibTableColumn
nbsRedundGroupCfgNumber = _NbsRedundGroupCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 2),
    _NbsRedundGroupCfgNumber_Type()
)
nbsRedundGroupCfgNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgNumber.setStatus("current")


class _NbsRedundGroupCfgOper_Type(OctetString):
    """Custom type nbsRedundGroupCfgOper based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsRedundGroupCfgOper_Type.__name__ = "OctetString"
_NbsRedundGroupCfgOper_Object = MibTableColumn
nbsRedundGroupCfgOper = _NbsRedundGroupCfgOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 13),
    _NbsRedundGroupCfgOper_Type()
)
nbsRedundGroupCfgOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgOper.setStatus("current")


class _NbsRedundGroupCfgModeAdmin_Type(Integer32):
    """Custom type nbsRedundGroupCfgModeAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 2),
          ("modeB", 3),
          ("notSupported", 1))
    )


_NbsRedundGroupCfgModeAdmin_Type.__name__ = "Integer32"
_NbsRedundGroupCfgModeAdmin_Object = MibTableColumn
nbsRedundGroupCfgModeAdmin = _NbsRedundGroupCfgModeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 15),
    _NbsRedundGroupCfgModeAdmin_Type()
)
nbsRedundGroupCfgModeAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgModeAdmin.setStatus("current")


class _NbsRedundGroupCfgModeOper_Type(Integer32):
    """Custom type nbsRedundGroupCfgModeOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 2),
          ("modeB", 3),
          ("notSupported", 1))
    )


_NbsRedundGroupCfgModeOper_Type.__name__ = "Integer32"
_NbsRedundGroupCfgModeOper_Object = MibTableColumn
nbsRedundGroupCfgModeOper = _NbsRedundGroupCfgModeOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 16),
    _NbsRedundGroupCfgModeOper_Type()
)
nbsRedundGroupCfgModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgModeOper.setStatus("current")


class _NbsRedundGroupCfgYcableAdmin_Type(Integer32):
    """Custom type nbsRedundGroupCfgYcableAdmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsRedundGroupCfgYcableAdmin_Type.__name__ = "Integer32"
_NbsRedundGroupCfgYcableAdmin_Object = MibTableColumn
nbsRedundGroupCfgYcableAdmin = _NbsRedundGroupCfgYcableAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 20),
    _NbsRedundGroupCfgYcableAdmin_Type()
)
nbsRedundGroupCfgYcableAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgYcableAdmin.setStatus("current")


class _NbsRedundGroupCfgYcableOper_Type(Integer32):
    """Custom type nbsRedundGroupCfgYcableOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsRedundGroupCfgYcableOper_Type.__name__ = "Integer32"
_NbsRedundGroupCfgYcableOper_Object = MibTableColumn
nbsRedundGroupCfgYcableOper = _NbsRedundGroupCfgYcableOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 21),
    _NbsRedundGroupCfgYcableOper_Type()
)
nbsRedundGroupCfgYcableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgYcableOper.setStatus("current")
_NbsRedundGroupCfgRowStatus_Type = RowStatus
_NbsRedundGroupCfgRowStatus_Object = MibTableColumn
nbsRedundGroupCfgRowStatus = _NbsRedundGroupCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 50),
    _NbsRedundGroupCfgRowStatus_Type()
)
nbsRedundGroupCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRedundGroupCfgRowStatus.setStatus("current")
_NbsRedundEventGrp_ObjectIdentity = ObjectIdentity
nbsRedundEventGrp = _NbsRedundEventGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 221, 100)
)
if mibBuilder.loadTexts:
    nbsRedundEventGrp.setStatus("current")
_NbsYcableTraps_ObjectIdentity = ObjectIdentity
nbsYcableTraps = _NbsYcableTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 221, 100, 0)
)
if mibBuilder.loadTexts:
    nbsYcableTraps.setStatus("current")

# Managed Objects groups


# Notification objects

nbsYcableTrapsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 221, 100, 0, 10)
)
nbsYcableTrapsStatusChanged.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-REDUNDANCY-MIB", "nbsRedundCfgStatusOper"))
)
if mibBuilder.loadTexts:
    nbsYcableTrapsStatusChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-REDUNDANCY-MIB",
    **{"nbsRedundancyMib": nbsRedundancyMib,
       "nbsRedundCfgGrp": nbsRedundCfgGrp,
       "nbsRedundCfgTableSize": nbsRedundCfgTableSize,
       "nbsRedundCfgTable": nbsRedundCfgTable,
       "nbsRedundCfgEntry": nbsRedundCfgEntry,
       "nbsRedundCfgNdx": nbsRedundCfgNdx,
       "nbsRedundCfgPartnerNdxAdmin": nbsRedundCfgPartnerNdxAdmin,
       "nbsRedundCfgPartnerNdxOper": nbsRedundCfgPartnerNdxOper,
       "nbsRedundCfgStatusAdmin": nbsRedundCfgStatusAdmin,
       "nbsRedundCfgStatusOper": nbsRedundCfgStatusOper,
       "nbsRedundCfgPreferredAdmin": nbsRedundCfgPreferredAdmin,
       "nbsRedundCfgStandbyTxAdmin": nbsRedundCfgStandbyTxAdmin,
       "nbsRedundCfgStandbyTxToggle": nbsRedundCfgStandbyTxToggle,
       "nbsRedundCfgIfTypeAdmin": nbsRedundCfgIfTypeAdmin,
       "nbsRedundCfgIfTypeOper": nbsRedundCfgIfTypeOper,
       "nbsRedundCfgGroupNumberAdmin": nbsRedundCfgGroupNumberAdmin,
       "nbsRedundCfgGroupNumberOper": nbsRedundCfgGroupNumberOper,
       "nbsRedundGroupCfgTableSize": nbsRedundGroupCfgTableSize,
       "nbsRedundGroupCfgTable": nbsRedundGroupCfgTable,
       "nbsRedundGroupCfgEntry": nbsRedundGroupCfgEntry,
       "nbsRedundGroupCfgNdx": nbsRedundGroupCfgNdx,
       "nbsRedundGroupCfgNumber": nbsRedundGroupCfgNumber,
       "nbsRedundGroupCfgOper": nbsRedundGroupCfgOper,
       "nbsRedundGroupCfgModeAdmin": nbsRedundGroupCfgModeAdmin,
       "nbsRedundGroupCfgModeOper": nbsRedundGroupCfgModeOper,
       "nbsRedundGroupCfgYcableAdmin": nbsRedundGroupCfgYcableAdmin,
       "nbsRedundGroupCfgYcableOper": nbsRedundGroupCfgYcableOper,
       "nbsRedundGroupCfgRowStatus": nbsRedundGroupCfgRowStatus,
       "nbsRedundEventGrp": nbsRedundEventGrp,
       "nbsYcableTraps": nbsYcableTraps,
       "nbsYcableTrapsStatusChanged": nbsYcableTrapsStatusChanged}
)
