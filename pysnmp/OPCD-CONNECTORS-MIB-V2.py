# SNMP MIB module (OPCD-CONNECTORS-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-CONNECTORS-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:14 2024
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

(opencode_systems,) = mibBuilder.importSymbols(
    "OPCD-SUPPORT-MIB-V2",
    "opencode-systems")

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

_Occonnectors_ObjectIdentity = ObjectIdentity
occonnectors = _Occonnectors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 16)
)
_Occonnectors_traps_ObjectIdentity = ObjectIdentity
occonnectors_traps = _Occonnectors_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 1)
)


class _Mcr_Host_Type(DisplayString):
    """Custom type mcr_Host based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Host_Type.__name__ = "DisplayString"
_Mcr_Host_Object = MibScalar
mcr_Host = _Mcr_Host_Object(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 1, 1),
    _Mcr_Host_Type()
)
mcr_Host.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Host.setStatus("current")


class _Mcr_Severity_Type(Integer32):
    """Custom type mcr_Severity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("normal", 4),
          ("warning", 5))
    )


_Mcr_Severity_Type.__name__ = "Integer32"
_Mcr_Severity_Object = MibScalar
mcr_Severity = _Mcr_Severity_Object(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 1, 2),
    _Mcr_Severity_Type()
)
mcr_Severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Severity.setStatus("mandatory")


