# SNMP MIB module (CPQGEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQGEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:23 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqGenUnreg_ObjectIdentity = ObjectIdentity
cpqGenUnreg = _CpqGenUnreg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151)
)
_CpqGenComponent_ObjectIdentity = ObjectIdentity
cpqGenComponent = _CpqGenComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151, 2)
)
_CpqTrapVarBind_ObjectIdentity = ObjectIdentity
cpqTrapVarBind = _CpqTrapVarBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151, 2, 2)
)


class _CpqGenEntOIDStr_Type(DisplayString):
    """Custom type cpqGenEntOIDStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqGenEntOIDStr_Type.__name__ = "DisplayString"
_CpqGenEntOIDStr_Object = MibScalar
cpqGenEntOIDStr = _CpqGenEntOIDStr_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 1),
    _CpqGenEntOIDStr_Type()
)
cpqGenEntOIDStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqGenEntOIDStr.setStatus("mandatory")
_CpqGenTrapID_Type = Integer32
_CpqGenTrapID_Object = MibScalar
cpqGenTrapID = _CpqGenTrapID_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 2),
    _CpqGenTrapID_Type()
)
cpqGenTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqGenTrapID.setStatus("mandatory")
_CpqSpecTrapID_Type = Integer32
_CpqSpecTrapID_Object = MibScalar
cpqSpecTrapID = _CpqSpecTrapID_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 3),
    _CpqSpecTrapID_Type()
)
cpqSpecTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSpecTrapID.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqGenericUnregistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 99999)
)
cpqGenericUnregistered.setObjects(
      *(("CPQGEN-MIB", "cpqGenEntOIDStr"),
        ("CPQGEN-MIB", "cpqGenTrapID"),
        ("CPQGEN-MIB", "cpqSpecTrapID"))
)
if mibBuilder.loadTexts:
    cpqGenericUnregistered.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQGEN-MIB",
    **{"compaq": compaq,
       "cpqGenericUnregistered": cpqGenericUnregistered,
       "cpqGenUnreg": cpqGenUnreg,
       "cpqGenComponent": cpqGenComponent,
       "cpqTrapVarBind": cpqTrapVarBind,
       "cpqGenEntOIDStr": cpqGenEntOIDStr,
       "cpqGenTrapID": cpqGenTrapID,
       "cpqSpecTrapID": cpqSpecTrapID}
)
