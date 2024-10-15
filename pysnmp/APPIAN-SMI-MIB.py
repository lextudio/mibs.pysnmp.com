# SNMP MIB module (APPIAN-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:29 2024
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

appian = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785)
)
appian.setRevisions(
        ("1900-01-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("delete", 2),
          ("inactivate", 3))
    )



class AcOpStatus(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("failed", 10),
          ("hw-not-present", 11),
          ("initializing", 3),
          ("maintenance", 7),
          ("offline", 2),
          ("operational", 1),
          ("provisioning", 5),
          ("selfTesting", 4),
          ("shuttingDown", 9),
          ("standby", 8),
          ("upgrading", 6))
    )



class AcSlotNumber(Integer32, TextualConvention):
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("ac0", 0),
          ("ac1", 1),
          ("ac10", 10),
          ("ac100", 100),
          ("ac11", 11),
          ("ac12", 12),
          ("ac13", 13),
          ("ac14", 14),
          ("ac15", 15),
          ("ac16", 16),
          ("ac2", 2),
          ("ac3", 3),
          ("ac4", 4),
          ("ac5", 5),
          ("ac6", 6),
          ("ac7", 7),
          ("ac8", 8),
          ("ac9", 9))
    )



class AcPortNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class AcLastChange(TimeTicks, TextualConvention):
    status = "current"


class AcMibVersion(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )



class AcSwVersion(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )



class AcNodeId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class AcRingId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class AcNodeArchitecture(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("drop-and-continue-pri", 4),
          ("drop-and-continue-sec", 5),
          ("linear", 1),
          ("ring", 2),
          ("ring-interconnect", 3),
          ("subtending-pri", 6),
          ("subtending-sec", 7),
          ("unconfigured", 0))
    )



# MIB Managed Objects in the order of their OIDs

_AcIdentifier_ObjectIdentity = ObjectIdentity
acIdentifier = _AcIdentifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 1)
)
_AcProductId_ObjectIdentity = ObjectIdentity
acProductId = _AcProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 1, 1)
)
_AcOsap_ObjectIdentity = ObjectIdentity
acOsap = _AcOsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2)
)
_AcPport_ObjectIdentity = ObjectIdentity
acPport = _AcPport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3)
)
_AcLport_ObjectIdentity = ObjectIdentity
acLport = _AcLport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4)
)
_AcTrunks_ObjectIdentity = ObjectIdentity
acTrunks = _AcTrunks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6)
)
_AcServices_ObjectIdentity = ObjectIdentity
acServices = _AcServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-SMI-MIB",
    **{"AcAdminStatus": AcAdminStatus,
       "AcOpStatus": AcOpStatus,
       "AcSlotNumber": AcSlotNumber,
       "AcPortNumber": AcPortNumber,
       "AcLastChange": AcLastChange,
       "AcMibVersion": AcMibVersion,
       "AcSwVersion": AcSwVersion,
       "AcNodeId": AcNodeId,
       "AcRingId": AcRingId,
       "AcNodeArchitecture": AcNodeArchitecture,
       "appian": appian,
       "acIdentifier": acIdentifier,
       "acProductId": acProductId,
       "acOsap": acOsap,
       "acPport": acPport,
       "acLport": acLport,
       "acTrunks": acTrunks,
       "acServices": acServices}
)