class _Mcr_Text_Type(DisplayString):
    """Custom type mcr_Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Text_Type.__name__ = "DisplayString"
_Mcr_Text_Object = MibScalar
mcr_Text = _Mcr_Text_Object(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

occonectors_LdapConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 2)
)
occonectors_LdapConnector.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_LdapConnector.setStatus(
        "current"
    )

occonectors_LdapConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 3)
)
occonectors_LdapConnector_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_LdapConnector_Canceled.setStatus(
        "current"
    )

occonectors_MmlConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 4)
)
occonectors_MmlConnector.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_MmlConnector.setStatus(
        "current"
    )

occonectors_MmlConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 5)
)
occonectors_MmlConnector_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_MmlConnector_Canceled.setStatus(
        "current"
    )

occonectors_UcpConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 6)
)
occonectors_UcpConnector.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_UcpConnector.setStatus(
        "current"
    )

occonectors_UcpConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 7)
)
occonectors_UcpConnector_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_UcpConnector_Canceled.setStatus(
        "current"
    )

occonectors_UcipConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 8)
)
occonectors_UcipConnector.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_UcipConnector.setStatus(
        "current"
    )

occonectors_UcipConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 9)
)
occonectors_UcipConnector_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_UcipConnector_Canceled.setStatus(
        "current"
    )

occonectors_CaiConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 10)
)
occonectors_CaiConnector.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CaiConnector.setStatus(
        "current"
    )

occonectors_CaiConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 11)
)
occonectors_CaiConnector_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CaiConnector_Canceled.setStatus(
        "current"
    )

occonectors_SoapConnectorTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 12)
)
occonectors_SoapConnectorTimeout.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_SoapConnectorTimeout.setStatus(
        "current"
    )

occonectors_SoapConnectorTimeout_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 13)
)
occonectors_SoapConnectorTimeout_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_SoapConnectorTimeout_Canceled.setStatus(
        "current"
    )

occonectors_SoapConnectorLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 14)
)
occonectors_SoapConnectorLimit.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_SoapConnectorLimit.setStatus(
        "current"
    )

occonectors_SoapConnectorLimit_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 15)
)
occonectors_SoapConnectorLimit_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_SoapConnectorLimit_Canceled.setStatus(
        "current"
    )

occonectors_CorbaSib = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 16)
)
occonectors_CorbaSib.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CorbaSib.setStatus(
        "current"
    )

occonectors_CorbaSib_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 17)
)
occonectors_CorbaSib_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CorbaSib_Canceled.setStatus(
        "current"
    )

occonectors_CorbaSmaf = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 18)
)
occonectors_CorbaSmaf.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CorbaSmaf.setStatus(
        "current"
    )

occonectors_CorbaSmaf_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 19)
)
occonectors_CorbaSmaf_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CorbaSmaf_Canceled.setStatus(
        "current"
    )

occonectors_CorbaSih = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 20)
)
occonectors_CorbaSih.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CorbaSih.setStatus(
        "current"
    )

occonectors_CorbaSih_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 21)
)
occonectors_CorbaSih_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CorbaSih_Canceled.setStatus(
        "current"
    )

occonectors_XMLConnectorTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 22)
)
occonectors_XMLConnectorTimeout.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_XMLConnectorTimeout.setStatus(
        "current"
    )

occonectors_XMLConnectorTimeout_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 23)
)
occonectors_XMLConnectorTimeout_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_XMLConnectorTimeout_Canceled.setStatus(
        "current"
    )

occonectors_XMLConnectorLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 24)
)
occonectors_XMLConnectorLimit.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_XMLConnectorLimit.setStatus(
        "current"
    )

occonectors_XMLConnectorLimit_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 25)
)
occonectors_XMLConnectorLimit_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_XMLConnectorLimit_Canceled.setStatus(
        "current"
    )

occonectors_ORACLEConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 26)
)
occonectors_ORACLEConnector.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ORACLEConnector.setStatus(
        "current"
    )

occonectors_ORACLEConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 27)
)
occonectors_ORACLEConnector_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ORACLEConnector_Canceled.setStatus(
        "current"
    )

occonectors_MYSQL_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 28)
)
occonectors_MYSQL_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_MYSQL_connector_CONNECT.setStatus(
        "current"
    )

occonectors_MYSQL_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 29)
)
occonectors_MYSQL_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_MYSQL_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_SMPP_SERVER_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 30)
)
occonectors_SMPP_SERVER_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_SMPP_SERVER_connector_CONNECT.setStatus(
        "current"
    )

occonectors_SMPP_SERVER_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 31)
)
occonectors_SMPP_SERVER_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_SMPP_SERVER_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_TELNET_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 32)
)
occonectors_TELNET_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_TELNET_connector_CONNECT.setStatus(
        "current"
    )

occonectors_TELNET_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 33)
)
occonectors_TELNET_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_TELNET_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_SMAF_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 34)
)
occonectors_CORBA_SMAF_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_SMAF_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_SMAF_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 35)
)
occonectors_CORBA_SMAF_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_SMAF_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_SIH_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 36)
)
occonectors_CORBA_SIH_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_SIH_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_SIH_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 37)
)
occonectors_CORBA_SIH_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_SIH_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_CX_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 38)
)
occonectors_CORBA_CX_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_CX_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_CX_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 39)
)
occonectors_CORBA_CX_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_CX_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_CIB_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 40)
)
occonectors_CORBA_CIB_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_CIB_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_CIB_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 41)
)
occonectors_CORBA_CIB_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_CIB_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_ALCATEL_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 42)
)
occonectors_CORBA_ALCATEL_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_ALCATEL_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_ALCATEL_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 43)
)
occonectors_CORBA_ALCATEL_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_ALCATEL_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CAI_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 44)
)
occonectors_CAI_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CAI_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CAI_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 45)
)
occonectors_CAI_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CAI_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_BROADCAST_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 46)
)
occonectors_BROADCAST_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_BROADCAST_connector_CONNECT.setStatus(
        "current"
    )

occonectors_BROADCAST_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 47)
)
occonectors_BROADCAST_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_BROADCAST_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_LDAP_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 48)
)
occonectors_LDAP_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_LDAP_connector_CONNECT.setStatus(
        "current"
    )

occonectors_LDAP_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 49)
)
occonectors_LDAP_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_LDAP_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_DIAMETER_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 50)
)
occonectors_DIAMETER_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_DIAMETER_connector_CONNECT.setStatus(
        "current"
    )

occonectors_DIAMETER_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 51)
)
occonectors_DIAMETER_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_DIAMETER_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_HTTPCLIENT_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 52)
)
occonectors_HTTPCLIENT_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_HTTPCLIENT_connector_CONNECT.setStatus(
        "current"
    )

occonectors_HTTPCLIENT_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 53)
)
occonectors_HTTPCLIENT_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_HTTPCLIENT_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_BOOKMARK_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 54)
)
occonectors_BOOKMARK_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_BOOKMARK_connector_CONNECT.setStatus(
        "current"
    )

occonectors_BOOKMARK_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 55)
)
occonectors_BOOKMARK_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_BOOKMARK_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_INPAYMENT_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 56)
)
occonectors_CORBA_INPAYMENT_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_INPAYMENT_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_INPAYMENT_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 57)
)
occonectors_CORBA_INPAYMENT_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_INPAYMENT_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_CORBA_PPSERVER_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 58)
)
occonectors_CORBA_PPSERVER_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_PPSERVER_connector_CONNECT.setStatus(
        "current"
    )

occonectors_CORBA_PPSERVER_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 59)
)
occonectors_CORBA_PPSERVER_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_CORBA_PPSERVER_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_ecm_CONNECTOR_CRASHED = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 60)
)
occonectors_ecm_CONNECTOR_CRASHED.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ecm_CONNECTOR_CRASHED.setStatus(
        "current"
    )

occonectors_ecm_CONNECTOR_CRASHED_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 61)
)
occonectors_ecm_CONNECTOR_CRASHED_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ecm_CONNECTOR_CRASHED_Canceled.setStatus(
        "current"
    )

occonectors_ecm_CONNECTOR_DISABLED = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 62)
)
occonectors_ecm_CONNECTOR_DISABLED.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ecm_CONNECTOR_DISABLED.setStatus(
        "current"
    )

occonectors_ecm_CONNECTOR_DISABLED_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 63)
)
occonectors_ecm_CONNECTOR_DISABLED_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ecm_CONNECTOR_DISABLED_Canceled.setStatus(
        "current"
    )

occonectors_MMLAUC_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 64)
)
occonectors_MMLAUC_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_MMLAUC_connector_CONNECT.setStatus(
        "current"
    )

occonectors_MMLAUC_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 65)
)
occonectors_MMLAUC_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_MMLAUC_connector_CONNECT_Canceled.setStatus(
        "current"
    )

occonectors_ecm_CONNECTOR_PROBLEM = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 66)
)
occonectors_ecm_CONNECTOR_PROBLEM.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ecm_CONNECTOR_PROBLEM.setStatus(
        "current"
    )

occonectors_ecm_CONNECTOR_PROBLEM_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 67)
)
occonectors_ecm_CONNECTOR_PROBLEM_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occonectors_ecm_CONNECTOR_PROBLEM_Canceled.setStatus(
        "current"
    )

mcr_HTTP_SERVER_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 68)
)
mcr_HTTP_SERVER_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_HTTP_SERVER_connector_CONNECT.setStatus(
        "current"
    )

mcr_HTTP_SERVER_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 69)
)
mcr_HTTP_SERVER_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_HTTP_SERVER_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_SPEECHLAB_TTS_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 70)
)
mcr_SPEECHLAB_TTS_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SPEECHLAB_TTS_connector_CONNECT.setStatus(
        "current"
    )

mcr_SPEECHLAB_TTS_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 71)
)
mcr_SPEECHLAB_TTS_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SPEECHLAB_TTS_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_CIMD2_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 72)
)
mcr_CIMD2_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_CIMD2_connector_CONNECT.setStatus(
        "current"
    )

mcr_CIMD2_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 73)
)
mcr_CIMD2_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_CIMD2_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_SOAP_CLIENT_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 74)
)
mcr_SOAP_CLIENT_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SOAP_CLIENT_connector_CONNECT.setStatus(
        "current"
    )

mcr_SOAP_CLIENT_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 75)
)
mcr_SOAP_CLIENT_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SOAP_CLIENT_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_BLRATING_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 76)
)
mcr_BLRATING_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_BLRATING_connector_CONNECT.setStatus(
        "current"
    )

mcr_BLRATING_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 77)
)
mcr_BLRATING_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_BLRATING_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_DMS_CLIENT_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 78)
)
mcr_DMS_CLIENT_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DMS_CLIENT_connector_CONNECT.setStatus(
        "current"
    )

mcr_DMS_CLIENT_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 79)
)
mcr_DMS_CLIENT_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DMS_CLIENT_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_CONNECT = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 80)
)
mcr_SMPP_EX_connector_CONNECT.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_CONNECT.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_CONNECT_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 81)
)
mcr_SMPP_EX_connector_CONNECT_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_CONNECT_Canceled.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_CLIENT_SESS = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 82)
)
mcr_SMPP_EX_connector_CLIENT_SESS.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_CLIENT_SESS.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_CLIENT_SESS_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 83)
)
mcr_SMPP_EX_connector_CLIENT_SESS_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_CLIENT_SESS_Canceled.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_CLIENT_CONN = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 84)
)
mcr_SMPP_EX_connector_CLIENT_CONN.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_CLIENT_CONN.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_CLIENT_CONN_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 85)
)
mcr_SMPP_EX_connector_CLIENT_CONN_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_CLIENT_CONN_Canceled.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_SERVER_CONN = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 86)
)
mcr_SMPP_EX_connector_SERVER_CONN.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_SERVER_CONN.setStatus(
        "current"
    )

mcr_SMPP_EX_connector_SERVER_CONN_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 16, 1, 0, 87)
)
mcr_SMPP_EX_connector_SERVER_CONN_Canceled.setObjects(
      *(("OPCD-CONNECTORS-MIB-V2", "mcr_Host"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Severity"),
        ("OPCD-CONNECTORS-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SMPP_EX_connector_SERVER_CONN_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-CONNECTORS-MIB-V2",
    **{"occonnectors": occonnectors,
       "occonnectors-traps": occonnectors_traps,
       "definitions": definitions,
       "occonectors-LdapConnector": occonectors_LdapConnector,
       "occonectors-LdapConnector-Canceled": occonectors_LdapConnector_Canceled,
       "occonectors-MmlConnector": occonectors_MmlConnector,
       "occonectors-MmlConnector-Canceled": occonectors_MmlConnector_Canceled,
       "occonectors-UcpConnector": occonectors_UcpConnector,
       "occonectors-UcpConnector-Canceled": occonectors_UcpConnector_Canceled,
       "occonectors-UcipConnector": occonectors_UcipConnector,
       "occonectors-UcipConnector-Canceled": occonectors_UcipConnector_Canceled,
       "occonectors-CaiConnector": occonectors_CaiConnector,
       "occonectors-CaiConnector-Canceled": occonectors_CaiConnector_Canceled,
       "occonectors-SoapConnectorTimeout": occonectors_SoapConnectorTimeout,
       "occonectors-SoapConnectorTimeout-Canceled": occonectors_SoapConnectorTimeout_Canceled,
       "occonectors-SoapConnectorLimit": occonectors_SoapConnectorLimit,
       "occonectors-SoapConnectorLimit-Canceled": occonectors_SoapConnectorLimit_Canceled,
       "occonectors-CorbaSib": occonectors_CorbaSib,
       "occonectors-CorbaSib-Canceled": occonectors_CorbaSib_Canceled,
       "occonectors-CorbaSmaf": occonectors_CorbaSmaf,
       "occonectors-CorbaSmaf-Canceled": occonectors_CorbaSmaf_Canceled,
       "occonectors-CorbaSih": occonectors_CorbaSih,
       "occonectors-CorbaSih-Canceled": occonectors_CorbaSih_Canceled,
       "occonectors-XMLConnectorTimeout": occonectors_XMLConnectorTimeout,
       "occonectors-XMLConnectorTimeout-Canceled": occonectors_XMLConnectorTimeout_Canceled,
       "occonectors-XMLConnectorLimit": occonectors_XMLConnectorLimit,
       "occonectors-XMLConnectorLimit-Canceled": occonectors_XMLConnectorLimit_Canceled,
       "occonectors-ORACLEConnector": occonectors_ORACLEConnector,
       "occonectors-ORACLEConnector-Canceled": occonectors_ORACLEConnector_Canceled,
       "occonectors-MYSQL-connector-CONNECT": occonectors_MYSQL_connector_CONNECT,
       "occonectors-MYSQL-connector-CONNECT-Canceled": occonectors_MYSQL_connector_CONNECT_Canceled,
       "occonectors-SMPP-SERVER-connector-CONNECT": occonectors_SMPP_SERVER_connector_CONNECT,
       "occonectors-SMPP-SERVER-connector-CONNECT-Canceled": occonectors_SMPP_SERVER_connector_CONNECT_Canceled,
       "occonectors-TELNET-connector-CONNECT": occonectors_TELNET_connector_CONNECT,
       "occonectors-TELNET-connector-CONNECT-Canceled": occonectors_TELNET_connector_CONNECT_Canceled,
       "occonectors-CORBA-SMAF-connector-CONNECT": occonectors_CORBA_SMAF_connector_CONNECT,
       "occonectors-CORBA-SMAF-connector-CONNECT-Canceled": occonectors_CORBA_SMAF_connector_CONNECT_Canceled,
       "occonectors-CORBA-SIH-connector-CONNECT": occonectors_CORBA_SIH_connector_CONNECT,
       "occonectors-CORBA-SIH-connector-CONNECT-Canceled": occonectors_CORBA_SIH_connector_CONNECT_Canceled,
       "occonectors-CORBA-CX-connector-CONNECT": occonectors_CORBA_CX_connector_CONNECT,
       "occonectors-CORBA-CX-connector-CONNECT-Canceled": occonectors_CORBA_CX_connector_CONNECT_Canceled,
       "occonectors-CORBA-CIB-connector-CONNECT": occonectors_CORBA_CIB_connector_CONNECT,
       "occonectors-CORBA-CIB-connector-CONNECT-Canceled": occonectors_CORBA_CIB_connector_CONNECT_Canceled,
       "occonectors-CORBA-ALCATEL-connector-CONNECT": occonectors_CORBA_ALCATEL_connector_CONNECT,
       "occonectors-CORBA-ALCATEL-connector-CONNECT-Canceled": occonectors_CORBA_ALCATEL_connector_CONNECT_Canceled,
       "occonectors-CAI-connector-CONNECT": occonectors_CAI_connector_CONNECT,
       "occonectors-CAI-connector-CONNECT-Canceled": occonectors_CAI_connector_CONNECT_Canceled,
       "occonectors-BROADCAST-connector-CONNECT": occonectors_BROADCAST_connector_CONNECT,
       "occonectors-BROADCAST-connector-CONNECT-Canceled": occonectors_BROADCAST_connector_CONNECT_Canceled,
       "occonectors-LDAP-connector-CONNECT": occonectors_LDAP_connector_CONNECT,
       "occonectors-LDAP-connector-CONNECT-Canceled": occonectors_LDAP_connector_CONNECT_Canceled,
       "occonectors-DIAMETER-connector-CONNECT": occonectors_DIAMETER_connector_CONNECT,
       "occonectors-DIAMETER-connector-CONNECT-Canceled": occonectors_DIAMETER_connector_CONNECT_Canceled,
       "occonectors-HTTPCLIENT-connector-CONNECT": occonectors_HTTPCLIENT_connector_CONNECT,
       "occonectors-HTTPCLIENT-connector-CONNECT-Canceled": occonectors_HTTPCLIENT_connector_CONNECT_Canceled,
       "occonectors-BOOKMARK-connector-CONNECT": occonectors_BOOKMARK_connector_CONNECT,
       "occonectors-BOOKMARK-connector-CONNECT-Canceled": occonectors_BOOKMARK_connector_CONNECT_Canceled,
       "occonectors-CORBA-INPAYMENT-connector-CONNECT": occonectors_CORBA_INPAYMENT_connector_CONNECT,
       "occonectors-CORBA-INPAYMENT-connector-CONNECT-Canceled": occonectors_CORBA_INPAYMENT_connector_CONNECT_Canceled,
       "occonectors-CORBA-PPSERVER-connector-CONNECT": occonectors_CORBA_PPSERVER_connector_CONNECT,
       "occonectors-CORBA-PPSERVER-connector-CONNECT-Canceled": occonectors_CORBA_PPSERVER_connector_CONNECT_Canceled,
       "occonectors-ecm-CONNECTOR-CRASHED": occonectors_ecm_CONNECTOR_CRASHED,
       "occonectors-ecm-CONNECTOR-CRASHED-Canceled": occonectors_ecm_CONNECTOR_CRASHED_Canceled,
       "occonectors-ecm-CONNECTOR-DISABLED": occonectors_ecm_CONNECTOR_DISABLED,
       "occonectors-ecm-CONNECTOR-DISABLED-Canceled": occonectors_ecm_CONNECTOR_DISABLED_Canceled,
       "occonectors-MMLAUC-connector-CONNECT": occonectors_MMLAUC_connector_CONNECT,
       "occonectors-MMLAUC-connector-CONNECT-Canceled": occonectors_MMLAUC_connector_CONNECT_Canceled,
       "occonectors-ecm-CONNECTOR-PROBLEM": occonectors_ecm_CONNECTOR_PROBLEM,
       "occonectors-ecm-CONNECTOR-PROBLEM-Canceled": occonectors_ecm_CONNECTOR_PROBLEM_Canceled,
       "mcr-HTTP-SERVER-connector-CONNECT": mcr_HTTP_SERVER_connector_CONNECT,
       "mcr-HTTP-SERVER-connector-CONNECT-Canceled": mcr_HTTP_SERVER_connector_CONNECT_Canceled,
       "mcr-SPEECHLAB-TTS-connector-CONNECT": mcr_SPEECHLAB_TTS_connector_CONNECT,
       "mcr-SPEECHLAB-TTS-connector-CONNECT-Canceled": mcr_SPEECHLAB_TTS_connector_CONNECT_Canceled,
       "mcr-CIMD2-connector-CONNECT": mcr_CIMD2_connector_CONNECT,
       "mcr-CIMD2-connector-CONNECT-Canceled": mcr_CIMD2_connector_CONNECT_Canceled,
       "mcr-SOAP-CLIENT-connector-CONNECT": mcr_SOAP_CLIENT_connector_CONNECT,
       "mcr-SOAP-CLIENT-connector-CONNECT-Canceled": mcr_SOAP_CLIENT_connector_CONNECT_Canceled,
       "mcr-BLRATING-connector-CONNECT": mcr_BLRATING_connector_CONNECT,
       "mcr-BLRATING-connector-CONNECT-Canceled": mcr_BLRATING_connector_CONNECT_Canceled,
       "mcr-DMS-CLIENT-connector-CONNECT": mcr_DMS_CLIENT_connector_CONNECT,
       "mcr-DMS-CLIENT-connector-CONNECT-Canceled": mcr_DMS_CLIENT_connector_CONNECT_Canceled,
       "mcr-SMPP-EX-connector-CONNECT": mcr_SMPP_EX_connector_CONNECT,
       "mcr-SMPP-EX-connector-CONNECT-Canceled": mcr_SMPP_EX_connector_CONNECT_Canceled,
       "mcr-SMPP-EX-connector-CLIENT-SESS": mcr_SMPP_EX_connector_CLIENT_SESS,
       "mcr-SMPP-EX-connector-CLIENT-SESS-Canceled": mcr_SMPP_EX_connector_CLIENT_SESS_Canceled,
       "mcr-SMPP-EX-connector-CLIENT-CONN": mcr_SMPP_EX_connector_CLIENT_CONN,
       "mcr-SMPP-EX-connector-CLIENT-CONN-Canceled": mcr_SMPP_EX_connector_CLIENT_CONN_Canceled,
       "mcr-SMPP-EX-connector-SERVER-CONN": mcr_SMPP_EX_connector_SERVER_CONN,
       "mcr-SMPP-EX-connector-SERVER-CONN-Canceled": mcr_SMPP_EX_connector_SERVER_CONN_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
