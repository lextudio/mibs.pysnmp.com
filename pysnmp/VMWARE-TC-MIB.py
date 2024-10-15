# SNMP MIB module (VMWARE-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:48 2024
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

(vmwSystem,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwSystem")


# MODULE-IDENTITY

vmwTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 11)
)
vmwTcMIB.setRevisions(
        ("2009-09-05 00:00",
         "2007-12-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwSubsystemTypes(Integer32, TextualConvention):
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
        *(("battery", 7),
          ("chassis", 2),
          ("cpu", 5),
          ("fan", 4),
          ("memory", 6),
          ("powerSupply", 3),
          ("raidController", 9),
          ("temperatureSensor", 8),
          ("unknown", 1),
          ("voltage", 10))
    )



class VmwCIMAlertTypes(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("communications", 2),
          ("deviceAlert", 5),
          ("environmentalAlert", 6),
          ("modelChange", 7),
          ("other", 1),
          ("processingError", 4),
          ("qos", 3),
          ("securityAlert", 8))
    )



class VmwCIMAlertFormat(Integer32, TextualConvention):
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
        *(("cimObjectPath", 2),
          ("other", 1),
          ("unknown", 0))
    )



class VmwSubsystemStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("failed", 5),
          ("marginal", 3),
          ("normal", 2),
          ("unknown", 1))
    )



class VmwCIMSeverity(Integer32, TextualConvention):
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
        *(("critical", 6),
          ("fatal", 7),
          ("information", 2),
          ("major", 5),
          ("minor", 4),
          ("other", 1),
          ("unknown", 0),
          ("warning", 3))
    )



class VmwCimName(OctetString, TextualConvention):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwConnectedState(OctetString, TextualConvention):
    status = "current"
    displayHint = "7a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )



class VmwLongDisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a"


class VmwLongSnmpAdminString(OctetString, TextualConvention):
    status = "current"
    displayHint = "4096t"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-TC-MIB",
    **{"VmwSubsystemTypes": VmwSubsystemTypes,
       "VmwCIMAlertTypes": VmwCIMAlertTypes,
       "VmwCIMAlertFormat": VmwCIMAlertFormat,
       "VmwSubsystemStatus": VmwSubsystemStatus,
       "VmwCIMSeverity": VmwCIMSeverity,
       "VmwCimName": VmwCimName,
       "VmwConnectedState": VmwConnectedState,
       "VmwLongDisplayString": VmwLongDisplayString,
       "VmwLongSnmpAdminString": VmwLongSnmpAdminString,
       "vmwTcMIB": vmwTcMIB}
)
