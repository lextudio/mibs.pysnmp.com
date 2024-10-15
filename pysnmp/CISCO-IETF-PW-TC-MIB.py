# SNMP MIB module (CISCO-IETF-PW-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:37 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

cpwTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 20000, 1)
)
cpwTCMIB.setRevisions(
        ("2006-07-21 12:00",
         "2003-02-26 12:00",
         "2002-05-28 12:00",
         "2002-01-30 12:00",
         "2001-12-20 12:00",
         "2001-07-12 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpwGroupID(Unsigned32, TextualConvention):
    status = "current"


class CpwVcIDType(Unsigned32, TextualConvention):
    status = "current"


class CpwVcIndexType(Unsigned32, TextualConvention):
    status = "current"


class CpwVcVlanCfg(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )



class CpwOperStatus(Integer32, TextualConvention):
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )



class CpwVcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5Vcc", 2),
          ("atmTransparent", 3),
          ("atmVccCell", 9),
          ("atmVpcCell", 10),
          ("basicCesPsn", 16),
          ("basicTdmIp", 17),
          ("cep", 8),
          ("e1Satop", 12),
          ("e3Satop", 14),
          ("ethernet", 5),
          ("ethernetVLAN", 4),
          ("ethernetVPLS", 11),
          ("frameRelay", 1),
          ("hdlc", 6),
          ("other", 0),
          ("ppp", 7),
          ("t1Satop", 13),
          ("t3Satop", 15),
          ("tdmCasCesPsn", 18),
          ("tdmCasTdmIp", 19))
    )



# MIB Managed Objects in the order of their OIDs

_CpwMIB_ObjectIdentity = ObjectIdentity
cpwMIB = _CpwMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 20000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-TC-MIB",
    **{"CpwGroupID": CpwGroupID,
       "CpwVcIDType": CpwVcIDType,
       "CpwVcIndexType": CpwVcIndexType,
       "CpwVcVlanCfg": CpwVcVlanCfg,
       "CpwOperStatus": CpwOperStatus,
       "CpwVcType": CpwVcType,
       "cpwMIB": cpwMIB,
       "cpwTCMIB": cpwTCMIB}
)
