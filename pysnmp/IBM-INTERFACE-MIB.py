# SNMP MIB module (IBM-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:33 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_IbmIROCroutinginterface_ObjectIdentity = ObjectIdentity
ibmIROCroutinginterface = _IbmIROCroutinginterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17)
)
_IbminterfaceClearTable_Object = MibTable
ibminterfaceClearTable = _IbminterfaceClearTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1)
)
if mibBuilder.loadTexts:
    ibminterfaceClearTable.setStatus("mandatory")
_IbminterfaceClearEntry_Object = MibTableRow
ibminterfaceClearEntry = _IbminterfaceClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1)
)
ibminterfaceClearEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibminterfaceClearEntry.setStatus("mandatory")


class _IbminterfaceClearInOctets_Type(Integer32):
    """Custom type ibminterfaceClearInOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearInOctets_Type.__name__ = "Integer32"
_IbminterfaceClearInOctets_Object = MibTableColumn
ibminterfaceClearInOctets = _IbminterfaceClearInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 1),
    _IbminterfaceClearInOctets_Type()
)
ibminterfaceClearInOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearInOctets.setStatus("mandatory")


class _IbminterfaceClearInUcastPkts_Type(Integer32):
    """Custom type ibminterfaceClearInUcastPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearInUcastPkts_Type.__name__ = "Integer32"
_IbminterfaceClearInUcastPkts_Object = MibTableColumn
ibminterfaceClearInUcastPkts = _IbminterfaceClearInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 2),
    _IbminterfaceClearInUcastPkts_Type()
)
ibminterfaceClearInUcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearInUcastPkts.setStatus("mandatory")


class _IbminterfaceClearInMulticastPkts_Type(Integer32):
    """Custom type ibminterfaceClearInMulticastPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearInMulticastPkts_Type.__name__ = "Integer32"
_IbminterfaceClearInMulticastPkts_Object = MibTableColumn
ibminterfaceClearInMulticastPkts = _IbminterfaceClearInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 3),
    _IbminterfaceClearInMulticastPkts_Type()
)
ibminterfaceClearInMulticastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearInMulticastPkts.setStatus("mandatory")


class _IbminterfaceClearInErrors_Type(Integer32):
    """Custom type ibminterfaceClearInErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearInErrors_Type.__name__ = "Integer32"
_IbminterfaceClearInErrors_Object = MibTableColumn
ibminterfaceClearInErrors = _IbminterfaceClearInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 4),
    _IbminterfaceClearInErrors_Type()
)
ibminterfaceClearInErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearInErrors.setStatus("mandatory")


class _IbminterfaceClearInAll_Type(Integer32):
    """Custom type ibminterfaceClearInAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearInAll_Type.__name__ = "Integer32"
_IbminterfaceClearInAll_Object = MibTableColumn
ibminterfaceClearInAll = _IbminterfaceClearInAll_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 5),
    _IbminterfaceClearInAll_Type()
)
ibminterfaceClearInAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearInAll.setStatus("mandatory")


class _IbminterfaceClearOutOctets_Type(Integer32):
    """Custom type ibminterfaceClearOutOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearOutOctets_Type.__name__ = "Integer32"
_IbminterfaceClearOutOctets_Object = MibTableColumn
ibminterfaceClearOutOctets = _IbminterfaceClearOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 6),
    _IbminterfaceClearOutOctets_Type()
)
ibminterfaceClearOutOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearOutOctets.setStatus("mandatory")


class _IbminterfaceClearOutUcastPkts_Type(Integer32):
    """Custom type ibminterfaceClearOutUcastPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearOutUcastPkts_Type.__name__ = "Integer32"
_IbminterfaceClearOutUcastPkts_Object = MibTableColumn
ibminterfaceClearOutUcastPkts = _IbminterfaceClearOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 7),
    _IbminterfaceClearOutUcastPkts_Type()
)
ibminterfaceClearOutUcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearOutUcastPkts.setStatus("mandatory")


class _IbminterfaceClearOutMulticastPkts_Type(Integer32):
    """Custom type ibminterfaceClearOutMulticastPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearOutMulticastPkts_Type.__name__ = "Integer32"
