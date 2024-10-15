# SNMP MIB module (IANATn3270eTC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANATn3270eTC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:11 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ianaTn3270eTcMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 61)
)
ianaTn3270eTcMib.setRevisions(
        ("2014-05-22 00:00",
         "2000-05-10 00:00",
         "1999-09-01 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IANATn3270eAddrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("unknown", 0))
    )



class IANATn3270eAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class IANATn3270eClientType(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("certificate", 8),
          ("domainName", 5),
          ("ipv4", 3),
          ("ipv6", 4),
          ("none", 1),
          ("other", 2),
          ("string", 7),
          ("truncDomainName", 6),
          ("userId", 9),
          ("x509dn", 10))
    )



class IANATn3270Functions(Bits, TextualConvention):
    status = "current"


class IANATn3270ResourceType(Integer32, TextualConvention):
    status = "current"
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
        *(("other", 1),
          ("printer", 3),
          ("terminal", 2),
          ("terminalOrPrinter", 4))
    )



class IANATn3270DeviceType(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ibm3278d2", 1),
          ("ibm3278d2E", 2),
          ("ibm3278d3", 3),
          ("ibm3278d3E", 4),
          ("ibm3278d4", 5),
          ("ibm3278d4E", 6),
          ("ibm3278d5", 7),
          ("ibm3278d5E", 8),
          ("ibm3287d1", 10),
          ("ibmDynamic", 9),
          ("unknown", 100))
    )



class IANATn3270eLogData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 2048),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANATn3270eTC-MIB",
    **{"IANATn3270eAddrType": IANATn3270eAddrType,
       "IANATn3270eAddress": IANATn3270eAddress,
       "IANATn3270eClientType": IANATn3270eClientType,
       "IANATn3270Functions": IANATn3270Functions,
       "IANATn3270ResourceType": IANATn3270ResourceType,
       "IANATn3270DeviceType": IANATn3270DeviceType,
       "IANATn3270eLogData": IANATn3270eLogData,
       "ianaTn3270eTcMib": ianaTn3270eTcMib}
)
