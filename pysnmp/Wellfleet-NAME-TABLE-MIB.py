# SNMP MIB module (Wellfleet-NAME-TABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-NAME-TABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:44 2024
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

(wfName,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfName")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNameEntry_ObjectIdentity = ObjectIdentity
wfNameEntry = _WfNameEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1)
)


class _WfNameDelete_Type(Integer32):
    """Custom type wfNameDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNameDelete_Type.__name__ = "Integer32"
_WfNameDelete_Object = MibScalar
wfNameDelete = _WfNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1, 1),
    _WfNameDelete_Type()
)
wfNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNameDelete.setStatus("mandatory")


class _WfNameName_Type(DisplayString):
    """Custom type wfNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WfNameName_Type.__name__ = "DisplayString"
_WfNameName_Object = MibScalar
wfNameName = _WfNameName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1, 2),
    _WfNameName_Type()
)
wfNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNameName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-NAME-TABLE-MIB",
    **{"wfNameEntry": wfNameEntry,
       "wfNameDelete": wfNameDelete,
       "wfNameName": wfNameName}
)
