# SNMP MIB module (DSX-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSX-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:42 2024
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

(ntEnterpriseDataTasmanInterfaces,
 ntEnterpriseDataTasmanMgmt,
 ntEnterpriseDataTasmanModules) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanInterfaces",
    "ntEnterpriseDataTasmanMgmt",
    "ntEnterpriseDataTasmanModules")

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

nndsxTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 3, 2)
)
nndsxTC.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class LEDState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("led-blinking-green", 5),
          ("led-blinking-red", 6),
          ("led-blinking-yellow", 7),
          ("led-green", 2),
          ("led-off", 1),
          ("led-red", 3),
          ("led-yellow", 4))
    )



# MIB Managed Objects in the order of their OIDs

_NndsxMIB_ObjectIdentity = ObjectIdentity
nndsxMIB = _NndsxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1)
)
_NndsxT1E1IfGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfGroup = _NndsxT1E1IfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2)
)
_NndsxT3E3IfGroup_ObjectIdentity = ObjectIdentity
nndsxT3E3IfGroup = _NndsxT3E3IfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSX-TC-MIB",
    **{"AlarmStatus": AlarmStatus,
       "LEDState": LEDState,
       "nndsxMIB": nndsxMIB,
       "nndsxT1E1IfGroup": nndsxT1E1IfGroup,
       "nndsxT3E3IfGroup": nndsxT3E3IfGroup,
       "nndsxTC": nndsxTC}
)