_IbminterfaceClearOutMulticastPkts_Object = MibTableColumn
ibminterfaceClearOutMulticastPkts = _IbminterfaceClearOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 8),
    _IbminterfaceClearOutMulticastPkts_Type()
)
ibminterfaceClearOutMulticastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearOutMulticastPkts.setStatus("mandatory")


class _IbminterfaceClearOutErrors_Type(Integer32):
    """Custom type ibminterfaceClearOutErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearOutErrors_Type.__name__ = "Integer32"
_IbminterfaceClearOutErrors_Object = MibTableColumn
ibminterfaceClearOutErrors = _IbminterfaceClearOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 9),
    _IbminterfaceClearOutErrors_Type()
)
ibminterfaceClearOutErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearOutErrors.setStatus("mandatory")


class _IbminterfaceClearOutAll_Type(Integer32):
    """Custom type ibminterfaceClearOutAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearOutAll_Type.__name__ = "Integer32"
_IbminterfaceClearOutAll_Object = MibTableColumn
ibminterfaceClearOutAll = _IbminterfaceClearOutAll_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 10),
    _IbminterfaceClearOutAll_Type()
)
ibminterfaceClearOutAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearOutAll.setStatus("mandatory")


class _IbminterfaceClearMaintTest_Type(Integer32):
    """Custom type ibminterfaceClearMaintTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearMaintTest_Type.__name__ = "Integer32"
_IbminterfaceClearMaintTest_Object = MibTableColumn
ibminterfaceClearMaintTest = _IbminterfaceClearMaintTest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 11),
    _IbminterfaceClearMaintTest_Type()
)
ibminterfaceClearMaintTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearMaintTest.setStatus("mandatory")


class _IbminterfaceClearDeviceSpecific_Type(Integer32):
    """Custom type ibminterfaceClearDeviceSpecific based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearDeviceSpecific_Type.__name__ = "Integer32"
_IbminterfaceClearDeviceSpecific_Object = MibTableColumn
ibminterfaceClearDeviceSpecific = _IbminterfaceClearDeviceSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 12),
    _IbminterfaceClearDeviceSpecific_Type()
)
ibminterfaceClearDeviceSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearDeviceSpecific.setStatus("mandatory")


class _IbminterfaceClearAll_Type(Integer32):
    """Custom type ibminterfaceClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noaction", 0))
    )


_IbminterfaceClearAll_Type.__name__ = "Integer32"
_IbminterfaceClearAll_Object = MibTableColumn
ibminterfaceClearAll = _IbminterfaceClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17, 1, 1, 13),
    _IbminterfaceClearAll_Type()
)
ibminterfaceClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibminterfaceClearAll.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-INTERFACE-MIB",
    **{"ibmIROCroutinginterface": ibmIROCroutinginterface,
       "ibminterfaceClearTable": ibminterfaceClearTable,
       "ibminterfaceClearEntry": ibminterfaceClearEntry,
       "ibminterfaceClearInOctets": ibminterfaceClearInOctets,
       "ibminterfaceClearInUcastPkts": ibminterfaceClearInUcastPkts,
       "ibminterfaceClearInMulticastPkts": ibminterfaceClearInMulticastPkts,
       "ibminterfaceClearInErrors": ibminterfaceClearInErrors,
       "ibminterfaceClearInAll": ibminterfaceClearInAll,
       "ibminterfaceClearOutOctets": ibminterfaceClearOutOctets,
       "ibminterfaceClearOutUcastPkts": ibminterfaceClearOutUcastPkts,
       "ibminterfaceClearOutMulticastPkts": ibminterfaceClearOutMulticastPkts,
       "ibminterfaceClearOutErrors": ibminterfaceClearOutErrors,
       "ibminterfaceClearOutAll": ibminterfaceClearOutAll,
       "ibminterfaceClearMaintTest": ibminterfaceClearMaintTest,
       "ibminterfaceClearDeviceSpecific": ibminterfaceClearDeviceSpecific,
       "ibminterfaceClearAll": ibminterfaceClearAll}
)
